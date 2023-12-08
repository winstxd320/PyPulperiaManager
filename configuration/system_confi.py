import colorama as estilo
import simplejson
from pathlib import Path
import clasesUsuarios.UsuariosEst as UsEst

colores = {
            
            "bluetable": estilo.Fore.BLUE,
            "yellowtable": estilo.Fore.YELLOW,
            "greentable": estilo.Fore.GREEN,
            "whitetable": estilo.Fore.WHITE
        } 

estilo_fuente = {

            "plain":"plain",
            "simple":"simple",
            "github":"github",
            "grid":"grid"
        
}

class conf_sistema:

    def colores_tabla(self, cambios) -> dict:
        try:
            if cambios in colores:
                print("Configuración aplicada.")
                return colores.get(cambios)
            else: 
                return colores.get("blanco")
                
                
        except Exception:
            print("No se realizaron cambios.")
    def estilo_tabla(self, cambios) -> dict:
        try:
            if cambios in estilo_fuente:
                print("Configuración aplicada.")
                return estilo_fuente.get(cambios)
            else:
                return estilo_fuente.get("simple") 
        except Exception:
            print("No se realizaron cambios.")
