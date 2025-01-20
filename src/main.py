from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from src.routers.send_message import router as send_message_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(send_message_router)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return RedirectResponse(url="/static/index.html")