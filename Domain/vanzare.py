def creeaza_vanzare(id_carte: int,tiltu_carte,gen_carte,pret,tip_reducere_client ) :
    """
    Creeaza o vanzare pentru carte
    :param id_carte: Id ul cartii
    :param tiltu_carte: Titlul cartii
    :param gen_carte: Genul cartii
    :param pret: Pretul cartii
    :param tip_reducere_client: Tip reducere client(none,silver,gold)
    :return: O vanzare
    """

    return {
        'id' : id_carte,
        'titlu' : tiltu_carte,
        'gen' : gen_carte,
        'pret' : pret,
        'reducere' :  tip_reducere_client,
    }


def get_id(vanzare) :
    """
    Getter pentru id ul prajiturii
    :param vanzare: cartea
    :return: id ul cartii
    """
    return vanzare['id']


def get_titlu(vanzare) :
    """
    Getter pentru titlul prajiturii
    :param vanzare: cartea
    :return: titlul cartii
    """
    return vanzare['titlu']


def get_gen(vanzare) :
    """
    Getter pentru genul prajiturii
    :param vanzare: cartea
    :return: genul cartii
    """
    return vanzare['gen']


def get_pret(vanzare) :
    """
    Getter pentru pretul prajiturii
    :param vanzare: cartea
    :return:pretul cartii
    """
    return vanzare['pret']


def get_reducere(vanzare) :
    """
    Getter pentru reducerea prajiturii
    :param vanzare: cartea
    :return: reducerea cartii
    """
    return vanzare['reducere']


def get_str(vanzare) :
    f'Vanzarea cu id ul {get_id(vanzare)} contine cartea {get_titlu(vanzare)}'