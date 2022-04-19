from flask import Flask, render_template, jsonify, request, session, redirect

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

@app.route('/jinyung')
def jinyung_page():
    return render_template('jinyung.html')

@app.route('/songhee')
def songhee_page():
    return render_template('songhee.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


