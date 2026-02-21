from flask import Flask, render_template, request

app = Flask(__name__)

# Эта команда показывает главную страницу (твой красивый дизайн)
@app.route('/')
def home():
    return render_template('index.html')

# Эта команда срабатывает, когда игрок нажимает "Оплатить"
@app.route('/buy', methods=['POST'])
def buy():
    nickname = request.form.get('nickname')
    item = request.form.get('item')
    
    # В будущем здесь будет код для оплаты (Qiwi, YooKassa)
    # И код для выдачи доната на сервер через RCON
    
    return f"<h3>Спасибо за заказ, {nickname}!</h3><p>Ты выбрал: {item}. (Тут позже прикрутим настоящую кассу)</p>"

if __name__ == '__main__':
    app.run(debug=True)
