from Domain.vanzare import get_titlu, creeaza_vanzare, get_id, get_pret, get_reducere, get_gen


def get_by_titlu(titlu, lista):
    """
    :param titlu:
    :param lista:
    :return:
    """
    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            return vanzare
    return None


def modificare_gen(titlu, gen_nou, lista, undo_list, redo_list):
    """
    Modifica genul cartii pentru un titlu dat
    :param titlu: titlul cartii al carui gen urmeaza sa fie modificat
    :param gen_nou: noul gen al acrtii
    :param lista: lista de vanzari
    :return:genul modificat in functie de titlul cartii
    """
    result = []

    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            result.append(creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                gen_nou,
                get_pret(vanzare),
                get_reducere(vanzare)
            ))
        else:
            result.append(vanzare)

    if get_by_titlu(titlu, lista) is None:
        raise ValueError("Nu exista titlul dat!")
    undo_list.append(lista)
    redo_list.clear()
    return result
