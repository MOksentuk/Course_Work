class Converter:
    __liter_const = 1.1365
    __glass_const = 0.273
    __pint_const = 0.56826

    def to_liter(self, amount):
        """Возвращение значения в литрах"""
        result = amount * self.__liter_const

        return result

    def to_glass(self, amount):
        """Перевод значения в стаканы"""
        result = amount * self.__liter_const / self.__glass_const

        return result

    def to_pint(self, amount):
        """Перевод значения в пинты"""
        result = amount * self.__liter_const / self.__pint_const

        return result
