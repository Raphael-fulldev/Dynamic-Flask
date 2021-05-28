from flask import render_template, flash, redirect, url_for, request, g, jsonify
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import MainSubscriptionForm, SubscriptionForm
from app.models import Subscription

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # form = SubscriptionForm(current_user.username)  # current user (original_user) to allow username change functionlity in forms.py
#     form = MainSubscriptionForm()
#     # form = SubscriptionForm()
#     list = 'asd'
#     if form.validate_on_submit():
#         pass
#     elif request.method == 'GET':
#         form.company.data = Subscription.query.all()
#         form.description.data = 'test2'
#         list = Subscription.query.all()
#         list='test'
#     return render_template('index.html', title="Home", form=form, list=list)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MainSubscriptionForm()
    if form.validate_on_submit():
        for x in form.subscription:
            sub = Subscription(company=x.data['company'], description=x.data['description'])
            db.session.add(sub)
            db.session.commit()
        return render_template('index.html', title="Home", form=form)
    elif request.method == 'GET':
        list = Subscription.query.all()
    return render_template('index.html', title="Home", form=form, list=list)