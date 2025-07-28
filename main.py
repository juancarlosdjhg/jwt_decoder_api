from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import jwt

app = FastAPI()

class TokenRequest(BaseModel):
    ak: str
    sk: str

@app.post("/jwt_token_decoder_api_juanito")
def generate_jwt_token(data: TokenRequest):
    try:
        headers = {
            "alg": "HS256",
            "typ": "JWT"
        }
        payload = {
            "iss": data.ak,
            "exp": int(time.time()) + 1800,
            "nbf": int(time.time()) - 5
        }

        token = jwt.encode(payload, data.sk, algorithm="HS256", headers=headers)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Token generation failed: {str(e)}")
