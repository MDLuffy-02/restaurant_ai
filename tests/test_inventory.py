from src.inventory.inventory import calculate_reorder_point

def test_reorder_point():
    assert calculate_reorder_point(10, 3, 5) == 35
