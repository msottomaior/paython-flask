import config_db
import model_users



def load_DB():
    flaskDB = config_db.getDB()
    return flaskDB

# Check user and return user as object from model
def check_pw(username, password):
    flask_db = load_DB()
    mycursor = flask_db.cursor()
    sql_query = "SELECT * FROM users WHERE email =%s AND pass =%s"
    user_info = (username, password)

    mycursor.execute(sql_query, user_info)
    db_user = mycursor.fetchone()
    if db_user is not None:
        user = model_users.Users(db_user[0], db_user[1], db_user[2], db_user[3],
                             db_user[4])
    else:
        user = None
    
    return user

# Sign up
def create_user(user):
    flask_db = load_DB()
    mycursor = flask_db.cursor()
    sql_query = "SELECT pass FROM users WHERE email = %s"
    user_info = (user.email,)

    mycursor.execute(sql_query, user_info)
    db_user = mycursor.fetchone()

    if db_user is None:
        sql_query = "INSERT INTO users (email, pass, name, address) VALUES (%s,%s,%s,%s)"
        values = (user.email, user.password, user.name, user.address)
        mycursor.execute(sql_query, values)

        flask_db.commit()
        mycursor.close()
        flask_db.close()
    else:
        return ('User already existed!!!')

    return ('You have successfully signed up, now you can log in!!!')
