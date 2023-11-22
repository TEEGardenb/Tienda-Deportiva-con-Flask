# este programa se ejecuta manualmente para crear los datos
import sqlite3

# establece una conexión con la base de datos
connection = sqlite3.connect("tienda_deportiva.sqlite3")
# crear un cursor, o canal de comunicación con la base de datos
cursor = connection.cursor()

# utiliza el cursor para ejecutar los comandos SQL
# necesarios para la creación de esta base de datos

# 1. borrar la tabla, si ya existe
cursor.execute("""
DROP TABLE IF EXISTS productos;
""")

# 2. crear la tabla, si no existe 
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    categoria TEXT NOT NULL,
    marca TEXT NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio INT NOT NULL
);
""")

# 3. elaborar la lista de datos
datos = [
    (101, 'Ropa', 'Nike', 'Camiseta Dry-Fit', 'Camiseta deportiva transpirable, ideal para entrenamientos intensos', 29900),
    (104, 'Calzado', 'Adidas', 'Zapatillas Ultraboost', 'Zapatillas para correr con tecnología Boost para mayor comodidad', 159900),
    (201, 'Equipamiento', 'Under Armour', 'Guantes de Levantamiento de Pesas', 'Guantes acolchados para proteger las manos durante el levantamiento de pesas', 59900),
    (203, 'Accesorios', 'Puma', 'Mochila Deportiva', 'Mochila espaciosa con compartimentos para llevar tus pertenencias de forma organizada', 79900),
    (207, 'Calzado', 'Reebok', 'Zapatillas CrossFit Nano X', 'Zapatillas diseñadas para entrenamientos de CrossFit con suela resistente', 129900),
    (208, 'Equipamiento', 'Nike', 'Balón de Fútbol', 'Balón oficial para partidos de fútbol, tamaño estándar y duradero', 49900),
    (301, 'Ropa', 'Adidas', 'Pantalones Deportivos', 'Pantalones cómodos y transpirables para actividades físicas', 89900),
    (302, 'Accesorios', 'Garmin', 'Reloj Deportivo GPS', 'Reloj con seguimiento GPS para correr, nadar y otras actividades deportivas', 249900),
    (304, 'Equipamiento', 'Wilson', 'Raqueta de Tenis', 'Raqueta de tenis profesional con tecnología avanzada para un mejor rendimiento', 149900),
]

# 4. insertar los datos en la tabla
cursor.executemany("""
INSERT INTO productos VALUES(?, ?, ?, ?, ?, ?);
""", datos)

# 5. grabar las transacciones
connection.commit()
connection.close()

# se ejecuta desde el Shell: python3 crear_db.py