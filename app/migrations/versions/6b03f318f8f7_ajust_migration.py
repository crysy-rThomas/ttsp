"""ajust migration

Revision ID: 6b03f318f8f7
Revises: b2759c7f1ab0
Create Date: 2024-07-16 12:20:24.651918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import pgvector.sqlalchemy


# revision identifiers, used by Alembic.
revision: str = '6b03f318f8f7'
down_revision: Union[str, None] = 'b2759c7f1ab0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('documents_user_id_fkey', 'documents', type_='foreignkey')
    op.drop_column('documents', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False))
    op.create_foreign_key('documents_user_id_fkey', 'documents', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###