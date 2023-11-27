from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations
from ToUser import to_user


def main():
    manager = Manager()
    math = MathOperations()
    converter = Converter()
    print(to_user(manager, math, converter))


if __name__ == "__main__":
    main()
