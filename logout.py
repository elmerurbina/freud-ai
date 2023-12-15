from flask import Flask, render_template, session

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/logout')
def logout():
    session.clear()
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)
