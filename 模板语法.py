import app_study
from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


class Girl:
    def __init__(self, name, address):
        self.name = name
        self.gender = '女'
        self.address = address

    def __str__(self):
        return self.name


@app.route('/show')
def show():
    name = '张三'  # str
    age = 18  # int
    gender = '男'  # str
    friends = ['李四', '王麻子', '秀儿', '秀芹']  # list
    person = {'name': '狗子', 'age': '18', 'gender': '男', 'hobby': '打羽毛球'}  # dict
    """
    上面的类型都是系统给的
    现在我们要使用girl类型就要自己创建
    """
    # 创建对象
    girlfriend = Girl('你猜', '地球中国')
    return render_template('show.html', name=name, age=age, gender=gender, friends=friends, person=person,
                           girl=girlfriend)


if __name__ == '__main__':
    app.run()
