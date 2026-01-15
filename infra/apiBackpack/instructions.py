
INSTRUCTIONS_QUERY = [
    "accountQuery",           # Ver dados da conta
    "balanceQuery",           # Ver saldos
    "collateralQuery",        # Ver margem
    "depositAddressQuery",    # Endereço de depósito
    "depositQueryAll",        # Histórico de depósitos
    "fillHistoryQueryAll",    # Histórico de execuções
    "fundingHistoryQueryAll", # Histórico de funding
    "interestHistoryQueryAll",# Histórico de juros
    "orderQuery",             # Ver uma ordem específica
    "orderQueryAll",          # Ver todas as ordens
    "positionQuery",          # Ver posições
    "pnlHistoryQueryAll",     # Histórico de P&L
    "positionHistoryQueryAll",# Histórico de posições
    "strategyQuery",          # Ver uma estratégia
    "strategyQueryAll",       # Ver todas estratégias
    "strategyHistoryQueryAll",# Histórico de estratégias
    "withdrawalQueryAll",     # Histórico de saques
    "borrowHistoryQueryAll",  # Histórico de empréstimos
]

INSTRUCTIONS_EXECUTE = [
    "orderExecute",           # Criar ordem
    "orderCancel",            # Cancelar ordem
    "orderCancelAll",         # Cancelar todas as ordens
    "withdraw",               # Sacar
    "borrowLendExecute",      # Emprestar/Pegar emprestado
    "quoteSubmit",            # Submeter cotação (RFQ)
    "strategyCreate",         # Criar estratégia
    "strategyCancel",         # Cancelar estratégia
    "strategyCancelAll",      # Cancelar todas estratégias
]