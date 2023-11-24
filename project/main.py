from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations
from ToUser import ToUser


def main():
    manager = Manager()
    math = MathOperations()
    converter = Converter()
    print(ToUser().work(manager, math, converter))


if __name__ == "__main__":
    main()
