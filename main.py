from fastapi import FastAPI, Header, HTTPException
from llama_cpp import Llama
import os

app = FastAPI()

# Carrega o modelo do disco (O Render mantém o arquivo após o download)
# Certifique-se de que o arquivo .gguf esteja no seu repositório ou baixado via script
model_path = "models/seu-modelo.gguf" 
llm = Llama(model_path=model_path, n_ctx=2048) 

SECRET_TOKEN = os.environ.get("SECRET_TOKEN")

@app.post("/chat")
async def chat(data: dict, authorization: str = Header(None)):
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=403, detail="Não autorizado")
    
    user_input = data.get("mensagem")
    
    # Inferência local (Sem API externa)
    output = llm(f"Q: {user_input} A:", max_tokens=100, stop=["Q:", "\n"], echo=False)
    resposta = output['choices'][0]['text']
    
    return {"resposta": resposta}
