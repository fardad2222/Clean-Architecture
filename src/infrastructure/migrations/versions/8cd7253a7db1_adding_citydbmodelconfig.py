"""Adding CityDBModelConfig

Revision ID: 8cd7253a7db1
Revises: 
Create Date: 2023-07-18 09:09:26.033473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cd7253a7db1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provinces',
    sa.Column('province_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('province_id')
    )
    op.create_table('cities',
    sa.Column('city_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('province_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['province_id'], ['provinces.province_id'], ),
    sa.PrimaryKeyConstraint('city_id'),
    sa.UniqueConstraint('city_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    op.drop_table('provinces')
    # ### end Alembic commands ###
