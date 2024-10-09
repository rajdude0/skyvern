"""Add bitwarden details to organizations

Revision ID: 6c90d565076b
Revises: c5848cc524b1
Create Date: 2024-10-02 22:12:34.959165+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6c90d565076b"
down_revision: Union[str, None] = "c5848cc524b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("organizations", sa.Column("bw_organization_id", sa.String(), nullable=True))
    op.add_column("organizations", sa.Column("bw_collection_ids", sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("organizations", "bw_collection_ids")
    op.drop_column("organizations", "bw_organization_id")
    # ### end Alembic commands ###