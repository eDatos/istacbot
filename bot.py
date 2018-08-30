from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import re

from telegram_custom import TelegramInput
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.slack import SlackInput
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.training_data import load_data
import credentials

from custom_stopwords import stopwords_custom
from policy import RestaurantPolicy

logger = logging.getLogger(__name__)
stemmer = SnowballStemmer("spanish")
spanish_stopwords = stopwords.words('spanish')
for stopword in stopwords_custom: spanish_stopwords.append(stopword)
spanish_stopwords.remove('eso')
spanish_stopwords.remove('no')
spanish_stopwords.remove("sí")

remove_punctuation_marks = re.compile(r"\w+")

class RestaurantAPI(object):
    def search(self, info):
        return ""


def train_dialogue(domain_file="domain/istac_domain_v9.yml",
                   model_path="models/dialogue_201802301413",
                   training_data_file="data/stories_v13.md"):

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
    training_data = load_data('data/nlu_train_v30.json')
    trainer = Trainer(config.load("config/nlu_model_config_v1.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="nlu_train_v30_201802301413")
    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/nlu_train_v30_201802301413/")
    agent = Agent.load("models/dialogue_201802301413", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel(), message_preprocessor=stopwords_clean_lambda)
    return agent

def run_stemming (serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/nlu_train_v24_stemming_2018072401405/")
    agent = Agent.load("models/dialogue_201807231114", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel(), message_preprocessor=stopwords_clean_lambda)
    return agent

def runTelegram(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/nlu_train_v30_201802301413")
    agent = Agent.load("models/dialogue_201802301413", interpreter=interpreter)

    input_channel = TelegramInput(
        access_token=credentials.access_token,  # you get this when setting up a bot
        verify=credentials.verify,  # this is your bots username
        webhook_url=credentials.webhook_url  # the url your bot should listen for messages
    )

    agent.handle_channel(HttpInputChannel(5004, "", input_channel), message_preprocessor=stopwords_clean_lambda)

def stemming(text):
    tokens = word_tokenize(text)
    tokens_stemmed = [stemmer.stem(token)for token in tokens ]
    spanish_stopwords_stemmed = [stemmer.stem(stopword)for stopword in spanish_stopwords]
    filtered_words = [word for word in tokens_stemmed if word not in spanish_stopwords_stemmed and re.match(remove_punctuation_marks, word) != None]
    frase = ''
    for word in filtered_words:
        frase = frase + word + ' '
    return frase

stemming_lambda = lambda text: stemming(text)
stopwords_clean_lambda = lambda text: stopwords_clean(text)

def stopwords_clean(text):
    text = text.lower()
    tokens = word_tokenize(text)
    filtered_words = [word for word in tokens if word not in spanish_stopwords and re.match(remove_punctuation_marks, word) != None]
    spanish_stopwords_stemmed = [stemmer.stem(stopword)for stopword in spanish_stopwords]
    spanish_stopwords_stemmed.remove('par')
    filtered_words_stemmed = [word for word in filtered_words if stemmer.stem(word) not in spanish_stopwords_stemmed]
    frase = ''
    for word in filtered_words_stemmed:
        frase = frase + word + ' '
    return frase


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
        description='starts the bot')

    parser.add_argument(
        'task',
        choices=["train-nlu", "train-dialogue", "run", "run-stemming", "run-telegram"],
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
    elif task == "run-stemming":
        run_stemming()
