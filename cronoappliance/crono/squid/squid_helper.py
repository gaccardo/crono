from django.utils import simplejson

class SquidHelper( object ):
    
    def get_users_as_json(self):
        users_database_pointer = open('/etc/squid3/passwd', 'r')
        users_database = users_database_pointer.readlines()
        users_database_pointer.close()
        users = list()

        for line in users_database:
            users.append(line.split(':')[0])

        return simplejson.dumps({'users': users})
