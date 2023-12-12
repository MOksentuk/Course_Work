from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import Math
from ToUser import to_user


def main():
    manager = Manager()
    math = Math()
    converter = Converter()
    to_user(manager, math, converter)


if __name__ == "__main__":
    main()
