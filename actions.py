from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import difflib
import locale
import re

import requests
import unidecode
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from rasa_core.actions.action import Action
from rasa_core.events import Restarted, SlotSet

import messages
import properties
from custom_stopwords import stopwords_custom
from variables import indicators, indicators_check, locations_check, hombres_indicadores, mujeres_indicadores, \
    indicators_with_sex

MAX_LENGTH_TELEGRAM_MESSAGE = 4096
URL = properties.url
COLOR = properties.color
DEFAULT_LOCATION = properties.default_location
NUMBER_SIMILAR_INDICATORS = properties.number_similar_indicators
locale.setlocale(locale.LC_ALL, properties.locale)
REGEX_HAS_YEAR =  r".*(\d{4}).*"

indexes_lower = [unidecode.unidecode(x).lower() for x in indicators.keys()]
stemmer = SnowballStemmer("spanish")
spanish_stopwords = stopwords.words('spanish')
remove_punctuation_marks = re.compile(r"\w+")
for stopword in stopwords_custom: spanish_stopwords.append(stopword)


class ActionShow(Action):
    restart_index = 0
    previous_date = None
    previous_indicator = None
    previous_location = None
    possible_location = None
    debug = True

    location_confidence = {'confidence': -1, 'value': DEFAULT_LOCATION}
    date_confidence = {'confidence': -1, 'value': ''}
    indicator_confidence = {'confidence': -1, 'value': ''}

    previuos_location_confidence = {'confidence': -1, 'value': ''}
    previous_date_confidence = {'confidence': -1, 'value': ''}
    previous_indicator_confidence = {'confidence': -1, 'value': ''}

    actions_ignore = ["action_hombres", "action_mujeres", "action_yes"]

    def reset(self):
        self.previous_date = None
        self.previous_indicator = None
        self.previous_location = None
        self.possible_location = None

        self.location_confidence = {'confidence': -1, 'value': DEFAULT_LOCATION}
        self.date_confidence = {'confidence': -1, 'value': ''}
        self.indicator_confidence = {'confidence': -1, 'value': ''}

        self.previuos_location_confidence = {'confidence': -1, 'value': ''}
        self.previous_date_confidence = {'confidence': -1, 'value': ''}
        self.previous_indicator_confidence = {'confidence': -1, 'value': ''}

        self.actions_ignore = ["action_hombres", "action_mujeres", "action_yes"]

    def name(self):
        return 'action_show'

    def run(self, dispatcher, tracker, domain):

        if self.restart_index != tracker.idx_after_latest_restart():
            self.restart_index = tracker.idx_after_latest_restart()
            self.reset()

        if (tracker.latest_action_name not in self.actions_ignore and next(tracker.get_latest_entity_values("var_What"), None) == None and next(
            tracker.get_latest_entity_values("var_Loc"), None) == None
                and next(tracker.get_latest_entity_values("var_Date"), None) == None):

            self.dont_understand_message(dispatcher)
            return []

        if (tracker.get_slot("var_What") != "listen_consulta_hombres" and tracker.get_slot(
                "var_What") != "listen_consulta_mujeres"):

            # Save all previous confidences
            self.previous_location_confidence = self.location_confidence.copy()
            self.previous_date_confidence = self.date_confidence.copy()
            self.previous_indicator_confidence = self.indicator_confidence.copy()

            # Reset all confidences
            self.location_confidence = {'confidence': -1, 'value': ''}
            self.date_confidence = {'confidence': -1, 'value': ''}
            self.indicator_confidence = {'confidence': -1, 'value': ''}

            if (self.debug):
                print("previous_location_slot: " + str(self.previous_location) + ", previous_date_slot: " + str(
                    self.previous_date) + ", previous_indicator_slot: " + str(self.previous_indicator))
            dispatcher.utter_message(messages.log_header + "previous_location_slot: " + str(self.previous_location) + ", previous_date_slot: " + str(
                    self.previous_date) + ", previous_indicator_slot: " + str(self.previous_indicator))

            ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
            date_slot = None
            location_slot = tracker.get_slot("var_Loc")
            if tracker.get_slot("var_Date") is not None:
                date_slot = ansi_escape.sub('', tracker.get_slot("var_Date"))

            indicator_slot = tracker.get_slot("var_What")

            if (self.debug):
                print("location_slot: " + repr(location_slot) + ", date_slot: " + repr(
                    date_slot) + ", indicator_slot: " + str(indicator_slot))



            if (date_slot and self.date_get_year(date_slot)):
                self.previous_date = date_slot
            self.previous_location = location_slot
            self.previous_indicator = indicator_slot

            # Localización por defecto: Canarias
            if (location_slot == None):
                location_slot = DEFAULT_LOCATION

            self.calculate_confidence_location(location_slot)
            self.calculate_confidence_indicator(indicator_slot)

            if (self.debug):
                print("location_slot: " + repr(location_slot) + ", date_slot: " + str(
                    date_slot) + ", indicator_slot: " + str(indicator_slot))

            dispatcher.utter_message(messages.log_header + "location_slot: " + repr(location_slot) + ", date_slot: " + str(
                    date_slot) + ", indicator_slot: " + str(indicator_slot))

            if self.location_confidence['confidence'] > 0.7 and self.indicator_confidence[
                'confidence'] > 0.7 and indicator_slot != None and location_slot != None:
                indicator = self.indicator_confidence["value"]
                response_indicator = requests.get(URL + indicators[indicator]).json()
                if (self.location_confidence['confidence'] > 0.9 and self.indicator_confidence[
                    'confidence'] > 0.9 and response_indicator != None):
                    return self.show_information(dispatcher, date_slot, location_slot, indicator, response_indicator)
                else:
                    date = self.getDate(date_slot, response_indicator, dispatcher)
                    if date:
                        dispatcher.utter_button_message(messages.low_confidence.format(
                                self.indicator_confidence["value"],
                                self.location_confidence["value"],
                                self.translate_date(date, response_indicator)
                            ), [{"title": "Sí", "payload": "si"}, {"title": "No", "payload": "no"}], button_type="custom")
                    return [SlotSet("var_What", self.indicator_confidence["value"]),
                            SlotSet("var_Loc", self.location_confidence["value"]),
                            SlotSet("var_Date", date_slot)]
            else:
                self.dont_understand_message(dispatcher)
                return [SlotSet("var_What", None), SlotSet("var_Loc", None),
                        SlotSet("var_Date", date_slot)]
        return [SlotSet("var_What", None)]

    def getDate(self, date, response_indicator, dispatcher):
        time = response_indicator['dimension']['TIME']
        date_list = [str(t['code'].lower()) for t in time['representation']]
        found = False
        if not date:
            return date_list[0].upper() # Si no se especifica fecha, se devuelve la más reciente
        if not self.date_get_year(date):
            year = str(datetime.datetime.now().year)
            if self.previous_date and self.date_get_year(self.previous_date):
                year = self.date_get_year(self.previous_date)[1]
            found = self.check_in_list(year + date, date_list)
        else:
            found = self.check_in_list(date, date_list)

        if not found and self.indicator_confidence['confidence'] > 0.9: # Solo se muestra el mensaje cuando tenemos una confianza superior al 0.9
            dispatcher.utter_message((messages.date_not_found))
            found = date_list[0].upper()
            self.previous_date = found
        else:
            found = found.upper()

        return found

    def check_in_list(self, value, var_list):
        for date in var_list:
            if (date.find(value) != -1):
                return str(date)
        return False

    def getGeographical(self, loc_slot, response_indicator, dispatcher):
        max_similarity = 0
        geographical_code = ""
        geographical_name = ""
        geographical_names = {}
        for element in response_indicator['dimension']['GEOGRAPHICAL']['representation']:
            difference = difflib.SequenceMatcher(None, self.stemming(loc_slot),
                                                 self.stemming(
                                                     self.get_geographical_name(element['title']['es']))).ratio()
            if element['granularityCode'] not in geographical_names:
                geographical_names[element['granularityCode']] = {}
            geographical_names[element['granularityCode']][
                self.get_geographical_name(element['title']['es'])] = difference

            if max_similarity < difference:
                geographical_code = element['code']
                geographical_name = self.get_geographical_name(element['title']['es'])
                max_similarity = difference

        if max_similarity > 0.7:
            return geographical_code, geographical_name
        else:

            location, similarity = self.get_most_similar_location(loc_slot)
            if (similarity < 0.90):
                dispatcher.utter_message(messages.try_another_date.format(
                        location,
                        self.get_location_granularities(response_indicator)
                    ))
            else:
                dispatcher.utter_message(messages.place_not_found.format(
                    self.get_location_granularities(response_indicator)
                ))
        return None, None

    def get_similar_indicators(self, indicator_slot, dispatcher):
        indicators_difference = {}
        for indicator in indicators:
            if (not re.match(r".*(Mujeres|Hombres)", indicator)): # Nunca se recomiendan indicadores de sexo.
                indicators_difference[indicator] = difflib.SequenceMatcher(None, self.stemming(indicator_slot),
                                                                       self.stemming(indicator)).ratio()
        indicators_sorted = sorted(indicators_difference, key=indicators_difference.get, reverse=True)
        if len(indicators_sorted) > 0:
            indicators_sorted.pop(0) # Eliminamos el primer el elemento porque coincide con indicator_slot.
        buttons = []
        for i in range(min(len(indicators_sorted), NUMBER_SIMILAR_INDICATORS)):
            print(indicators_sorted[i])
            buttons.append({"title": str(indicators_sorted[i]), "payload": indicators_sorted[i]})

        if len(buttons) > 0:
            dispatcher.utter_button_message(messages.similar_indicators, buttons,
                                            button_type="custom")

    def get_geographical_name(self, nombre):
        result = re.match('(\w+)\s+\((\w+)\)', nombre)
        if (result):
            return result[2] + " " + result[1]
        else:
            return nombre

    def stemming(self, text):
        tokens = word_tokenize(text)
        filtered_words = [stemmer.stem(word) for word in tokens if
                          word not in spanish_stopwords and re.match(remove_punctuation_marks, word) != None]
        frase = ''
        for word in filtered_words:
            frase = frase + word + ' '
        return frase.lower()

    def stopwords_clean(self, text):
        text = text.lower()
        tokens = word_tokenize(text)
        filtered_words = [word for word in tokens if
                          word not in spanish_stopwords and re.match(remove_punctuation_marks, word) != None]
        spanish_stopwords_stemmed = [stemmer.stem(stopword) for stopword in spanish_stopwords]
        spanish_stopwords_stemmed.remove('par')
        filtered_words_stemmed = [word for word in filtered_words if
                                  stemmer.stem(word) not in spanish_stopwords_stemmed]
        frase = ''
        for word in filtered_words_stemmed:
            frase = frase + word + ' '
        print(frase)
        return frase

    def get_indicator(self, indicator_slot, dispatcher):
        indicators_difference = {}
        indicators_sorted = None
        for indicator in indicators:
            indicators_difference[indicator] = difflib.SequenceMatcher(None, self.stemming(indicator_slot),
                                                                       self.stemming(indicator)).ratio()
            indicators_sorted = sorted(indicators_difference, key=indicators_difference.get, reverse=True)

        if indicators_difference[indicators_sorted[0]] > 0.7:
            return indicators_sorted[0]
        else:

            dispatcher.utter_message(messages.indicator_not_valid)

            self.get_similar_indicators(indicator_slot, dispatcher)

    def get_most_similar_location(self, location_slot):
        max_location = {"value": '', "ratio": 0}
        for location in locations_check:
            difference = difflib.SequenceMatcher(None, self.stemming(location_slot),
                                                 self.stemming(location)).ratio()
            if (difference > max_location["ratio"]):
                max_location["ratio"] = difference
                max_location["value"] = location

        if (self.debug):
            print(max_location["value"], max_location["ratio"])
        return max_location["value"], max_location["ratio"]

    def dont_understand_message(self, dispatcher):
        dispatcher.utter_message(messages.sorry_ask_again)

    def calculate_confidence_location(self, location_slot):
        if location_slot is not None:
            for location in locations_check:
                difference = difflib.SequenceMatcher(None, self.stemming(location_slot.lower()),
                                                     self.stemming(location.lower())).ratio()
                if (difference > self.location_confidence["confidence"]):
                    self.location_confidence["confidence"] = difference
                    self.location_confidence["value"] = location

    def calculate_confidence_indicator(self, indicator_slot):
        if indicator_slot is not None:

            for indicator in indicators_check.keys():
                difference = difflib.SequenceMatcher(None, self.stemming(indicator_slot),
                                                     self.stemming(indicator)).ratio()
                if (difference > self.indicator_confidence["confidence"]):
                    self.indicator_confidence["confidence"] = difference
                    self.indicator_confidence["value"] = indicators_check[indicator]

            for indicator in indicators:
                difference = difflib.SequenceMatcher(None, self.stemming(indicator_slot),
                                                     self.stemming(indicator)).ratio()
                if (difference > self.indicator_confidence["confidence"]):
                    self.indicator_confidence["confidence"] = difference
                    self.indicator_confidence["value"] = indicator
        if (self.debug):
            print(str(self.indicator_confidence["confidence"]))
            print(str(self.indicator_confidence["value"]))

    def show_information(self, dispatcher, date_slot, location_slot, indicator, response_indicator):
        date = None
        if (indicator):
            if (location_slot != None):
                geographic_location_code, geographic_location_name = self.getGeographical(location_slot,
                                                                                          response_indicator,
                                                                                          dispatcher)
            if (geographic_location_code is None):
                location_slot = None
            else:
                date = self.getDate(date_slot, response_indicator, dispatcher)
                if (not date):
                    return [SlotSet("var_Date", None)]
        if (geographic_location_code and date and indicator):  # If all params where found.
            dispatcher.utter_message("Aquí tienes la información:")

            DBDate = date

            # Requests to ISTAC API https://www3.gobiernodecanarias.org/istac/api/indicators/v1.0/
            response_all = requests.get(URL + indicators[
                indicator] + "/data?representation=GEOGRAPHICAL[" + geographic_location_code + "],MEASURE[ABSOLUTE],TIME[" + DBDate + "]").json()

            print(URL + indicators[
                indicator] + "/data?representation=GEOGRAPHICAL[" + geographic_location_code + "],MEASURE[ABSOLUTE],TIME[" + DBDate + "]")

            if (response_all['observation'] and response_all['observation'][0]):
                res_data = str(response_all['observation'][0])
                res_unit = response_indicator['dimension']['MEASURE']['representation'][0]['quantity']['unit']['es']
                res_unitSymbol = {"start": "", "end": "", "description": ""}
                res_unit_multiplier = response_indicator['dimension']['MEASURE']['representation'][0]['quantity']['unitMultiplier']['es'].lower()

                if ('unitSymbol' in [str(keys) for keys in
                                     response_indicator['dimension']['MEASURE']['representation'][0][
                                         'quantity'].keys()]):
                    unitSymbol = response_indicator['dimension']['MEASURE']['representation'][0]['quantity'][
                        'unitSymbol']
                    res_unitSymbolPosition = \
                        response_indicator['dimension']['MEASURE']['representation'][0]['quantity'][
                            'unitSymbolPosition']
                    if (res_unitSymbolPosition == "START"):
                        res_unitSymbol["start"] = unitSymbol
                        res_unit_multiplier = ' de ' + res_unit_multiplier + ' ' if res_unit_multiplier != 'unidades' else ''
                    else:
                        res_unitSymbol["end"] = unitSymbol
                        res_unit_multiplier = ' ' + res_unit_multiplier + ' de ' if res_unit_multiplier != 'unidades' else ''
                else:
                    res_unitSymbol["description"] = ' (' + res_unit.lower() + ')'
                    res_unit_multiplier = ' ' + res_unit_multiplier + ' ' if res_unit_multiplier != 'unidades' else ''

                res_interperiod = self.get_annual_rate(indicator, geographic_location_code, DBDate)
                dispatcher.utter_message("*{} en {} en {}: {}{}{}{}{}{}*".format(
                    indicator,
                    geographic_location_name,
                    self.translate_date(date, response_indicator),
                    res_unitSymbol["start"],
                    self.format_number(res_data),
                    res_unit_multiplier,
                    res_unitSymbol["end"],
                    res_unitSymbol["description"],
                    res_interperiod

                ))

                self.you_can_also_ask(indicator, response_indicator, dispatcher)
                self.get_similar_indicators(indicator, dispatcher)



        return [SlotSet("var_What", self.indicator_confidence["value"]),
                SlotSet("var_Loc", self.location_confidence["value"]),
                SlotSet("var_Date", date_slot)]

    def format_number(self, number):
        formatted_number = locale.format('%.2f', float(number), 1)
        formatted_number = re.sub(',00$', '', formatted_number)
        return formatted_number

    def translate_date(self, date, response_indicator):
        for date_indicator in response_indicator['dimension']['TIME']['representation']:
            if (date == date_indicator['code']):
                return date_indicator['title']['es'].lower()

    def get_location_granularities(self, response_indicator):
        res_granularities = response_indicator['dimension']['GEOGRAPHICAL']['granularity']
        granularities = []
        location_granularities = ''

        for granularity in res_granularities:
            if granularity not in granularities:
                granularities.append(granularity['title']['es'].lower())

        for i in range(0, len(granularities)):
            if (i == 0):
                location_granularities = location_granularities + granularities[i]
            elif ((i + 1) < len(granularities)):
                location_granularities = location_granularities + ', ' + granularities[i]
            else:
                conjunction = " y "
                if (granularities[i].startswith('i')):
                    conjunction = " e "
                location_granularities = location_granularities + conjunction + granularities[i]



        return location_granularities

    def get_annual_rate(self, indicator, geographic_location_code, DBDate):
        response_annual_rate = requests.get(URL + indicators[
            indicator] + "/data?representation=GEOGRAPHICAL[" + geographic_location_code + "],MEASURE[ANNUAL_PUNTUAL_RATE],TIME[" + DBDate + "]").json()

        if (response_annual_rate['observation'] and self.is_number(response_annual_rate['observation'][0])):
            return messages.annual_puntual_rate.format(self.format_number(response_annual_rate['observation'][0]))
        else:
            response_annual_rate = requests.get(URL + indicators[
                indicator] + "/data?representation=GEOGRAPHICAL[" + geographic_location_code + "],MEASURE[ANNUAL_PERCENTAGE_RATE],TIME[" + DBDate + "]").json()
            if (response_annual_rate['observation'] and self.is_number(response_annual_rate['observation'][0])):
                return messages.annual_percentage_rate.format(self.format_number(response_annual_rate['observation'][0]))
        return ""

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def you_can_also_ask(self, indicator, response_indicator, dispatcher):
        if (self.indicator_has_sex(indicator)):
            dispatcher.utter_message(messages.you_can_also_ask_sex.format(
                self.get_location_granularities(response_indicator)
            ))
        else:
            dispatcher.utter_message(messages.you_can_also_ask.format(
                self.get_location_granularities(response_indicator)
            ))

    def indicator_has_sex(self, indicator):
        indicator = indicator.replace(". Mujeres", "")
        indicator = indicator.replace(". Hombres", "")
        if (indicator in indicators_with_sex):
            return True
        return False

    def date_get_year(self, date):
        return re.match(REGEX_HAS_YEAR, date)

