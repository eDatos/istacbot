import json

with open('../data/nlu_train.json', mode="r", encoding="utf-8") as json_data:
    nlu_train = json.load(json_data)

    for synonym_entity in nlu_train["rasa_nlu_data"]["entity_synonyms"]:
        print("\"" + synonym_entity["value"] + "\": ", end="")
        print( synonym_entity["synonyms"], end=",\n")

