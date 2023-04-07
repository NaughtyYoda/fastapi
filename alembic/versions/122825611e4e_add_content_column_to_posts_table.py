"""add content column to posts table

Revision ID: 122825611e4e
Revises: 2d7eb1a514c1
Create Date: 2023-04-07 00:00:09.412348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122825611e4e'
down_revision = '2d7eb1a514c1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
