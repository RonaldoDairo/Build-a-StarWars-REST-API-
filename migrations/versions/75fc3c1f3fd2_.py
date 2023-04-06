"""empty message

Revision ID: 75fc3c1f3fd2
Revises: 104bc4bf7b06
Create Date: 2023-04-01 18:11:42.341793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75fc3c1f3fd2'
down_revision = '104bc4bf7b06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username_person', sa.String(length=40), nullable=False),
    sa.Column('history_person', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username_person')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=150), nullable=False))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    op.drop_table('people')
    # ### end Alembic commands ###