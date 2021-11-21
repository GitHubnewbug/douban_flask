from flask import Flask,render_template
import sqlite3
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/index')
def index():
    # return render_template("index.html")
    return home()


@app.route('/movie')
def moive():
    datalist=[]
    # pic=[]
    conn=sqlite3.connect("movies.db")
    cur=conn.cursor()
    sql="select * from movie250"
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()

    return render_template('movie.html',movies=datalist)


@app.route('/score')
def score():
    score=[]        #评分
    count=[]        #评分电影数量
    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        count.append(item[1])
    cur.close()
    conn.close()
    return render_template('score.html',score=score,count=count)


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/word')
def word():
    return render_template('word.html')

if __name__ == '__main__':
    app.run()
