import os
import tempfile

'''
В этом задании вам нужно создать интерфейс для работы с файлами. Интерфейс должен предоставлять следующие 
возможности по работе с файлами:

- чтение из файла, метод read возвращает строку с текущим содержанием файла

- запись в файл, метод write принимает в качестве аргумента строку с новым содержанием файла

- сложение объектов типа File, результатом сложения является объект класса File, при этом создается новый файл 
и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен 
создаваться в директории, полученной с помощью функции tempfile.gettempdir. Для получения нового пути можно 
использовать os.path.join.

- возвращать в качестве строкового представления объекта класса File полный путь до файла

- поддерживать протокол итерации, причем итерация проходит по строкам файла

При создании экземпляра класса File в конструктор передается полный путь до файла на файловой системе. Если файла с
 таким путем не существует, он должен быть создан при инициализации.
'''


class File:
    def __init__(self, file):
        self.file = file
        if not os.path.exists(file):
            self.write('')
        self._iter_file = None

    def __add__(self, other_file):
        new_file = File(
            os.path.join(tempfile.gettempdir(), 'file_sum')
        )
        new_file.write(self.read() + other_file.read())
        return new_file

    def __str__(self):
        return self.file

    def __iter__(self):
        self._iter_file = open(self.file, 'r')
        return self

    def __next__(self):
        if self._iter_file is None:
            raise StopIteration

        result = self._iter_file.readline()
        if not result:
            self._iter_file.close()
            raise StopIteration

        return result

    def read(self):
        with open(self.file, 'r') as file_read:
            return file_read.read()

    def write(self, record):
        with open(self.file, 'w') as file_write:
            file_write.write(record)


path_to_file = 'some_filename'
print(os.path.exists(path_to_file))

file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
print(f'File contains: {file_obj.read()}')

file_obj.write('some text')
print(file_obj.read())

file_obj.write('other text')
print(file_obj.read())


file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')

new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
print(new_file_obj)

for line in new_file_obj:
    print(ascii(line))

new_path_to_file = str(new_file_obj)
print(os.path.exists(new_path_to_file))

file_obj_3 = File(new_path_to_file)
print(file_obj_3)