from flask import Flask, render_template, jsonify, request
import crawling
from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.db9jo


app = Flask(__name__)
exec("crawling")
# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dongwoo')
def dongwoo_page():
    return render_template('dongwoo.html')

@app.route('/heejeong')
def heejeong_page():
    return render_template('heejeong.html')

@app.route('/jinyoung')
def jinyung_page():
    return render_template('jinyoung.html')

@app.route('/songhee')
def songhee_page():
    crawling_result=crawling.game15_result
    return render_template('songhee.html',
                           game1=crawling_result[0], game2=crawling_result[1],
                           game3=crawling_result[2], game4=crawling_result[3],
                           game5=crawling_result[4], game6=crawling_result[5],
                           game7=crawling_result[6], game8=crawling_result[7],
                           game9=crawling_result[8], game10=crawling_result[9],
                           game11=crawling_result[10], game12=crawling_result[11],
                           game13=crawling_result[12], game14=crawling_result[13],
                           game15=crawling_result[14]
                           )

@app.route('/dongwoo/comment')
def comment_listing():
    member = request.args.get('id')
    comments = list(db.comments.find({'member': member}, {'_id': False}))

    msg = 'comment_listing is called'
    return jsonify({'comments': comments, 'msg': msg})

@app.route('/dongwoo/comment', methods=['POST'])
def comment_save():
    name = request.form['name_give']
    comment = request.form['comment_give']
    member = request.form['member_give']

    comment_info = {
        'name': name,
        'member': member,
        'comment': comment
    }

    db.comments.insert_one(comment_info)

    msg = 'comment_save is called'
    return jsonify({'msg': msg})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
