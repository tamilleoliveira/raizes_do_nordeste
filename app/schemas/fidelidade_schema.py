from pydantic import BaseModel

class FidelidadeRequest(BaseModel):
    cliente_id: int
    pontos: int
    status: str