"""empty message

Revision ID: b26de28ce928
Revises: ee369a4d434b
Create Date: 2022-12-15 21:30:35.905534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b26de28ce928'
down_revision = 'ee369a4d434b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('context', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    # ### end Alembic commands ###
