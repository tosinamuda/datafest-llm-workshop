import uvicorn
from app.config import Config
from app.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=Config().port)
