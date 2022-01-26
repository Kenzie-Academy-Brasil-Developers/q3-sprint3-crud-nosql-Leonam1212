def check_creation_post(request):
    if request['title'] in request and request['author'] in request and request['tags'] in request and request['content'] in request:
        return True
    return False

def check_update(title, author, tags, content):
    if  type(title) == str and type(author) == str and type(tags) == str and type(content) == str:
            return True
    return False

def check_post_exist(post_id: int, list_bd):
    for posts in list_bd:
        if posts['_id'] == post_id:
            return True
    return False