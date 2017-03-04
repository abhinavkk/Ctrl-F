import json
from flask import Flask, redirect, request, render_template, jsonify
from url_transcriber import searchKeyword

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search_keyword', methods=['POST'])
def searchKeyWord():
    """ Getting json time list for the keyword from the URL """
    
    url = request.form["url"]
    keyword = request.form["keyword"]

    result = searchKeyword(url, keyword)

    if not result:
        return jsonify(dict())

    return jsonify(timeStamp(result))


def timeStamp(list_time):
    """ Format timestamp """
    format_time = dict()
    i = 0
    for time in list_time:
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        if h==0:
            format_time[str(i)] = {"%02d:%02d" % (m, s): time}
        else:
            format_time[str(i)] = {"%d:%02d:%02d" % (h, m, s): time}
        i += 1
    return format_time


if __name__ == '__main__':
    app.run()
