from flask import Flask, render_template, redirect, request, render_template_string, session, url_for
from src.db.connection import Connection
import os

CONFIG = {
    "HOST": "127.0.0.1",
    "NAME": "root",
    "PASSWORD": "student",
    "DATABASE": "web_app"
}
SECRET_KEY = "isdoahfuhds"

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'P{\xde\xcdUD^\xb1-\x16K\x06\x8e\xe0\x04\xab\xd3IY\xf5O\xb9\xb5~'


class User:
    def __init__(self):
        self.id = None
        self.username = None

    def load_credentials_from_db(self, username):
        try:
            conn = Connection(CONFIG["HOST"], CONFIG["NAME"], CONFIG["PASSWORD"], CONFIG["DATABASE"])
            cursor = conn.get_connection().cursor()
            query = f"SELECT id, username FROM user WHERE username='{username}'"
            cursor.execute(query)
            result = cursor.fetchall()[0]
            self.id = result[0]
            self.username = result[1]
            conn.close_connection()
        except Exception as e:
            print(e)

    def load_user_from_db(self, id):
        try:
            conn = Connection(CONFIG["HOST"], CONFIG["NAME"], CONFIG["PASSWORD"], CONFIG["DATABASE"])
            cursor = conn.get_connection().cursor()
            query = f"SELECT id, username FROM user WHERE id='{id}'"
            cursor.execute(query)
            result = cursor.fetchall()[0]
            self.id = result[0]
            self.username = result[1]
            conn.close_connection()
        except Exception as e:
            print(e)

    def add_contact(self, type, name, surname, value):
        try:
            conn = Connection(CONFIG["HOST"], CONFIG["NAME"], CONFIG["PASSWORD"], CONFIG["DATABASE"])
            mydb = conn.get_connection()
            cursor = mydb.cursor()
            query = f"INSERT INTO contact(type, name, surname, value, user_id) VALUES ('{type}', '{name}', '{surname}', '{value}', {self.id});"
            cursor.execute(query)
            mydb.commit()
            conn.close_connection()
        except Exception as e:
            print(e)

    def is_valid(self, username, password):
        try:
            conn = Connection(CONFIG["HOST"], CONFIG["NAME"], CONFIG["PASSWORD"], CONFIG["DATABASE"])
            cursor = conn.get_connection().cursor()
            query = f"SELECT CASE WHEN username='{username}' AND password='{password}' THEN true ELSE false END AS result FROM user;"
            print(query)
            cursor.execute(query)
            result = cursor.fetchall()[0][0]
            conn.close_connection()
            return result
        except Exception as e:
            print(e)

        return False

    def load_contacts(self):
        try:
            conn = Connection(CONFIG["HOST"], CONFIG["NAME"], CONFIG["PASSWORD"], CONFIG["DATABASE"])
            cursor = conn.get_connection().cursor()
            query = f"SELECT * FROM contact WHERE user_id='{self.id}';"
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close_connection()
            return result

        except Exception as e:
            print(e)


def renderHTML(templateHTML, user: User):
    return templateHTML.format(user=user)


@app.route('/', methods=["GET"])
def login_page():
    return render_template('login.jinja2')


@app.route('/', methods=["POST"])
def login():
    user = User()
    if user.is_valid(request.form["username"], request.form["password"]):
        print("dfo")
        user.load_credentials_from_db(request.form["username"])
        session["user_id"] = user.id
        session['username'] = user.username
        return redirect(url_for('application_page', name=user.username))
    return redirect("/")


@app.route('/contacts/<name>', methods=["GET"])
def contacts_page(name):
    user = User()
    user.load_credentials_from_db(name)
    contacts = user.load_contacts()
    return render_template('contacts.jinja2', content={'contacts': contacts})


@app.route('/contacts/<name>', methods=["POST"])
def add_contact(name):
    print(request.form)

    user = User()
    user.load_credentials_from_db(name)
    user.add_contact(request.form['type'], request.form['name'], request.form['surname'], request.form['value'])
    contacts = user.load_contacts()
    return render_template('contacts.jinja2', content={'contacts': contacts})


@app.route('/app', methods=["GET"])
def application_page():
    name = request.args.get('name')
    template = '''
                <!DOCTYPE html>
                <html>
                  <head>
                    <title>Contact app</title>
                    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/main.css') }}">
                  </head>
                  <body>
                    <div class="div-form">
                        <div>
                            <h1>Hello ''' + str(name) + '''!</h1>
                            <button class="app-button"><a href="/contacts/''' + str(name) + '''">Show your contacts</a></button>
                        </div>
                    </div>
                  </body>
                </html>
        '''
    return render_template_string(template)


@app.route('/index')
def index():
    name = request.args.get('name')

    template = '''
            <!DOCTYPE html>
            <html>
              <head>
                <title>No Filter</title>
              </head>
              <body>
                <p>''' + str(name) + '''</p>
              </body>
            </html>'''
    return render_template_string(template)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    
