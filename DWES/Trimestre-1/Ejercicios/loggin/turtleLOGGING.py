'''

Los componentes principales del módulo logging:

Logger
Handler
Filter
Formatter


Las instancias se agrupan en la instancia LogRecord y se intercambian dentro de la misma


Logger
-------------------------------------------------------------------------------------
Los logger registran las acciones durante la ejecución de un programa.
No se pueden usar directamente como instancia,
sino que se los solicita con la función logging.getLogger(nombre_del_logger)



Handler
-------------------------------------------------------------------------------------
Los handler recopilan la información del logger y la reenvían.
El handler es una clase básica que determina cómo actúa la interfaz de las instancias del handler.
Para establecer el destino, debes utilizar el tipo de handler correspondiente.
StreamHandler envía los datos a las secuencias, mientras que FileHandler los envía a los archivos.

Mediante el métodosetLevel() puedes establecer el nivel mínimo de gravedad que un mensaje
de registro requiere para ser reenviado a dicho handler.


Formatter
-------------------------------------------------------------------------------------
Los formatter (objetos de formato), a diferencia de los handler, se pueden utilizar directamente
como instancias en el código de la aplicación. Con estas instancias puedes determinar el formato
en el que se emitirá la notificación en el archivo de registro.


Filter
-------------------------------------------------------------------------------------
Los filter permiten crear definiciones aún más precisas para los mensajes de salida.
Establece primero los filtros y, después, añádelos al handler o al logger correspondiente mediante
el método addFilter().


'''


##import turtle
##import logging
##turtle.bgcolor("green")
##turtle.fd(30)
##turtle.lt(90)
##turtle.fd(50)
##logging.info('It is going well.')
##turtle.circle(50)
##logging.error('Oops, looks like you’re running in circles.')

'''
FORMATO DEL MENSAJE DE LOGGING
[nivel de gravedad]:[origen del mensaje]:[mensaje].

'''
import logging, turtle
logging.basicConfig(level=logging.DEBUG)

##turtle.bgcolor("green")
##turtle.fd(30)
##turtle.lt(90)
##turtle.fd(50)
##logging.info('It is going well.')
##turtle.circle(50)
##logging.error('Oops, looks like you’re running in circles.')

'''
HANDLER
----------------------------------------------------------------------------------------
Guardar el logging de Python en un archivo
El método logging to file de Python funciona de dos maneras:
- puedes crear un archivo de registro mediante la configuración básica
- o utilizar el handler.


FileHandler es una instancia de la clase de logging y actúa junto con la instancia de registro.
Se encarga de determinar qué datos de registro se envían, adónde y en qué formato.
Además de FileHandler, existen otros handler de logging como StreamHandler y NullHandler.
Sin embargo, para evaluar posteriormente los datos de registro, se recomienda crear un archivo
de registro.

Para crear un FileHandler que inserte mensajes DEBUG en un archivo, sigue estos pasos:

'''


import logging
#CREAMOS  NUESTRO LOGGER LLAMADO: ejemplo_Log
logger = logging.getLogger('ejemplo_Log')
#ESTABLECEMOS EL NIVEL A MODO DEBUG, DE ESTA FORMA MANEJAMOS TODOS LO NIVELES DE LOG
logger.setLevel(logging.DEBUG)
#EN FH CREAMOS UNA INSTANCIA DE FILEHADLER CON EL NOMBRE DEL ARCHIVO O FICHERO PARA GUARDAR EL LOG
fh = logging.FileHandler('debug.log')
#FIJAROS QUE ESTABLECEMOS PARA EL FH (FILEHANDLER) EL NIVEL DE CAPTURA.LO PONEMOS AL MÍNIMO 
fh.setLevel(logging.DEBUG)
#AÑADIMOS EL FILEHANDLER A NUESTRO LOGGER
logger.addHandler(fh)

#LANZAMOS VARIOS MENSAJES DE LOG A NUESTRO LOGER
logger.debug('mensaje debug')
logger.info('mensaje info')
logger.warning('mensaje warning')
logger.error('mensaje error')
logger.critical('mensaje critical')


'''
FORMATTER
----------------------------------------------------------------------------------------
Un ejemplo de cómo puedes configurar el formato utilizando los atributos del formatter.
En la ventana del bloc de notas del archivo debug.log se indican los mensajes de registro
con los datos de fecha, hora, nombre del logger, nivel de registro y mensaje.

'''
#
#import logging
##CREAMOS  NUESTRO LOGGER LLAMADO: ejemplo_Log
#logger = logging.getLogger('ejemplo_Log')
##ESTABLECEMOS EL NIVEL A MODO DEBUG, DE ESTA FORMA MANEJAMOS TODOS LO NIVELES DE LOG
#logger.setLevel(logging.DEBUG)
##EN FH CREAMOS UNA INSTANCIA DE FILEHADLER CON EL NOMBRE DEL ARCHIVO O FICHERO PARA GUARDAR EL LOG
#fh = logging.FileHandler('debug_FORMATEADO.log')
##FIJAROS QUE ESTABLECEMOS PARA EL FH (FILEHANDLER) EL NIVEL DE CAPTURA.LO PONEMOS AL MÍNIMO 
#fh.setLevel(logging.DEBUG)
##AÑADIMOS EL FILEHANDLER A NUESTRO LOGGER
#logger.addHandler(fh)
##CREAMOS EL FORMATER PARA DARLE NUESTRO FORMATO PROPIO AL LOG
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
##AÑADIMOS EL FORMATER A NUESTRO HANDLER
#fh.setFormatter(formatter)
##NO HACE FALTA AÑADIRLO DE NUEVO
##AÑADIMOS EL HANDLER OTRA VEZ A NUESTRO LOGGER
##logger.addHandler(fh)
#
##LANZAMOS VARIOS MENSAJES DE LOG A NUESTRO LOGER
#logger.debug('mensaje debug')
#logger.info('mensaje info')
#logger.warning('mensaje warning')
#logger.error('mensaje error')
#logger.critical('mensaje critical')


'''

RESUMEN
----------------------------------------------------------------------------------------
El logging de Python es una herramienta útil para prevenir errores,
controlar los ataques de piratas informáticos o, simplemente, llevar a cabo análisis.
Mientras que otros lenguajes de programación registran los datos de tercera mano,
el módulo logging de Python forma parte de la biblioteca estándar del lenguaje.
Al incorporar este método en el código, se crean mensajes de registro de diferentes niveles,
tanto en los archivos como en la consola. Las funciones de formato y filtro, así como los handler,
permiten al usuario configurarlo de manera fácil. Para simplificar todavía más el trabajo con los
archivos de registro en Python, asegúrate de asignar nombres sencillos a los logger y a sus
directorios.

'''