class ActionAskHowCanHelp(Action):
    def name(self):
        return 'action_ask_howcanhelp'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(messages.greeting[0])
        dispatcher.utter_message(messages.greeting[1])
        return [Restarted()]


class ActionYes(Action):
    def name(self):
        return 'action_yes'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Perfecto!")
        return []


class ActionNo(Action):
    def name(self):
        return 'action_no'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(messages.dont_worry)
        return [Restarted()]


class ActionMujeres(Action):
    def name(self):
        return 'action_mujeres'

    def run(self, dispatcher, tracker, domain):

        if tracker.get_slot("var_What") != None and re.match(r"(.*)(mujeres|Mujeres|Hombres|hombres)",
                                                             tracker.get_slot("var_What")):

            return [SlotSet("var_What", tracker.get_slot("var_What").lower().replace("hombres", "mujeres")),
                    SlotSet("var_Loc", tracker.get_slot("var_Loc")),
                    SlotSet("var_Date", tracker.get_slot("var_Date"))]
        elif (tracker.get_slot("var_What") == None):
            buttons = []
            for indicador in mujeres_indicadores:
                buttons.append({"title": indicador, "payload": indicador})

            dispatcher.utter_button_message(
                messages.similar_indicators_women,
                buttons,
                button_type="vertical")

            return [SlotSet("var_What", "listen_consulta_mujeres"),
                    SlotSet("var_Loc", tracker.get_slot("var_Loc")),
                    SlotSet("var_Date", tracker.get_slot("var_Date"))]
        else:
            return [SlotSet("var_What", tracker.get_slot("var_What") + " Mujeres"),
                    SlotSet("var_Loc", tracker.get_slot("var_Loc")),
                    SlotSet("var_Date", tracker.get_slot("var_Date"))]


