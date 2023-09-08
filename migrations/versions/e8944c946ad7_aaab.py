"""aaab

Revision ID: e8944c946ad7
Revises: 
Create Date: 2023-09-08 20:20:56.458840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8944c946ad7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usersAddress',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('zipCode', sa.String(), nullable=True),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('complement', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usersIdentifications',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nacionality', sa.String(), nullable=True),
    sa.Column('document', sa.String(), nullable=True),
    sa.Column('birthDate', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('photo', sa.LargeBinary(), nullable=True),
    sa.Column('isUpdated', sa.Boolean(), nullable=True),
    sa.Column('emailVerified', sa.Boolean(), nullable=True),
    sa.Column('address_id', sa.String(), nullable=True),
    sa.Column('identification_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['usersAddress.id'], ),
    sa.ForeignKeyConstraint(['identification_id'], ['usersIdentifications.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('usersIdentifications')
    op.drop_table('usersAddress')
    # ### end Alembic commands ###
