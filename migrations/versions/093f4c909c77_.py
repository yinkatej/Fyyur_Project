"""empty message

Revision ID: 093f4c909c77
Revises: 13718e838d71
Create Date: 2022-08-03 16:46:32.112895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '093f4c909c77'
down_revision = '13718e838d71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('no_upcoming_shows', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'no_upcoming_shows')
    # ### end Alembic commands ###
