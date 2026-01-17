import os
from datetime import datetime

def ordenar_por_fecha(path: str) -> dict:
    try:
        if not os.path.exists(path):
            return {"error": "La ruta especificada no existe."}

        archivos = []
        for nombre in os.listdir(path):
            ubicacionCompleta = os.path.join(path, nombre)
            
            if os.path.isfile(ubicacionCompleta):
                timestamp = os.path.getmtime(ubicacionCompleta) #fecha del archivo
                fechaFormato = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')
                
                archivos.append({
                    'nombre': nombre,
                    'fecha_raw': timestamp, 
                    'fecha': fechaFormato
                })

        archivos_ordenados = sorted(archivos, key=lambda x: x['fecha_raw'], reverse=True)

        return {
            'directorio': path,
            'total_archivos': len(archivos_ordenados),
            'archivos': archivos_ordenados
        }

    except Exception as e:
        return {'error': f'Error al organizar el directorio: {str(e)}'}