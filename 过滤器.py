from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    msg = '<h1>hello world</h1>'
    n1 = 'hello world'
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    json = [{'a': 1}, {'b': 2}, {'c': 3}]
    list1 = [2, 5, 3, 8]
    return render_template('过滤器.html', msg=msg, n1=n1, dict=dict1, json=json, list=list1)
    # return render_template('演示控制块.html', numbers=numbers)


if __name__ == '__main__':
    app.run()
