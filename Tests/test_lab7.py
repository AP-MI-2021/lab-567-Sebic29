
from Logic.Crud import create_sell
from Logic.undo_and_redo import do_undo, do_redo


def undo_redo_lab7():

    start_program = []
    undo_list = []
    redo_list = []
    start_program = create_sell(start_program, 1, 't1', 'g1', 10, 'Silver', undo_list, redo_list)
    start_program = create_sell(start_program, 2, 't2', 'g2', 10.50, 'Gold', undo_list, redo_list)
    start_program = create_sell(start_program, 3, 't3', 'g2', 100, 'Gold', undo_list, redo_list)
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 0
    start_program = do_undo(undo_list, redo_list, start_program)
    assert start_program == []
    start_program = create_sell(start_program, 1, 't1', 'g1', 10, 'Silver', undo_list, redo_list)
    start_program = create_sell(start_program, 2, 't2', 'g2', 10.50, 'Gold', undo_list, redo_list)
    start_program = create_sell(start_program, 3, 't3', 'g2', 100, 'Gold', undo_list, redo_list)
    start_program = do_redo(undo_list,redo_list,start_program)
    assert len(start_program) == 3
    start_program = do_undo(undo_list,redo_list,start_program)
    assert len(start_program) == 2
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = do_redo(undo_list,redo_list,start_program)
    assert len(start_program) == 2
    start_program = do_redo(undo_list,redo_list,start_program)
    assert len(start_program) == 3
    start_program = do_undo(undo_list,redo_list,start_program)
    assert len(start_program) == 2
    start_program = do_undo(undo_list,redo_list,start_program)
    assert len(start_program) == 1
    start_program = create_sell(start_program, 6, 't5', 'g3', 100, 'Gold', undo_list, redo_list)
    start_program = do_redo(undo_list,redo_list,start_program)
    assert len(start_program) == 2
    start_program = do_undo(undo_list,redo_list,start_program)
    assert len(start_program) == 1
    start_program = do_undo(undo_list,redo_list,start_program)
    assert len(start_program) == 0
    start_program = do_redo(undo_list,redo_list,start_program)
    assert len(start_program) == 1
    start_program = do_redo(undo_list,redo_list,start_program)
    assert len(start_program) == 2
    start_program = do_redo(undo_list,redo_list,start_program)
    assert len(start_program) == 2


