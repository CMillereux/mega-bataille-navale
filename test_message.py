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
