class Bushel:
    quart_const = 32

    def __init__(self, amount):
        self.amount = float(amount) * self.quart_const
