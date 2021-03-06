from Domain.vanzare import get_str, creeaza_vanzare, get_gen, get_titlu, get_pret, get_reducere
from Logic.Crud import create_sell, update, delete, read
from Logic.min_pret_per_gen import min_pret_per_gen
from Logic.modificare_gen import modificare_gen
from Logic.ordonare_crescator_pret import ordonare_crescator
from Logic.reducere import reducere_tip
from Logic.titluri_distincte import distinct_title
from Logic.undo_and_redo import do_undo, do_redo


def show_menu():
    print('1. CRUD ')
    print('2. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold ')
    print('3. Modificarea genului pentru un titlu dat ')
    print('4. Determinarea prețului minim pentru fiecare gen ')
    print('5. Ordonarea vânzărilor crescător după preț ')
    print('6. Afișarea numărului de titluri distincte pentru fiecare gen.')
    print('u.Undo')
    print('r.Redo')
    print('x. Exit ')


def handle_add(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii: "))
        nume = input("Dati numele cartii ce urmeaza a fi pusa in vanzare: ")
        gen = input("Introduceti genul cartii: ")
        pret = float(input("Dati pretul cartii: "))
        reducere = input("Introduceti tipul cardului de fidelitate: ")
        return create_sell(vanzari, id_vanzare, nume, gen, pret, reducere, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzari


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))


def handle_update(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii care se actualizeaza: "))
        nume = input("Dati noul nume al cartii ce urmeaza a fi pusa in vanzare: ")
        gen = input("Introduceti noul gen al cartii: ")
        pret = float(input("Dati noul pret al cartii: "))
        reducere = input("Introduceti tipul cardului de fidelitate: ")
        return update(vanzari, creeaza_vanzare(id_vanzare, nume, gen, pret, reducere), undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzari


def handle_delete(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input("Dati id-ul vanzarii care se va sterge: "))
        vanzari = delete(vanzari, id_vanzare, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return vanzari
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzari


def handle_show_details(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii pentru care doriti detalii: "))
    vanzare = read(vanzari, id_vanzare)
    print(f'Titlul cartii: {get_titlu(vanzare)}')
    print(f'Genul cartii: {get_gen(vanzare)}')
    print(f'Pretul cartii: : {get_pret(vanzare)}')
    print(f'Tipul reducerii: {get_reducere(vanzare)}')


def handle_crud(vanzari, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii vanzare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            vanzari = handle_add(vanzari, undo_list, redo_list)
        elif optiune == '2':
            vanzari = handle_update(vanzari, undo_list, redo_list)
        elif optiune == '3':
            vanzari = handle_delete(vanzari, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'd':
            handle_show_details(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return vanzari


def handle_reducere_pret(vanzari, undo_list, redo_list):
    try:
        tip_reducere = input('Introduceti tipul de reducere ce va fi aplicat.')
        vanzari = reducere_tip(vanzari, tip_reducere, undo_list, redo_list)
        print('Preturile au fost reduse cu succes')
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzari


def handle_modificare_gen(vanzari, undo_list, redo_list):
    try:
        titlul = input('Intrduceti titlul cartii careia vreti sa ii modificati genul ')
        nou_gen = input('Inroduceti noul gen al cartii in care vreti sa fie schimbat ')
        vanzari = modificare_gen(titlul, nou_gen, vanzari, undo_list, redo_list)
        print('Inlocuirea a fost realizata cu succes')
    except ValueError as ve:
        print('Eroare:', ve)

    return vanzari


def handle_min_pret_per_gen(vanzari):
    result = min_pret_per_gen(vanzari)
    for gen in result:
        print(f"Pretul minim pentru genul {gen} este {result[gen]}")


def handle_ordonare_crescator_pret(vanzari):
    ordonate = ordonare_crescator(vanzari)
    handle_show_all(ordonate)


def handle_titluri_distincte(vanzari):
    result = distinct_title(vanzari)
    for gen in result:
        print(f'{gen}: {len(result[gen])}')


def handle_undo(vanzari, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, vanzari)
    if undo_result is not None:
        return undo_result
    return vanzari


def handle_redo(vanzari, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, vanzari)
    if redo_result is not None:
        return redo_result
    return vanzari


def run_ui(vanzari, undo_list, redo_list):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            vanzari = handle_crud(vanzari, undo_list, redo_list)
        elif optiune == '2':
            vanzari = handle_reducere_pret(vanzari, undo_list, redo_list)
        elif optiune == '3':
            vanzari = handle_modificare_gen(vanzari, undo_list, redo_list)
        elif optiune == '4':
            vanzari = handle_min_pret_per_gen(vanzari)
        elif optiune == '5':
            vanzari = handle_ordonare_crescator_pret(vanzari)
        elif optiune == '6':
            handle_titluri_distincte(vanzari)
        elif optiune == 'u':
            vanzari = handle_undo(vanzari, undo_list, redo_list)
        elif optiune == 'r':
            vanzari = handle_redo(vanzari, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return vanzari
