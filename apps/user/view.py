from flask import Blueprint, render_template, request, redirect

from apps.user.model import User

user_bp = Blueprint('user', __name__)

users = list()


@user_bp.route('/')
def user_center():
    return render_template('user/show.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取post提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg='用户名已存在')
            user = User(username, password, repassword)
            users.append(user)
            return redirect('/')

    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return '用户登录'


@user_bp.route('/del')
def del_user():
    username = request.args.get('username')
    for user in users:
        if user.username == username:
            users.remove(user)
            return redirect('/')
    else:
        return '删除失败'


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return '用户退出'
