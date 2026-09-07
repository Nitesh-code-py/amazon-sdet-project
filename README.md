# Amazone SDET Automation Project

![Tests](https://img.shields.io/badge/Tests-4%20Passed-green)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Playwright](https://img.shields.io/badge/Playwright-UI%20Testing-orange)

A simple and clean SDET project for Amazon with UI and API testing.

## Tech Stack
- Python 3.14
- Playwright for UI Testing
- Requests for API Testing
- Pytest for Test Framework
- HTML Report for Results

## What I Tested

**1. UI Tests (Amazon.in):**
- Search for laptop and verify results
- Check Amazon logo is visible

**2. API Tests (FakeStore API):**
- Get all products and check response
- Add new product and verify

Total 4 tests - All Passed

## Project Folder


## How to Run This Project

pip install -r requirements.txt
playwright install
pytest --html=report.html -v

After running, open report.html in your browser to see the result.
