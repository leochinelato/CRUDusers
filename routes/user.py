from flask import Blueprint
from database.users import USERS

user_route = Blueprint('user', __name__)

"""
    show_users (GET)        -> Ver os usuários
    new_user   (POST)       -> Inserir os dados do novo usuário
    form_new_user (GET)     -> o formulário para criar um usuário novo
    form_edit_user (GET)    -> o formulário para editar um usuário já existente
    edit_user (POST)        -> atualizar o usuário com as informações da rota anterior
    delete_user (DELETE)    -> deletar o usuario
    update_user (PUT)       -> alterar os dados desse usuário

"""

@user_route.route('/')
def show_users():
    pass

@user_route.route('/', methods=['POST'])
def new_user():
    pass

@user_route.route('/new')
def form_new_user(user_id):
    pass

@user_route.route('/<int:user_id>/edit')
def form_edit_user(user_id):
    pass

@user_route.route('/<int:user_id>/update', methods=['PUT'])
def update_user(user_id):
    pass

@user_route.route('/<int:user_id>/delete', methods=['DELETE'])
def delete_user(user_id)