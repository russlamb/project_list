"""projects table

Revision ID: 9c2266e421d6
Revises: 
Create Date: 2019-01-08 13:26:28.639618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c2266e421d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('is_live', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_name'), 'project', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_name'), table_name='project')
    op.drop_table('project')
    # ### end Alembic commands ###