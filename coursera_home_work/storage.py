import argparse
import json
import os
import tempfile

'''
Если при запуске утилиты переданы оба ключа, происходит добавление переданного значения по ключу и сохранение 
данных в файле. Если передано только имя ключа, происходит чтение файла хранилища и вывод на печать значений, 
которые были сохранены по данному ключу
'''


class Storage:
    def __init__(self, path):
        self.storage_path = path

    def _write(self, data):
        with open(self.storage_path, 'w') as write_file:
            json.dump(data, write_file)

    def _read(self):
        try:
            with open(self.storage_path, 'r') as read_file:
                return json.load(read_file)
        except FileNotFoundError:
            return {}

    def _update_by_key(self, key, value):
        data = self._read()

        if key in data:
            data[key].append(value)
        else:
            data.update({key: [value]})

        self._write(data)

    def apply(self, key, value):
        if key and value:
            self._update_by_key(key, value)
        else:
            return self._read()[key]


def main():
    parser = argparse.ArgumentParser(description='Ping script')
    parser.add_argument('-key', dest="key", default='hello')
    parser.add_argument('-val', dest="value", default='hi')
    args = parser.parse_args()

    key = args.key
    value = args.value
    storage = Storage(os.path.join(tempfile.gettempdir(), 'storage.data'))
    return storage.apply(key, value)


main()
