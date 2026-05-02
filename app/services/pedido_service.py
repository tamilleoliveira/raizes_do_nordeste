import random

pedidos = []

def criar_pedido(pedido):
    pedido.status = "aguardando_pagamento"
    pedidos.append(pedido)
    return pedido

def processar_pagamento(pedido_id: int):
    status_pagamento = random.choice(["aprovado", "recusado"])

    return {
        "pedido_id": pedido_id,
        "status": status_pagamento
    }