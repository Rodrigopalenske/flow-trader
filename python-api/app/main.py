from fastapi import FastAPI, Request, HTTPException
import uvicorn
import logging
import json
import re

# Configuração do logging
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Função auxiliar para formatar erro JSON com contexto
def format_json_error(raw_body: str, error: json.JSONDecodeError):
    try:
        error_pos = error.pos
        snippet_start = max(0, error_pos - 20)
        snippet_end = min(len(raw_body), error_pos + 20)
        snippet = raw_body[snippet_start:snippet_end]
        marker = ' ' * (error_pos - snippet_start - 1) + '^' if snippet_start <= error_pos < snippet_end else ''
        return f"{str(error)}, raw body: {raw_body}, error at position {error_pos}: {snippet}\n{marker}"
    except Exception:
        return f"{str(error)}, raw body: {raw_body}"

# Endpoint para receber ticks
@app.post("/tick")
async def receive_tick(request: Request):
    try:
        body = await request.body()
        raw_body = body.decode('utf-8', errors='replace')
        data = json.loads(raw_body)
        message = f"Received tick: {json.dumps(data)}"
        print(message)
        logger.info(message)
        return {"status": "received"}
    except json.JSONDecodeError as e:
        message = f"Error decoding JSON in /tick: {format_json_error(raw_body, e)}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")
    except Exception as e:
        message = f"Unexpected error in /tick: {str(e)}, raw body: {raw_body}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint para controle (start/pause)
@app.post("/control")
async def control(request: Request):
    try:
        body = await request.body()
        raw_body = body.decode('utf-8', errors='replace')
        data = json.loads(raw_body)
        message = f"Control request: {json.dumps(data)}"
        print(message)
        logger.info(message)
        return {"status": "start"}  # Alterar para "pause" para testar pausa
    except json.JSONDecodeError as e:
        message = f"Error decoding JSON in /control: {format_json_error(raw_body, e)}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")
    except Exception as e:
        message = f"Unexpected error in /control: {str(e)}, raw body: {raw_body}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint para verificar ordens
@app.post("/ordem")
async def check_order(request: Request):
    try:
        body = await request.body()
        raw_body = body.decode('utf-8', errors='replace')
        data = json.loads(raw_body)
        message = f"Order request: {json.dumps(data)}"
        print(message)
        logger.info(message)
        return {"status": "executed"}
    except json.JSONDecodeError as e:
        message = f"Error decoding JSON in /ordem: {format_json_error(raw_body, e)}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")
    except Exception as e:
        message = f"Unexpected error in /ordem: {str(e)}, raw body: {raw_body}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint para verificar configurações
@app.post("/config")
async def check_config(request: Request):
    try:
        body = await request.body()
        raw_body = body.decode('utf-8', errors='replace')
        data = json.loads(raw_body)
        message = f"Config request: {json.dumps(data)}"
        print(message)
        logger.info(message)
        return {"status": "updated"}
    except json.JSONDecodeError as e:
        message = f"Error decoding JSON in /config: {format_json_error(raw_body, e)}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")
    except Exception as e:
        message = f"Unexpected error in /config: {str(e)}, raw body: {raw_body}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint para solicitar candles
@app.get("/candles")
async def get_candles(symbol: str, timeframe: str, count: int):
    try:
        message = f"Candles requested: symbol={symbol}, timeframe={timeframe}, count={count}"
        print(message)
        logger.info(message)
        return {"candles": []}  # Retorna vazio para simulação
    except Exception as e:
        message = f"Unexpected error in /candles: {str(e)}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint para informações da conta
@app.post("/account")
async def receive_account(request: Request):
    try:
        body = await request.body()
        raw_body = body.decode('utf-8', errors='replace')
        data = json.loads(raw_body)
        message = f"Account info: {json.dumps(data)}"
        print(message)
        logger.info(message)
        return {"status": "received"}
    except json.JSONDecodeError as e:
        message = f"Error decoding JSON in /account: {format_json_error(raw_body, e)}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")
    except Exception as e:
        message = f"Unexpected error in /account: {str(e)}, raw body: {raw_body}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint para informações de posições
@app.post("/positions")
async def receive_positions(request: Request):
    try:
        body = await request.body()
        raw_body = body.decode('utf-8', errors='replace')
        # Tenta sanitizar JSON removendo vírgulas finais em arrays
        sanitized_body = re.sub(r',\s*\]', ']', raw_body)
        sanitized_body = re.sub(r',\s*\}', '}', sanitized_body)
        try:
            data = json.loads(sanitized_body)
        except json.JSONDecodeError as e:
            # Se a sanitização falhar, tenta novamente com o corpo original
            data = json.loads(raw_body)
        # Verifica se o campo 'positions' existe e é um array
        if "positions" not in data:
            message = f"Missing 'positions' field in /positions request, raw body: {raw_body}, sanitized: {sanitized_body}"
            print(message)
            logger.error(message)
            raise HTTPException(status_code=400, detail="Missing 'positions' field")
        if not isinstance(data["positions"], list):
            message = f"'positions' field must be a list, raw body: {raw_body}, sanitized: {sanitized_body}"
            print(message)
            logger.error(message)
            raise HTTPException(status_code=400, detail="'positions' must be a list")
        message = f"Positions info: {json.dumps(data)}"
        print(message)
        logger.info(message)
        return {"status": "received"}
    except json.JSONDecodeError as e:
        message = f"Error decoding JSON in /positions: {format_json_error(raw_body, e)}, attempted sanitized body: {sanitized_body}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")
    except Exception as e:
        message = f"Unexpected error in /positions: {str(e)}, raw body: {raw_body}, attempted sanitized body: {sanitized_body}"
        print(message)
        logger.error(message)
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8082)