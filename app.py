from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Vehicule

app = Flask(__name__)
app.secret_key = 'Proyects123**'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres.votjisdewytppsljubiy:pruebabbase123@aws-0-us-west-2.pooler.supabase.com:6543/postgres?sslmode=require"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -- RUTAS ---
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first() ## Buscar usuario
        if user and user.password == request.form['password']: ## Verificar credenciales
            login_user(user) ## Iniciar sesión
            return redirect(url_for('index')) ## Redirigir al dashboard
        flash('Invalid username or password') ## Mensaje de error
    return render_template('login.html')

## RUTA DEL DASHBOARD
@app.route('/')
@login_required
def index():
    vehiculos = Vehicule.query.all()
    return render_template('inventario.html', vehiculos=vehiculos)

## RUTA PARA AGREGAR VEHICULO
@app.route('/crear_vehiculo',methods=['POST','GET'])
@login_required
def add_vehicule():
    if request.method == 'GET':
        return render_template('crear_vehiculo.html')
    brand = request.form.get('brand')
    model = request.form.get('model')
    year = request.form.get('year')
    kilometers = request.form.get('kilometers')
    color = request.form.get('color')
    price = request.form.get('price')

    new_vehicule = Vehicule(brand=brand, model=model, year=year, kilometers=kilometers, color=color, price=price)
    db.session.add(new_vehicule)
    db.session.commit()
    flash('Vehículo agregado exitosamente!')
    return redirect(url_for('index'))

##RUTA PARA EDITAR VEHICULOS
@app.route('/editar_vehiculo/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_vehicule(id):
    vehicule = Vehicule.query.get_or_404(id)
    if request.method == 'POST' : 
        vehicule.brand = request.form['brand']
        vehicule.model = request.form['model']
        vehicule.year = request.form['year']
        vehicule.kilometers = request.form['kilometers']
        vehicule.color = request.form['color']
        vehicule.price = request.form['price']
        db.session.commit()
        flash('Vehículo actualizado exitosamente!')
        return redirect(url_for('index'))
    return render_template('editar_vehiculo.html', vehicule=vehicule)

## Ruta para clientes
@app.route('/clientes')
@login_required
def clients():
    return render_template('clientes.html')


##PARA CERRAR SESIÓN
@app.route('/logout')
def logout(): 
    logout_user() ## Cerrar sesión
    return redirect(url_for('login')) ## Redirigir al login

with app.app_context(): ## Crear tablas
    db.create_all() ## Crear tablas

## INICIAR LA APLICACIÓN
if __name__ == '__main__':
    app.run(debug=True)
