"""User DB

Revision ID: 594481f9bee9
Revises: 
Create Date: 2023-04-16 18:02:39.960100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '594481f9bee9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.String(length=32), nullable=False),
    sa.Column('account', sa.String(length=320), nullable=False),
    sa.Column('password', sa.CHAR(length=60), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('account')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###