"""empty message

Revision ID: 508af33f47e0
Revises: 7558371103f6
Create Date: 2023-05-10 15:42:09.093779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '508af33f47e0'
down_revision = '7558371103f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
