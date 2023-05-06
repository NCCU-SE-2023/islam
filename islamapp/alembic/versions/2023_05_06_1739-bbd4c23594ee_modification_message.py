"""modification message

Revision ID: bbd4c23594ee
Revises: 594481f9bee9
Create Date: 2023-05-06 17:39:53.168639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbd4c23594ee'
down_revision = '594481f9bee9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('cookie', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'cookie')
    # ### end Alembic commands ###