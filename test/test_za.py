from src.za import container_ship


def test_container_ship():
    consumption = [3, 5, 2, 1]
    timestamps = [0, 3, 5, 8]
    assert container_ship(cons=consumption, stamps=timestamps) == 25
