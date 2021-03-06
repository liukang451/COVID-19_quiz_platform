"""Updated

Revision ID: eedbe13fb5c4
Revises: a02b9f53b9cb
Create Date: 2020-05-24 20:00:48.613855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eedbe13fb5c4'
down_revision = 'a02b9f53b9cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    # ### end Alembic commands ###
