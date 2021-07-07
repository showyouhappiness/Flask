from flask import Flask

app = Flask(__name__)
# 这里使用from_pyfile，app使用from_object
app.config.from_pyfile('settings.py')


@app.route('/projects/')  # 如果定义时加/，请求路由中不管有没有添加了/，都会显示正常页面，因为会Flask会自动进行重定向，在尾部加上一个斜杠
def projects():
    return 'The project page'


@app.route('/about')  # 如果定义时没有加/，而请求路由中如果添加了/，则会显示Net Found
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run()
