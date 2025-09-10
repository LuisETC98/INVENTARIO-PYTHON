import sqlite3

DB_FILENAME = "inventario.db"

def get_connection():
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Crea la tabla si no existe."""
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo INTEGER NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            precio INTEGER NOT NULL,
            cantidad INTEGER NOT NULL
        );
        """)
        conn.commit()