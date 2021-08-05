from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def index():
    return fastapi.responses.RedirectResponse(url="/api/calculate")


@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z is not None and z == 0:
        # FIXME: Doesn't comply with standard error response schema
        return fastapi.responses.JSONResponse(
            content={"detail": "z=0 will create division by zero error."},
            status_code=400,
        )

    result = x + y
    result = result / z if z else result

    return {
        "body": {
            "x": x,
            "y": y,
            "z": z,
        },
        "result": result,
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=8000,
        reload=True,
        debug=True,
    )
