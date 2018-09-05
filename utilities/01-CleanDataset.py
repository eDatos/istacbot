
# coding: utf-8

# # Limpieza del dataset
# 
# La generación del dataset se hace de forma automática empleando la herramienta chatito (https://rodrigopivi.github.io/Chatito/). Sin embargo, este tipo de generación puede dar lugar a frases sin demasiado sentido como, por ejemplo:
# 
# ```javascript
#       {
#         "text": "Quiero la poblacion del Arico del Enero por favor",
#         "intent": "inform",
#         "entities": [
#           {
#             "end": 19,
#             "entity": "var_What",
#             "start": 7,
#             "value": "la poblacion"
#           },
#           {"end": 29, "entity": "var_Loc", "start": 24, "value": "Arico"},
#           {"end": 39, "entity": "var_Date", "start": 34, "value": "Enero"}
#         ]
# ```
# 
# En este las preposiciones: '**del** Enero' y '**del** Arico' están mal.
# 
# Este notebook tiene como objetivo eliminar del dataset todos aquellos ejemplos en los que la preposición este mal.

# In[46]:


import json
import re

with open('nlu_train.json',  encoding="utf8") as json_data:
    dataset = json.load(json_data)

original_dataset = len(dataset['rasa_nlu_data']['common_examples'])

patterns = []
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for mes in meses:
    patterns.append(re.compile(r".*durante el " + mes + ".*"))
    patterns.append(re.compile(r".*del " + mes + ".*"))
patterns.append(re.compile(r".*en hoy.*"))
patterns.append(re.compile(r".*del hoy.*"))
patterns.append(re.compile(r".*durante hoy.*"))
patterns.append(re.compile(r".*durante el hoy.*"))

este_date = ["este trimestre", "este año", "este mes"]

for este in este_date:
    patterns.append(re.compile(r".*durante el " + este + ".*"))
    patterns.append(re.compile(r".*del " + este + ".*"))

patterns.append(re.compile(r".*del La.*"))
patterns.append(re.compile(r".*del El.*"))

start_position = 15

remove_texts = []

for index in range(start_position, len(dataset['rasa_nlu_data']['common_examples'])):
    text = dataset['rasa_nlu_data']['common_examples'][index]['text']
    for pattern in patterns:
        if re.match(pattern, text):
            remove_texts.append(index)

for index in sorted(remove_texts, reverse=True):
    del dataset['rasa_nlu_data']['common_examples'][index]

print(len(dataset['rasa_nlu_data']['common_examples']))
print(original_dataset)

with open('datasetLimpio.json', 'w', encoding="utf8") as outfile:
    json.dump(dataset, outfile, ensure_ascii=False)



