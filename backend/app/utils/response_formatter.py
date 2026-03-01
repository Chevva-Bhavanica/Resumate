# app/utils/response_formatter.py

from fastapi.responses import JSONResponse
from typing import Any, Optional

# --------------------------------------------------
# Standard Success Response
# --------------------------------------------------
def success_response(data: Any, message: str = "Success", status_code: int = 200):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data
        }
    )

# --------------------------------------------------
# Standard Error Response
# --------------------------------------------------
def error_response(message: str, status_code: int = 400, data: Optional[Any] = None):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "data": data
        }
    )
