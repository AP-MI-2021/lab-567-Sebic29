from Domain.vanzare import get_pret


def ordonare_crescator(lst_vanzari):
    """
    Ordoneaza crescator vanzarile dupa pret
    :param lst_vanzari: O lista
    :return: O lista cu vanzarile ordonate crescator
    """
    result = sorted(lst_vanzari, key=lambda vanzare: get_pret(vanzare))
    return result