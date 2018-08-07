from flask import Flask

app = Flask(__name__)


@app.route('/index/<user>', methods=['GET', 'POST', 'PUT', 'DELECT'])   #< >可以使用这个传参数， 使用method来指定方法
def hello_world(user):
    return 'Hello World!%s'%user


if __name__ == '__main__':
    app.run(host='0.0.0.0')
