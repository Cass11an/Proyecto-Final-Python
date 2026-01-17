import os
import csv
from datetime import datetime
from typing import Any, Dict

def analizarCSV(ubicacionCSV: str) -> Dict[str, Any] | None:
    deudores = []
    nombres = []
    deuda = 0
    fechaActual = datetime.now()

    try:
        if os.path.exists(ubicacionCSV):
            with open(ubicacionCSV, "r") as file:
                archivo = csv.DictReader(file, delimiter= ',')
                for row in archivo:
                    fechaVencimiento = datetime.strptime(row['FechaVencim'],'%d/%m/%Y')
                    if fechaVencimiento < fechaActual:
                        deudores.append(row)
                
                totalDeudores = len(deudores)

                if not deudores:
                    result = {
                    'TotalDeudores': 0,
                    'DeudaTotal': 0,
                    'NombresDeudores': ''
                    }

                else:
                    for d in deudores:
                        deuda = deuda + float(d['MontoDeuda'])
                        nombres.append(d['Nombre'])

                    result = {
                        'TotalDeudores': totalDeudores,
                        'DeudaTotal': deuda,
                        'NombresDeudores': nombres
                    }

                return result
    except Exception as e:
        print(f'Error al leer el archivo CSV: {e}')
        
        result = {
                'TotalDeudores': 0,
                'DeudaTotal': 0,
                'NombresDeudores': ''
                }
        return result
