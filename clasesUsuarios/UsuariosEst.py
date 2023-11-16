import sqlite3 as bd
import sys
import os
import tabulate 


# Obtener la ruta al directorio que contiene UsuariosAv.py
ruta_modulo = os.path.abspath("clasesUsuarios")

# Agregar la ruta al principio de sys.path si no está presente
if ruta_modulo not in sys.path:
    sys.path.insert(0, ruta_modulo)

# Ahora puedes importar el módulo UsuariosAv desde main.py
import UsuariosAv as usAv

con = bd.connect("BdApp.bd")
cur = con.cursor()
#cur.execute("CREATE TABLE Productos(Id, Nombre, Cantidad, NombreProveedor)")
#res = cur.execute("SELECT name FROM sqlite_master") Verifica si la tabla a sido creada.


#Esta clase y la clase UsuariosAv() son un puente de entrada entre los datos y la base de datos (BdApp.bd) conectada a la aplicación.
#La clase UsuariosEst() contiene las funciones de usuarios estandares, ya que no permite ingresar directamente un comando sql para
#Crear una tabla, ya existe una tabla creada para este tipo de usuarios (Tabla Productos). Más información en la documentación que viene en el respositorio.
class UsuariosEst:
    
    def __init__(self) -> None:
        self._registros = []
        self._campos = []
        
    #El Metodo InsetarRgistros recibe los datos de la clase interfazUsuario() del metodo DatosEntrada.
    def InsertarRegistros(self, id, NombreProducto, Cantidad, NombreProveedor) -> None:
        con.execute("INSERT INTO Productos(Id, Nombre, Cantidad, NombreProveedor) VALUES ({}, '{}', '{}', '{}')".format(id, NombreProducto, Cantidad, NombreProveedor))
        con.commit()
        
    #El metodo actualizarRegistros recibe los datos de la clase interfazUsuarios() del metodo DtEntradaActualizarDatos().
    def actualizarRegistros(self, Nombre_colum, Id, Dato_nuevo) -> None:
        con.execute("UPDATE Productos SET {} = '{}' WHERE id = {}".format(Nombre_colum, Dato_nuevo ,Id))
        con.commit()
        
        print("Registro actualizado de forma correcta.")

    # El metodo MostrarConsulta muestra las consultas para ver todos los registros almacenados en la tabla por defecto (Productos)
    def MostrarConsulta(self) -> None:
        
    
       # Se agregan los campos a la lista self_campos
        for i in con.execute("PRAGMA table_info(Productos)").fetchall():
            self._campos.append(i[1])
        
       
       # Se crea una matriz bidimesionaln y se agregan los registos a la matriz
        for indice, datos in enumerate(con.execute("SELECT * FROM Productos")):
            registros = list(datos)
            self._registros.append([])
            for i in registros:
                self._registros[indice].append(i)
                
        print(tabulate.tabulate(self._registros, headers=self._campos, tablefmt="github"))
        con.commit()
        self.actualizarTabla()
        
        
    # El Metodo BorrarRegistros borra los datos almacenados en la tabla Productos por medio Id. Ingresado por el usuario
    def BorrarRegistros(self, id) -> None:
        for registros in cur.execute("SELECT * FROM Productos"):
            if not id in registros: # Esta condición verifica si el Id ingresado por existe en la tabla Productos. 
                print("El id '{}' no se encuentra registrado.".format(id))
            else:
                con.execute("DELETE FROM Productos WHERE Id = {}".format(id))
                con.commit()
                self
                for i in registros:
                    print(i)
                
                print("Registro '{}' se elimino de forma exitosa.".format(id))
        con.commit()
    
    
    def actualizarTabla(self) -> None:
        
        if self._campos and self._registros: 
            self._campos.clear()
            self._registros.clear()
        
        
        
        

    # El metodo crearOtrTabla crea una tabla nueva. Esta opcion es solo para usuarios avanzados.

# -------------------------------------------------------------------------------------------------------------------------------

