from repo.base import BaseRepo

class UserRepo(BaseRepo):
    def listUser(self, limit, page):
        offset = limit * (page - 1)
        sql = "SELECT * FROM user LIMIT {} OFFSET {}".format(limit, offset)
        users = self.db.select(sql)
        return users
    
    def getUserById(self, id):
        users = self.db.select("SELECT * FROM user WHERE id = " + str(id))
        if len(users) > 0:
            return users[0]
        else:
            return None

    def createUser(self, data):
        user = {
            "name": data['name'],
            "account": data['account'],
            "server": data['server'],
            "profile": data['profile'] if "profile" in data else "",
            "description": data['description'] if "description" in data else ""
        }
        inserted = self.db.insertone("user", user)
        return inserted > 0
    
    def updateUser(self, data):
        user = {}
        if "name" in data: user["name"] = data["name"]
        if "account" in data: user["account"] = data["account"]
        if "server" in data: user["server"] = data["server"]
        if "profile" in data: user["profile"] = data["profile"]
        if "description" in data: user["description"] = data["description"]
        if "deleted" in data: user["deleted"] = data["deleted"]

        updated = self.db.update("user", user, "id = {}".format(data['id']))
        return updated > 0
    
    def deleteUser(self, id):
        deleted = self.db.update("user", { "deleted": 1 }, "id = {}".format(id))
        return deleted > 0