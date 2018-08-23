# Changelog nlu train dataset

# nlu_train_v23.json

- Añadidos ejemplos del tipo:
`Hola! Quiero saber los datos del paro en Tenerife` y `Dame el paro en Canarias`

# nlu_train_v22.json

- Ejemplos con cemento:
```json
 {
                "text": "cemento",
                "intent": "inform",
                "entities": [
                    {
                        "end": 7,
                        "entity": "var_What",
                        "start": 0,
                        "value": "Venta mayor de cemento"
                    }
                ]
            }
```

- Añadidos más ejemplos de "empleo" como sinónimo de "Tasa de empleo"

# nlu_train_v21.json

- Ejemplos con todos los tipos de indicadores.
- Ejemplos con localidades en solitario para que no haga falta añadir una preposición, para que el bot lo entienda con una variable de tipo **var_Loc**:
```json
            {
                "text": "Gran Canaria",
                "intent": "inform",
                "entities": [
                    {
                        "end": 12,
                        "entity": "var_Loc",
                        "start": 0,
                        "value": "Gran Canaria"
                    }
                ]
            },
```
- Sinónimos para la Seguridad Social (SS).
- Ejemplos con "hasta luego".
- Añadida la palabra "opciones" a la intención **Ayuda**.
- Añadidos ejemplos de tipo:
    - TIME: 2011
    - LOCATION: La Laguna
    - ENTITY: Afiliaciones a la Seguridad Social

