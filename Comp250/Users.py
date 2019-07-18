counter=0;
from flask import Flask,request,jsonify,session
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
import json
import smtplib
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__)
CORS(app)
jwt=JWTManager(app)
DEBUG=True
app.config.from_object(__name__)
with open('config.json','r') as c:
    params=json.load(c)['params']
app.config.update(
    SECRET_KEY='Gobindrai1',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:"password"localhost:5432/portfoliousers',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    USER_ENABLE_EMAIL=True,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    # MAIL_USE_TLS = True,
    MAIL_USERNAME='',
    MAIL_PASSWORD=''
)

db = SQLAlchemy(app)
mail = Mail(app)


class Users(db.Model):
     __tablename__='user_reg2'
     id =db.Column(db.Integer,primary_key=True)
     username = db.Column(db.String)
     lastname = db.Column(db.String)
     email=db.Column(db.String)
     password = db.Column(db.String)
     confirmcode=db.Column(db.Integer)
     def __init__(self,username,lastname,email,password,confirmcode):
            # self.id=id
            self.username=username
            self.lastname=lastname
            self.email=email
            self.password=password
            self.confirmcode=confirmcode


class UserConfirm(db.Model):
    __tablename__ = 'userconfirm'
    id = db.Column(db.Integer,db.ForeignKey('user_reg2.id'),primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    userid = db.Column(db.Integer,primary_key=True)
    def __init__(self,id,email, password):
        self.id=id
        self.email = email
        self.password = password


@app.route('/reg',methods=['POST'])
def reg():
    global counter;
    username = request.get_json()['username']
    lastname = request.get_json()['lastname']
    email = request.get_json()['email']
    password = generate_password_hash(request.get_json()['password'])
    data=Users.query.filter_by(email=email).first()
    if data:
        result1=jsonify("Already Registered");
        return result1
    else:
        counter +=1
        address1 = Users(username, lastname, email,password,counter)
        db.session.add(address1)
        db.session.commit()
        mail.send_message('Hey' + str(username), sender='honeykaurp1989@gmail.com',
                          recipients=[email],
                          body='Thanks For Login and here is your Confirm code' + "\n" + str(counter)
                          )
        result ={
            "username":username,
            "lastname":lastname,
            "email":email,
            "password":password
        }
        result=jsonify({"Successfully":result});
        return result

@app.route('/confirmed',methods=['POST'])
def confirmed():
    email = request.get_json()['email']
    password = request.get_json()['password']
    confirmcode = request.get_json()['confirmcode']
    data=Users.query.filter_by(email=email).first()
    confirmedcode = data.confirmcode
    id=data.id;
    print(id,confirmedcode)
    if confirmedcode==int(confirmcode):
        address2 = UserConfirm(id,email,password);
        db.session.add(address2);
        db.session.commit();
        result = {
            "id":id,
            "username": email,
            "password": password
        }
        result = jsonify({"Successfully"});
        return result;

    else:
        data = Users.query.filter_by(email=email).first()
        result= jsonify({"Something Wrong":data.password});
        return result;

@app.route('/login',methods=['POST'])
def login():
    email = request.get_json()['email']
    password = request.get_json()['password']
    data = Users.query.filter_by(email = email).first()
    if  data and check_password_hash(data.password,password):
        token=create_access_token(identity={"username":data.username,"lastname":data.lastname,"id":data.id,"email":data.email})
        return jsonify({"token":token})
    else:
        resp=jsonify({"error":"INVALID USER"});
        return resp

if __name__ == '__main__':
    app.run()

