from app import db


class Project(db.Model):
    """
    SQL Alchemy data model for project
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    description = db.Column(db.String(500))
    is_live = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Project {}, {}, {}>'.format(self.name, self.description, "Y" if self.is_live else "N")

