from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def news():
    the_news = {
        'XXX1': '1',
        'XXX2': '2',
        'XXX3': '3',
        'XXX4': '4',
    }
    context = {
        'title': '新闻',
        'the_news': the_news,
    }
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
#test1