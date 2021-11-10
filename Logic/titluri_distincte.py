from Domain.vanzare import get_titlu, get_gen


def distinct_title(lst_vanzari):
    """
    Afisarea titlurilor distincte pentru fiecare gen
    :param lst_vanzari: O lista de vanzari
    :return: Returneaza numarul de titluri distincete pentru fiecare gen
    """

    result = {}
    for vanzare in lst_vanzari:
        if get_gen(vanzare) not in result:
            result[get_gen(vanzare)] = []
            result[get_gen(vanzare)].append(get_titlu(vanzare))
        else:
            result[get_gen(vanzare)].append(get_titlu(vanzare))

    return result
