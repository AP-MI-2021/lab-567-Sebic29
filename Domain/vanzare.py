def creeaza_vanzare(id_carte: int, tiltu_carte, gen_carte, pret, tip_reducere_client):
    """
    Creeaza o vanzare pentru carte
    :param id_carte: Id ul cartii
    :param tiltu_carte: Titlul cartii
    :param gen_carte: Genul cartii
    :param pret: Pretul cartii
    :param tip_reducere_client: Tip reducere client(none,silver,gold)
    :return: O vanzare
    """

    return [
        id_carte,
        tiltu_carte,
        gen_carte,
        pret,
        tip_reducere_client
    ]


def get_id(vanzare):
    """
    Getter pentru id ul prajiturii
    :param vanzare: cartea
    :return: id ul cartii
    """
    return vanzare[0]


def get_titlu(vanzare):
    """
    Getter pentru titlul prajiturii
    :param vanzare: cartea
    :return: titlul cartii
    """
    return vanzare[1]


def get_gen(vanzare):
    """
    Getter pentru genul prajiturii
    :param vanzare: cartea
    :return: genul cartii
    """
    return vanzare[2]


def get_pret(vanzare):
    """
    Getter pentru pretul prajiturii
    :param vanzare: cartea
    :return:pretul cartii
    """
    return vanzare[3]


def get_reducere(vanzare):
    """
    Getter pentru reducerea prajiturii
    :param vanzare: cartea
    :return: reducerea cartii
    """
    return vanzare[4]


def get_str(vanzare):
    return f'Vanzarea cu id ul {get_id(vanzare)} contine cartea {get_titlu(vanzare)}'
