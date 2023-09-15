# todo: criar um enum para os status dos produtos

from enum import Enum


class ProductStatus(int, Enum):
    INATIVO = 0
    ATIVO = 1
