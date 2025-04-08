
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from scraper import scrap_meshoo  # Importing from scraper.py

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI deployed successfully on Vercel!"}

@app.get("/scrape")
def scrape(
    base_url: str = Query(..., description="Base URL to scrape"),
    pages: int = Query(1, description="Number of pages to scrape")
):
    return scrap_meshoo(base_url, pages)
handler=app