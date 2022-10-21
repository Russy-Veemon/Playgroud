from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def playground1():
    return render_template("playground.html", times=3, color="rgb(118, 189, 255)")	

@app.route('/play/<int:times>')
def playground2(times):
    return render_template("playground.html", times=times, color="rgb(118, 189, 255)")	

@app.route('/play/<int:times>/<string:color>')
def playground3(times, color):
    return render_template("playground.html", times=times, color=color)	

if __name__=="__main__":
    app.run(debug=True)