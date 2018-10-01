# Para cada fichero partial, hay que añadir una entrada con su nombre y especificar el número de veces que
# queremos que Chatito añada al dataset de entrenamiento los ejemplos generados con ese fichero.
#
# Esto es necesario porque hay entidades como respuestaSi que solo tienen un ejemplo y Rasa necesita más de uno para
# aprender correctamente. Además, Chatito, a partir de la versión 2.1.0 no soporta de forma nativa generar ejemplos
# repetidos. Sin embargo, los cambios introducidos en la versión 2.1.1 son necesarios porque añaden soporte para
# caracteres internacionales como "ñ".

partials = {
    "slot-date.chatito": 7,
    "entidad-Despedida.chatito": 7,
    "slot-loc.chatito": 7,
    "entidad-RespuestaNo.chatito": 7,
    "entidad-RespuestaSi.chatito": 7,
    "entidad-SaludoPixelPerfect.chatito": 7,
    "slot-what.chatito": 4,
    "entidad-Saludo.chatito": 7,
    "entidad-Ayuda.chatito": 4,
    "entidad-Mujeres.chatito": 7,
    "entidad-Hombres.chatito": 7,
    "entidad-ListadoIndicadores.chatito": 3,
    "entidad-Inform.chatito": 1
}