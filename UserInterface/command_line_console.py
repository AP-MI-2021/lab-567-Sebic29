from Domain.vanzare import get_str
from Logic.Crud import delete, create_sell

def show_menu():
    print("Comenzile sunt:")
    print("Add: {id_carte} {titlu} {gen} {pret} {tip_reducere}")
    print("Delete: {id_carte}")
    print("Showall")
    print("Exit")


def handle_add(carte, lst):
    """
    Adauga o carte in lista de vanzari
    :param carte: O carte
    :param lst: Lista de vanzari
    :return: O lista de vanzari in care sunt adaugate noile vanzari de carti
    """
    try:
        if len(lst) != 6:
            raise ValueError("Numar invalid de parametrii")
        id_carte = int(lst[1])
        titlu = lst[2]
        gen = lst[3]
        pret = float(lst[4])
        tip_reducere = lst[5]

        return create_sell(carte, id_carte, titlu, gen, pret, tip_reducere)
    except ValueError as ve:
        print("EROARE", ve)
    return carte


def handle_show_all(vanzari):
    """
    Afiseaza vanzarile
    :param vanzari: o lista de vanzari
    :return:
    """
    for vanzare in vanzari:
        print(get_str(vanzare))


def handle_delete(vanzari, lst):
    """
    Stergerea cheltuielii
    :param vanzari: lista cu cheltuieli
    :param lst: o lista ce contine parametrii cheltuielii
    :return: lista de cheltuieli cu cheltuiala stearsa
    """
    if len(lst) != 2:
        raise ValueError("Nu ati introdus numarul exact de parametrii")
    try:
        new_cheltuieli = delete(vanzari, int(lst[1]))
        print("Stergerea s-a efectual cu succes")
        return new_cheltuieli
    except ValueError as va:
        print('Error:', va)
    return vanzari


def run_command(vanzari):
    show_menu()
    while True:

        command = input("Introduceri comanda dorita: ")
        commands = command.split(";")
        for command in commands:

            lst = command.split()

            if lst[0] == "Add":
                vanzari = handle_add(vanzari, lst)
            elif lst[0] == "Showall":
                handle_show_all(vanzari)
            elif lst[0] == "Delete":
                vanzari = handle_delete(vanzari, lst)
            elif lst[0] == "Exit":
                return 0
            else:
                print("Comanda invalida!")
