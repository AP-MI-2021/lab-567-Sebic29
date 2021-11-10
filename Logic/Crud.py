from Domain.vanzare import creeaza_vanzare, get_id


def create_sell(lst_vanzari, id_carte, titlu_carte, gen_Carte, pret, tip_reducere_client, undo_list: list,
                redo_list: list):
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
    if read(lst_vanzari, id_carte) is not None:
        raise ValueError("Deja exista o vanzare cu id-ul {0}".format(id_carte))
    vanzare = creeaza_vanzare(id_carte, titlu_carte, gen_Carte, pret, tip_reducere_client)
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare: int = None):
    """
    Citeste o vanzare
    :param lst_vanzari:Lista de vanzari
    :param id_vanzare:id ul vanzarii
    :return: vanzare cu id-ul id_vanzare sau lista cu toate vanzarile, daca id_vanzare=None
    """
    if not id_vanzare:
        return lst_vanzari

    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_cu_id = vanzare

    if vanzare_cu_id:
        return vanzare_cu_id
    return None


def update(lst_vanzari, new_vanzare, undo_list: list,
           redo_list: list):
    """
    Actualizeaza o vanzare.
    :param lst_vanzari: lista de vanzari.
    :param new_vanzare:vanzarea care se va actualiza cu cea exista pe acel id.
    :return: o lista cu vanzarea actualizata.
    """

    if read(lst_vanzari, get_id(new_vanzare)) is None:
        raise ValueError(f'Nu exista o vanzarea cu id ul {get_id(new_vanzare)} pe care sa o actualizam')

    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(vanzare)
        else:
            new_vanzari.append(new_vanzare)

    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari


def delete(lst_vanzari, id_vanzare: int, undo_list: list,
           redo_list: list):
    """
    Sterge o vanzare existenta in lista
    :param lst_vanzari: O lista de vanzazri
    :param id_vanzare:id ul vanzarii care urmeaza sa fie stearsa
    :return: o lista de vaznari fara vanzarea cu id-ul id_vanzare.
    """

    if read(lst_vanzari, id_vanzare) is None:
        raise ValueError(f'Nu exista vanzarea cu id ul {id_vanzare} pe care sa o stergem')

    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)

    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari
