import clasesUsuarios.UsuariosEst as UsEst


# fetchall() muestra en una tupla todas las tablas creadas en base de datos.
# fetchone() muestra la primera tabla de la tupla.


if __name__ == "__main__":

    interfaz =  UsEst.interfazUsuario()
    interfaz.metodoEjecion()
