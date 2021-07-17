from flask import Flask, Response, make_response

import settings

app = Flask(__name__)
app.config.from_object(settings)

"""
response响应：
    返回值的类型：
        1. str                  自动转成response对象
        2. dict                 json
        3. response对象  
        4. make_response()      response对象
        5. redirect()  重定向    302状态码
        6. render_template()    模板渲染 + 模板 
"""


# 返回字典
@app.route('/index')
def index():
    return {'a': '<h1>北京</h1>', 'b': '上海', 'c': '深圳'}  # 如果是字典，Content-Type默认为: application/json


# 返回字符串
@app.route('/index1')
def index1():
    return '<h1>深圳</h1>'  # 如果是字符串，Content-Type默认为: text/html; charset=utf-8


# 返回元组
@app.route('/index2')
def index2():
    s = '''
    <title>快去学习</title>
    <h1>别玩了，快去学习</h1>
    <P style='color:red;font-size: 28px;'>不学习，没饭吃</p>
    '''
    return s, 404  # 元组是前面这种形式传值的，不是一般的元组传值


# 返回Response
@app.route('/index3')
def index3():
    return Response('不学习就没饭吃！', content_type='text/html; charset=utf-8')  # 返回一个Response对象


@app.route('/index4')
def index4():
    content = '''
    <title>快去学习</title>
    <h1>别玩了，快去学习</h1>
    <P style='color:red;font-size: 28px;'>不然没饭吃</p>
    '''
    response = make_response(content)
    response.headers['mytest'] = '123abc'
    response.headers['mytask'] = 'hello'
    return response


if __name__ == '__main__':
    app.run()
