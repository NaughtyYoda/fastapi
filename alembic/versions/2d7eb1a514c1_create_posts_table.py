"""create posts table

Revision ID: 2d7eb1a514c1
Revises: 
Create Date: 2023-04-06 23:41:51.931184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d7eb1a514c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table('posts')
