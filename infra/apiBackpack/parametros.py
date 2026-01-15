"""
Módulo de Configuração de Parâmetros (Laboratório Manual)

Este arquivo define os parâmetros para execução manual de operações na API.
Siga o PADRÃO DE DESENVOLVIMENTO para adicionar novas operações.

Como usar:
1. Defina/Verifique os dicionários de operação abaixo.
2. Atribua à variável `OP_ATUAL` a operação que deseja executar.
3. Rode `python scripts/executar_manual.py`.
"""
from typing import Dict, Optional, Any, TypedDict

class OperationConfig(TypedDict):
    """Definição de tipo para configurações de operação."""
    instruction: str
    params: Optional[Dict[str, Any]]
    endpoint: str
    method: str

# ==============================================================================
# 1. CONSULTAS DE CONTA (READ-ONLY)
# ==============================================================================

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
        # "symbol": "SOL_USDC" # Opcional: filtrar por par
    },
    "endpoint": "/api/v1/fills",
    "method": "GET"
}

OP_HISTORICO_DEPOSITOS: OperationConfig = {
    "instruction": "depositQueryAll",
    "params": {
        "limit": "10"
    },
    "endpoint": "/api/v1/wlc/deposits", # Endpoint correto segundo docs
    "method": "GET"
}

OP_ORDENS_ABERTAS: OperationConfig = {
    "instruction": "orderQueryAll",
    "params": {
        "symbol": "SOL_USDC" # Obrigatório para este endpoint em algumas exchanges, verificar doc específica
    },
    "endpoint": "/api/v1/orders",
    "method": "GET"
}



# ==============================================================================
# 🚀 SELEÇÃO DA OPERAÇÃO ATUAL
# Escolha qual operação será executada pelo script manual.
# ==============================================================================

# OP_ATUAL = OP_SALDO
OP_ATUAL = OP_HISTORICO_FILLS
# OP_ATUAL = OP_ORDENS_ABERTAS
# OP_ATUAL = OP_CRIAR_ORDEM_LIMIT

# ==============================================================================
# EXPORTAÇÃO (Não alterar abaixo)
# ==============================================================================
instruction: str = OP_ATUAL["instruction"]
params: Optional[Dict[str, Any]] = OP_ATUAL["params"]
endpoint: str = OP_ATUAL["endpoint"]
method: str = OP_ATUAL["method"]