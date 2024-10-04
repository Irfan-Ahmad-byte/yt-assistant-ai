from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.config.config import Config
from app.routers import agent
from app.dependencies import security


app = FastAPI()


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins= Config.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routing
app.include_router(agent.app, prefix="/agent", tags=["YT agent"], dependencies=[Depends(security.get_api_key)])


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app.main:app', host="0.0.0.0", port=8001, reload=False, log_level="debug")