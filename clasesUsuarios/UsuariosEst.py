import sqlite3 as bd
import sys
import os
import tabulate 
import colorama as estilo
import simplejson
from pathlib import Path 
from configuration.system_confi import conf_sistema, colores, estilo_fuente
import help.comand
import clasesUsuarios.UsuariosAv as usAv

estilo.init(autoreset=True)
# Obtener la ruta las rutas del paquete help y el modulo UsuariosAv.py
ruta_modulo = os.path.abspath("clasesUsuarios")
ruta_data = Path("help").absolute()
ruta_configuration = Path("configuration/configuration.json").absolute()
var_confi_tabla = colores.get("whitetable")
var_confi_letra = estilo_fuente.get("simple")
a = ruta_data in sys.path # La variable a retorna False.  

# # Agregar la ruta al principio de sys.path si no está presente
# if ruta_modulo not in sys.path :
#     sys.path.insert(0, ruta_modulo)
# import UsuariosAv as usAv

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
        self._verificador = None
        self.confi_tabla = var_confi_tabla
        self.confi_letra_tabla = var_confi_letra
        
    #El Metodo InsetarRgistros recibe los datos de la clase interfazUsuario() del metodo DatosEntrada.
    def InsertarRegistros(self, id, NombreProducto, Cantidad, NombreProveedor) -> None:
            
        # Agregar un verificador. Si el id ya existe o no.
            
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
        
       
       # Se crea una matriz bidimesional y se agregan los registos a la matriz
        for indice, datos in enumerate(con.execute("SELECT * FROM Productos")):
            registros = list(datos)
            self._registros.append([])
            for i in registros:
                self._registros[indice].append(i)
            
    
        print(self.confi_tabla + tabulate.tabulate(self._registros, self._campos, tablefmt=self.confi_letra_tabla))
        
        con.commit()
        self.actualizarTabla()
        
        
    # El Metodo BorrarRegistros borra los datos almacenados en la tabla Productos por medio Id. Ingresado por el usuario
    def BorrarRegistros(self, id) -> None:
        for registros in cur.execute("SELECT * FROM Productos"):
            if id in registros: # Esta condición verifica si el Id existe en la tabla Productos. 
                self._verificador = True
                break
            else:
                self._verificador = False
                
        if self._verificador == True:
            con.execute("DELETE FROM Productos WHERE Id = {}".format(id))
            con.commit()
            print("El id {} se borro de forma exitosa.".format(id))
            self._verificador = False
        else:
            print("El id '{}' no se encuentra registrado.".format(id))
                
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
        self._UsEst = UsuariosEst()
        self.UsAv = usAv.UsuariosAv()
        self.conf = conf_sistema()
        self._NombreColum = None   
        self._NuevoValor = None
        self._opciones = None
        self._comandoSql = None
        self._verificador = None
        self._comandosUsEst = {"input data": self.DatosEntrada,
                             "update data": self.DtEntradaActualizarDatos,
                             "delete data": self.DtEntradaEliminarDatos,
                             "consulte table": self._UsEst.MostrarConsulta,
                             "info": lambda: print(help.comand.infAplicacion),
                             "help": lambda: print(help.comand.comandos)}
                             
                            
        self._comandosUsAv = {"au create table": self.CrearTabla,
                              "au delete table": self.ElimTabla,
                              "au input data": self.IngreDat,
                              "au delete data": self.EliminarReg,
                              "au update data": self.ActDatos,
                              "au consulte table": self.ConsulTabla,
                              "tables": self.tablasExistentes}

    
    # El metodo metodoEjecucion contiene todos comandos que el usuario puede ingresar para hacer una gestión.
    def metodoEjecion(self) -> None:

        #Interfaz de usuarios estandar
        print("PyPulperiaManager version 1.0.\nENTER 'help' para obtener más información.")
        print("Usa los comandos para orientar al programa que debes hacer.")
        print("Más información en la sección " + estilo.Fore.RED +  "comandos en el apartado de ayuda")
        
        while True: 
            opciones = str(input("> ")).lower()
            
            for claves_usEst in self._comandosUsEst:
                
                if opciones == "":
                    break
                elif opciones == claves_usEst:
                    self._comandosUsEst[claves_usEst]()
                else:
                    continue
            # Interfaz de usuarios avanzados
            if opciones == "avanced user.on":
                print("opcion usuarios avanzado habilitado.")
                while True:
                    opciones = str(input("> ")).lower()
                    for claves_usAv in self._comandosUsAv:        
                        if opciones == "":
                            break
                        elif opciones == claves_usAv:
                            self._comandosUsAv[claves_usAv]()
                        else:
                            pass
                    if opciones == "avanced user.off":
                        break
                    else:
                        continue
                print("opciones de usuarios avanzados deshabilitado.")
            
            if opciones == "conftable":
                print("configuraciones de tabla.")
                opciones = str(input("> ")).lower().strip()
                self._UsEst.confi_tabla = self.conf.colores_tabla(opciones)
                usAv.var_tabla_colores = self._UsEst.confi_tabla
            elif opciones == "confstyle":
                print("configuraciones de estilo.")
                opciones = str(input("> ")).lower().strip()
                self._UsEst.confi_letra_tabla = self.conf.estilo_tabla(opciones)
                usAv.var_tabla_estilo = self._UsEst.confi_letra_tabla
            
        
