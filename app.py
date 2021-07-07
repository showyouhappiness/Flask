from flask import Flask
import settings

app = Flask(__name__)
print(app.config)
app.config.from_object(settings)


# app.config.from_pyfile('settings.py') #使用pyfile,则不需要导入就可以使用，但是需要加上文件类型(.py)，同时使用字符串格式


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/test')
def hello_world_test():
    return 'Hello World test！!'


# 这个装饰器@app.route('/test')的底层其实就是通过使用的add_url_rule()这个函数将rule字符串跟视图函数进行绑定
app.add_url_rule('/test', view_func=hello_world_test)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # 端口号最好在启动之前设置，如果在之后设置重新启动也可以
