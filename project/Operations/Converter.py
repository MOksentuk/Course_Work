class Converter:
    __liter_const = 1.1365
    __glass_const = 0.273
    __pint_const = 0.56826

    def __init__(self):
        self.result = None

    def to_liter(self, obj):
        """Возвращение значения в литрах"""
        result = obj.amount * self.__liter_const

        self.result = result

    def to_glass(self, obj):
        """Перевод значения в стаканы"""
        result = obj.amount * self.__liter_const / self.__glass_const

        self.result = result

    def to_pint(self, obj):
        """Перевод значения в пинты"""
        result = obj.amount * self.__liter_const / self.__pint_const

        self.result = result
