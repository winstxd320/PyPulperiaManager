import clasesUsuarios.UsuariosEst as UsEst
import clasesUsuarios.UsuariosAv as UsAv
# fetchall() muestra en una tupla todas las tablas creadas en base de datos.
# fetchone() muestra la primera tabla de la tupla.

if __name__ == "__main__":

    interfaz =  UsEst.interfazUsuario()
    basedatos = UsEst.UsuariosEst()
    
    
    #basedatos.MostrarConsulta()
    interfaz.metodoEjecion()
    #a.ConsultaUsuAv()
    #print(UsEst.con.execute("SELECT name FROM sqlite_master").fetchall())

    



