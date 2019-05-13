# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

import os
from flask import redirect, render_template, render_template_string, Blueprint
from flask import request, url_for
from flask_user import current_user, login_required, roles_accepted
from app.init_app import app, db
from app.models import UserProfileForm

# The Home page is accessible to anyone
@app.route('/debug')
def debug_page():

    db_location = os.environ['SQLALCHEMY_DATABASE_URI']
    print ('db_location',db_location)

    if os.path.isfile(db_location):
        print ('YUP DB THERE')
        msg = 'OK' + db_location
    else:
        print ('ERROR DB NOT THERE')
        msg = 'OK' + db_location

    return msg
    #xx = os.getenv('MAIL_USERNAME')
    #yy = os.getenv('MAIL_PASSWORD')
    #print 'xx',xx



@app.route('/')
def home_page():
    return render_template('pages/home_page.html')


# These pages are  accessible to authenticated users (users that have logged in)
@app.route('/user')
#@login_required  # Limits access to authenticated users
def user_page():
    return render_template('pages/user_page.html' )

@app.route('/cv')
#@login_required  # Limits access to authenticated users
def cv_page():
    return render_template('pages/cv.html' )

@app.route('/data_gbpusd')
#@login_required  # Limits access to authenticated users
def data_gbpusd_page():
    return render_template('pages/data_gbpusd.html' )

@app.route('/todo')
#@login_required  # Limits access to authenticated users
def todo_page():
    return render_template('pages/todo.html' )

@app.route('/medareda_wiki')
#login_required  # Limits access to authenticated users
def mr_wiki():
    return render_template('pages/mr_wiki.html' )

@app.route('/mr_video')
#login_required  # Limits access to authenticated users
def mr_video_page():
    return render_template('pages/mr_video_page.html' )

@app.route('/medareda')
#login_required  # Limits access to authenticated users
def medareda_page():
    return render_template('pages/medareda_page.html' )

@app.route('/tech_used')
#login_required  # Limits access to authenticated users
def tech_used_page():
    return render_template('pages/tech_used_page.html' )

# The Admin page is accessible to users with the 'admin' role
@app.route('/admin')
@roles_accepted('admin')  # Limits access to users with the 'admin' role
def admin_page():

    db_location = os.environ['SQLALCHEMY_DATABASE_URI']
    print ('db_location',db_location)

    if os.path.isfile(db_location):
        print ('YUP DB THERE')
    else:
        print ('ERROR DB NOT THERE')

    users = db.session.query('id','email','confirmed_at','is_active').from_statement('SELECT id,email,confirmed_at,is_active from users')
    return render_template('pages/admin_page.html' , users = users , db_location = db_location )


@app.route('/pages/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    # Initialize form
    form = UserProfileForm(request.form, current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('home_page'))

    # Process GET or invalid POST
    return render_template('pages/user_profile_page.html',
                           form=form)
