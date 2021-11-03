from Domain.vanzare import get_gen, get_pret


def min_pret_per_gen(lst_vanazri):
    """
    Determina prețului minim pentru fiecare gen
    :param lst_vanazri: lista vanzarilor
    :return: pretul minim pentru fiecare gen
    """
    rezultat = {}
    for vanzare in lst_vanazri:
        gen = get_gen(vanzare)
        pret = get_pret(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat
