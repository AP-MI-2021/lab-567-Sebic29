from Domain.vanzare import creeaza_vanzare, get_pret, get_gen
from Logic.Crud import create_sell, update, read, delete
from Logic.reducere import reducere_tip
from Logic.modificare_gen import modificare_gen
from Logic.undo_and_redo import do_undo, do_redo


def test_undo_redo_update():
    carti = []
    undo_list = []
    redo_list = []

    carti = create_sell(carti, 1, 'ana', 'legenda', 34.5, 'none', undo_list, redo_list)
    carti = create_sell(carti, 2, 'oocaa', 'romantic', 90, 'silver', undo_list, redo_list)
    carti = create_sell(carti, 3, 'mouse', 'densene', 99, 'gold', undo_list, redo_list)
    c_updated = creeaza_vanzare(1, 'cartenou', 'gen33', 34.33, 'gold')

    updated = update(carti, c_updated, undo_list, redo_list)
    if len(undo_list) > 0:
        updated = do_undo(undo_list, redo_list, updated)
    assert c_updated not in updated
    if len(redo_list) > 0:
        updated = do_redo(undo_list, redo_list, updated)
    assert c_updated in updated


def test_undo_redo_delete():
    carti = []
    undo_list = []
    redo_list = []

    carti = create_sell(carti, 1, 'ana', 'legenda', 34.5, 'none', undo_list, redo_list)
    carti = create_sell(carti, 2, 'oocaa', 'romantic', 90, 'silver', undo_list, redo_list)
    carti = create_sell(carti, 3, 'mouse', 'densene', 99, 'gold', undo_list, redo_list)
    delete_carti = 3
    c_deleted = read(carti, delete_carti)
    deleted = delete(carti, delete_carti, undo_list, redo_list)
    if len(undo_list) > 0:
        deleted = do_undo(undo_list, redo_list, deleted)
    assert c_deleted in deleted
    if len(redo_list) > 0:
        deleted = do_redo(undo_list, redo_list, deleted)
    assert c_deleted not in deleted


def test_undo_redo_discount():
    carti = []
    undo_list = []
    redo_list = []

    carti = create_sell(carti, 1, 'ana', 'legenda', 34.5, 'none', undo_list, redo_list)
    carti = create_sell(carti, 2, 'oocaa', 'romantic', 90, 'Gold', undo_list, redo_list)
    carti = create_sell(carti, 3, 'mouse', 'densene', 99, 'Gold', undo_list, redo_list)
    carti = reducere_tip(carti, 'Gold', undo_list, redo_list)

    assert get_pret(carti[1]) == 81.0
    carti = do_undo(undo_list, redo_list, carti)
    assert get_pret(carti[1]) == 90
    carti = do_redo(undo_list, redo_list, carti)
    assert get_pret(carti[1]) == 81


def test_undo_redo_modificare_gen():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create_sell(vanzari, 1, 't1', 'g1', 10, 'Silver', undo_list, redo_list)
    vanzari = create_sell(vanzari, 2, 't2', 'g2', 10.50, 'Gold', undo_list, redo_list)
    vanzari = create_sell(vanzari, 3, 't2', 'g2', 100, 'Gold', undo_list, redo_list)
    vanzari = create_sell(vanzari, 5, 't5', 'g2', 9, 'Silver', undo_list, redo_list)
    vanzari = create_sell(vanzari, 4, 't4', 'g4', 20, 'Silver', undo_list, redo_list)
    vanzari = create_sell(vanzari, 6, 't6', 'g4', 25.0, 'Gold', undo_list, redo_list)
    vanzari = modificare_gen('t2','g10',vanzari,undo_list,redo_list)
    assert get_gen(vanzari[1]) == 'g10'
    vanzari = do_undo(undo_list,redo_list,vanzari)
    assert get_gen(vanzari[1]) == 'g2'
    vanzari = do_redo(undo_list,redo_list,vanzari)
    assert get_gen(vanzari[1]) ==  'g10'

    assert get_gen(vanzari[2]) == 'g10'
    vanzari = do_undo(undo_list, redo_list, vanzari)
    assert get_gen(vanzari[2]) == 'g2'
    vanzari = do_redo(undo_list, redo_list, vanzari)
    assert get_gen(vanzari[2]) == 'g10'





test_undo_redo_update()
test_undo_redo_delete()
test_undo_redo_discount()
test_undo_redo_modificare_gen()