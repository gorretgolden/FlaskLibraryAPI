"""initial migration

Revision ID: cea6110ff31f
Revises: 
Create Date: 2023-03-02 15:03:01.715353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cea6110ff31f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('contact', sa.String(length=200), nullable=True),
    sa.Column('user_type', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publishing_companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('contact', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('name')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('isbn', sa.String(length=50), nullable=True),
    sa.Column('publishing_date', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('price_unit', sa.String(length=10), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('publishing_company_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['publishing_company_id'], ['publishing_companies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('publishing_companies')
    op.drop_table('profiles')
    op.drop_table('users')
    # ### end Alembic commands ###
