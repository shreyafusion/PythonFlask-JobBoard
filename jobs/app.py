from flask import Flask, render_template

app = (__name__)

@apps.route('/')
@apps.route('/jobs')
def jobs():
    return render_template('index.html') 

