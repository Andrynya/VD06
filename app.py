from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        имя = request.form.get('name')
        город = request.form.get('city')
        хобби = request.form.get('hobby')
        возраст = request.form.get('age')
        user_data = {
            'name': имя,
            'city': город,
            'hobby': хобби,
            'age': возраст
        }
    return render_template('index.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)