from flask import Flask
app = Flask(name)


@app.route('/')
def hello_world():
    return 'У меня получилось!'


if name == 'main':
    app.run(debug=True, host='0.0.0.0')
