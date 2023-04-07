from fastapi import FastAPI
from . import models, config
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)  # creates tables within postgres

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,  # it's a function that runs before every request
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Successfully connected to your favourite Post's API"}
