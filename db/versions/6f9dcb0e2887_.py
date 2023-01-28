"""empty message

Revision ID: 6f9dcb0e2887
Revises: 9565125ee169
Create Date: 2023-01-27 22:31:16.031260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f9dcb0e2887'
down_revision = '9565125ee169'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone_number',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('votes', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('votes', 'created_at')
    op.alter_column('users', 'phone_number',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###