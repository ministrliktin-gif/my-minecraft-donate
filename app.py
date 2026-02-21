import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Проверяем, существует ли файл, чтобы не гадать
    if not os.path.exists('templates/index.html'):
        return "Ошибка: Файл templates/index.html не найден на сервере!"
    return render_template('index.html')

@app.route('/buy', methods=['POST'])
def buy():
    nickname = request.form.get('nickname')
    item = request.form.get('item')
    return f"<h3>Заказ принят, {nickname}!</h3><p>Товар: {item}</p>"

if __name__ == '__main__':
    # На Render порт задается автоматически через переменную окружения
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
