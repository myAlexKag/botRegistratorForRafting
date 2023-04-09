# Данный модуль читает настройки из файла конфигурации settings.conf
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

logger.info('Начато чтение конфига')
try:
    settings_file_lines = open("settings.conf", mode="r").read().strip().split('\n')
    API_TOKEN = str(settings_file_lines[1]).strip()
except:
    logger.critical("Не найден или некоректный файл настроек settings.conf")
    exit(1)
