from repo.user import UserRepo
from flask import request

class UserController():
    def __init__(self, db):
        self.repo = UserRepo(db)
    
    def list(self):
        limit = int(request.args['limit']) if 'limit' in request.args else 20
        page = int(request.args['page']) if 'page' in request.args else 1
        if limit < 0 or page < 0: raise Exception("params invalid")
        if page == 0: page = 1

        users = self.repo.listUser(limit, page)
        return users

    def detail(self):
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            raise Exception("param id invalid")

        user = self.repo.getUserById(id)
        if user is None:
            raise Exception("user not exists")
        else:
            return user

    def create(self):
        data = request.get_json()
        print("data received: ", data)
        
        isOk = self.repo.createUser(data)
        if isOk:
            return True
        else:
            raise Exception("create user failed")
    
    def update(self):
        data = request.get_json()
        print("data received: ", data)
        if "id" not in data: raise Exception("param id not exists")

        user = self.repo.getUserById(data['id'])
        if user is None:
            raise Exception("user not exists")
        
        isOk = self.repo.updateUser(data)
        if isOk:
            return True
        else:
            raise Exception("update user failed")
    
    def delete(self):
        data = request.get_json()
        print("data received: ", data)
        if "id" not in data: raise Exception("param id not exists")

        user = self.repo.getUserById(data['id'])
        if user is None:
            raise Exception("user not exists")

        isOk = self.repo.deleteUser(data['id'])
        if isOk:
            return True
        else:
            raise Exception("delete user failed")