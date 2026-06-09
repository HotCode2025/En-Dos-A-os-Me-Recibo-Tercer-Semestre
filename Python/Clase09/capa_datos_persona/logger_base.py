import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log', encoding='utf-8'), # Guarda los logs en un archivo llamado 'capa_datos.log' con codificación utf-8
                    log.StreamHandler()
                ]) # Configura el nivel de log a DEBUG para capturar todos los mensajes

# Llamamos una configuración básica para el logger
if __name__ == "__main__":
    log.debug("Mensaje a nivel DEBUG")
    log.info("Mensaje a nivel INFO")
    log.warning("Mensaje a nivel WARNING")
    log.error("Mensaje a nivel ERROR")
    log.critical("Mensaje a nivel CRITICAL")

# Este código sirve para implementar un Sistema de Logueo (Logging). En programación profesional, no usamos print() para rastrear errores o eventos, porque los print() se pierden cuando cerrás la consola.

# ¿Para qué sirve esto y de qué sirve?
# El Logging es como la "caja negra" de un avión. Sirve para:
# Auditoría: Saber exactamente a qué hora y en qué línea de código ocurrió un evento.
# Persistencia: Los mensajes se guardan en un archivo (.log), por lo que podés revisar qué falló hace tres días.
# Filtrado: Podés decidir qué tan detallada querés que sea la información (desde "avisos de depuración" hasta "errores críticos").
# Separación de entornos: En desarrollo ves todo, pero en producción podés configurar que solo se guarden los errores graves.

