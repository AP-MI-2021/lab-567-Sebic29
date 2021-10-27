from Domain.vanzare import creeaza_vanzare, get_id


def create_sell(lst_vanzari, id_carte, titlu_carte, gen_Carte, pret, tip_reducere_client):
    """
    Creeaza o lista de vanzari
    :param lst_vanzari: Lista de carti pusa spre vanzare
    :param id_carte: id ul cartii
    :param titlu_carte: Titlul cartii
    :param gen_Carte: Genul cartii
    :param pret: Pretul cartii
    :param tip_reducere_client: Tipul reducerii de aplicat clientului
    :return: O lista
    """

    vanzare = creeaza_vanzare(id_carte, titlu_carte, gen_Carte, pret, tip_reducere_client)
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare: int = None):
    """
    Citeste o vanzare
    :param lst_vanzari:Lista de vanzari
    :param id_vanzare:id ul vanzarii
    :return: vanzare cu id-ul id_vanzare sau lista cu toate vanzarile, daca id_vanzare=None
    """
    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_cu_id = vanzare

    if vanzare_cu_id:
        return vanzare_cu_id
    return lst_vanzari


def update(lst_vanzari, new_vanzare):
    """
    Actualizeaza o vanzare.
    :param lst_vanzari: lista de vanzari.
    :param new_vanzare:vanzarea care se va actualiza cu cea exista pe acel id.
    :return: o lista cu vanzarea actualizata.
    """

    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(vanzare)
        else:
            new_vanzari.append(new_vanzare)
    return new_vanzari


def delete(lst_vanzari, id_vanzare: int):
    """
    Sterge o vanzare existenta in lista
    :param lst_vanzari: O lista de vanzazri
    :param id_vanzare:id ul vanzarii care urmeaza sa fie stearsa
    :return: o lista de vaznari fara vanzarea cu id-ul id_vanzare.
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)

    return new_vanzari
