from typing import Dict, Any

def get_status() -> dict[str, str]:
    return {"status": "API is running"}


def process_request(data: str) -> dict[str, str]:
    return {"message": f"Processed data: {data}"}
