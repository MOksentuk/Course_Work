class Manager:
    def checker(self, obj):
        check_const = 2909.4

        return obj.amount < check_const  #

    def plus(self, lhs, rhs) -> int:
        result = lhs.amount * lhs.const + rhs.amount * rhs.const
        self.checker(result)

        return result

    def to_liter(self, obj):
        return obj.amount * obj.const

    def to_glass(self, obj):
        const = 0.273
        return obj.amount * obj.const / const

    def to_pint(self, obj):
        const = 0.56826
        return obj.amount * obj.const / const


class Quart:
    const = 1.1365

    def __init__(self, amount):
        self.amount = amount * 1.1365
    # def to_liter(self, ):



class Gallon:
    const = 4.546

    def __init__(self, amount):
        self.amount = amount


class Bushel:
    const = 36.368

    def __init__(self, amount):
        self.amount = amount


q1 = Quart(12)
g1 = Gallon(23)
manager = Manager()

print(manager.to_glass(q1))
print(manager.to_liter(q1))

print(manager.checker(q1))
print(manager.checker(g1))
print(manager.to_liter(g1))
print(manager.to_pint(g1))
