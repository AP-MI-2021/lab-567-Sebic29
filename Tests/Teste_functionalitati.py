from Domain.vanzare import get_id, get_pret, get_reducere, get_gen
from Logic.Crud import create_sell
from Logic.min_pret_per_gen import min_pret_per_gen
from Logic.modificare_gen import modificare_gen
from Logic.ordonare_crescator_pret import ordonare_crescator
from Logic.reducere import reducere_tip
from Logic.titluri_distincte import distinct_title
from Logic.undo_and_redo import do_redo, do_undo


def get_idd(lst_vanzari, id_vanzare):
    """
    Returneaza vanzarea cu id ul introdus ca parametru
    :param lst_vanzari: O lista cu vanzari
    :param id_vanzare: Id
    :return: Returneaza lista cu id ul id_vanzare
    """
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            return vanzare


def test_reducere():
    vanzari = []
    vanzari = create_sell(vanzari, 1, 't1', "g1", 15, "Silver", [], [])
    vanzari = create_sell(vanzari, 3, 't3', "g3", 8, "Silver", [], [])

    vanzari = reducere_tip(vanzari, 'Silver', [], [])
    assert get_pret(get_idd(vanzari, 1)) == 14.25
    assert get_pret(get_idd(vanzari, 3)) == 7.6

    vanzari = create_sell(vanzari, 2, 't2', "g2", 12, "Gold", [], [])
    vanzari = create_sell(vanzari, 4, 't4', "g4", 20, "Gold", [], [])

    vanzari = reducere_tip(vanzari, 'Gold', [], [])
    assert get_pret(get_idd(vanzari, 2)) == 10.8
    assert get_pret(get_idd(vanzari, 4)) == 18


def test_modificare_gen():
    start_program = []
    undo_list = []
    redo_list = []
    start_program = create_sell(start_program, 1, 't1', 'g1', 10, 'Silver', undo_list, redo_list)
    start_program = create_sell(start_program, 2, 't2', 'g2', 10.50, 'Gold', undo_list, redo_list)
    start_program = create_sell(start_program, 3, 't3', 'g2', 100, 'Gold', undo_list, redo_list)
    start_program = modificare_gen('t2','Actiune',start_program,undo_list,redo_list)
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 3


def test_min_pret_per_gen():
    vanzari = []
    vanzari = create_sell(vanzari, 1, 't1', "g1", 15, "Silver", [], [])
    vanzari = create_sell(vanzari, 3, 't3', "g4", 8, "Silver", [], [])
    vanzari = create_sell(vanzari, 2, 't2', "g3", 12, "Gold", [], [])
    vanzari = create_sell(vanzari, 4, 't4', "g4", 20, "Gold", [], [])
    result = min_pret_per_gen(vanzari)
    assert result['g4'] == 8
    assert result['g1'] == 15
    assert result['g3'] == 12


def test_ordonare_crescator():
    vanzari = []
    vanzari = create_sell(vanzari, 1, 't1', "g1", 15, "Silver", [], [])
    vanzari = create_sell(vanzari, 3, 't3', "g4", 8, "Silver", [], [])
    vanzari = create_sell(vanzari, 2, 't2', "g3", 12, "Gold", [], [])
    vanzari = create_sell(vanzari, 4, 't4', "g4", 20, "Gold", [], [])
    vanzari = ordonare_crescator(vanzari)
    assert get_pret(vanzari[3]) == 20
    assert get_pret(vanzari[2]) == 15
    assert get_pret(vanzari[1]) == 12
    assert get_pret(vanzari[0]) == 8


def test_titluri_distincte():
    vanzari = []
    vanzari = create_sell(vanzari, 1, 't1', 'g1', 10, 'Silver', [], [])
    vanzari = create_sell(vanzari, 2, 't2', 'g2', 10.50, 'Gold', [], [])
    vanzari = create_sell(vanzari, 3, 't3', 'g2', 100, 'Gold', [], [])
    vanzari = create_sell(vanzari, 5, 't5', 'g2', 9, 'Silver', [], [])
    vanzari = create_sell(vanzari, 4, 't4', 'g4', 20, 'Silver', [], [])
    vanzari = create_sell(vanzari, 6, 't6', 'g4', 25.0, 'Gold', [], [])
    assert distinct_title(vanzari) == {'g1': ['t1'], 'g2': ['t2', 't3', 't5'], 'g4': ['t4', 't6']}


def teste_functionalitati():
    test_reducere()
    test_modificare_gen()
    test_min_pret_per_gen()
    test_ordonare_crescator()
    test_titluri_distincte()
