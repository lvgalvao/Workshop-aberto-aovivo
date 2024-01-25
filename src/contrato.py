from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"

class Vendas(BaseModel):

    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        produto (str): nome do produto
        quantidade (PositiveInt): quantidade de produtos
        categoria (str): categoria do produto

    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: str
    categoria: CategoriaEnum

    @field_validator('categoria')
    def categoria_deve_estar_no_enum(cls, error):
        return error