
infAplicacion = """
PyPulperiaManager es un software de código abierto desarrollado por WinstXD320, para almacenar y
gestionar datos de una forma sencilla. Para descargar y ver más apliaciones gratuitas, visita la web  
https://winstxd320.github.io/
"""

comandos = """
información para el usuario:

Esta aplicación tiene por defecto una tabla llamada productos, en donde se pueden almacenar distintos datos
relaconados a un producto. Los campos de la tabla son ID, Nombre, cantidad, NombreProveedor.  

| Id   | Nombre   | Cantidad   | NombreProveedor   |
|------|----------|------------|-------------------|

campo Id --> Se guardan datos de tipo Integer(números enteros), esto para identificar de fomra unica 
al producto en la tabla de datos. El número tiene que ser unico, este no se puede repetir. 

Nombre --> Se guardan datos de tipo cadena de texto. En el campo Nombre se guarda el nombre del producto.

Cantidad --> Se guardan datos de tipo cadena de texto. En el campo cantidad se pueden ingresar datos númericos, representados como 
cadena de texto; a su vez estos datos númericos puede estar reprentados por unidades de medida, como Libras(LB), Cajas(CJ), Unidades(UND).

| Id   | Nombre   | Cantidad   | NombreProveedor   |
|------|----------|------------|-------------------|
|  001 |   Arroz  |  100Lb     |EmpresaLacteos S.A.|
|  002 |   Dulces |   50CJ     |EmpresaDulces S.A. |

NombreProveedor --> Se guarda datos de tipo cadena de texto. Puedes guardar el nombre del proveedor de producto. 

Comandos:

Comandos de usuarios estandares:

input data --> Ingresa datos a la tabla de productos.
update data --> Actualiza los datos ingresaros en la tabla de productos.
delete data --> Borra los datos de la tabla de productos.
consulte table --> Muestra la tabla de productos.

Comandos de configuración:

conftable --> Cambia el color de la tabla.
    | bluetable --> Cambia el color de la tabla a azul.
    | yellowtable --> Cambia el color de la tabla a amarillo. 
    | greentable --> Cambia el color de la tabla a verde.
    | whitetable --> Cambia el color de la tabla a blanco.
    
confstyle --> Cambia el estílo de la tabla.
    
    | plain
    | simple
    | github
    | grid    

avanced user.on --> Activa la función de usuarios avanzados
avanced user.off --> Desactiva la función de usuarios avanzados y vuelve a la función estadar con la tabla productos.

La función usuarios avanzados fue pensada para aquellos usuarios que desean ingresar instrucciones del Lenguaje de Definición de Datos
(DDL). 

Una una vez ingresado el 'comando avanced user.on', el programa le avisara por medio de un mensaje en consola, que el modo usuarios avanzados esta 
activado.

Comandos de usuarios avanzados:

au create table --> Crea una nueva tabla por medio de la  instrucción sql CREATE TABLE.
au input data --> Almacena datos por medio de la instrucción sql INSERT.
au update data --> Actualiza los datos por medio de la instrucción sql UPDATE.
au delete data --> Borra los datos de la tabla por medio de la instrucción sql DELETE.
au delete table --> Elimina una tabla de datos por medio de la instrucción sql DROP.
au consulte table --> Muestra una tabla ya creada. 
tables --> Muestra todas las tablas creadas por el usuario.
    | La tabla sqlite_sequence rastrea la información sobre las secuencias que se utilizan para generar valores en columnas con la propiedad AUTOINCREMENT.
"""
