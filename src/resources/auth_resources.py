from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from src.resources.blocklist import BLOCKLIST
from src.utils.mapped_roles import MappedRole
from src.schemas.user_schema import LoginSchema
from src.controllers.auth_controllers import AuthControllers

blp = Blueprint("authentication", __name__, description="Operations on authentication")

@blp.route("/login")
class UserLogin(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(LoginSchema)
    def post(self,user_data):
        obj = AuthControllers()
        role = obj.validate_user(user_data['username'],user_data['password'])
        if role:
            get_role = MappedRole.get_mapped_role(role)
            access_token = create_access_token(identity=user_data["username"],additional_claims={"role": get_role})
            return {"access_token": access_token}, 201
        else:
            abort(401, message="Invalid credentials")


@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200