# Envia los datos a la clase usuarioEst() para almacenarlos en la tabla. Estos datos son enviados a metodo
# InsertarDatos.
    def DatosEntrada(self) -> None:
        #self.PaqueteDatos = BaseDatos()
        while True:
            try:
                self.id = int(input("Ingrese el ID del producto: "))
                for id in con.execute("SELECT * FROM Productos"):
                    if self.id in id:
                        self._verificador = True
                        break
                    else:
                        self._verificador = False
                        continue
            
                if self._verificador == True:
                    print("El {} ya se encuentra registrado.".format(self.id))
                else:
                    break
            except Exception:
                print("Error al ejecutar el comando.")
        self._NombreProducto = str(input("Ingrese el Nombre del producto: ")).strip()
        self._Cantidad = str(input("Ingrese la cantidad de productos: ")).strip()
        self._NombreProveedor = str(input("Ingrese el Nombre del proveedor: ")).strip()
        print("Datos ingresados.")
        self._UsEst.InsertarRegistros(self.id, self._NombreProducto, self._Cantidad, self._NombreProveedor) # Clase BaseDatos. Aqui se introducen los datos a la base datos. 
        
    #Envia la transacion a la clase BaseDatos para  elimina los registros de tabla productos por medio de su id.
    def DtEntradaEliminarDatos(self) -> None:
        try:
            self.id = int(input("Ingrese el ID del producto para eliminarlo: "))
            self._UsEst.BorrarRegistros(self.id)
        except Exception:
            print("Error al ejecutar el comando")
    #El metodo DtEntradaActualizarDatos envia los datos a la clase UsuariosEst(), despues metodo actualizar registros para luego
    #realizar la transacción y actualizar los datos en algún registro en especifico.
    def DtEntradaActualizarDatos(self) -> None:
        self._NombreColum = str(input("Ingrese el nombre de la columna: "))
        self.id = int(input("Ingrese el Id del producto: "))
        self._NuevoValor = str(input("Ingrese el nuevo valor: ")) 
        self._UsEst.actualizarRegistros(self._NombreColum, self.id, self._NuevoValor)
        
    #**************************************************************************************************
    #El metodo CrearTabla crea una tabla por medio del comando sql CREATE TABLE.
    def CrearTabla(self) -> None:
        print("Escriba el comando sql para crear una tabla: ")
        try:
            self._comandoSql = input("> ").strip()
            if "CREATE TABLE" in self._comandoSql or "create table" in self._comandoSql:
                usAv.UsuariosAv().CrearOtrTabla(NuevaTabla=self._comandoSql)
                print("Tabla creada de forma existosa.")
            else:
                print("Error al intentar usar CREATE. Intente escribir CREATE TABLE o create table.")
        except Exception:
            print("{} <-  Error al intentar usar la instrucción CREATE.".format(self._comandoSql))
            
        

    #El metodo ElimTabla elimina una tabla por medio del comando sql DROP TABLE.
    def ElimTabla(self) -> None:

        print("Escriba el comando sql para eliminar una tabla: ")
        try:
            self._comandoSql = input("> ").strip()
            if self._comandoSql.strip() == "DROP TABLE Productos" or self._comandoSql.strip() == "drop table Productos":
                print("La tabla Productos no puede ser eliminada.")
            else:
                if "DROP TABLE" in self._comandoSql or "drop table" in self._comandoSql: 
                    usAv.UsuariosAv().EliminarTablas(EliminarTabla=self._comandoSql)  
                    print("Tabla eliminada de forma exitosa.")
                else:
                    print("Error al intentar usar DROP. Intente escribir DROP TABLE o drop table.")
        except Exception:
            print("{} <- Error al intentar usar la instrucción DROP.".format(self._comandoSql))     
         
               
    # El metodo IngreDat ingresa datos una tabla por medio del comando sql INSERT.
    def IngreDat(self) -> None:
        print("Escriba el comando sql para insertar datos en la tabla: ")
        try: 
            self._comandoSql = input("> ").strip()
            if "INSERT" in self._comandoSql or "insert" in self._comandoSql:
                usAv.UsuariosAv().InsDatosCd( IngDatos=self._comandoSql)
                print("Datos ingresados.")
            else:
                print("Error al intentar usar INSERT. Intente escribir INSERT o insert.")

        except Exception:
            print("{} <- Error al intentar usar la instrucción INSERT.".format(self._comandoSql))
            
    def ConsulTabla(self) -> None:
        
        print("Ingrese el nombre de la tabla a consultar: ")
        self._comandoSql = input("> ").strip()
        usAv.UsuariosAv().ConsultaUsuAv(self._comandoSql)
        

    def EliminarReg(self) -> None:
        print("Ingrese el comando sql para eliminar registro")
        try:
            
            self._comandoSql = input("> ").strip()
            if "DELETE" in self._comandoSql or "delete" in self._comandoSql:
                usAv.UsuariosAv().ElimRegis(EliminarReg=self._comandoSql)
                print("registro eliminado.")
            else:
                print("Error al intentar usar INSERT. Intente escribir DELETE o delete.")
        except Exception:
            print("{} <- Error al intentar usar la instrucción DELETE.".format(self._comandoSql)) 
            
    def ActDatos(self) -> None:
        print("Ingrese el comando sql para actualizar el registro")
        try:
            self._comandoSql = input("> ").strip()
            if "UPDATE" in self._comandoSql or "update" in self._comandoSql:
                usAv.UsuariosAv().ActDatTabla(ActualizarDato=self._comandoSql)
                print("registro actualizado.")
            else:
                print("Error al intentar usar INSERT. Intente escribir UPDATE o update.")
        except Exception:
            print("{} <- Error al intentar usar la instrucción UPDATE.".format(self._comandoSql)) 
    def tablasExistentes(self) -> usAv.UsuariosAv:
        return usAv.UsuariosAv().TablasCreadas()
    
    
        