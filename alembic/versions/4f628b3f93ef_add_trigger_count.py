"""add_trigger_count

Revision ID: 4f628b3f93ef
Revises: b666d1766c3a
Create Date: 2022-04-05 14:51:54.358728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f628b3f93ef'
down_revision = 'b666d1766c3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message_group_pool', sa.Column('trigger_count', sa.BIGINT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message_group_pool', 'trigger_count')
    # ### end Alembic commands ###
