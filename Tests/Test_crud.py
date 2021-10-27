from Domain.vanzare import creeaza_vanzare, get_id
from Logic.Crud import create_sell, read, update, delete


def get_data():
    return [
        creeaza_vanzare(1, 't1', 'g1', 100, 'Silver'),
        creeaza_vanzare(2, 't2', 'g2', 10, None),
        creeaza_vanzare(3, 't3', 'g3', 23.4, 'Gold'),
        creeaza_vanzare(4, 't4', 'g4', 30, 'Gold'),
        creeaza_vanzare(5, 't5', 'g5', 20.0, 'Silver'),
        creeaza_vanzare(6, 't6', 'g6', 9.5, None),
    ]


def test_create():
    vanzari = get_data()
    param = (9, 't9', 'g9', 15, 'Silver')
    p_new = creeaza_vanzare(*param)
    new_vanzari = create_sell(vanzari, *param)
    assert len(new_vanzari) == len(vanzari) + 1
    assert p_new in new_vanzari


def test_read():
    vanzari = get_data()
    some_s = vanzari[2]
    assert read(vanzari, get_id(some_s)) == some_s
    assert read(vanzari, None) == vanzari


def test_update():
    vanzari = get_data()
    s_updated = creeaza_vanzare(1, 'new name', 'new genre', 198.87, 'None')
    updated = update(vanzari, s_updated)
    assert s_updated in updated
    assert s_updated not in vanzari
    assert len(updated) == len(vanzari)




def test_delete():
    vanzari = get_data()
    for_delete = 6
    p_deleted = read(vanzari, for_delete)
    deleted = delete(vanzari, for_delete)
    assert p_deleted not in deleted
    assert p_deleted in vanzari
    assert len(deleted) == len(vanzari) - 1


def Test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
