from Domain.vanzare import get_id, get_pret, get_reducere, get_gen
from Logic.Crud import create_sell
from Logic.min_pret_per_gen import min_pret_per_gen
from Logic.modificare_gen import modificare_gen
from Logic.ordonare_crescator_pret import ordonare_crescator
from Logic.reducere import reducere_tip


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
    vanzari = create_sell(vanzari, 1, 't1', "g1", 15, "Silver")
    vanzari = create_sell(vanzari, 3, 't3', "g3", 8, "Silver")

    vanzari = reducere_tip(vanzari, 'Silver')
    assert get_pret(get_idd(vanzari, 1)) == 14.25
    assert get_pret(get_idd(vanzari, 3)) == 7.6

    vanzari = create_sell(vanzari, 2, 't2', "g2", 12, "Gold")
    vanzari = create_sell(vanzari, 4, 't4', "g4", 20, "Gold")

    vanzari = reducere_tip(vanzari, 'Gold')
    assert get_pret(get_idd(vanzari, 2)) == 10.8
    assert get_pret(get_idd(vanzari, 4)) == 18


def test_modificare_gen():
    vanzari = []
    vanzari = create_sell(vanzari, 1, 't1', "g1", 15, "Silver")
    vanzari = create_sell(vanzari, 3, 't2', "g3", 8, "Silver")
    vanzari = create_sell(vanzari, 2, 't2', "g2", 12, "Gold")
    vanzari = create_sell(vanzari, 4, 't4', "g4", 20, "Gold")
    vanzari = modificare_gen('t2', 'Actiune', vanzari)
    assert get_gen(get_idd(vanzari, 2)) == 'Actiune'
    assert get_gen(get_idd(vanzari, 3)) == 'Actiune'
    assert get_gen(get_idd(vanzari, 4)) == 'g4'


def test_min_pret_per_gen():
    vanzari = []
    vanzari = create_sell(vanzari, 1, 't1', "g1", 15, "Silver")
    vanzari = create_sell(vanzari, 3, 't3', "g4", 8, "Silver")
    vanzari = create_sell(vanzari, 2, 't2', "g3", 12, "Gold")
    vanzari = create_sell(vanzari, 4, 't4', "g4", 20, "Gold")
    result = min_pret_per_gen(vanzari)
    assert result['g4'] == 8
    assert result['g1'] == 15
    assert result['g3'] == 12


def test_ordonare_crescator():
    vanzari = []
    vanzari = create_sell(vanzari, 1, 't1', "g1", 15, "Silver")
    vanzari = create_sell(vanzari, 3, 't3', "g4", 8, "Silver")
    vanzari = create_sell(vanzari, 2, 't2', "g3", 12, "Gold")
    vanzari = create_sell(vanzari, 4, 't4', "g4", 20, "Gold")
    vanzari = ordonare_crescator(vanzari)
    assert get_pret(vanzari[3]) == 20
    assert get_pret(vanzari[2]) == 15
    assert get_pret(vanzari[1]) == 12
    assert get_pret(vanzari[0]) == 8


def teste_functionalitati():
    test_reducere()
    test_modificare_gen()
    test_min_pret_per_gen()
    test_ordonare_crescator()