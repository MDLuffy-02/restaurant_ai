def test_database_module_import():
    from config.database import get_connection
    assert callable(get_connection)

    connection = get_connection()
    assert connection is not None
    print("Database connected")
    
