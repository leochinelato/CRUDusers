from flask import Blueprint, render_template, request, url_for, redirect
from database.users import USERS

user_route = Blueprint('user', __name__)

"""
    (x) show_users (GET)        -> Ver os usuários
    (x) new_user   (POST)       -> Inserir os dados do novo usuário
    (x) form_new_user (GET)     -> o formulário para criar um usuário novo
    () form_edit_user (GET)    -> o formulário para editar um usuário já existente
    () edit_user (POST)        -> atualizar o usuário com as informações da rota anterior
    (x) delete_user (DELETE)    -> deletar o usuario
    () update_user (PUT)       -> alterar os dados desse usuário

"""


@user_route.route('/')
def show_users():
    return render_template('users_list.html', users=USERS)


@user_route.route('/new')
def form_new_user():
    return render_template('new_user.html')


@user_route.route('/create', methods=['POST'])
def new_user():

    data = request.json

    new_user = {
        "id": len(USERS) + 1,
        "name": data['name'],
        "email": data['email'],
        "description": data['description'],
    }

    USERS.append(new_user)

    return redirect(url_for('user.show_users'))


@user_route.route('/edit/<int:user_id>')
def form_edit_user(user_id):
    user = None
    for u in USERS:
        if u['id'] == user_id:
            user = u
    return render_template('new_user.html', user=user)


@user_route.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    edited_user = None

    data = request.json

    for u in USERS:
        if u['id'] == user_id:
            u['name'] = data['name']
            u['email'] = data['email']
            u['description'] = data['description']

            edited_user = u

    return redirect(url_for('user.show_users'))


@user_route.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global USERS
    USERS = [u for u in USERS if u["id"] != user_id]

    return redirect(url_for('user.show_users'))
