import json

from flask import Flask, request, render_template, redirect, url_for

import settings

app = Flask(__name__)
app.config.from_object(settings)

users = []


@app.route('/', endpoint='index')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    r = render_template('register.html')
    return r


@app.route('/submit_registration', methods=['GET', 'POST'])
def submit_registration():
    print(request.full_path)
    """
     /submit_registration?username=123&address=123这里必须和HTML页面里面的form表单相结合，
     如果from表单没有name属性，这里则是/submit_registration? 
     """
    print(request.path)  # /submit_registration
    print(request.method)
    # 这里是GET请求获取值的方法
    if request.method == 'GET':
        print(request.args)  # 字典类型
        username = request.args.get('username')
        password = request.args.get('password')
        repassword = request.args.get('repassword')
        print(username, password)  # 这时我们就可以将用户名和密码保存在数据库中

    else:
        # 这里是POST请求获取值的方法
        print(request.form)  # 字典类型
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        print(username, password)  # 这时我们就可以将用户名和密码保存在数据库中
    if password == repassword:
        user = {'username': username, 'password': password}
        users.append(user)
        print(users)
        return redirect(url_for('index'))
    else:
        return '两次密码不一致'


@app.route('/show')
def show():
    return json.dumps(users)


@app.route('/test')
def test():
    url = url_for('index')  # 路径反向解析 ，因为有时路径很长  我们可以设置一个小名 通过小名来获取路径
    print(url)  # 得到的路径
    return 'test'


print(app.url_map)  # 路由规则表；根据路由规则表找到匹配的函数，然后执行函数（render_template('register.html')）。

if __name__ == '__main__':
    app.run()
