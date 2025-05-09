from fastapi import FastAPI
from app.routes import router
app = FastAPI(
title = "Smart Job Tracker API",
description = "Track your job applications using Smart Job Tracker API",
version = "0.1.0"
)
app.include_router(router)