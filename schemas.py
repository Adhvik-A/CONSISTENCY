from pydantic import BaseModel


class ConsistencyResponse(BaseModel):
    mean_runs: float
    std_deviation: float
    failure_rate: float
    consistency_index: float
    consistency_label: str