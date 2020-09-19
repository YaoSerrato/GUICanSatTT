# Interfaz de usuario para la recepción de telemetría proveniente del CanSat.
Este repositorio contiene el código en *python* desarrollado para la interfaz gráfica de usuario del CanSat. Para la interfaz se utilizó la paquetería PyQt5. Esta interfaz se
ejecuta en una computadora en la estación en Tierra y está conectada a una antena que recibe datos de telemetría provenientes del CanSat. La interfaz crea y guarda un archivo
*.csv* que contiene los datos receibidos por la estación en Tierra durante la misión del CanSat.

Cabe mencionar que la interfaz, y en general el CanSat completo, se diseñaron bajo los requerimientos proporcionados por la competencia
[Annual CanSat Competition](http://www.cansatcompetition.com/) en su edición 2019.

## Datos de telemetría
El microcontrolador del CanSat se encarga de formar los paquetes de datos y los direcciona, por medio de un módulo XBee, a la antena de abordo, la cual se encarga de transmitirlos
a la estación en Tierra. La siguiente tabla muestra los datos que son trasmitidos desde el CanSat a una frecuencia de 1 [Hz].

No. | Parámetro                         | Descripción                                                         | Unidad
--- | --------------------------------- | ------------------------------------------------------------------- | -------------------
1   | Número de paquete                 | Indica el número de paquete que se está transmitiendo.              | -
2   | Tiempo de misión                  | Indica el tiempo en que se envía el paquete.                        | s
3   | Ángulo *pitch*                    | Valor de inclinación alrededor del eje x.                           | °
4   | Ángulo *roll*                     | Valor de inclinación alrededor del eje y.                           | °
5   | Ángulo *azimuth*                  | Valor del GDL de azimut del Sistema de Registro de Descenso.        | °
6   | Presión barométrica               | Valor de presión barométrica de la atmósfera.                       | Pa
7   | Temperatura                       | Temperatura del aire.                                               | °C
8   | Altura                            | Estimación de altura con respecto al sitio de lanzamiento.          | m
9   | Número de satélites               | Número de satélites detectados por el GPS.                          | -
10  | Latitud                           | Valor de latitud otorgado por el GPS.                               | °
11  | Longitud                          | Valor de longitud otorgado por el GPS.                              | °
12  | Altitud                           | Valor de altitud otorgado por el GPS con respecto al nivel del mar. | msnm
13  | Velocidad de rotación del rotor   | Velocidad angular de las hélices.                                   | rpm
14  | Estado de la máquina de estados   | Estado actual de la misión.                                         | -

## Componentes de la interfaz
La interfaz tiene tres ventanas:
  1. **Ventana de configuración**: ventana donde el usuario especifica el nombre y la ruta donde desea guardar el archivo *.csv* con los datos de la misión, así como
  el puerto de comunicación serial al cuál está conectada la antena y el XBee de la estación en Tierra. La ventana de configuración también le proporciona al usuario la opción
  de configurar al CanSat previo al lanzamiento. Esta configuración previa contempla la adquisición de los valores de referencia para la altura y la inclinación del CanSat en
  los tres ejes (*pitch*, *roll* y *azimuth*), y también el sistema se asegura de que todos los mecanismos están colocados en sus configuraciones iniciales correctas. La siguiente
  imagen muestra cómo luce la ventana de configuración.
  
  <p align="center">
    <img height="500" src="https://github.com/YaoSerrato/GUICanSatTT/blob/master/configwindow.png">
  </p>
  
  2. **Ventana de monitoreo**: ventana principal de la interfaz que se muestra cuando el usuario ha terminado de operar la ventana de configuración. En esta ventana se
  despliegan los datos del CanSat conforme los va recibiendo la estación en Tierra. La ventana de monitoreo despliega los datos de manera numérica y gráfica. La siguiente
  imagen muestra cómo luce esta ventana.
  
  <p align="center">
    <img height="500" src="https://github.com/YaoSerrato/GUICanSatTT/blob/master/monitorwindow.png">
  </p>
  
  3. **Ventana de visualización**: una vez que el CanSat toca Tierra de nuevo, la ventana de monitoreo deja de desplegar datos, se crea y guarda el archivo *.csv* en la ruta
  especificada, se cierra la ventana de monitoreo y se abre la ventana de visualización. Esta última ventana le muestra al usuario, de manera más interactiva, los datos recibidos
  durante la misión. El usuario puede escoger qué datos ver, hacer acercamientos, desplazar la gráfica y guardarla en un archivo de imagen. La siguiente figura muestra a la 
  ventana de visualización.
  
  <p align="center">
    <img height="500" src="https://github.com/YaoSerrato/GUICanSatTT/blob/master/seewindow.png">
  </p>
  
  ## Multiprocesos
En ediciones anteriores del concurso de CanSats tuvimos el problema de que la interfaz perdía paquetes de datos debido a que tomaba mucho tiempo graficar los que ya
había recibido. Esto se debía a que ambas operaciones se realizaban de manera seciencial: recepción y después graficación. El proceso de graficación, por lo
demandante que es en términos de recursos computacionales, es más lento que el proceso de recepción de datos. Para solucionar este problema en el desarrollo del CanSat se 
siguió un enfoque de multiprocesos: se reservó un proceso para la recepción de datos y otro para la graficación. Ambos procesos se comunicaban entre sí por medio de una
fila. Las tramas de datos recibidas se iban acumulando en la fila y, cuando el proceso de graficación terminaba de desplegar los datos previos, tomaba todos los que se llegaron
a acumular hasta ese momento en la fila y los desplegaba. De esta forma, la graficación de datos ya no bloqueaba a la recepción de datos y viceversa. La siguiente imagen muestra
un diagrama de este esquema de multiprocesos.

  <p align="center">
    <img height="600" src="https://github.com/YaoSerrato/GUICanSatTT/blob/master/multiprocess.png">
  </p>
  
  
