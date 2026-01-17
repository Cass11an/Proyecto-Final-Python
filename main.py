from nexus_tools.gestor_archivos import analizarCSV
from nexus_tools.mensajes import notificaciones
from nexus_tools.web_resumen import web_resumen
from nexus_tools.organizar_directorios import organizar_directorios
import asyncio
import traceback
import json
from typing import Any, Dict
from fastmcp import FastMCP

#configuracion del mcp
mcp =  FastMCP('nexus', '1.0.0')

#funciones de utilidad

def format_response(data: Any) -> Dict[str, Any]: #para asegurar que la respuesta sea un dict
    if isinstance(data, Dict):
        payload = data
    else:
        payload = json.dumps(data, ensure_ascii=False, indent=4)
        
    return payload

#herramientas del mcp

@mcp.tool(name='analizar_csv', description='Analiza un archivo CSV y devuelve una lista de deudores.')
def AnalizarCSV_wrapper(path: str = "./archivos/clientes.csv") -> Dict[str, Any]: #ruta por defecto
    result = analizarCSV(path)
    return format_response(result)

@mcp.tool(name='enviar_notificaciones', description='Envía notificaciones a una lista de números de teléfono.')
def EnviarNotificaciones_wrapper(mensaje: str, numeros: list[str]) -> str:
    mensajes_enviados = notificaciones(mensaje, numeros) 
    return format_response(mensajes_enviados)

@mcp.tool(name='organizar_directorio', description='Ordena las carpetas de un directorio por fecha de modificación.')
def OrganizarDirectorio_wrapper(path: str) -> Dict[str, Any]:
    organizacion = organizar_directorios(path)
    return format_response(organizacion)

@mcp.tool(name='web_resumen', description='Genera un resumen de una página web dada su URL.')
def WebResumen_wrapper(url: str) -> Dict[str, Any]:
    resumen = web_resumen(url)
    return format_response(resumen)


#funcion main
def main():
    print("iniciando el mcp server demo", flush=True)

    try:
        if hasattr(mcp, 'run_server_async'):
            asyncio.run(mcp.run_stdio_async())
        else:
            mcp.run()
    except Exception as e:
        print(f'Ha ocurrido un error al iniciar el servidor: {e}')
        traceback.print_exc()

if __name__ == "__main__":
    main()
