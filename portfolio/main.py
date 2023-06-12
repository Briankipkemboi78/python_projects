from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = [
        {
            'title': 'Project 1',
            'description': 'This is a description of Project 1'
        },
        {
            'title': 'Project 2',
            'description': 'This is a description of Project 2'
        }
    ]
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
