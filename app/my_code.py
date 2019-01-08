from app.models import  Project
from app import db

def save_project(name, description, is_live):
    project = Project(name=name, description=description, is_live=is_live)

    if project:
        db.session.add(project)
        db.session.commit()

def delete_project(name):
    project = Project.query.filter_by(name=name).first()
    if project:
        db.session.delete(project)
        db.session.commit()

def get_project(name):
    project = Project.query.filter_by(name=name).first()
    return project

def get_projects_all():
    return Project.query.all()