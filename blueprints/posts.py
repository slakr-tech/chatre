from flask import Blueprint, render_template, session, redirect, url_for, request, flash
import sys
sys.path.append("..")
import database as db
from auth import auth
from user import User

posts = Blueprint("posts", __name__, static_folder='static', template_folder='templates')

@posts.route('/create')
def create_post():
    auth_status = auth()
    post = request.args.get('p')
    print('auth status 1:', auth_status[1].id)
    for i in auth_status:
        print(auth_status)
    if post and auth_status[0]:
        db.add_post(post, auth_status[1].id)
        flash('post created')

    elif not post:
        flash('You must write something for your post')

    elif not auth_status[0]:
        flash('You must be signed in to create a post, make sure you have cookies enabled')

    return redirect(url_for('index'))

@posts.route('/remove')
def delete_post():
    auth_status = auth()
    post_id = request.args.get('p')

    if post_id:
        db.remove_post(auth_status[1].id, post_id)
        flash('post removed')

    elif not post_id:
        flash('Could not delete post')

    elif not auth_status[0]:
        flash('You must be signed in to delete a post, make sure you have cookies enabled')

    return redirect(url_for('index'))