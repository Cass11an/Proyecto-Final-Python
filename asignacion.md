# PROYECTO FINAL (Integración Total)

Todos los temas vistos + Servidor MCP.

### Proyecto Final: "NEXUS: Servidor de Herramientas para IA"

**Duración:** 3 días.

Descripción General:

El estudiante construirá un Servidor MCP (Model Context Protocol). El objetivo no es hacer una IA, sino crear el "cuerpo" que una IA (como Gemini) utilizaría para interactuar con la computadora del estudiante. NEXUS expondrá todas las habilidades aprendidas en el curso como "herramientas".

**Arquitectura del Proyecto:**

1. **Estructura del Proyecto:**
    - Uso estricto de entorno virtual (`uv` o `venv`).
    - Archivo `main.py` (Servidor FastMCP).
    - Paquete `nexus_tools/` con módulos importados.
2. Herramientas a Desarrollar (Tools):
    
    El servidor debe exponer al menos 4 herramientas funcionales decoradas con @mcp.tool:
    
    - `tool_analizar_csv(ruta)`: Reutiliza lógica del Proyecto 2. Lee un CSV y devuelve un resumen JSON (total de deuda, promedio, etc.).
    - `tool_web_resumen(url)`: Reutiliza lógica del Proyecto 3. Hace scraping a una URL y devuelve título y texto limpio.
    - `tool_organizar_directorio(ruta)`: Reutiliza lógica del Proyecto 3 (OS). Ordena una carpeta por extensiones o fechas.
    - `tool_notificar_equipo(mensaje, numeros)`: Reutiliza lógica del Proyecto 2 (WhatsApp). Envía mensajes.

3. **Integración y Lógica:**
    - El alumno debe implementar validaciones robustas.
    - Las respuestas deben estar formateadas correctamente para que la IA las entienda (JSON/Texto).
    
4. **Entregable Final:**
    - Código fuente completo.
    - Archivo de configuración JSON para el cliente MCP.
    - **El éxito del proyecto es que la IA logre ejecutar esa cadena de comandos usando el código Python del alumno.**