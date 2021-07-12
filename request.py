from flask import Flask, request, make_response

import settings

app = Flask(__name__)
app.config.from_object(settings)


# 返回字典
@app.route('/index')
def index():
    print(request.headers)
    return 'welcome everyone'


if __name__ == '__main__':
    app.run()
