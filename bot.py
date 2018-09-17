from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import re

import requests
import spacy
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.training_data import load_data

import credentials
import properties
import variables
from custom_stopwords import stopwords_custom
from policy import RestaurantPolicy
from remove_from_stopwords import remove_stopwords
from telegram_custom import TelegramInput
from facebook_custom import FacebookInput

logging.basicConfig(filename=properties.location + 'bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

stemmer = SnowballStemmer("spanish")
spanish_stopwords = stopwords.words('spanish')
for stopword in stopwords_custom: spanish_stopwords.append(stopword)
for stopword in remove_stopwords:
    spanish_stopwords.remove(stopword)

remove_punctuation_marks = re.compile(r"\w+")
spacy_parser = spacy.load('es')

class RestaurantAPI(object):
    def search(self, info):
        return ""


def train_dialogue(domain_file="domain/istac_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/stories.md"):

    fallback = FallbackPolicy(fallback_action_name="utter_default",
                              nlu_threshold=0.4)

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=3),
                            RestaurantPolicy(), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        epochs=400,
        batch_size=100,
        validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    training_data = load_data('data/nlu_train.json')
    trainer = Trainer(config.load("config/nlu_model_config_v1.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="nlu_train")
    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/nlu_train/")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel(), message_preprocessor=clean_text_input_lambda)
    return agent

def runTelegram(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/nlu_train")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    input_channel = TelegramInput(
        access_token=credentials.access_token,  # you get this when setting up a bot
        verify=credentials.verify,  # this is your bots username
        webhook_url=credentials.webhook_url  # the url your bot should listen for messages
    )

    agent.handle_channel(HttpInputChannel(credentials.port, "", input_channel), message_preprocessor=clean_text_input)

def runFacebook(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/nlu_train")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    input_channel = FacebookInput(
        fb_verify="desarrollotestistacbot",  # you need tell facebook this token, to confirm your URL
        fb_secret="e88bce9287cb4e8fa745299ac7330472",  # your app secret
        fb_access_token="EAADWZAjXEZBbcBAKAkLNGZCjrZCMXbLZA0md9R2SJcavEvwno6QdsusRZCtF2N4nXTV9DZAlqP4Mdj0bTaQJ49n4UgtqotvJOkjD3BQrPnPgZCCskYeoLZA8ZAFO8mfhwEzZChoS5t80L8AvgWXwZAsGRvOKCwTg1yQn7CetpqxBIWsS1eOuas7ZAcnppEgNwCwLNpfgZD"  # token for the page you subscribed to
    )

    agent.handle_channel(HttpInputChannel(5004, "", input_channel), message_preprocessor=clean_text_input)

clean_text_input_lambda = lambda text: clean_text_input(text)

def clean_text_input(text):
    text_stopwords_cleaned = stopwords_clean(text)
    return date_clean(text_stopwords_cleaned)

def date_clean(text):
    query = {'locale': 'es_ES', 'dims': '["time"]', 'text': text}
    response_duckling = requests.post(properties.duckling_server, data=query).json()
    if (response_duckling):
        grain = response_duckling[0]["value"]["grain"]
        match = response_duckling[0]["body"].lower()
        date = re.match(r"(\d{4})-(\d{2})-(\d{2}).*", response_duckling[0]["value"]["value"])
        has_year = re.match(r"(.*\d{4}.*|.*años?.*)", match)
        if (date):
            if (match in variables.months):
                return text.replace(match, variables.months[match])
            elif (grain == "day" or grain == "month"):
                if has_year:
                    return text.replace(match, date[1] + "M" + date[2])
                else:
                    return text.replace(match, "M" + date[2])
            elif (grain == "quarter"):
                quarter = str(int(int(date[2]) / 3) + 1)
                if has_year:
                    return text.replace(match, date[1] + "Q" + quarter)
                else:
                    return text.replace(match, "Q" + quarter)
    return text

def stopwords_clean(text):
    text = remove_accents_and_lower(text)
    tokens = spacy_parser(text)
    tokens = [token.orth_ for token in tokens if not token.orth_.isspace()]
    filtered_words = [word for word in tokens if word not in spanish_stopwords and re.match(remove_punctuation_marks, word) != None]
    spanish_stopwords_stemmed = [stemmer.stem(stopword)for stopword in spanish_stopwords]
    spanish_stopwords_stemmed.remove('par')
    filtered_words_stemmed = [word for word in filtered_words if stemmer.stem(word) not in spanish_stopwords_stemmed]
    frase = ''
    for word in filtered_words_stemmed:
        frase = frase + word + ' '
    return frase

def remove_accents_and_lower(text):
    text.lower()
    text = text.replace('á', 'a')
    text = text.replace('é', 'e')
    text = text.replace('í', 'i')
    text = text.replace('ó', 'o')
    text = text.replace('ú', 'u')
    return text


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
        description='starts the bot')

    parser.add_argument(
        'task',
        choices=["train-nlu", "train-dialogue", "run", "run-stemming", "run-telegram", "run-facebook"],
        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    elif task == "run-telegram":
        runTelegram()
    elif task == "run-facebook":
        runFacebook()
