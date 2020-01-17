from flask import Flask,request

app = Flask(__name__)
# import requests

@app.route('/')
def hello_world():
    if(str(request.headers.get('User-Agent')).startswith('python-requests')):
        return "小子，使用爬虫是吧？滚你的"
    else:
        return "这里假装有很多数据"


if __name__ == "__main__":
    app.run(debug=True,port="5001")