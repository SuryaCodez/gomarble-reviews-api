# **Review Scraper API**

This project is a an FastAPI server capable of extracting reviews information from any given product page. The scraper uses Playwright for browser automation and OpenAI's API for dynamically detecting CSS selectors for review elements.
This repository i have used 2717recovery webpage as example product page to test implementation.

---

## **Features**
- Extract product reviews, including the title, body, rating, and reviewer name.
- Returns reviews in a structured JSON response.
- Implements FastAPI for a clean and scalable API interface.
- Uses Playwright for precise web scraping.

---
## **How To Run Project**
### **Prerequisites**
- Python 3.9+
- Install dependencies: FastAPI, Playwright, OpenAI.
- Install Playwright binaries: playwright install
### **Installation**
- Clone the repository: git clone https://github.com/SuryaCodez/gomarble-reviews-api
- Navigate to the project directory: cd gomarble-reviews-api
- Install the dependencies: pip install -r requirements.txt
### **Running the Server**
- Start the FastAPI server: uvicorn main:app --reload
- Access the API Documentation for the swagger GUI of FastAPI: http://127.0.0.1:8000/docs
---
## **API Implementation Details**
### **Technologies Used**
- FastAPI: For building the RESTful API.
- Playwright: For web scraping and extracting reviews dynamically.
- OpenAI: To extract CSS selectors dynamically based on the webpage HTML structure.
---
## Setup and Dependencies:
The code uses **FastAPI** to create an API endpoint, **Playwright** for web scraping, and **OpenAI API** for analyzing HTML and extracting CSS selectors. All necessary dependencies are listed in the `requirements.txt`.

### API Structure:

- A FastAPI application is created with a single endpoint: `/api/reviews`.
- The endpoint accepts a query parameter `page` (URL to the example product page) and returns a structured response containing the number of reviews and the review details.

### Web Scraping for Reviews:

- The `extract_reviews` function uses **Playwright** to scrape product reviews from the provided page URL.
- A browser instance is launched in headless mode to navigate to the page.
- The function waits for the page to load completely and for a specific CSS selector (`jdgm-rev-widg.jdgm-rev-widg__reviews`) that contains the reviews.
- The review content is extracted using the `.all_text_contents()` method.

### Response Structure:

Once reviews are extracted, they are formatted into a structured response containing:

- **Title**: The review content itself.
- **Body**: The same as the title for simplicity.
- **Rating**: Defaulted to 5 (as no real rating extraction is implemented).
- **Reviewer**: Defaulted to "Anonymous" (as no reviewer extraction is implemented).

  The total number of reviews (`reviews_count`) is also calculated and included in the response.
---

## Usage Instructions:

1. Save the code as `main.py`.
2. Install the dependencies from `requirements.txt` using the command:
   ```
   pip install -r requirements.txt
   ```
3. Run the application using the `uvicorn` server:
   ```
   uvicorn main:app --reload
   ```
4. Once the server starts, the API can be accessed at `http://127.0.0.1:8000/docs` to test it via the Swagger UI.

---
