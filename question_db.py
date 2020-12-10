from flask import render_template, request
import os

from dotenv import load_dotenv
from Models import Users, Topics, Questions


from app import app

load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY')




@app.route("/")
def home():
    return render_template('home.j2')


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.j2')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.j2')
    elif request.method == 'POST':
        details = dict(request.form)
        print(details)
        Users.create(username=details['username'],
                     password=details['password'],
                     email=details['email'],
                     institution=details['institution'])
        return render_template('about.j2')


@app.route("/read", methods=['GET', 'POST'])
def read():
    if request.method == 'GET':
        users = Users.select()
        return render_template('read.j2', users=users)


@app.route("/delete", methods=['GET'])
def delete():
    if request.method == 'GET':
        id = request.args.get('id')  #This gets the id from the "read" template "<td><a href="/delete?id={{ user.id }}">DELETE</a>"
        delRows = Users.delete().where(Users.id == id).execute()
        if delRows > 0:
            return render_template('delsuccess.j2')
        else:
            return render_template('delfailed.j2')


@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        id = request.args.get('id')  #This gets the id from the "read" template "<td><a href="/update?id={{ user.id }}">DELETE</a>"
        user = Users.select().where(Users.id == id).get()
        return render_template('update.j2', user=user)
    elif request.method == 'POST':
        details = dict(request.form)
        Users.update(username=details['username'],
                     password=details['password'],
                     email=details['email'],
                     institution=details['institution']).where(Users.id == details['id']).execute()
        return render_template('about.j2')


@app.route("/enter_question", methods=['GET', 'POST'])
def enter_question():
    if request.method == 'GET':
        return render_template('enter_question.j2')
    elif request.method == 'POST':
        details = dict(request.form)
        Questions.create(textbook=details['textbook'],
                         chapter=details['chapter'],
                         section=details['section'],
                         submitted_by=details['submitted_by'],
                         question_text=details['question_text'],
                         topic=details['topic'],)
        return render_template('about.j2')


@app.route("/topics", methods=['GET', 'POST'])
def enter_topic():
    if request.method == 'GET':
        topics = Topics.select()
        return render_template('topics.j2', topics=topics)
    elif request.method == 'POST':
        details = dict(request.form)
        print(details)
        Topics.create(topic=details['topic'])
    return render_template('home.j2')



if __name__ == '__main__':
    app.run()
