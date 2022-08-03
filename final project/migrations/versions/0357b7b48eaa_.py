"""empty message

Revision ID: 0357b7b48eaa
Revises: 22e14fd2d3c7
Create Date: 2022-07-26 18:24:52.487159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0357b7b48eaa'
down_revision = '22e14fd2d3c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('card', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'card', ['card'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'card')
    # ### end Alembic commands ###
