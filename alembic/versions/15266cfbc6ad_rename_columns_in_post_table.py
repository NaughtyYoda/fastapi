"""rename columns in post table

Revision ID: 15266cfbc6ad
Revises: a3b7f088f764
Create Date: 2023-04-07 14:50:43.031025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15266cfbc6ad'
down_revision = 'a3b7f088f764'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='posts', column_name='id', new_column_name='post_id')
    op.alter_column(table_name='posts', column_name='title', new_column_name='post_title')
    op.alter_column(table_name='posts', column_name='content', new_column_name='post_content')


def downgrade():
    op.alter_column(table_name='posts', column_name='post_id', new_column_name='id')
    op.alter_column(table_name='posts', column_name='post_title', new_column_name='title')
    op.alter_column(table_name='posts', column_name='post_content', new_column_name='content')
