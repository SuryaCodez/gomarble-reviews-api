from fastapi import FastAPI, Query
from pydantic import BaseModel
import openai
import os
import json
import asyncio
import sys
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
from playwright.sync_api import sync_playwright
app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")
class Review(BaseModel):
    title: str
    body: str
    rating: int
    reviewer: str

class ReviewsResponse(BaseModel):
    reviews_count: int
    reviews: list[Review]

def get_css_selectors(page_html: str):
    prompt = f"Extract the CSS selectors for product reviews, review title, body, rating, and reviewer name from the following HTML:\n{page_html}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    selectors = response["choices"][0]["text"].strip()
    return json.loads(selectors) 

def extract_reviews(page_url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page_url="https://2717recovery.com/products/recovery-cream"
        page.goto(page_url)
        page.wait_for_load_state("networkidle")
        page.wait_for_selector("jdgm-rev-widg.jdgm-rev-widg__reviews")
        reviews = page.locator("jdgm-rev-widg.jdgm-rev-widg__reviews").all_text_contents()
        browser.close()
    reviews_count = len(reviews)
    reviews_data = [
        {
            "title": review,
            "body": review,
            "rating": 5, 
            "reviewer": "Anonymous" 
        }
        for review in reviews
    ]
    return reviews_count, reviews_data

@app.get("/api/reviews", response_model=ReviewsResponse)
def get_reviews(page: str ):
    try:
        reviews_count, reviews = extract_reviews(page)
        return {"reviews_count": reviews_count, "reviews": reviews}
    except Exception as e:
        print(f"error occured: {e}")
        return {"reviews_count":0,"reviews":[]}
    

# Instructions to run
# Save this code in a file (main.py) and run using: uvicorn main:app --reload
