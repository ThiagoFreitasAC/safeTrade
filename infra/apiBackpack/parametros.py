"""
Módulo de Configuração de Parâmetros 
"""
from typing import Dict, Optional, Any, TypedDict

class OperationConfig(TypedDict):
    """Definição de tipo para configurações de operação."""
    instruction: str
    params: Optional[Dict[str, Any]]
    endpoint: str
    method: str

# 1. CONSULTAS DE CONTA (READ-ONLY)

OP_SALDO: OperationConfig = {
    "instruction": "balanceQuery",
    "params": None,
    "endpoint": "/api/v1/capital",
    "method": "GET"
}

OP_HISTORICO_FILLS: OperationConfig = {
    "instruction": "fillHistoryQueryAll",
    "params": {
        "limit": "100",
    },
    "endpoint": "/api/v1/fills",
    "method": "GET"
}

OP_HISTORICO_DEPOSITOS: OperationConfig = {
    "instruction": "depositQueryAll",
    "params": {
        "limit": "10"
    },
    "endpoint": "/api/v1/wlc/deposits", 
    "method": "GET"
}

OP_ORDENS_ABERTAS: OperationConfig = {
    "instruction": "orderQueryAll",
    "params": {
        "symbol": "SOL_USDC" 
    },
    "endpoint": "/api/v1/orders",
    "method": "GET"
}



# SELEÇÃO DA OPERAÇÃO ATUAL

# OP_ATUAL = OP_SALDO
OP_ATUAL = OP_HISTORICO_FILLS
# OP_ATUAL = OP_ORDENS_ABERTAS
# OP_ATUAL = OP_CRIAR_ORDEM_LIMIT

# EXPORTAÇÃO (Não alterar abaixo)

instruction: str = OP_ATUAL["instruction"]
params: Optional[Dict[str, Any]] = OP_ATUAL["params"]
endpoint: str = OP_ATUAL["endpoint"]
method: str = OP_ATUAL["method"]