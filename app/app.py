# app scripts

from flask import Flask, render_template, url_for, jsonify, request
from draws import LottoGame, LOTTODRAWS


app = Flask(__name__)

@app.route('/get_res')
def get_res():
    d = request.args.get('d', 0, type=str)
    l_draw = LottoGame(d)
    res = [str(n) for n in l_draw.generate_result()]
    return jsonify(results=res)

@app.route('/lottodraw/<chosen>')
def lottodraw(chosen):
    title = LOTTODRAWS[chosen]
    return render_template('lottodraws.html', title=title,
                            choices=LOTTODRAWS,
                            chosen=chosen,
                            digits=int(chosen.split('_')[0]))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Choose a draw',
                            choices=LOTTODRAWS)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    