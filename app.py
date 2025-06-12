from flask import Flask,render_template,request,redirect
app=Flask(__name__ )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Team/')
def services():
    return render_template('about.html')
@app.route('/About/')
def About():
    return render_template('pets.html')

@app.route('/Pets')
def Pets():
    return render_template('pets.html')
if __name__ == '__main__':
    app.run(debug=True,port=8000)