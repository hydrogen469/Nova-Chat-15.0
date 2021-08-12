from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from wtform_fields import *

from models import *

#Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

#Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://jlouvyxuavdbwi:d61d95493dd725d770ef5a1726775f45e8ebbf431f48de4784a96cbbc7339031@ec2-35-169-188-58.compute-1.amazonaws.com:5432/de0rjnv4rmlt7f'
db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
  return User.query.get(int(id))

@app.route("/", methods=["GET", "POST"])

def index():
  reg_form = RegistrationForm()
  if reg_form.validate_on_submit():
      username = reg_form.username.data
      password = reg_form.password.data

      hashed_pswd = pbkdf2_sha256.hash(password)

      user = User(username=username, password=hashed_pswd)
      db.session.add(user)
      db.session.commit()

      flash('Registered into Nova Chat. Please log in.', 'success')
      return redirect(url_for('login'))

  return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  login_form = LoginForm()
  if login_form.validate_on_submit():
    user_object = User.query.filter_by(username=login_form.username.data).first()
    login_user(user_object)
    return redirect(url_for('chat'))
    return render_template("login.html", form=login_form)

@app.route("/chat", methods=['GET', 'POST'])
@login_required
def chat():
  if not current_user.is_authenticated:
      flash('Please log in.', 'danger')
      return redirect(url_for('login'))

  return "Chat with Stars"

@app.route("/logout", methods=['GET'])
def logout():
  logout_user()
  flash('Logged out successfully!', 'success')
  return redirect(url_for('login'))

if __name__ == "__main__":
  app.run(debug=True)