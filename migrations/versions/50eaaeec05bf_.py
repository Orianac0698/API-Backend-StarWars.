"""empty message

Revision ID: 50eaaeec05bf
Revises: bcf7f7a15cdd
Create Date: 2024-05-03 00:12:01.020593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50eaaeec05bf'
down_revision = 'bcf7f7a15cdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('character_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('favorite_character_Id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorite_planet_Id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorite_user_Id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'character', ['character_id'], ['id'])
        batch_op.create_foreign_key(None, 'planet', ['planet_id'], ['id'])
        batch_op.drop_column('character_Id')
        batch_op.drop_column('user_Id')
        batch_op.drop_column('planet_Id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_Id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('user_Id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('character_Id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorite_user_Id_fkey', 'user', ['user_Id'], ['id'])
        batch_op.create_foreign_key('favorite_planet_Id_fkey', 'planet', ['planet_Id'], ['id'])
        batch_op.create_foreign_key('favorite_character_Id_fkey', 'character', ['character_Id'], ['id'])
        batch_op.drop_column('planet_id')
        batch_op.drop_column('character_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###