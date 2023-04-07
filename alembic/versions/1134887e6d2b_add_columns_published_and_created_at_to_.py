"""add columns published and created at to post table

Revision ID: 1134887e6d2b
Revises: bfb0fefbd5fd
Create Date: 2023-04-07 15:31:28.446898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1134887e6d2b'
down_revision = 'bfb0fefbd5fd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('post_published', sa.Boolean(), nullable=True, server_default='TRUE'))
    op.add_column(
        'posts',
        sa.Column('post_created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))
    )


def downgrade():
    op.drop_column('posts', 'post_published')
    op.drop_column('posts', 'post_created_at')