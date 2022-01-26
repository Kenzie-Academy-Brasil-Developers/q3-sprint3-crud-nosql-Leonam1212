from flask import jsonify, request
from http import HTTPStatus
from app.models.post_model import Post

# Funcção para pegar todos os posts
def get_posts():
    # Post.serializable()
    posts_list = Post.get_all_posts()
    return jsonify(list(posts_list)), HTTPStatus.OK

def create_posts():
    data = request.get_json()
    post = Post(**data)
   
    post.create_post()

    return jsonify(post.__dict__), HTTPStatus.CREATED

def delete_post(post_id):
    deleted_post = Post.deleted_post(post_id)
    return jsonify(deleted_post), HTTPStatus.OK

def get_one_post_return(post_id): 
    selected_post_by_id = Post.get_one_post(post_id)
    return jsonify(selected_post_by_id), HTTPStatus.OK

def patch_one_post(id):
    data = request.get_json()

    update_post = Post.patch_post(id, **data)
    

    return jsonify(update_post), HTTPStatus.OK