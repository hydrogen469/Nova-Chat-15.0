from flask import Flask, render_template

from wtform_fields import *

from models import *

#Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

#Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://jlouvyxuavdbwi:d61d95493dd725d770ef5a1726775f45e8ebbf431f48de4784a96cbbc7339031@ec2-35-169-188-58.compute-1.amazonaws.com:5432/de0rjnv4rmlt7f'
db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])

def index():
  reg_form = RegistrationForm()
  if reg_form.validate_on_submit():
      username = reg_form.username.data
      password = reg_form.password.data

      user_object = User.qurey.filter_by(username=username).first()
      if user_object:
          return "Oops! Someone has already taken this username!"

      user = User(username=username, password=password)
      db.session.add(user)
      db.session.commit()
      return "Inserted into DB!"

  return render_template("index.html", form=reg_form)

if __name__ == "__main__":
  app.run(debug=True)