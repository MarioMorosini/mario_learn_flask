"""empty message

Revision ID: 83d637a917ab
Revises: 90435ac7a3c3
Create Date: 2018-10-01 17:05:23.953239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83d637a917ab'
down_revision = '90435ac7a3c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
