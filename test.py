class Manager:
    def to_liter(self, obj):
        return obj.amount * obj.const
    def to_glass(self, obj):
        const = 0.273
        return obj.amount / const


class Quart:
    const = 1.1365

    def __init__(self, amount):
        self.amount = amount


q1 = Quart(12)

manager = Manager()
print(manager.to_glass(q1))