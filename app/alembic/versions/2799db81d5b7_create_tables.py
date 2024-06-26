"""Create tables

Revision ID: 2799db81d5b7
Revises: 
Create Date: 2024-03-02 00:00:55.428541

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2799db81d5b7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coin_data',
    sa.Column('coin', sa.String(length=255), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('json', sa.JSON(none_as_null=255), nullable=False),
    sa.PrimaryKeyConstraint('coin', 'date'),
    schema='public'
    )
    op.create_table('coin_month_data',
    sa.Column('coin', sa.String(), nullable=False),
    sa.Column('year', sa.Date(), nullable=False),
    sa.Column('month', sa.Date(), nullable=False),
    sa.Column('min_price', sa.Float(), nullable=True),
    sa.Column('max_price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('coin', 'year', 'month'),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coin_month_data', schema='public')
    op.drop_table('coin_data', schema='public')
    # ### end Alembic commands ###
