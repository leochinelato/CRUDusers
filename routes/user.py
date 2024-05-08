from flask import Blueprint, render_template, request, url_for, redirect
from database.models.user import User

user_route = Blueprint('user', __name__)


@user_route.route('/')
def show_users():
    """Users list"""
    users = User.select()
    return render_template('users_list.html', users=users)


@user_route.route('/new')
def form_new_user():
    return render_template('new_user.html')


@user_route.route('/create', methods=['POST'])
def new_user():
    data = request.json

    User.create(
        name=data['name'],
        email=data['email'],
        description=data['description'],
    )

    return redirect(url_for('user.show_users'))


@user_route.route('/edit/<int:user_id>')
def form_edit_user(user_id):
    user = User.get_by_id(user_id)
    return render_template('new_user.html', user=user)


@user_route.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json

    edited_user = User.get_by_id(user_id)
    edited_user.name = data['name']
    edited_user.email = data['email']
    edited_user.description = data['description']
    edited_user.save()

    return render_template('users_list.html', user=edited_user)


@user_route.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_by_id(user_id)
    user.delete_instance()

    return redirect(url_for('user.show_users'))
