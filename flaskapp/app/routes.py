from flask import Flask, session, redirect, url_for, escape, request
import pymysql
import json

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    port=3306,
    db="flask",
    user="flask03",  # flask01
    password="flask03"  # flask01
)

cursor = db.cursor()


@app.route("/")
def index():
    print(session)
    return "Hello, world!"


@app.route("/auth/register", methods=["GET", "POST"])
def register():
    response = {
        'success': False,
        'error': ''
    }
    # https://comic.naver.com/webtoon/detail.nhn?titleId=570503&no=230&weekday=thu
    if request.method == 'GET':
        data = request.args
        # data = requests.form POST방식
        _email = data["email"]
        _pass = data["password"]
        _name = data["username"]

        SQL = "INSERT INTO `user`(`user_email`, `user_pass`, `user_name`, `created_at`) " \
              "VALUES('{email}', '{password}', '{username}', now())"

        cursor.execute(SQL.format(email=_email, password=_pass, username=_name))
        db.commit()

        #   127.0.0.1:5000/auth/register?email=kim@naver.com&password=123456&username=kim
        #   SELECT * FROM `user`;
        response['success'] = True
        return json.dumps(response)

    return json.dumps(response)


@app.route("/auth/login")
def login():
    response = {
        'success': False,
        'error': ''
    }

    # 127.0.0.1:5000/auth/login?email=kim@naver.com&password=123456
    if request.method == 'GET':
        data = request.args
        # data = requests.form
        _email = data["email"]
        _pass = data["password"]

        print(session)

        SQL = "SELECT * FROM `user` WHERE `user_email`='{email}' and `user_pass`='{password}'"
        cursor.execute(SQL.format(email=_email, password=_pass))
        fetch = cursor.fetchone()
        print(fetch)

        if fetch and _email == fetch[1] and _pass == fetch[2]:
            session["user_id"] = fetch[0]
            session["user_email"] = fetch[1]
            session["user_pass"] = fetch[2]
            session["user_name"] = fetch[3]

        print(session)

        response['success'] = True
        return json.dumps(response)

    return json.dumps(response)


@app.route("/auth/logout")
def logout():
    response = {
        'success': False,
        'error': ''
    }

    session.clear()
    print(session)

    response['success'] = True
    return json.dumps(response)


@app.route("/auth/changepass")
def changePass():
    response = {
        'success': False,
        'error': ''
    }

    if request.method == 'GET':
        data = request.args
        # data = requests.form
        _id = session["user_id"]
        _email = session["user_email"]
        _pass = session["user_pass"]

        _newPass = data["newpass"]

        SQL = "SELECT * FROM `user` WHERE `user_id`={id}"
        cursor.execute(SQL.format(id=_id))
        fetch = cursor.fetchone()
        print(fetch)

        if fetch and _email == fetch[1] and _pass == fetch[2]:
            SQL = "UPDATE `user` SET `user_pass`='{newPass}' WHERE `user_id`={id}"
            cursor.execute(SQL.format(newPass=_newPass, id=_id))
            db.commit()

        response['success'] = True
        return json.dumps(response)

    return json.dumps(response)


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('register'))
#     print(url_for('login'))
#     print(url_for('changePass'))

@app.route("/board/write")
def boardWrite():
    response = {
        'success': False,
        'error': ''
    }
    if isLogin():
        data = request.args
        # data = request.from
        _title = data['title']
        _description = data['description']
        _id = session["user_id"]

        SQL = "INSERT INTO `boards`(`board_title`, `board_description`, `writed_by`, `created_at`, `updated_at`) " \
              "VALUES('{title}', '{description}', '{user_id}', now(), now())"
        cursor.execute(SQL.format(title=_title, description=_description, user_id=_id))
        db.commit()

        response['success'] = True
        return json.dumps(response)

    return json.dumps(response)


@app.route("/board/delete/<board_id>")
def boardDelete(board_id):
    response = {
        'success': False,
        'error': ''
    }

    if isLogin():
        _id = session['user_id']

        SQL = "DELETE FROM `boards` WHERE board_id={board_id} and writed_by={user_id}"
        cursor.execute(SQL.format(board_id=board_id, user_id=_id))
        db.commit()

        response['success'] = True
        return json.dumps(response)

    return json.dumps(response)


@app.route("/board/update/<board_id>")
def boardUpdate(board_id):
    response = {
        'success': False,
        'error': ''
    }

    if isLogin():
        data = request.args
        # data = requests.form
        _id = session['user_id']
        _title = data['title']
        _description = data['description']

        SQL = "UPDATE `boards` SET board_title='{title}' , board_description='{description}' , updated_at=now() WHERE board_id={board_id} and writed_by={user_id}"
        cursor.execute(SQL.format(board_id=board_id, user_id=_id, title=_title, description=_description))
        db.commit()

        response['success'] = True
        return json.dumps(response)

    return json.dumps(response)


@app.route("/test")
def test():
    testData = {
        'firstAttribute': 1,
        'secondAttribute': 2
    }
    return json.dumps(testData)


@app.route("/board/list")
def getBoardList():
    response = {
        'success': False,
        'boards': [],
        'error': '',
    }
    # if isLogin():
    SQL = "SELECT board_title, board_description FROM `boards`"
    cursor.execute(SQL)
    response["boards"] = cursor.fetchall()
    response["success"] = True

    return json.dumps(response)

@app.route("/db/applist")
def getApplist():
    response = {
        'success': False,
        'applist': [],
        'error': '',
    }
    # if isLogin():
    SQL = "SELECT * FROM `applist` limit 10"
    cursor.execute(SQL)
    response["applist"] = cursor.fetchall()
    response["success"] = True

    return json.dumps(response)



@app.route("/board/get/<board_id>")
def getBoardDetail(board_id):
    response = {
        'success': False,
        'board': [],
        'error': '',
    }

    if isLogin():
        SQL = "SELECT board_title, board_description FROM `boards` WHERE board_id={board_id}"
        cursor.execute(SQL.format(board_id=board_id))
        response["board"] = cursor.fetchone()

        return json.dumps(response)

    return json.dumps(response)


def isLogin():
    try:
        _id = session["user_id"]
        _email = session["user_email"]
        _pass = session["user_pass"]

        SQL = "SELECT * FROM `user` WHERE `user_id`={id}"
        cursor.execute(SQL.format(id=_id))
        fetch = cursor.fetchone()
        print(fetch)

        if fetch and _email == fetch[1] and _pass == fetch[2]:
            return True
    except:
        return False

    return False


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.debug = True
    app.run()