class ActionHombres(Action):
    def name(self):
        return 'action_hombres'

    def run(self, dispatcher, tracker, domain):

        if tracker.get_slot("var_What") != None and re.match(r"(.*)(mujeres|Mujeres|Hombres|hombres)",
                                                             tracker.get_slot("var_What")):

            return [SlotSet("var_What", tracker.get_slot("var_What").lower().replace("mujeres", "hombres")),
                    SlotSet("var_Loc", tracker.get_slot("var_Loc")),
                    SlotSet("var_Date", tracker.get_slot("var_Date"))]
        elif (tracker.get_slot("var_What") == None):

            buttons = []
            for indicador in hombres_indicadores:
                buttons.append({"title": indicador, "payload": indicador})

            dispatcher.utter_button_message(
                messages.similar_indicators_men,
                buttons,
                button_type="vertical")

            return [SlotSet("var_What", "listen_consulta_hombres"),
                    SlotSet("var_Loc", tracker.get_slot("var_Loc")),
                    SlotSet("var_Date", tracker.get_slot("var_Date"))]
        else:
            return [SlotSet("var_What", tracker.get_slot("var_What") + " Hombres"),
                    SlotSet("var_Loc", tracker.get_slot("var_Loc")),
                    SlotSet("var_Date", tracker.get_slot("var_Date"))]


class ActionHelp(Action):
    def name(self):
        return 'action_help'

    def run(self, dispatcher, tracker, domain):
        for help_message in messages.help:
            dispatcher.utter_message(help_message)
        return [Restarted()]


class ActionSaludoPixelPerfect(Action):
    def name(self):
        return 'action_saludo_pixelperfect'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(messages.saludo_pixelperfect)
        return [Restarted()]

class ActionListadoIndicadores(Action):
    def name(self):
        return 'action_listado_indicadores'

    def run(self, dispatcher, tracker, domain):
        if len(indicators) > 0:
            list_indicators = messages.indicators_list + '\n'

        for indicator in indicators.keys():
            if (len(list_indicators + "\n" + indicator)  < MAX_LENGTH_TELEGRAM_MESSAGE):
                list_indicators = list_indicators + "\n" + indicator
            else:
                dispatcher.utter_message(list_indicators)
                list_indicators = "" + indicator
        dispatcher.utter_message(list_indicators)
        return [Restarted()]