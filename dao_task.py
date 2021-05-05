import config_db
import model_users
#from main_flask import db


# def load_DB():
#     flaskDB = config_db.getDB()
#     return flaskDB


def create_task(task):


    flask_db = load_DB()
    mycursor = flask_db.cursor()

    sql_query = "INSERT INTO todo (user_id, from_date, task) VALUES (%s,%s,%s)"
    values = (task.user_id, task.from_date, task.task)
    mycursor.execute(sql_query, values)

    flask_db.commit()
    mycursor.close()
    flask_db.close()

    return 'New task included!'


def delete_task(task):
    flask_db = load_DB()
    mycursor = flask_db.cursor()


    sql_query = "DELETE FROM todo WHERE (user_id, from_date, task) VALUES (%s,%s,%s)"
    values = (task.user_id, task.from_date, task.task)
    mycursor.execute(sql_query, values)

    flask_db.commit()
    mycursor.close()
    flask_db.close()

    return 'New task included!'
