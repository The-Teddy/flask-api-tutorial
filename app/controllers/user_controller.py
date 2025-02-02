from flask import Blueprint, request, jsonify, make_response

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route('/', methods=['POST'])
def create():

    data = request.get_json()

    print("dados da requisição: ", data)

    return make_response("usuário criado com sucesso"), 201

@user_bp.route('/', methods=['GET'])
def index():

    users = [{"name": "Marcio", "age": 25},{"name": "Jaqueline", "age": 24}]

    return jsonify({"users": users}), 200

@user_bp.route('/<id>', methods=['PUT'])
def update(id):

    data = request.get_json()

    print("id do usuário a ser atualizado: ", id)
    print("dados para atualizar: ", data)

    return make_response("usuário atualizado com sucesso"), 200

@user_bp.route('/<id>', methods=['DELETE'])
def delete(id):

    print('id do usuário a ser deletado: ', id)

    return make_response("usuário deletado com sucesso"), 200

