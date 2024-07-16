"""add document/splits

Revision ID: b2759c7f1ab0
Revises: 7832ccf8a722
Create Date: 2024-07-16 09:53:35.469260

"""
from typing import Sequence, Union
import pgvector.sqlalchemy
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2759c7f1ab0'
down_revision: Union[str, None] = '7832ccf8a722'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('documents',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('splits',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('topic', sa.String(), nullable=True),
    sa.Column('topic_vector', pgvector.sqlalchemy.Vector(dim=384), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('content_vector', pgvector.sqlalchemy.Vector(dim=384), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('document_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['document_id'], ['documents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('splits')
    op.drop_table('documents')
    # ### end Alembic commands ###