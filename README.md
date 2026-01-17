
**NEXUS: Servidor de Herramientas para IA (MCP)**

NEXUS es un servidor robusto basado en el Model Context Protocol (MCP) que actúa como el "cuerpo" operativo para modelos de lenguaje a gran escala (LLMs). Este proyecto permite que una IA interactúe directamente con el sistema de archivos, analice datos estructurados, realice web scraping y automatice comunicaciones por WhatsApp, todo desde una única interfaz unificada.

**Herramientas Disponibles (Tools)**
NEXUS expone cuatro herramientas principales diseñadas para ser consumidas por asistentes inteligentes:

    Analizar CSV (tool_analizar_csv): Procesa archivos de datos financieros para identificar deudores, calcular montos totales y generar resúmenes ejecutivos.

    Web Resumen (tool_web_resumen): Extrae y limpia el contenido principal de cualquier URL (ideal para Wikipedia), eliminando ruido HTML y entregando texto puro.

    Organizar Directorio (tool_organizar_directorio): Gestiona el sistema de archivos local, ordenando carpetas por fecha de modificación o extensiones de archivo.

    Notificar Equipo (tool_notificar_equipo): Puente de comunicación que utiliza pywhatkit para enviar mensajes automáticos a una lista de contactos predefinida.

**Requisitos Previos**
- Python 3.10 o superior.
- Navegador Chrome (para el envío de WhatsApp).
- Cuenta de WhatsApp Web iniciada en el navegador predeterminado.

**Validaciones Implementadas**
- Robustez de Datos: Limpieza automática de caracteres no numéricos en teléfonos.
- Seguridad de Archivos: Verificación de existencia de rutas antes de operaciones de lectura/escritura.
- Manejo de Excepciones: Respuestas JSON consistentes incluso en caso de errores de red o formato.