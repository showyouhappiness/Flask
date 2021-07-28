from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


# 使用add_template_filter
# @app.route('/')
# def hello_everyone():
#     msg = 'hi hello hi everyone'
#     list1 = [1, 3, 5, 9]
#     return render_template('自定义过滤器.html', msg=msg, list1=list1)


@app.route('/')
def hello_everyone():
    msg = 'hi hello hi everyone'
    list1 = [1, 3, 5, 9]
    return render_template('base.html', msg=msg, list1=list1)


def replace_hello(value):
    value = value.replace('hi', '')
    return value.strip()


app.add_template_filter(replace_hello, 'replace')


# 使用装饰器
@app.template_filter('list_reverse')
def list_reverse(li):
    temp_list = list(li)
    temp_list.reverse()
    return temp_list


if __name__ == '__main__':
    app.run()
