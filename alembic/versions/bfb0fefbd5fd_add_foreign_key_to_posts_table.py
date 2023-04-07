"""add foreign key to posts table

Revision ID: bfb0fefbd5fd
Revises: 15266cfbc6ad
Create Date: 2023-04-07 15:12:59.484770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfb0fefbd5fd'
down_revision = '15266cfbc6ad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['user_id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('posts_users_fk', 'posts')
    op.drop_column('posts', 'owner_id')
