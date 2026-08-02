import sqlite3

def init_db():
    conn = sqlite3.connect("ldpanamerican.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            email TEXT,
	    empresa TEXT,
	    codigo_pais TEXT,
            telefono TEXT,
            mensaje TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route('/soluciones/employer-of-record')
def eor():
    # Asegúrate de guardar el HTML en la carpeta templates con el nombre 'eor.html'
    return render_template("eor.html")

@app.route('/soluciones/talent-acquisition-hunting')
def talent():
    # Guarda el HTML en la carpeta templates con el nombre 'talent.html'
    return render_template('talent.html')

@app.route('/soluciones/payroll-nomina-global')
def payroll():
    # Guarda el HTML en la carpeta templates con el nombre 'payroll.html'
    return render_template('payroll.html')

@app.route('/soluciones/bpo-tercerizacion-servicios')
def bpo():
    # Guarda el HTML en la carpeta templates con el nombre 'bpo.html'
    return render_template('bpo.html')

@app.route('/soluciones/accounting-finance')
def accounting_finance():
    # Guarda el HTML en tu carpeta templates con el nombre 'accounting.html'
    return render_template('accounting.html')

@app.route('/nosotros')
def nosotros():
    # Renderiza la nueva plantilla independiente de la sección corporativa
    return render_template('nosotros.html')
@app.route('/nosotros2')
def nosotros2():
    # Renderiza la nueva plantilla independiente de la sección corporativa
    return render_template('nosotros2.html')
@app.route('/nosotros3')
def nosotros3():
    # Renderiza la nueva plantilla independiente de la sección corporativa
    return render_template('nosotros3.html')

@app.route("/contacto", methods=["POST"])
def contacto():
    # Usamos .get() para que si el campo no existe, devuelva None en lugar de un error 400
    nombre = request.form.get("nombre", "")
    email = request.form.get("email", "")
    empresa = request.form.get("empresa", "")          # Nuevo campo del modal
    codigo_pais = request.form.get("codigo_pais", "")
    telefono = request.form.get("telefono", "")
    mensaje = request.form.get("mensaje", "")    
    # telefono_completo = f"{codigo_pais} {telefono}".strip()

    # Guardar en la base de datos (Asegúrate de que tu tabla tenga estas columnas)
    try:
        conn = sqlite3.connect("ldpanamerican.db")
        cursor = conn.cursor()
        cursor.execute("""
	    INSERT INTO contactos (nombre, email, empresa, codigo_pais, telefono, mensaje)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, email, empresa, codigo_pais, telefono, mensaje))
        conn.commit()
        conn.close()
        print(f"📩 Lead guardado: {nombre} de {empresa}")
        return "OK"
    except Exception as e:
        print(f"❌ Error en DB: {e}")
        return "Error", 500

@app.route("/admin")
def admin():
    conn = sqlite3.connect("ldpanamerican.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contactos")
    datos = cursor.fetchall()

    conn.close()

    return render_template("admin.html", contactos=datos)


if __name__ == "__main__":
    app.run(debug=True, port=5001)











