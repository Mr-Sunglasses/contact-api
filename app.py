from my_app import app, db
from flask import render_template, session, redirect, url_for
from my_app.forms import Query_User
from my_app.models import Query_Model

@app.route('/', methods=['GET', 'POST'])
def home():
    form = Query_User()

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['message'] = form.message.data

        my_query = Query_Model(name=session['name'], email=session['email'], message=session['message'])
        db.session.add(my_query)
        db.session.commit()

        return redirect(url_for('thankyou'))

    return render_template('home.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/all_query')
def allquery():
    quries = Query_Model.query.all()
    return render_template('get_all.html', quries=quries)

if __name__ == '__main__':
    app.run(debug=True)