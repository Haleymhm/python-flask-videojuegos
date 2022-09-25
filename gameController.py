from db import conexion_db

def get_games():
    conexion = conexion_db()
    games = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos")
        games = cursor.fetchall()
    conexion.close()
    return games