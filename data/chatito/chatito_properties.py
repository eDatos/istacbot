# Para cada fichero partial, hay que añadir una entrada con su nombre y especificar el número de veces que
# queremos que Chatito añada al dataset de entrenamiento los ejemplos generados con ese fichero.
#
# Esto es necesario porque hay entidades como respuestaSi que solo tienen un ejemplo y Rasa necesita más de uno para
# aprender correctamente. Además, Chatito, a partir de la versión 2.1.0 no soporta de forma nativa generar ejemplos
# repetidos. Sin embargo, los cambios introducidos en la versión 2.1.1 son necesarios porque añaden soporte para
# caracteres internacionales como "ñ".

partials = {
    "istacbot-partial-all.chatito": 1,
    "istacbot-partial-date.chatito": 7,
    "istacbot-partial-Despedida.chatito": 7,
    "istacbot-partial-loc.chatito": 7,
    "istacbot-partial-RespuestaNo.chatito": 7,
    "istacbot-partial-RespuestaSi.chatito": 7,
    "istacbot-partial-SaludoPixelPerfect.chatito": 7,
    "istacbot-partial-what.chatito": 4,
    "istacbot-partial-Saludo.chatito": 7,
    "istacbot-partial-Ayuda.chatito": 4,
    "istacbot-partial-Mujeres.chatito": 7,
    "istacbot-partial-Hombres.chatito": 7,
    "istacbot-partial-ListadoIndicadores.chatito": 3,
    "istacbot-partial-inform.chatito": 1
}