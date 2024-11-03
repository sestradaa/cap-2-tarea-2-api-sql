import sqlite3
import os
from flask import Flask, render_template, abort, request, url_for, redirect, send_from_directory
from db import get_db_connection


app = Flask(__name__)

@app.route('/favicon3.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon3.ico')

@app.route('/', methods=['GET'])
def index():
        return render_template('base.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/post', methods=['GET'])
def get_all_post():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
   
    return render_template(template_name_or_list="post/posts.html", posts=posts)


@app.route('/post/<int:post_id>', methods=['GET'])
def get_one_post(post_id):
    if request.method == "GET":
        conn = get_db_connection()
        post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
        conn.close()
    return render_template('post/post.html', post=post)

@app.route('/post/create', methods=["GET", "POST"])
def create_one_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        mensaje = ""
        if (title.strip() == ""):
            return render_template("post/create.html", mensaje = "Ingrese título")
        elif  (content.strip() == ""):
            return render_template("post/create.html", mensaje = "Ingrese Contenido")
        else:   
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for("get_all_post"))
    elif request.method == "GET":
       return render_template("post/create.html")


@app.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_one_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    #if post: si encontro el registro
    conn.close()
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        mensaje = ""
        if (title.strip() == ""):
            context = {'post_error':post_id, 'newTitle' : title, 'newContent' : content, "mensaje": "Ingrese título"}
            return render_template(template_name_or_list="post/edit.html", **context)
            #return render_template("post/edit.html", mensaje = "Ingrese título")
        elif  (content.strip() == ""):
            context = {'post_error':post_id, 'newTitle' : title, 'newContent' : content, "mensaje": "Ingrese Contenido"}
            return render_template(template_name_or_list="post/edit.html", **context)
            #return render_template("post/edit.html", **context)
        else: 
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
            conn.commit()
            conn.close()
            return redirect(url_for('get_all_post'))
    elif request.method == 'GET':
        return render_template(template_name_or_list="post/edit.html", post=post)


@app.route('/post/delete/<int:post_id>', methods=['POST'])
def delete_one_post(post_id):
    conn = get_db_connection()

    if request.method == "POST":
        conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
        conn.commit()
        conn.close()

    return redirect(url_for('get_all_post'))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
    #app.run(debug=True, port=3000, host='0.0.0.0')
    
########################################################################## END BLOQUE 2