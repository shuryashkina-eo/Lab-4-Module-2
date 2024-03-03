class Earphones:
    """
            Создание и подготовка к работе объекта "Наушники"

            :param name: Марка, защищенный аргумент, пользователь не может создать новые виды наушников
            :param manufacturer: Производитель, защищенный аргумент, пользователь не может создать новые виды наушников

    """
    def __init__(self, name: str, manufacturer: str):
        self._name = name
        self._manufacturer = manufacturer

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @manufacturer.setter
    def manufacturer(self, new_manufacturer: str):
        self._manufacturer = new_manufacturer

    def __str__(self):
        return f'Наушники марки "{self._name}" производителя "{self._manufacturer}"'

    def __repr__(self):
        return f'{self.__class__.__name__}: name={self._name!r}, manufacturer ={self._manufacturer})'

class Wired_Earphones(Earphones):
    """
                Создание и подготовка к работе объекта "Проводные наушники"

                :param name: Марка, защищенный аргумент, пользователь не может создать новые виды наушников
                :param manufacturer: Производитель, защищенный аргумент, пользователь не может создать новые виды наушников
                :param condition: Состояние, ради избежания ошибок вводится через setter
    """
    def __init__(self, name: str, manufacturer: str, condition: str):
        super().__init__(name, manufacturer)
        if condition != 'plugged' and condition != 'unplugged':
            raise ValueError('Может принимать только значение plugged или unplugged')
        self.condition = condition

    def plug(self):
        condition = 'plugged'
    """
            Функция, которая подключает наушники к устройству.
            Если наушники уже подключены, не делает ничего.

            :return: Не возвращает ничего
    """

    def unplug(self):
        condition = 'unlugged'
    """
                Функция, которая отключает наушники от устройства.
                Если наушники не были подключены к устройству, не делает ничего.

                :return: Не возвращает ничего
    """

    def __str__(self):
        return f'Наушники марки "{self._name}" производителя "{self._manufacturer}" сейчас находятся в состоянии "{self.condition}"'

    def __repr__(self):
        return f'{self.__class__.__name__}: name={self._name!r}, manufacturer ={self._manufacturer!r}, condition={self.condition!r})'


class Wireless_Earphones(Earphones):
    """
                    Создание и подготовка к работе объекта "Беспроводные наушники"

                    :param name: Марка, защищенный аргумент, пользователь не может создать новые виды наушников
                    :param manufacturer: Производитель, защищенный аргумент, пользователь не может создать новые виды наушников
                    :param charge: Процент заряда, ради избежания ошибок вводится через setter
    """
    def __init__(self, name: str, manufacturer: str, charge: int):
        super().__init__(name, manufacturer)
        if not isinstance(charge, int):
            raise TypeError('Процент зарядки может быть только типа int')
        if charge < 0 or charge > 100:
            raise ValueError('Процент зарядки не может быть меньше 0 или больше 100 процентов')
        self._charge = charge

    def battery_is_low(self):
        if self._charge > 20:
            print('Наушники готовы к работе')
        else:
            print('Батарея разряжена. Заряд батареи меньше 20%')

    """
                Функция, которая проверяет состояния батареи наушников.

                :return: Возвращает 'Наушники готовы к работе', если батарея заряжена больше чем на 20%
                Возвращает 'Батарея разряжена. Заряд батареи меньше 20%', если батарея заряжена на 20% и меньше
        """
    def __str__(self):
        return f'Наушники марки "{self._name}" производителя "{self._manufacturer}" имеют  {self._charge} процентов заряда'

    def __repr__(self):
        return f'{self.__class__.__name__}: name={self._name!r}, manufacturer ={self._manufacturer!r}, charge={self._charge!r})'

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, new_charge: int):
        self._charge = new_charge

