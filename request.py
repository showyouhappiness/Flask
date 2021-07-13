from flask import Flask, request, make_response

import settings

app = Flask(__name__)
app.config.from_object(settings)


# 返回字典
@app.route('/index')
def index():
    print(request.headers)  # request对象，对象访问属性，也可以调用方法。
    return 'welcome everyone'


if __name__ == '__main__':
    app.run()
