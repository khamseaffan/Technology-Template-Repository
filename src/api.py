from typing import Dict, Any

def get_status() -> Dict[str, str]:
    return {"status": "API is running"}

def process_request(data: str) -> Dict[str, Any]:
    return {"message": f"Processed data: {data}"}
