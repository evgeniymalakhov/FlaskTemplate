"""empty message

Revision ID: cdaca37b37bb
Revises: f2ceb2b60b67
Create Date: 2019-11-17 04:59:56.706041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdaca37b37bb'
down_revision = 'f2ceb2b60b67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
