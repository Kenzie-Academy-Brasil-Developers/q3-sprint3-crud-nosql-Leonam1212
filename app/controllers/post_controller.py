from flask import jsonify, request
from http import HTTPStatus
from app.models.post_model import Post

# Funcção para pegar todos os posts
def get_posts():
    # Post.serializable()
    posts_list = Post.get_all_posts()
    print(list(posts_list))
    
    return jsonify(list(posts_list)), HTTPStatus.OK

def create_posts():
    data = request.get_json()
    if 'title' in data and 'author' in data and 'tags' in data and 'content' in data:
        post = Post(**data)
        post.create_post()
        return jsonify(post.__dict__), HTTPStatus.CREATED
    return {"messege": "Verifique se as chaves necessárias foram preenchidas"}, HTTPStatus.BAD_REQUEST

def delete_post(post_id):
    deleted_post = Post.deleted_post(post_id)
    return jsonify(deleted_post), HTTPStatus.OK

def get_one_post_return(id): 
    posts_list = Post.get_all_posts()
    for post in list(posts_list):
        if post['_id'] == id:
            selected_post_by_id = Post.get_one_post(id)
            return jsonify(selected_post_by_id), HTTPStatus.OK
    return {"messege": f' O id {id} não existe no banco de dados'}, 404

def patch_one_post(id):
    data = request.get_json()

    if 'title' in data and 'author' in data and 'tags' in data and 'content' in data:
        update_post = Post.patch_post(id, **data)
        return jsonify(update_post), HTTPStatus.OK

    print(data)
    return {"messege": "verifique se as chaves necessárias foram preenchidas"}, HTTPStatus.BAD_REQUEST
    
