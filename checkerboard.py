from flask import Flask, render_template
app = Flask(__name__)   
@app.route('/')
def eightBoxes():
    return render_template('checkerboard_page1.htm')
@app.route('/4')
def fourBoxes():
    return render_template('checkerboard_page2.htm')
@app.route('/<x>/<y>')
def randomBoxes(x, y):
    return render_template('checkerboard_page3.htm', timesx=int(x), timesy=int(y))
if __name__=="__main__":  
    app.run(debug=True)   
