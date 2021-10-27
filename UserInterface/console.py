from Domain.vanzare import get_str, creeaza_vanzare, get_gen, get_titlu, get_pret, get_reducere
from Logic.Crud import create_sell, update, delete, read


def show_menu():
    print('1. CRUD')
    print('x. Exit')


def handle_add(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii: "))
    nume = input("Dati numele cartii ce urmeaza a fi pusa in vanzare: ")
    gen = input("Introduceti genul cartii: ")
    pret = float(input("Dati pretul cartii: "))
    reducere = input("Introduceti tipul cardului de fidelitate: ")
    return create_sell(vanzari,id_vanzare, nume, gen, pret, reducere)


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))


def handle_update(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii care se actualizeaza: "))
    nume = input("Dati noul nume al cartii ce urmeaza a fi pusa in vanzare: ")
    gen = input("Introduceti noul gen al cartii: ")
    pret = float(input("Dati noul pret al cartii: "))
    reducere = input("Introduceti tipul cardului de fidelitate: ")
    return update(vanzari, creeaza_vanzare(id_vanzare, nume, gen, pret, reducere))


def handle_delete(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii care se va sterge: "))
    vanzari = delete(vanzari, id_vanzare)
    return vanzari


def handle_show_details(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii pentru care doriti detalii: "))
    vanzare = read(vanzari, id_vanzare)
    print(f'Titlul cartii: {get_titlu(vanzare)}')
    print(f'Genul cartii: {get_gen(vanzare)}')
    print(f'Pretul cartii: : {get_pret(vanzare)}')
    print(f'Tipul reducerii: {get_reducere(vanzare)}')


def handle_crud(vanzari):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii vanzare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            vanzari = handle_add(vanzari)
        elif optiune == '2':
            vanzari = handle_update(vanzari)
        elif optiune == '3':
            vanzari = handle_delete(vanzari)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'd':
            handle_show_details(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return vanzari



def run_ui(vanzari):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            vanzari = handle_crud(vanzari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return vanzari