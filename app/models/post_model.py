from datetime import datetime
import pymongo
from app.exceptions.post_exists import PostNotExistError
from app.exceptions.update_exception import InvalidDataUpdateError

from app.services.post_service import check_post_exist, check_update

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['kenzie']


class Post:
    def __init__(self, *args, **kwargs) -> None:
        self.title = kwargs['title']
        self.author = kwargs['author']
        self.tags = kwargs['tags']
        self.content = kwargs['content']
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self._id = len(list(db.posts.find())) + 1


    def create_post(self):
        if not check_update(self.__dict__['title'], self.__dict__['author'], self.__dict__['tags'], self.__dict__['content']):
            raise InvalidDataUpdateError
        
        db.posts.insert_one(self.__dict__)

    @staticmethod
    def get_all_posts():
        posts_list = list(db.posts.find())
        print(posts_list)
        return posts_list
  
    
    @staticmethod
    def deleted_post(post_id):
            
        if not check_post_exist(post_id, list(db.posts.find())):
            raise PostNotExistError

        deleted_post = db.posts.find_one_and_delete({"_id": post_id})
        return deleted_post
    

    @staticmethod
    def get_one_post(id):
        selected_post = db.posts.find_one({"_id":id})
        return selected_post



    @staticmethod
    def patch_post(id: int, **kwargs: str):
        # Dado que será atualizado
        filter = {"_id":id}
        if not check_post_exist(id, list(db.posts.find())):
            raise PostNotExistError

        if check_update(kwargs['title'], kwargs['author'], kwargs['tags'], kwargs['content']):
            data = {
                    "$set": {'title': kwargs['title'], 'author': kwargs['author'], 'tags': kwargs['tags'], 'content': kwargs['content'], 'updated_at': datetime.now()}}
                    
            db.posts.update_one(filter, data)
            
            get_data = dict(db.posts.find_one({"_id": id}))

            return get_data
        raise InvalidDataUpdateError

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def create(self):
    #         id = db.posts.insert_one(self.__dict__).inserted_id
    #         # if not _id:
    #         #     raise InvalidPostError
    #         new_post = db.posts.find_one({'_id': id})
    #         del new_post['_id']
    #         return new_post











# reated_at, updated_at, title, author, tags, content, id: int = 1
#   self.created_at = created_at
#         self.updated_at = updated_at
#         self.title = title
#         self.author = author
#         self.tags = tags
#         self.content = content
#         self = id