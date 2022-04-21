<<<<<<< .merge_file_a17100
from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

=======
from flask import Flask, render_template
import crawling
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
>>>>>>> .merge_file_a18140

app = Flask(__name__)

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
<<<<<<< Updated upstream
    result=crawling.result
    return render_template('songhee.html', result=result)
=======
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
>>>>>>> Stashed changes

@app.route('/dongwoo/game', methods=['GET'])
def game_info():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://loawa.com/char/%EB%B0%94%EB%9E%8C%EC%9D%98%EB%82%98%EB%9D%BC%EC%97%90%EC%84%9C%EC%98%A8%EB%AA%A8%ED%97%98%EA%B0%80', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    char_id = soup.select_one('#char-app > div > div.char-title-bar.mt-2 > h2')
    print(char_id)

    char = {
        'id': char_id
    }

    return jsonify({'char': char,  'msg': '연결 완료'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


