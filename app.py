from flask import Flask
from db.db import DB
from util.response import wrapResp
from controller.user import UserController
import config

app = Flask(__name__)
app.config["DEBUG"] = config.DEBUG

myDB = DB(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PASS, database=config.DB_DATABASE)
userController = UserController(myDB)

@app.route('/')
def home(): return 'Hello Page!'

@app.route('/user/all', methods=['GET'])
def userAll(): return wrapResp(userController.all)

@app.route('/user/detail', methods=['GET'])
def userDetail(): return wrapResp(userController.detail)

@app.route('/user/create', methods=['POST'])
def user_create(): return wrapResp(userController.create)

@app.route('/user/update', methods=['POST'])
def user_update(): return wrapResp(userController.update)

@app.route('/user/delete', methods=['POST'])
def user_delete(): return wrapResp(userController.delete)

app.run(host=config.HOST, port=config.PORT)