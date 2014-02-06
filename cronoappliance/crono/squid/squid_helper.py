from django.utils import simplejson
from passlib.apache import HtpasswdFile

USERS_DATABASE = '/etc/squid3/passwd'

class SquidHelper( object ):

    def __init__(self, database):
        self.ht = HtpasswdFile(database, new=False)

    def user_exists(self, user):
        return user in simplejson.loads(self.get_users_as_json())['users']

    def get_users_as_json(self):
        return simplejson.dumps({'users': self.ht.users()})

    def save(self, user, password):
        self.ht.set_password(user, password)
        self.ht.save()


if __name__ == '__main__':
    sh = SquidHelper(USERS_DATABASE)
    print sh.get_users_as_json()
