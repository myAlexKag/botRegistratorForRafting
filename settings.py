# Данный модуль читает настройки из файла конфигурации settings.conf
try:
    settings_file_lines = open("settings.conf", mode="r").read().strip().split('\n')
    API_TOKEN = str(settings_file_lines[1]).strip()
except:
    print(f'Внимание, не найден файл конфигурации.\nПроверьте его наличие')
    # exit(1)
