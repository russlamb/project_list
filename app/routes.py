import uuid

from flask import render_template, flash, redirect

from app import app
from app.my_code import get_project, get_projects_all, save_project, delete_project
from app.forms import ProjectForm, DeleteProjectForm

@app.route('/')
@app.route('/index')
def index():
    """
    Display the main webpage
    :return: Flask template
    """
    projects = get_projects_all()
    return render_template('index.html', title='Home', projects=projects)

@app.route('/project/<project_name>', methods=['GET','POST'])
def show_project(project_name):
    """
    Get project from database and display
    :return: Flask template
    """
    project = get_project(project_name)
    form = DeleteProjectForm()
    if form.validate_on_submit():
        flash('Project deleted {}'.format(project_name))
        delete_project(project_name)
        return redirect('/index')
    return render_template("show_project.html",title="Project Detail", project=project, form=form)

@app.route('/add',methods=['GET','POST'])
def project_form():
    """
    Display the add project form
    :return: Flask template
    """
    form = ProjectForm()
    if form.validate_on_submit():
        flash('Project submitted for {}, is_live={}'.format(form.name.data, form.is_live.data))
        save_project(form.name.data, form.description.data, form.is_live.data)
        return redirect('/index')
    return render_template("add_project.html",title="Add New", form=form)

