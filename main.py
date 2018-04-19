
        #obj = Blog.query.order_by(Blog.id.desc()).first()
 #if request.method == 'POST':
  #      blog = str(request.args.get('id'))
   #     entry = Blog.query.get(blog)
    #    title = entry.title
     #   body = entry.body
      #  return render_template('/blog.html', title = title , body = body)
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1200))
       
    def __init__(self, title, body):
        self.title = title
        self.body = body
    
    def __repr__(self):
        return '<Blog %r>' % id



@app.route('/', methods=['POST', 'GET'])
def newpost():
    return render_template('/newpost.html')

@app.route('/blog', methods=['POST', 'GET'])
def blogs():
    if request.method == 'POST':
        title = request.form['text']
        blog_body = request.form['body']
        if len(blog_body) == 0 and len(title) == 0:
            title_error = "Please enter more than one character"
            body_error = "Please enter more than one character"
            return render_template('/newpost.html', body_error=body_error, title_error = title_error)
        if len(title) == 0:
            title_error = "Please enter more than one character"
            return render_template('/newpost.html', title_error = title_error)
        if len(blog_body) == 0:
            body_error = "Please enter more than one character"
            return render_template('/newpost.html', body_error=body_error)
        new_blog = Blog(title=title, body=blog_body)
        db.session.add(new_blog)
        db.session.commit()
        return render_template('/blog.html', title = title, body = blog_body)
    if request.args.get('id'):
        db.create_all()
        post = request.args.get('id')
        b_id = Blog.query.filter_by(id=post).first()
        title = b_id.title
        body = b_id.body
        return render_template('/blog.html', title = title, body = body)
    db.create_all()
    blogs = Blog.query.all()
    return render_template('/blogs.html', blogs=blogs)



if __name__ == '__main__':
    app.run()
    
    