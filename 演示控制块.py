from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/show')
def show():
    numbers = ['11', '22', '33', '444', '555', '666']
    return render_template('演示控制块.html', numbers=numbers)


if __name__ == '__main__':
    app.run()
