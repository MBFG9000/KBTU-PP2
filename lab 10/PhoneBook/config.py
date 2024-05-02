#задача данного файла взять данные с файла 
#ini и перевести их в переменные в которые будут импортированы в код
#русские буквы в ини выдает ошибку кодировки 
from configparser import ConfigParser

def load_config(filename = 'connection.ini', section = 'postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    #нужно проверить секцию чтобы загрузить данные постгреса
    config = {}

    if parser.has_section(section):
        parameters = parser.items(section)

        for param in parameters:
            config[param[0]] = param[1]

    else:
        raise Exception ('Указанная вами секция {0} не найдена в файле {1}'.format(section, filename))           

    return config

#Когда скрипт запускается непосредственно (а не импортируется как модуль), 
#значение __name__ устанавливается равным "__main__"

if __name__ == '__main__':
    config = load_config()
    print(config)