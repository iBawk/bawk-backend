from enum import Enum


class ProductStatus(int, Enum):
    INATIVO = 0
    ATIVO = 1


class Theme(int, Enum):
    DARK = 0
    LIGHT = 1


class Panel(int, Enum):
    BUYER = 0
    SELLER = 1
