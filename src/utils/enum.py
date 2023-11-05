from enum import Enum


class Situation(int, Enum):
    ATIVO = 1
    INATIVO = 2
    
class PaymentMethod(int, Enum):
    PIX = 2
    CARTAO = 1