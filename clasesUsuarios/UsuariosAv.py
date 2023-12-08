import clasesUsuarios.UsuariosEst as UsEst
from configuration.system_confi import colores, estilo_fuente
import tabulate

var_tabla_colores = colores.get("whitetable")
var_tabla_estilo = estilo_fuente.get("simple")
#Esta clase contiene todas la funciones de usuarios avanzados. Los paramtros que recibe esta clase deben ser comandos
#Sql.
class UsuariosAv:

    def __init__(self):

        self._registros = []
        self._campos = []
        self.confi_tabla = var_tabla_colores
        self.confi_letra_tabla = var_tabla_estilo
    def CrearOtrTabla(self, NuevaTabla) -> None:
  
        UsEst.con.execute(NuevaTabla)
        UsEst.con.commit()
       
    def ActDatTabla(self, ActualizarDato) -> None:
        
        UsEst.con.execute(ActualizarDato)
        UsEst.con.commit()
        
    def EliminarTablas(self, EliminarTabla, ) -> None:

      
        UsEst.con.execute(EliminarTabla)
        UsEst.con.commit()
        
    def InsDatosCd(self, IngDatos) -> None:
        UsEst.con.execute(IngDatos)
        UsEst.con.commit()
        
    def ElimRegis(self, EliminarReg) -> None:
        
        UsEst.con.execute(EliminarReg)
        UsEst.con.commit()

    def ConsultaUsuAv(self, NombreTabla) -> None:
        try:
            for i in UsEst.con.execute(f"PRAGMA table_info({NombreTabla})").fetchall():
                self._campos.append(i[1])
                
            for indice, datos in enumerate(UsEst.con.execute(f"SELECT * FROM {NombreTabla}")):
                registros = list(datos)
                self._registros.append([])
                for i in registros:
                    self._registros[indice].append(i)
                
            print(self.confi_tabla + tabulate.tabulate(self._registros, headers=self._campos, tablefmt=self.confi_letra_tabla))
            self.actualizarTabla()
        except Exception: 
            print("Tabla no existe.")    
    def actualizarTabla(self) -> None:
        
        if self._campos and self._registros: 
            self._campos.clear()
            self._registros.clear()
    
    def TablasCreadas(self) -> None :
       
        for tablas in UsEst.con.execute("SELECT name FROM sqlite_master").fetchall():
            print(self.confi_tabla + tablas[0])
       
        
      