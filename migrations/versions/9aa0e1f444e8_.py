"""empty message

Revision ID: 9aa0e1f444e8
Revises: 840daf4878a2
Create Date: 2019-02-06 15:51:00.609749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aa0e1f444e8'
down_revision = '840daf4878a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'customer', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.drop_column('customer', 'user_id')
    # ### end Alembic commands ###
