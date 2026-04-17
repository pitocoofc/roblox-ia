from fastapi import FastAPI, Header, HTTPException
from app.services.ai_engine import processar_texto

app = FastAPI()

# Autenticação simples por Token (mais seguro que URL)
SECRET_TOKEN = "seu_token_aqui"

@app.post("/chat")
async def chat(data: dict, authorization: str = Header(None)):
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=403, detail="Não autorizado")
    
    user_input = data.get("mensagem")
    resultado = processar_texto(user_input)
    
    return {"resposta": resultado}
