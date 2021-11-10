from Logic.Crud import create_sell
from Tests.Test_crud import Test_crud
from Tests.Teste_functionalitati import teste_functionalitati
from Tests.test_undo_redo import test_undo_redo
from UserInterface.command_line_console import run_command
from UserInterface.console import run_ui


def main():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create_sell(vanzari, 1, 't1', 'g1', 10, 'Silver', undo_list, redo_list)
    vanzari = create_sell(vanzari, 2, 't2', 'g2', 10.50, 'Gold', undo_list, redo_list)
    vanzari = create_sell(vanzari, 3, 't3', 'g2', 100, 'Gold', undo_list, redo_list)
    vanzari = create_sell(vanzari, 5, 't5', 'g2', 9, 'Silver', undo_list, redo_list)
    vanzari = create_sell(vanzari, 4, 't4', 'g4', 20, 'Silver', undo_list, redo_list)
    vanzari = create_sell(vanzari, 6, 't6', 'g4', 25.0, 'Gold', undo_list, redo_list)
    vanzari = run_ui(vanzari, undo_list, redo_list)


if __name__ == '__main__':
    Test_crud()
    teste_functionalitati()
    test_undo_redo()
    main()
