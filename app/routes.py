from flask import render_template,redirect,url_for,request, flash
from app import app
from TopFive import GetBoroughList,TopFive
from app.forms import SelectBorough

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    borough_list = GetBoroughList()
    borough_list.sort()
    form = SelectBorough()
    form.borough.choices = borough_list
    if form.is_submitted():
        return redirect(url_for('show', borough=form.borough.data))
    return render_template('base.html', form=form, borough_list=borough_list)

@app.route('/show')
def show():
    borough = request.args.get('borough')
    top_trees = TopFive(borough)
    return render_template('show.html', borough=borough, top_trees=top_trees)