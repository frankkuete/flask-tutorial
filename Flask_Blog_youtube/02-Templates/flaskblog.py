from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Frank Kuete',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
{
        'author': 'Ann Nowe',
        'title': 'Blog Post 4',
        'content': 'Fourth post content',
        'date_posted': 'April 21, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='My fabulous Blog')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/example")
def example():
    return render_template('example.html', title='example')

if __name__ == '__main__':
    app.run(debug=True)
