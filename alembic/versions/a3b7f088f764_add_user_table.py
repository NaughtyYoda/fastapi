"""add user table

Revision ID: a3b7f088f764
Revises: 122825611e4e
Create Date: 2023-04-07 13:32:54.764279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3b7f088f764'
down_revision = '122825611e4e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('user_email', sa.String(), nullable=False),
        sa.Column('user_password', sa.String(), nullable=False),
        sa.Column('user_created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False),
        sa.PrimaryKeyConstraint('user_id'),
        sa.UniqueConstraint('user_email')
    )


def downgrade():
    op.drop_table('users')
