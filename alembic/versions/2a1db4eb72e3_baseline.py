"""baseline

Revision ID: 2a1db4eb72e3
Revises: 
Create Date: 2022-01-12 08:28:16.056281

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2a1db4eb72e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blockchain',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('description', sa.TEXT(), nullable=False),
                    sa.Column('symbol', sa.VARCHAR(length=30), nullable=False),
                    sa.Column('logo', sa.VARCHAR(length=250), nullable=False),
                    sa.Column('chain_id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('block_confirmation', sa.INTEGER(), nullable=False),
                    sa.Column('is_extension_available', sa.BOOLEAN(), nullable=True),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('name', 'symbol'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('token',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('description', sa.TEXT(), nullable=False),
                    sa.Column('symbol', sa.VARCHAR(length=30), nullable=False),
                    sa.Column('logo', sa.VARCHAR(length=250), nullable=True),
                    sa.Column('blockchain_id', sa.BIGINT(), nullable=False),
                    sa.Column('allowed_decimal', sa.INTEGER(), nullable=True),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['blockchain_id'], ['blockchain.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('blockchain_id', 'symbol'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('conversion_fee',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('percentage_from_source', sa.DECIMAL(), nullable=True),
                    sa.Column('amount', sa.DECIMAL(), nullable=True),
                    sa.Column('token_id', sa.BIGINT(), nullable=True),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['token_id'], ['token.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('token_pair',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('from_token_id', sa.BIGINT(), nullable=False),
                    sa.Column('to_token_id', sa.BIGINT(), nullable=False),
                    sa.Column('conversion_fee_id', sa.BIGINT(), nullable=True),
                    sa.Column('is_enabled', sa.BOOLEAN(), nullable=True),
                    sa.Column('min_value', sa.DECIMAL(), nullable=True),
                    sa.Column('max_value', sa.DECIMAL(), nullable=True),
                    sa.Column('contract_address', sa.VARCHAR(length=250), nullable=False),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['conversion_fee_id'], ['conversion_fee.row_id'], ),
                    sa.ForeignKeyConstraint(['from_token_id'], ['token.row_id'], ),
                    sa.ForeignKeyConstraint(['to_token_id'], ['token.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('from_token_id', 'to_token_id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('wallet_pair',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('token_pair_id', sa.BIGINT(), nullable=False),
                    sa.Column('from_address', sa.VARCHAR(length=250), nullable=False),
                    sa.Column('to_address', sa.VARCHAR(length=250), nullable=False),
                    sa.Column('deposit_address', sa.VARCHAR(length=250), nullable=True),
                    sa.Column('signature', sa.VARCHAR(length=250), nullable=True),
                    sa.Column('signature_expiry', sa.TIMESTAMP(), nullable=False),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['token_pair_id'], ['token_pair.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('deposit_address'),
                    sa.UniqueConstraint('from_address', 'to_address'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('conversion',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('wallet_pair_id', sa.BIGINT(), nullable=False),
                    sa.Column('deposit_amount', sa.DECIMAL(), nullable=False),
                    sa.Column('claim_amount', sa.DECIMAL(), nullable=True),
                    sa.Column('fee_amount', sa.DECIMAL(), nullable=True),
                    sa.Column('status', sa.VARCHAR(length=30), nullable=False),
                    sa.Column('claim_signature', sa.VARCHAR(length=250), nullable=True),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['wallet_pair_id'], ['wallet_pair.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('conversion_transaction',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('conversion_id', sa.BIGINT(), nullable=False),
                    sa.Column('status', sa.VARCHAR(length=30), nullable=True),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['conversion_id'], ['conversion.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('transaction',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('conversion_transaction_id', sa.BIGINT(), nullable=False),
                    sa.Column('from_token_id', sa.BIGINT(), nullable=False),
                    sa.Column('to_token_id', sa.BIGINT(), nullable=False),
                    sa.Column('transaction_visibility', sa.VARCHAR(length=30), nullable=True),
                    sa.Column('transaction_operation', sa.VARCHAR(length=30), nullable=True),
                    sa.Column('transaction_hash', sa.VARCHAR(length=250), nullable=True),
                    sa.Column('transaction_amount', sa.DECIMAL(), nullable=True),
                    sa.Column('status', sa.VARCHAR(length=30), nullable=True),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['conversion_transaction_id'], ['conversion_transaction.row_id'], ),
                    sa.ForeignKeyConstraint(['from_token_id'], ['token.row_id'], ),
                    sa.ForeignKeyConstraint(['to_token_id'], ['token.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('conversion_transaction')
    op.drop_table('conversion')
    op.drop_table('wallet_pair')
    op.drop_table('token_pair')
    op.drop_table('conversion_fee')
    op.drop_table('token')
    op.drop_table('blockchain')
    # ### end Alembic commands ###
