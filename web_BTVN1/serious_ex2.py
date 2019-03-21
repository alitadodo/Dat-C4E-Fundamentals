from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = [
        Dat : {
            "name": "Pham Tien Dat"
            "age": 25
            "hobbies": "game"
        },
        Hoang : {
            "name": "Pham Dinh Hoang"
            "age": 23
            "hobbies": "girls"
        }
    ]

    return render_template('serious_ex2.html',
                            users=users)

if __name__ == '__main__':
  app.run(debug=True)
 