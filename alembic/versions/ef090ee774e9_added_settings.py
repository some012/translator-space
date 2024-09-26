"""Added settings

Revision ID: ef090ee774e9
Revises: f65663855b44
Create Date: 2024-09-26 16:25:22.784050

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'ef090ee774e9'
down_revision: Union[str, None] = 'f65663855b44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings',
                    sa.Column('sid', sa.Uuid(), nullable=False),
                    sa.Column('user_sid', sa.Uuid(), nullable=False),
                    sa.Column('activity', sa.Boolean(), nullable=False, comment='Active account or not'),
                    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
                    sa.Column('updated', sa.DateTime(timezone=True), nullable=False),
                    sa.ForeignKeyConstraint(['user_sid'], ['users.user.sid'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('sid', 'user_sid'),
                    sa.UniqueConstraint('sid'),
                    schema='users'
                    )
    op.create_unique_constraint(None, 'user', ['sid'], schema='users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("user_sid_key", 'user', schema='users', type_='unique')
    op.drop_table('settings', schema='users')
    # ### end Alembic commands ###
