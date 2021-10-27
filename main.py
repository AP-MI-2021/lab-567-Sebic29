from Tests.Test_crud import Test_crud
from UserInterface.console import run_ui


def main():
    vanzari = []
    vanzari = run_ui(vanzari)


if __name__ == '__main__':
    Test_crud()
    main()