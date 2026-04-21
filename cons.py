from fastapi import FastAPI
from services import BattingConsistencyService
from schemas import ConsistencyResponse

app = FastAPI()

@app.get("/consistency", response_model=ConsistencyResponse)
def get_consistency_index():
    service = BattingConsistencyService()
    result = service.calculate_bci()
    return result