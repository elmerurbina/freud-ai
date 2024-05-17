from flask import Flask, render_template

app =Flask(__name__)

@app.route('/profesionalPlans')
def profesionalPlans ():

    return render_template('profesionalPlans.html')


if __name__ == '__main__':
    app.run(debug=True)