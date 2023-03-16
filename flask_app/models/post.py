# import the function to create a db instance
from flask_app.config.mysqlconnection import connectToMySQL, DB
# import datetime to convert our datetime to Month Day, Year format
from datetime import datetime

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.created_by = data['created_by'] #this is the FK from users table
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

    #call this method to retrieve all posts
    @classmethod
    def get_all_posts(cls):
        # list to hold posts for query results / user search
        all_posts = []
        # get all posts from db, update date formatting, append to list, then return list
        query = "SELECT * FROM posts;"
        results = connectToMySQL(cls.DB).query_db(query)
        for post in results:
            formatted_post = Post.convert_dates(post)
            all_posts.append(cls(formatted_post))
        return all_posts
    
    #call this method to retrieve specific posts
    @classmethod
    def get_search_results(cls):
        # list to hold posts for query results / user search
        search_results = []
        # get all posts from db, update date formatting, append to list, then return list
        query = "SELECT * FROM posts;"
        results = connectToMySQL(cls.DB).query_db(query)
        for post in results:
            formatted_post = Post.convert_dates(post)
            search_results.append(cls(formatted_post))
        return search_results
    
    #call this method to retrieve one specific post
    @classmethod
    def get_post_by_id(cls, data):
        # post_list used to convert the list of dicts into a list
        post_list = []
        # get the post from db by id, update date formatting, append to list, then return list
        query = "SELECT * FROM posts WHERE id = %(id)s;"
        data = {'id' : id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        for post in results:
            formatted_post = Post.convert_dates(post)
            post_list.append(cls(formatted_post))
        return post_list