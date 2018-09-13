from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from flask import Blueprint, request, jsonify

from telegram import (Bot, InlineKeyboardButton, Update, InlineKeyboardMarkup,
                      KeyboardButton, ReplyKeyboardMarkup, ParseMode, ChatAction)

import csv
import datetime
import re
from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels.rest import HttpInputComponent
import messages
import properties
import telegram_users

logger = logging.getLogger(__name__)


class TelegramOutput(Bot, OutputChannel):
    """Output channel for Telegram"""

    @classmethod
    def name(cls):
        return "telegram"

    def __init__(self, access_token):
        super(TelegramOutput, self).__init__(access_token)

    def send_text_message(self, recipient_id, message):
        if (re.match("^{}".format(messages.log_header), message)):
            save_log(message, recipient_id, messages.user_debug)
        else:
            if (messages.greeting == message):
                message = custom_greeting(message, recipient_id)

            message = save_log(message, recipient_id, messages.user_bot)
            return self.send_message(recipient_id, message, parse_mode=ParseMode.HTML)


    def send_image_url(self, recipient_id, image_url):
        return self.send_photo(recipient_id, image_url)

    def send_text_with_buttons(self, recipient_id, text,
                               buttons, button_type="inline", **kwargs):
        """Sends a message with keyboard.

        For more information: https://core.telegram.org/bots#keyboards

        :button_type inline: horizontal inline keyboard

        :button_type vertical: vertical inline keyboard

        :button_type custom: custom keyboard
        """

        text = save_log(text, recipient_id, messages.user_bot)

        for button in buttons:
            save_log(button["title"], recipient_id, messages.user_bot)

        if button_type == "inline":
            button_list = [[InlineKeyboardButton(s["title"],
                            callback_data=s["payload"]) for s in buttons]]
            reply_markup = InlineKeyboardMarkup(button_list)
            
        elif button_type == "vertical":
            button_list = [[InlineKeyboardButton(s["title"],
                            callback_data=s["payload"])] for s in buttons]
            reply_markup = InlineKeyboardMarkup(button_list)
            
        elif button_type == "custom":
            button_list = []
            for bttn in buttons:
                if isinstance(bttn, list):
                    button_list.append([KeyboardButton(s['title'])
                                        for s in bttn])
                else:
                    button_list.append([KeyboardButton(bttn["title"])])
            reply_markup = ReplyKeyboardMarkup(button_list,
                                               resize_keyboard=True,
                                               one_time_keyboard=True)
        else:
            logger.error('Trying to send text with buttons for unknown '
                         'button type {}'.format(button_type))
            return

        return self.send_message(recipient_id, text, reply_markup=reply_markup, timeout=20)

class TelegramInput(HttpInputComponent):
    """Telegram input channel"""

    @classmethod
    def name(cls):
        return "telegram"

    def __init__(self, access_token, verify, webhook_url, debug_mode=True):
        self.access_token = access_token
        self.verify = verify
        self.webhook_url = webhook_url
        self.debug_mode = debug_mode

    @staticmethod
    def _is_location(message):
        if message:
            return message.location
        else:
            return ''

    @staticmethod
    def _is_user_message(message):
        if message:
            return message.text
        else:
            return ''

    @staticmethod
    def check_has_not_exceeded_time(message):
        if message and (datetime.datetime.now() - message.date) < datetime.timedelta(minutes=properties.discard_messages_max_minutes):
            return message.text
        else:
            return ''

    @staticmethod
    def _is_button(update):
        return update.callback_query

    def blueprint(self, on_new_message):
        telegram_webhook = Blueprint('telegram_webhook', __name__)
        out_channel = TelegramOutput(self.access_token)

        @telegram_webhook.route("/", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @telegram_webhook.route("/set_webhook", methods=['GET', 'POST'])
        def set_webhook():
            s = out_channel.setWebhook(self.webhook_url)
            if s:
                logger.info("Webhook Setup Successful")
                return "Webhook setup successful"
            else:
                logger.warning("Webhook Setup Failed")
                return "Invalid webhook"
        set_webhook()
        
        @telegram_webhook.route("/webhook", methods=['GET', 'POST'])
        def message():
            if request.method == 'POST':

                if not out_channel.get_me()['username'] == self.verify:
                    logger.debug("Invalid access token, check it "
                                 "matches Telegram")
                    return "failed"

                update = Update.de_json(request.get_json(force=True),
                                        out_channel)
                if self._is_button(update):
                    message = update.callback_query.message
                    text = update.callback_query.data
                else:
                    message = update.message
                    if self._is_user_message(message) and self.check_has_not_exceeded_time(message):
                        text = message.text.replace('/bot', '')
                    elif self._is_location(message):
                        text = ('{{"lng":{0}, "lat":{1}}}'
                                ''.format(message.location.longitude,
                                          message.location.latitude))
                    else:
                        return "success"
                sender_id = message.chat.id
                try:
                    if text == '_restart' or text == '/restart':
                        on_new_message(UserMessage(text, out_channel,
                                                   sender_id))
                        on_new_message(UserMessage('/start', out_channel,
                                                   sender_id))
                    elif text == '/start':
                            on_new_message(UserMessage("hola", out_channel,
                                                       sender_id))
                    else:
                        on_new_message(UserMessage(text, out_channel,
                                                   sender_id))
                    save_log(text, sender_id, messages.user)
                except Exception as e:
                    logger.error("Exception when trying to handle "
                                 "message.{0}".format(e))
                    logger.error(e, exc_info=True)
                    if self.debug_mode:
                        raise
                    pass

                return "success"

        return telegram_webhook

def custom_greeting(message, sender_id):
    print(sender_id)
    if sender_id in telegram_users.users.keys():
        return message.format(" " + telegram_users.users[sender_id])
    return message.format("")

def save_log(text, sender_id, user):
    message_match = re.match("^(ERROR: )?(.*)", text)
    type_message = ""

    if (message_match[1]):
        text = message_match[2]
        type_message=messages.error_log
    try:
        with open(get_log_filename(), 'a', newline='') as csvfile:
            log = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            log.writerow([sender_id, user, text, type_message, str(datetime.datetime.now())])
    except Exception as e:
        logger.error("Error al guardar log. {}".format(e))
        return ""
    return text

def get_log_filename():
    return properties.location + str(datetime.date.today().isocalendar()[0]) + "_" + str(datetime.date.today().isocalendar()[1]) + ".csv"
