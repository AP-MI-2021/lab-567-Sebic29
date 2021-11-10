from Domain.vanzare import creeaza_vanzare
from Logic.Crud import create_sell
from Logic.undo_and_redo import do_undo, do_redo


def get_data():
    return [
        creeaza_vanzare(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_vanzare(2, 'v2', 'gen2', 20, 'none'),
        creeaza_vanzare(3, 'v3', 'gen3', 12, 'gold'),
        creeaza_vanzare(4, 'v4', 'gen4', 34, 'silver'),
    ]


def test_undo_redo():
    vanzari = get_data()
    undo_lst = []
    redo_lst = []
    result = create_sell(vanzari, 5,'t1', 'g9',15, 'Silver', undo_lst, redo_lst)
    result = do_undo(undo_lst, redo_lst, result)
    assert len(result) == len(vanzari)
    result = do_undo(undo_lst, redo_lst, result)
    assert result == None
    result = do_redo(undo_lst, redo_lst, result)
    assert len(result) == len(vanzari) + 1
