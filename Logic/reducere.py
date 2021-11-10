from Domain.vanzare import get_reducere, get_pret, get_id, get_titlu, get_gen, creeaza_vanzare


def reducere_tip(lst_vanzari, tip_reducere, undo_list, redo_list):
    """
    
    :param lst_vanzari: O lista de vanzari
    :param tip_reducere: Reducerea ce va fi aplicata in fucntie de tipul de reducere Silver/Gold
    :return: Returneaza o lista cu reducirile aplicate.
    """
    dict_reducere = {
        'Silver': 5,
        'silver': 5,
        'Gold': 10,
        'gold': 10,
        'None': None,
        'none': None,

    }
    if tip_reducere != 'Silver' and tip_reducere != 'Gold':
        raise ValueError('Tipul de reducere poate fi Silver sau Gold')

    if tip_reducere == ' ':
        raise ValueError('Textul introdus nu poate fi gol')

    result = []
    for vanzare in lst_vanzari:
        if tip_reducere == get_reducere(vanzare):
            pret_nou = get_pret(vanzare) - (dict_reducere[tip_reducere] / 100) * get_pret(vanzare)
            result.append(creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                pret_nou,
                tip_reducere
            ))
        else:
            result.append(vanzare)
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return result
