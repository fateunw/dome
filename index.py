from flask import Flask
from flask import render_template
from spider import getBdMsg
from flask import request

app = Flask(__name__)

# https://www.baidu.com/s?&wd=python

#装饰器，给函数新增功能
@app.route('/')
def index():
    return(render_template('index.html'))


@app.route('/s')
def s(): 
    keyword = request.args.get('wd')
    text = getBdMsg(keyword)
    return text


if __name__ == '__main__':
    app.run()