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
# тесчу работу с ноута fgjdkg,fgjdnf
# и я всё ещё могу здесь работать


class РодительскийКласс:
    def __init__(self, атрибут_родительского_класса):
        self.атрибут_родительского_класса = атрибут_родительского_класса

    def метод_родительского_класса(self):
        print("Метод родительского класса")

class Подкласс(РодительскийКласс):
    def __init__(self, атрибут_родительского_класса, атрибут_подкласса):
        # Вызываем конструктор родительского класса
        super().__init__(атрибут_родительского_класса)
        self.атрибут_подкласса = атрибут_подкласса

    def метод_подкласса(self):
        print("Метод подкласса")

# Создаем объекты на основе родительского и подкласса
родительский_объект = РодительскийКласс("Атрибут родительского класса")
подкласс_объект = Подкласс("Атрибут родительского класса", "Атрибут подкласса")

print(родительский_объект.атрибут_родительского_класса)
родительский_объект.метод_родительского_класса()

print(подкласс_объект.атрибут_родительского_класса)
print(подкласс_объект.атрибут_подкласса)
подкласс_объект.метод_родительского_класса()
подкласс_объект.метод_подкласса()