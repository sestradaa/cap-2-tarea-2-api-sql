# tarea final

## Configuración del Entorno y Ejecución del Proyecto Flask

Este documento describe los pasos necesarios para configurar un entorno de desarrollo virtual, instalar las dependencias del proyecto, y ejecutar la aplicación Flask.

### Prerrequisitos

Asegúrate de tener instalados los siguientes requisitos en tu máquina:

- Python 3.x
- `pip` (la herramienta de instalación de paquetes de Python)
- `virtualenv` (para crear entornos virtuales)

### 1. Crear un Entorno Virtual, activar el Entorno Virtual com git-bash, instalar las dependencias del requirements.txt y por último ejecutar el aplicativo Flask

```bash
virtualenv .env
source .env/Scripts/activate
pip install -r requirements.txt
python estudiante.py
pip freeze > requirements.txt   
python app.py
```

### *Para desactivar el entorno virtual* `deactivate`

## (SENIOR DEVELOPER) POR FAVOR CORREGIR LOS SIGUIENTES ERRORES: 
## Examen final Python API Developer
## pregunta 1
## Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar brevemente.
Python al ser un lenguaje inteligente  y tener una gran cantidad de bibliotecas cuenta con los siguientes casos de uso:

1. Procesamiento de Datos: Una de las especialidades de Python es el tratamiento de la data antes de trabajarla, para ello realiza una limpieza (elimina, reemplaza o  formatea valores nulos) y transformación de datos (agrupa, crea nuevos campos o asigna nuevas características a los datos).
2. Visualización de Datos: Gracias a las gráficos dinámicos, colores, diseños atractivos, herramientas de importación y exportación de datos podemos explicar, debati, comunicar e interactuar con otros usuarios nuestro proyecto, entre las librerías populares tenemos: Matplotlib: Gráficos estáticos, Seaborn (gráficos con mejor diseño y de gran complejidad) , Plotly (gráficos dinámicos, pudiendo ser vistos en la web)

3. Machine Learning: Python nos permite crear modelos estadisticos para realizar predicciones, probabilidades sobre base de datos, los cuales permiten mejorar cual proceso de negocio, usando biblioteca como: Scikit-learn ( algoritmos para clasificación, reducción de dimensionalidad , regresión, clustering),  PyTorch (desarrollo de modelos avanzados), etc.
4. Bases de Datos: Permite la conexión a diversas base de datos relacionales y no relacionales, ya importarlas, procesarlas, generar modelos estaditicos, accederlas x medio de api, visualizarlas en un proyecto web. Como por ejemplo: SQLAlchemy, SQLite, PyMongo(bases de datos NoSQL), etc.

5. Desarrollo de Aplicaciones de Datos: Permite crear interfaces amigables de tipo escritorio y web, facilitando la interacción con el usuario, ya sea x medio de reportes, pantallas, gráficos, etc. De una manera menos compleja a comparación de otros lenguajes.

## pregunta 2
## ¿Cómo se diferencian Flask de Django? Argumentar.
Son varias las diferencias,  Django es un framework ideal para proyectos web complejos, en cambio Flask para pequeñas aplicaciones web (single page applications, SPA). En tema de seguridad, la autenticación de usuarios de Django es muy superior,  incluye ORM, autenticación, administración, etc.
En velocidad ambos son buenos, muchos profesionales lo usan, pero Flask es más rápido que Django debido a su estructura minimalista, flexible
En API Rest, Flask es mejor, pero las API Rest de Django tienen la opción de convertirse en páginas HTML como endpoints.
Respecto a bases de datos Django tiene su propio ORM, modelos de datos, mientras Flask usa un conector de bases de datos externo y no cuenta con modelos propios de datos.

## pregunta 3
3. ¿Qué es un API? Explicar en sus propias palabras
API (Interfaz de Programación de Aplicaciones) es un medio muy usado e indispensable en la actualidad para comunicar diferentes aplicaciones o sistemas, para ello tiene reglas, protocolos, funciones, servicios, manuales, q en conjunto permiten saber como generar solicitudes y las respuestas q podemos recibir, para luego poder manipularlas en nuestro entorno de desarrollo. Usa métodos como post, get, put, delete, y recién parámetro de tipo path, query, body, etc.

## pregunta 4
4. ¿Cuál es la principal diferencia entre REST y WebSockets
La diferencia es que REST recibe y responde a solicitudes, en cambio WebSockets permite la comunicación bidireccional entre el cliente y el servidor.

EL uso ideal de Rest es en infraestructuras escalables y operaciones CRUD sin estado.
EL uso ideal de WebSockets es para comunicación en tiempo real, bidireccional y con baja latencia
 
## pregunta 5
5. Describir un ejemplo de API comercial y como funciona – usar otros ejemplos no vistos en el curso		

La API de PayPal, permite a las empresas aceptar pagos (transferencias, compras en linea) en línea de manera segura y eficiente,  facilitando la venta de productos o servicios en línea desde la comodidad de su casa.
Teniendo el cliente que agregar sus productos al carrito de compras y procede al pago en el sitio web, luego la aplicación proporciona los detalles del pago (monto, moneda, etc.) para poder procesar la compra.
El cliente es redirigido a la página de PayPal, donde puede iniciar sesión en su cuenta de PayPal y autorizar el pago.
PayPal procesa el pago y, si es aprobado, devuelve una respuesta con la confirmación de la transacción.
La tienda recibe la confirmación del pago y puede proceder con el envío de los productos o la provisión del servicio.

Funcionamiento:
1: Registro y configuración inicial para tener una cuenta de comerciante credenciales de la API, como el Client ID y el Secret Key, que se usarán para autenticar las solicitudes de pago realizadas por la tienda en línea o aplicación.
2: Integración de la API en el sitio web o aplicación utilizando SDKs o bibliotecas proporcionadas por PayPal, que están disponibles en varios lenguajes de programación como JavaScript, Python, PHP, Ruby, etc.
3: Confirmación y ejecución del pago: Una vez que el cliente autoriza el pago en PayPal, el sistema de PayPal envía una respuesta de confirmación que se procesa en el sistema de la tienda. La tienda entonces ejecuta el pago (completa la transacción), y PayPal transfiere el dinero a la cuenta de PayPal del comerciante.
4: Transferencia de fondos
Después de que el pago ha sido confirmado, PayPal realiza la transferencia del monto correspondiente a la cuenta de PayPal del comerciante, descontando sus tarifas de procesamiento.		
		








