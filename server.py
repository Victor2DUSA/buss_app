from flask import Flask, render_template_string
from main import MyApp

app = Flask(__name__)

@app.route('/')
def index():
    template = '''
            <!doctype html>
            <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>My Kivy App</title>
            </head>
            <body>
                {{kivy}}
            </body>
            </html>
            '''
    return render_template_string(template, kivy=MyApp().root.to_widget())

if __name__ == '__main__':
    app.run()
