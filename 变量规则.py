from flask import Flask

app = Flask(__name__)
# 这里使用from_pyfile，app使用from_object
app.config.from_pyfile('settings.py')
data = {'a': '北京', 'b': '上海', 'c': '深圳'}


@app.route('/')
def index():
    return '我是首页'


@app.route('/city/<string:key>')
def get_city(key):
    print(type(key))
    return data.get(key)


@app.route('/add/<int:num>')
def add_num(num):
    result = num + 10
    '''
    这里必须转成对应的格式。不然就报错
    The return type must be a string, dict, tuple, Response instance, or WSGI callable，
    '''
    return str(result)


@app.route('/add/<float:money>')
def add_money(money):
    result = money + 10
    return str(result)


@app.route('/index/<path:p>')
def get_path(p):
    print(p, 'p的类型是：{}'.format(type(p)))
    return p


@app.route('/index/<uuid:uid>')  # 这里必须传递uuid的格式，可以通过uuid模块里面的uuid4获取  uuid.uuid4()
def get_uuid(uid):
    print(uid, 'uid的类型是：{}'.format(type(uid)))
    return '获取唯一的标识码'


if __name__ == '__main__':
    app.run()
