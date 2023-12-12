class Converter:

    def __init__(self):
        self.result = None
        self.__liter_const = 1.1365
        self.__glass_const = 0.273
        self.__pint_const = 0.56826

    def to_liter(self, obj):
        """Перевод значения в литры"""
        self.result = round(obj.amount * self.__liter_const)

    def to_glass(self, obj):
        """Перевод значения в стаканы"""
        self.result = round(obj.amount * self.__liter_const / self.__glass_const)

    def to_pint(self, obj):
        """Перевод значения в пинты"""
        self.result = round(obj.amount * self.__liter_const / self.__pint_const)
