# import the function to create a db instance
from flask_app.config.mysqlconnection import connectToMySQL, DB
# import datetime to convert our datetime to Month Day, Year format
from datetime import datetime


class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.can_post = data['can_post'] # 0 False, 1 True || I might move this to a superuser later
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def convert_dates(dict):
        # using if statements so this can be called whenever w/o worry of key errors
        # convert created_at date to month day, year
        if dict['created_at']:
            created_date = datetime.strptime(str(dict['created_at']),'%Y-%m-%d %H:%M:%S')
            dict['created_at'] = created_date.strftime('%B %d, %y')
        # convert updated_at date to month day, year
        if dict['updated_at']:
            created_date = datetime.strptime(str(dict['updated_at']),'%Y-%m-%d %H:%M:%S')
            dict['updated_at'] = created_date.strftime('%B %d, %y')
        return dict

    @classmethod
    def get_all_users(cls):
        users = []
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        for user in results:
            created_date = datetime.strptime(str(user['created_at']),'%Y-%m-%d %H:%M:%S')
            user['created_at'] = created_date.strftime('%B %d, %y')
            users.append(cls(user))
        return users

        
