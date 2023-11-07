class Gallon:
    quart_const = 4

    def __init__(self, amount):
        self.amount = amount * self.quart_const
