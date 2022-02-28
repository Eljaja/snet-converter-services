from datetime import date

from constants.entity import TokenEntities
from domain.entities.blockchain import Blockchain
from utils.general import datetime_to_str


class Token:
    def __init__(self, row_id: int, id: str, name: str, description: str, symbol: str, logo: str, allowed_decimal: int,
                 token_address: str, created_by: str, created_at: date, updated_at: date, blockchain_obj: Blockchain):
        self.row_id = row_id
        self.id = id
        self.name = name
        self.description = description
        self.symbol = symbol
        self.logo = logo
        self.allowed_decimal = int(allowed_decimal)
        self.token_address = token_address
        self.blockchain_obj = blockchain_obj
        self.created_by = created_by
        self.created_at = datetime_to_str(created_at)
        self.updated_at = datetime_to_str(updated_at)

    def to_dict(self):
        blockchain = {} if self.blockchain_obj is None else self.blockchain_obj.to_dict()
        return {
            TokenEntities.ROW_ID.value: self.row_id,
            TokenEntities.ID.value: self.id,
            TokenEntities.NAME.value: self.name,
            TokenEntities.DESCRIPTION.value: self.description,
            TokenEntities.SYMBOL.value: self.symbol,
            TokenEntities.LOGO.value: self.logo,
            TokenEntities.ALLOWED_DECIMAL.value: self.allowed_decimal,
            TokenEntities.TOKEN_ADDRESS.value: self.token_address,
            TokenEntities.CREATED_BY.value: self.created_by,
            TokenEntities.CREATED_AT.value: self.created_at,
            TokenEntities.UPDATED_AT.value: self.updated_at,
            TokenEntities.BLOCKCHAIN.value: blockchain
        }
