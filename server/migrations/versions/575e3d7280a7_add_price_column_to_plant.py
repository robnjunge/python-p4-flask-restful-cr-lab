"""Add price column to Plant

Revision ID: 575e3d7280a7
Revises: 5866e4023569
Create Date: 2023-10-21 00:10:06.966735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '575e3d7280a7'
down_revision = '5866e4023569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('plants')
    op.drop_table('newsletters')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('newsletters',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('body', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plants',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('image', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('plant')
    # ### end Alembic commands ###
