"""empty message

Revision ID: 1b2e32fbfe7c
Revises: 0357b7b48eaa
Create Date: 2022-07-26 18:37:34.728285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b2e32fbfe7c'
down_revision = '0357b7b48eaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'card', 'user', ['user'], ['id'])
    op.drop_constraint('user_card_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'card')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('card', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_card_fkey', 'user', 'card', ['card'], ['id'])
    op.drop_constraint(None, 'card', type_='foreignkey')
    op.drop_column('card', 'user')
    # ### end Alembic commands ###
