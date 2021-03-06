"""table be

Revision ID: 61e1ebb9387a
Revises: 
Create Date: 2022-06-11 11:44:12.384614

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2

# revision identifiers, used by Alembic.
revision = '61e1ebb9387a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BE_PYTHON',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=230), nullable=False),
    sa.Column('geometry', geoalchemy2.types.Geometry(srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('BE_PYTHON')
    # ### end Alembic commands ###
