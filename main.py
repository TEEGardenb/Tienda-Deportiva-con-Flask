from flask import Flask, render_template, redirect
import sqlite3
from pprint import pprint

# cargamos los datos
connection = sqlite3.connect("tienda_deportiva.sqlite3")
connection.row_factory = sqlite3.Row # modo diccionario
cursor = connection.cursor()
cursor.execute("""
SELECT * FROM productos;
""")
productos = [dict(producto) for producto in cursor.fetchall()]
print(productos)
cursor.close()
connection.close()

# aplicación
app = Flask(__name__)

# Ruta principal
@app.route('/')
def ruta_raiz():
  return render_template('index.html', productos=productos)

# Ruta del producto
@app.route('/producto/<int:pid>')
def ruta_producto(pid):
  for producto in productos:
    if pid == producto['id']:
      return render_template('producto.html', producto=producto)
  return redirect('/')
  
# programa principal
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)