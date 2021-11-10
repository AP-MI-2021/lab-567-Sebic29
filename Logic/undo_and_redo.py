
def do_undo(undo_list:list, redo_list:list,current_list):
    """
    Face un undo
    :param undo_list: Lista pentru undo
    :param redo_list: Lista pentru redo
    :return:
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()
    return None


def do_redo(undo_list:list , redo_list:list,current_list):
    """
    Face un redo
    :param undo_list: Lista pentru undo
    :param redo_list: Lista pentru redo
    :return:
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    else:
        return None