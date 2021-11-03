from Logic.Crud import create_sell
from Tests.Test_crud import Test_crud
from Tests.Teste_functionalitati import teste_functionalitati
from UserInterface.console import run_ui


def main():
    vanzari = []
    vanzari = create_sell(vanzari, 1, 't1', 'g1', 10, 'Silver')
    vanzari = create_sell(vanzari, 2, 't2', 'g2', 10.50, 'Gold')
    vanzari = create_sell(vanzari, 3, 't3', 'g2', 100, 'Gold')
    vanzari = create_sell(vanzari, 5, 't5', 'g2', 9, 'Silver')
    vanzari = create_sell(vanzari, 4, 't4', 'g4', 20, 'Silver')
    vanzari = create_sell(vanzari, 6, 't6', 'g4', 25.0, 'Gold')
    vanzari = run_ui(vanzari)


if __name__ == '__main__':
    Test_crud()
    teste_functionalitati()
    main()
