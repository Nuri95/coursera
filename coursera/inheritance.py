import csv
from enum import Enum

'''
Предположим есть данные о разных автомобилях и спецтехнике. Данные представлены в виде таблицы с характеристиками.
Вся техника разделена на три вида: спецтехника, легковые и грузовые автомобили. Обратите внимание на то,
что некоторые характеристики присущи только определенному виду техники. Например, у легковых автомобилей 
есть характеристика «кол-во пассажирских мест», а у грузовых автомобилей — габариты кузова: «длина», «ширина» и «высота».
Вам необходимо создать свою иерархию классов для данных, которые описаны в таблице.
Классы должны называться CarBase (базовый класс для всех типов машин), Car (легковые автомобили),
Truck (грузовые автомобили) и SpecMachine (спецтехника). Все объекты имеют обязательные атрибуты:

- car_type, значение типа объекта и может принимать одно из значений: «car», «truck», «spec_machine».

- photo_file_name, имя файла с изображением машины, допустимы названия файлов изображений с расширением 
из списка: «.jpg», «.jpeg», «.png», «.gif»

- brand, марка производителя машины

- carrying, грузоподъемность

В базовом классе CarBase нужно реализовать метод get_photo_file_ext для получения расширения файла изображения.
Расширение файла можно получить при помощи os.path.splitext.

Для грузового автомобиля необходимо в конструкторе класса определить атрибуты: body_length, body_width, body_height,
отвечающие соответственно за габариты кузова — длину, ширину и высоту. Габариты передаются в параметре body_lwh строка,
в которой размеры разделены латинской буквой «x»). Обратите внимание на то, что характеристики кузова должны быть
вещественными числами и характеристики кузова могут быть не валидными (например, пустая строка). В таком случае всем
атрибутам, отвечающим за габариты кузова, присваивается значение равное нулю.

Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, возвращающий объем кузова.

В классе Car должен быть определен атрибут passenger_seats_count (количество пассажирских мест),
а в классе SpecMachine — extra (дополнительное описание машины).

Полная информация о атрибутах классов приведена в таблице ниже, где 1 - означает, что атрибут обязателен для объекта,
0 - атрибут должен отсутствовать.


Обратите внимание, что у каждого объекта из иерархии должен быть свой набор атрибутов и методов.
Например, у класса легковой автомобиль не должно быть метода get_body_volume в отличие от класса 
грузового автомобиля. Имена атрибутов и методов должны совпадать с теми, что описаны выше.

Далее вам необходимо реализовать функцию get_car_list, на вход которой подается имя файла в формате csv.
Файл содержит данные, аналогичные строкам из таблицы. Вам необходимо прочитать этот файл построчно при помощи модуля
стандартной библиотеки csv. Затем проанализировать строки на валидность и создать список объектов с автомобилями и 
специальной техникой. Функция должна возвращать список объектов.

Вы можете использовать для отладки работы функции get_car_list следующий csv-файл:
'''

class CarTypes(str, Enum):
    CAR = 'car'
    TRUCK = 'truck'
    SPEC_MACHINE = 'spec_machine'


class CarBaseError(Exception):
    pass


class PhotoFormatError(CarBaseError):
    pass


class CarBase:

    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        ext = photo_file_name[photo_file_name.rfind('.'):]
        if ext in ['.jpg', '.jpeg', '.png', '.gif']:
            self.photo_file_name = photo_file_name
        else:
            raise PhotoFormatError
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        index = self.photo_file_name.rfind('.')
        return self.photo_file_name[index:] if index != -1 else ''


class Car(CarBase):
    car_type = CarTypes.CAR

    def __init__(self, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(self.car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    car_type = CarTypes.TRUCK

    def __init__(self, photo_file_name, brand, carrying, body_lwh):
        super().__init__(self.car_type, photo_file_name, brand, carrying)

        dimensions = body_lwh.split('x')
        body_length, body_width, body_height = [
            float(dimension)
            for dimension in dimensions
            if dimension != ''
        ] if len(dimensions) == 3 else [0, 0, 0]

        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def body_lwh(self, body_lwh):
        pass

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = CarTypes.SPEC_MACHINE

    def __init__(self, photo_file_name, brand, carrying, extra):
        super().__init__(self.car_type, photo_file_name, brand, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type, brand, passenger_count, file_name, body_lwh, carrying, extra = row
                if car_type == CarTypes.CAR:
                    car = Car(
                        photo_file_name=file_name,
                        brand=brand,
                        carrying=carrying,
                        passenger_seats_count=passenger_count,
                    )
                elif car_type == CarTypes.TRUCK:
                    car = Truck(
                        photo_file_name=file_name,
                        brand=brand,
                        carrying=carrying,
                        body_lwh=body_lwh
                    )
                elif car_type == CarTypes.SPEC_MACHINE:
                    car = SpecMachine(
                        photo_file_name=file_name,
                        brand=brand,
                        carrying=carrying,
                        extra=extra,
                    )
                else:
                    continue
                car_list.append(car)
            except ValueError:
                continue
            except PhotoFormatError as e:
                print(e)
                continue
    return car_list

file_name ='/home/nuri/Documents/PycharmProjects/coursera/coursera/_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv'
cars = get_car_list(file_name)
print(len(cars))

for car_ in cars:
    print(type(car_))

print(cars[0].passenger_seats_count)
print(cars[1].get_body_volume())

car_ = Car(brand='Bugatti Veyron', photo_file_name='bugatti.png', carrying='0.312', passenger_seats_count='2')
print(car_.car_type, car_.brand, car_.photo_file_name, car_.carrying, car_.passenger_seats_count, sep='\n')
truck = Truck(brand='Nissan', photo_file_name='nissan.jpeg', carrying='1.5', body_lwh='3.92x2.09x1.87')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')
spec_machine = SpecMachine(brand='Komatsu-D355', photo_file_name='d355.jpg', carrying='93', extra='pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
print(spec_machine.get_photo_file_ext())
