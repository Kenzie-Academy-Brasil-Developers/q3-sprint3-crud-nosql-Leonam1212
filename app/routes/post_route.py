from app.controllers import post_controller
from app.exceptions.create_post_invalid import InvalidPostError
from app.exceptions.post_exists import PostNotExistError
from app.exceptions.update_exception import InvalidDataUpdateError

def post_routes(app):
    @app.get("/posts")
    def read_posts():
        return post_controller.get_posts()
    
    @app.get("/posts/<int:id>")
    def read_post_by_id(id:int):
        return post_controller.get_one_post_return(id)
    
    @app.post("/posts")
    def create_post():
        try:
            return post_controller.create_posts()
        except InvalidDataUpdateError:
            return {"messege": "Verifique se todos os campos são do tipo String"}, 400

    @app.patch("/posts/<int:id>")
    def update_post(id:int):
        try:
            return post_controller.patch_one_post(id)
        except InvalidDataUpdateError:
            return {"messege": "Verifique se todos os campos são do tipo String"}, 400
        except PostNotExistError:
            return {"messege": f"Post com id {id} não encontrado"}, 404

    @app.delete("/posts/<int:id>")
    def delete_post(id:int):
        try:
            return post_controller.delete_post(id)
        except PostNotExistError:
            return {"messege": "Post não encontrado"}, 404