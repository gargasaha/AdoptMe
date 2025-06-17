from flask import Flask,render_template,request,redirect
import mysql.connector
app=Flask(__name__ )


def dbConnect():
    host = 'localhost'
    user = 'root'
    password = '9932'
    database = 'Travarsa'

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )    
        return connection
    except Exception:
        print("error")

@app.route('/')
def index():
    dbConnect()
    return render_template('index.html')

@app.route('/Team/')
def services():
    return render_template('about.html#team')
@app.route('/About/')
def About():
    return render_template('about.html')

@app.route('/Pets')
def Pets():
    return render_template('pets.html')


@app.route('/Contact',methods=['POST'])
def Contact():
    if request.method=="POST":
        print(request.form['name'], request.form['email'], request.form['message'])
        conn=dbConnect()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)", 
                       (request.form['name'], request.form['email'], request.form['message']))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/')
    
@app.route('/view')
def getData():
    conn=dbConnect()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contact",)
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view.html',data=data)

@app.route('/delete/<int:id>')
def deleteData(id):
    conn=dbConnect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM contact WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/view')

@app.route('/update/<int:id>', methods=['GET'])
def updateData(id):
    conn=dbConnect()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contact",)
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view.html',message=id,data=data)

@app.route('/actualUpdate', methods=['POST'])
def actualUpdate():
    id = request.form.get('id')
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(name, email, message,id)

    conn = dbConnect()
    cursor = conn.cursor()
    cursor.execute("UPDATE contact SET name = %s, email = %s, message = %s WHERE id = %s", 
                   (name, email, message, id))
    conn.commit()
    cursor.close()
    conn.close()    

    return redirect('/view')
if __name__ == '__main__':
    app.run(debug=True,port=8000)