#La clase interfazUsuario() gestiona todas las entradas de teclado del usuario.
class interfazUsuario:
    def __init__(self) -> None:
        self.id = None
        self._NombreProducto = None
        self._NombreProveedor = None
        self._Cantidad = None
        self._PaqueteDatos = UsuariosEst()
        self.UsAv = usAv.UsuariosAv()
        self._NombreColum = None   
        self._NuevoValor = None
        self._opciones = None
        self._comandoSql = None
        self._comandosUsEst = {"input data": self.DatosEntrada,
                             "update data": self.DtEntradaActualizarDatos,
                             "delete data": self.DtEntradaEliminarDatos,
                             "consulte table": self._PaqueteDatos.MostrarConsulta}

        self._comandosUsAv = {"au create table": self.CrearTabla,
                              "au delete table": self.ElimTabla,
                              "au input data": self.IngreDat,
                              "au delete data": self.EliminarReg,
                              "au consulte table": self.ConsulTabla}

    # El metodo metodoEjecucion contiene todos comandos que el usuario puede ingresar para hacer una gestión.
    def metodoEjecion(self) -> None:

        #Interfaz de usuarios estandar
         while True:
            print("*" * 5, "Sistema de gestión de datos versión 1.0", "*" * 5)
            opciones = str(input("> ")).lower()
            for claves_usEst in self._comandosUsEst:
                if opciones in claves_usEst:
                    self._comandosUsEst[claves_usEst]()
                else:
                    continue
            # Interfaz de usuarios avanzados
            if opciones == "avanced user.on":

                print("opcion usuarios avanzado habilitado.")
                while True:
                    opciones = str(input("> ")).lower()
                    for claves_usAv in self._comandosUsAv:
                        if opciones in claves_usAv:
                            self._comandosUsAv[claves_usAv]()
                        else:
                            continue
                    if opciones == "avanced user.off":
                        break
                    else:
                        continue
                print("opciones de usuarios avanzados deshabilitado.")
            print()

# Envia los datos a la clase usuarioEst() para almacenarlos en la tabla. Estos datos son enviados a metodo
# InsertarDatos.
    def DatosEntrada(self) -> None:
        #self.PaqueteDatos = BaseDatos()
        self.id = int(input("Ingrese el ID del producto: "))
        self._NombreProducto = str(input("Ingrese el Nombre del producto: "))
        self._Cantidad = int(input("Ingrese la cantidad de productos: "))
        self._NombreProveedor = str(input("Ingrese el Nombre del proveedor: "))
        print("Datos ingresados.")
        self._PaqueteDatos.InsertarRegistros(self.id, self._NombreProducto, self._Cantidad, self._NombreProveedor) # Clase BaseDatos. Aqui se introducen los datos a la base datos. 
        
    #Envia la transacion a la clase BaseDatos para  elimina los registros de tabla productos por medio de su id.
    def DtEntradaEliminarDatos(self) -> None:
        self.id = int(input("Ingrese el ID del producto para eliminarlo: "))
        self._PaqueteDatos.BorrarRegistros(self.id)

    #El metodo DtEntradaActualizarDatos envia los datos a la clase UsuariosEst(), despues metodo actualizar registros para luego
    #realizar la transacción y actualizar los datos en algún registro en especifico.
    def DtEntradaActualizarDatos(self) -> None:
        self._NombreColum = str(input("Ingrese el nombre de la columna: "))
        self.id = int(input("Ingrese el Id del producto: "))
        self._NuevoValor = str(input("Ingrese el nuevo valor: ")) 
        self._PaqueteDatos.actualizarRegistros(self._NombreColum, self.id, self._NuevoValor)

    #El metodo CrearTabla crea una tabla por medio del comando sql CREATE TABLE.
    def CrearTabla(self) -> None:

        print("Escriba el comando sql para crear una tabla: ")
        self._comandoSql = input("> ")
        usAv.UsuariosAv().CrearOtrTabla(NuevaTabla=self._comandoSql)
        print("Tabla creada de forma exitosa.")

    #El metodo ElimTabla elimina una tabla por medio del comando sql DROP TABLE.
    def ElimTabla(self) -> None:

        print("Escriba el comando sql para eliminar una tabla: ")
        self._comandoSql = input("> ")
        if self._comandoSql.strip() == "DROP TABLE Productos" or self._comandoSql.strip() == "drop table Productos":
            print(" AVISO -> Esta tabla no se puede eliminar. ")
        else:
            usAv.UsuariosAv().EliminarTablas(EliminarTabla=self._comandoSql)
            print("Tabla eliminada de forma exitosa.")

    # El metodo IngreDat ingresa datos una tabla por medio del comando sql INSERT.
    def IngreDat(self) -> None:
        print("Escriba el comando sql para insertar datos en la tabla: ")
        self._comandoSql = input("> ")
        usAv.UsuariosAv().InsDatosCd( IngDatos=self._comandoSql)
        print("Datos ingresados.")


    def ConsulTabla(self) -> None:
        
        print("Ingrese el nombre de la tabla a consultar: ")
        self._comandoSql = input("> ")
        usAv.UsuariosAv().ConsultaUsuAv(self._comandoSql)
        

    def EliminarReg(self) -> None:
        print("Ingrese el comando sql para eliminar registro")
        self._comandoSql = input("> ")
        usAv.UsuariosAv().ElimRegis(EliminarReg=self._comandoSql)
        print("registro eliminado.")