from protocol.message import compose, compose_connexion, compose_bullet, compose_response, parse_message


def test_compose_reponse():
    data = compose_response(1, 2)

    position_navire['hit'] = False
    navire.hit_positions.append(position_navire)

    position_navire2 = position_navire.copy()
    position_navire2['hit'] = True
    navire.hit_positions.append(position_navire2)
    assert navire.est_detruit is False
    assert isinstance(navire, navire)


def test_compose_connexion():
    data = compose_connexion(1, 2)

    assert data == b'\x01\x01\x02'



    from protocol import compose_bullet, parse_message, compose_connexion


def test_compose_bullet():
    data = compose_bullet(1, 2)
    assert data == b'\x01\x01\x02'


def test_parse():
    data = parse_message(b'\x01\x01\x02')
    assert data == (1, b'\x01\x02')


def test_compose_connexion():
    data = compose_connexion("Player 1")
    assert data == b'\x00Player 1'

def tir_dans_eau():
    quadrillage = Quadrillage ()
    assert data == 

def touche():
    data =  ()
    assert data == 

def coule():
    data =  ()
    assert data == 

def disposition_bateau() :
    data =  ()
    assert data == 

def pseudo() :
    data =  ()
    assert data == 

def modif_pseudo() :
    data =  ()
    assert data == 

def format_pseudo() :
    data =  ()
    assert data == 

def tire_joueur() :
    data =  ()
    assert data == 

def tire_adverse() :
    data =  ()
    assert data == 

def nuke() :
    data =  ()
    assert data == 

def bateau_petit() :
    data =  ()
    assert data == 

def bateau_grand() :
    data =  ()
    assert data == 

def case_vide() :
    data =  ()
    assert data == 

def case_prise() :
    data =  ()
    assert data == 

