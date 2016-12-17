import pymongo

def get_coll():
    client = pymongo.MongoClient()
    db = client.cindy
    user = db.user_collection
    return user


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        user = {"name": self.name, "email": self.email}
        coll = get_coll()
        id = coll.insert(user)
        print(id)

    @staticmethod
    def query_users():
        users = get_coll().find()
        return users