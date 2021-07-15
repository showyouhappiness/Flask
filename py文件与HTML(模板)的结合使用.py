import json

from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)

users = []


@app.route('/')
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
        address = request.args.get('address')
        print(username, address)  # 这时我们就可以将用户名和密码保存在数据库中

    else:
        # 这里是POST请求获取值的方法
        print(request.form)  # 字典类型
        username = request.form.get('username')
        address = request.form.get('address')
        print(username, address)  # 这时我们就可以将用户名和密码保存在数据库中
    user = {'username': username, 'address': address}
    users.append(user)
    print(users)
    return '提交成功'


@app.route('/show')
def show():
    return json.dumps(users)


print(app.url_map)  # 路由规则表；根据路由规则表找到匹配的函数，然后执行函数（render_template('register.html')）。

if __name__ == '__main__':
    app.run()
