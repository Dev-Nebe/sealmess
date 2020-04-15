"""empty message

Revision ID: c2dd9410a475
Revises: f42a9735d245
Create Date: 2020-04-14 20:20:23.977954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2dd9410a475'
down_revision = 'f42a9735d245'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('providers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('providers')
    # ### end Alembic commands ###
