from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.channels import HttpInputChannel
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.channel import UserMessage
from rasa_core.channels.direct import CollectingOutputChannel
from rasa_core.channels.rest import HttpInputComponent
from flask import Blueprint, request, jsonify
from nltk.corpus import stopwords

logger = logging.getLogger(__name__)
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk import word_tokenize
import re
from istac_chatbot.policy import RestaurantPolicy
from istac_chatbot.custom_stopwords import stopwords_custom

stemmer = SnowballStemmer("spanish")
spanish_stopwords = stopwords.words('spanish')
for stopword in stopwords_custom: spanish_stopwords.append(stopword)
spanish_stopwords.remove('eso')
remove_punctuation_marks = re.compile(r"\w+")


class SimpleWebBot(HttpInputComponent):
    """A simple web bot that listens on a url and responds."""

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint('custom_webhook', __name__)

        @custom_webhook.route("/status", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @custom_webhook.route("/", methods=['POST'])
        def receive():
            payload = request.json
            sender_id = payload.get("sender", None)
            text = payload.get("message", None)
            out = CollectingOutputChannel()
            on_new_message(UserMessage(text, out, sender_id))
            responses = [m for _, m in out.messages]
            return jsonify(responses)
    
        return custom_webhook

def run(serve_forever=True):
    #path to your NLU model
    interpreter = RasaNLUInterpreter("models/nlu/default/nlu_train_v29_201807300802/")
    # path to your dialogues models
    agent = Agent.load("models/dialogue_201807300803", interpreter=interpreter)
    #http api endpoint for responses
    input_channel = SimpleWebBot()
    if serve_forever:
        agent.handle_channel(HttpInputChannel(5004, "/chat", input_channel, message_preprocessor=stopwords_clean))
    return agent

stopwords_clean_lambda = lambda text: stopwords_clean(text)

def stopwords_clean(text):
    text = text.lower()
    tokens = word_tokenize(text)
    filtered_words = [word for word in tokens if word not in spanish_stopwords and re.match(remove_punctuation_marks, word) != None]
    spanish_stopwords_stemmed = [stemmer.stem(stopword)for stopword in spanish_stopwords]
    spanish_stopwords_stemmed.remove('par')
    # spanish_stopwords_stemmed.remove('si')
    filtered_words_stemmed = [word for word in filtered_words if stemmer.stem(word) not in spanish_stopwords_stemmed]
    frase = ''
    for word in filtered_words_stemmed:
        frase = frase + word + ' '
    # DEBUG print(frase)
    return frase