"""rename address

Revision ID: e3cb860c12b1
Revises: 9bd10b7222ed
Create Date: 2025-05-11 17:41:17.966660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3cb860c12b1'
down_revision = '9bd10b7222ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
     op.alter_column('departments', 'address',  new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
     op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
