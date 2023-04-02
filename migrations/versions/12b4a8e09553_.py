"""empty message

Revision ID: 12b4a8e09553
Revises: c75cdf783881
Create Date: 2023-04-02 17:38:28.928219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12b4a8e09553'
down_revision = 'c75cdf783881'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('history', sa.String(length=250), nullable=False),
    sa.Column('tipes', sa.String(length=250), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
