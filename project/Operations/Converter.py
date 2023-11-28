class Converter:
    __liter_const = 1.1365
    __glass_const = 0.273
    __pint_const = 0.56826

    def __init__(self):
        self.result = None

    def to_liter(self, obj):
        """Возвращение значения в литрах"""
        self.result = obj.amount * self.__liter_const

    def to_glass(self, obj):
        """Перевод значения в стаканы"""
        self.result = obj.amount * self.__liter_const / self.__glass_const

    def to_pint(self, obj):
        """Перевод значения в пинты"""
        self.result = obj.amount * self.__liter_const / self.__pint_const
