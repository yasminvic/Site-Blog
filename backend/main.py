from configs.config import *
from routes import *

with app.app_context():
    db.create_all()
    CORS(app)
    app.run(debug=True, port=5000, host='0.0.0.0')

    
#declarando a rota
# @app.route("/")
# def home():
#     return render_template('home.html', posts=posts)

# @app.route("/about")
# def about():
#     return render_template('about.html')

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()

#     #validando form
#     if(form.validate_on_submit()):
#         return redirect(url_for('home'))
    
#     return render_template('register.html', form=form)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     #mensagem de validação
#     if(form.validate_on_submit()):   
#        if(form.email.data != "exemplo@gmail.com"):                  #o danger é pro alert do bootstrap
#         flash('Email or Password are incorrect. Please, try again!', 'danger') 
#        else:
#             return redirect(url_for('home'))
    
#     return render_template('login.html', form=form)

# app.run(debug = True, host = '0.0.0.0', port = 5000)