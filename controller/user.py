from controller.base import BaseControler
from flask import request

class UserController(BaseControler):
    def all(self):
        users = self.db.select("SELECT * FROM user")
        return users

    def detail(self):
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            raise Exception("id not exists")

        users = self.db.select("SELECT * FROM user WHERE id = " + str(id))
        return users

    def create(self):
        data = request.get_json()
        print("data received: ", data)
        user = {
            "username": data['name'],
            "email": data['email'],
            "password": data['password'],
            "number": data['number']
        }
        inserted = self.db.insertone("user", user)
        print(inserted, "records inserted.")
        return inserted
    
    def update(self):
        data = request.get_json()
        print("data received: ", data)
        if "id" not in data: raise Exception("id not exists")

        user = {}
        if "name" in data: user["username"] = data["name"]
        if "email" in data: user["email"] = data["email"]
        if "password" in data: user["password"] = data["password"]
        if "bio" in data: user["bio"] = data["bio"]
        if "image" in data: user["image"] = data["image"]
        if "number" in data: user["number"] = data["number"]

        updated = self.db.update("user", user, "id = {}".format(data['id']))
        print(updated, "records updated.")
        return updated
    
    def delete(self):
        data = request.get_json()
        print("data received: ", data)
        if "id" not in data: raise Exception("id not exists")

        deleted = self.db.update("user", { "deleted": 1 }, "id = {}".format(data['id']))
        print(deleted, "records deleted.")
        return deleted