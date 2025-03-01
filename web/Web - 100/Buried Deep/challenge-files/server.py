from flask import Flask, send_from_directory
from os import getenv

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

@app.route('/static/css/style.css')
def css():
    return send_from_directory('static/css', 'style.css')

@app.route('/hidden')
def flag_part1():
    return send_from_directory('hidden', 'flag1.txt')

@app.route('/secret')
def flag_part2():
    return send_from_directory('secret', 'flag2.txt')

@app.route('/cryptic')
def flag_part3():
    return send_from_directory('cryptic', 'flag3.txt')

@app.route('/forbidden')
def flag_part4():
    return send_from_directory('forbidden', 'flag4.txt')

@app.route('/buried')
def flag_part5():
    return send_from_directory('buried', 'flag5.txt')

@app.route('/pvt')
def fake_flag1():
    return send_from_directory('pvt', 'flag6.txt')

@app.route('/underground')
def fake_flag2():
    return send_from_directory('underground', 'flag7.txt')

@app.route('/secret_path')
def fake_flag3():
    return send_from_directory('secret_path', 'flag8.txt')

@app.route('/hidden_flag')
def fake_flag4():
    return send_from_directory('hidden_flag', 'flag9.txt')

@app.route('/buried_flag')
def fake_flag5():
    return send_from_directory('buried_flag', 'flag10.txt')

@app.route('/encrypted')
def fake_flag6():
    return send_from_directory('encrypted', 'flag11.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=getenv('PORT'))
