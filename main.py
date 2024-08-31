from fastapi import FastAPI
from database import models
from database.database import engine
from routers import post
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(post.router)

models.Base.metadata.create_all(engine)

origins = [
    'http://localhost:3000' #React application
]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)