from fastapi import FastAPI

app = FastAPI()


@app.post("/test")
async def test_route():
    """
    Test Route for this API
    """
    return {"result": "LGTM"}
