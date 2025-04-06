# Tamiko Web Scraper

![Tamiko Web Scraper](https://img.shields.io/badge/Streamlit-App-blue)  
**Developed as part of the MLSA YE Ramzan Series**

## Overview
The **Tamiko Web Scraper** is a versatile web scraping tool built using Python and Streamlit. It allows users to scrape text, images, or HTML attributes from any website by providing a URL, HTML tag, class name (optional), data type, and attribute (if applicable). The scraped data is displayed in a user-friendly interface and can be downloaded as an Excel file, with images available for individual download. This project was created as part of the MLSA YE Ramzan series, combining skills from web scraping, dynamic UI development, and data automation.

---

## Features
- **Flexible Scraping**: Scrape text, image URLs, or specific attributes from any website.
- **Interactive UI**: Built with Streamlit for an intuitive, browser-based experience.
- **Data Export**: Save scraped data to an Excel file (`tamiko_scraped_data.xlsx` or `tamiko_scraped_images.xlsx`).
- **Image Downloads**: Download scraped images individually.
- **Error Handling**: Displays warnings for invalid URLs or scraping errors.

---

## How It Was Made
This project integrates concepts from three bootcamps in the MLSA YE Ramzan series:
1. **Bootcamp 1: Learn the Power of Web Scraping**  
   - Used `requests` to fetch webpage content and `BeautifulSoup` to parse HTML and extract data based on user inputs (tag, class, data type, attribute).
2. **Bootcamp 2: Build Dynamic Websites with Python**  
   - Leveraged `Streamlit` to create an interactive UI where users input scraping parameters and view results in real-time.
3. **Bootcamp 3: Automate Your Spreadsheets with Python**  
   - Utilized `pandas` to structure scraped data into a DataFrame and save it to an Excel file using `BytesIO` for in-memory processing.

### Development Process
- **Requirements**: Installed necessary libraries (`requests`, `beautifulsoup4`, `streamlit`, `pandas`, `openpyxl`) via `pip`.
- **Code Structure**: 
  - Defined a `scrape_data` function to handle the scraping logic.
  - Built a `main` function for the Streamlit UI and result handling.
  - Removed unnecessary dependencies (e.g., `os`, `zipfile`) to streamline the app.
- **UI Design**: Added a custom title ("Tamiko Web Scraper"), a subtitle, and a loading spinner for better user experience.
- **Output**: Provided Excel downloads for all data types and individual image downloads using `BytesIO`.

---

## Prerequisites
- **Python 3.8+**: Ensure Python is installed on your system.
- **Libraries**: Install the required libraries using:
  ```bash
  pip install requests beautifulsoup4 streamlit pandas openpyxl
  ```

---

## How to Run
1. **Clone or Download**:
   - Save the code in a file named `app.py` in a project folder (e.g., `TamikoWebScraper`).
2. **Navigate to the Folder**:
   ```bash
   cd /path/to/TamikoWebScraper
   ```
3. **Run the App**:
   ```bash
   streamlit run app.py
   ```
4. **Access the App**:
   - Open your browser and go to `http://localhost:8501`.
5. **Usage**:
   - Enter a website URL (e.g., `https://example.com`).
   - Specify an HTML tag (e.g., `p`, `img`, `a`), optional class name, data type (Text, Image, Attribute), and attribute (e.g., `src`, `href`).
   - Click "Scrape Data" to view and download the results.

---

## Example Usage
- **Text**: URL: `https://example.com`, Tag: `p`, Data Type: `Text` → Scrapes paragraph text.
- **Images**: URL: `https://books.toscrape.com`, Tag: `img`, Class: `thumbnail`, Data Type: `Image`, Attribute: `src` → Scrapes image URLs and downloads images.
- **Attributes**: URL: `https://news.ycombinator.com`, Tag: `a`, Class: `storylink`, Data Type: `Attribute`, Attribute: `href` → Scrapes link URLs.

---

## Acknowledgments
- **MLSA YE Ramzan Series**: This project was inspired by and built for the series, combining web scraping, dynamic UI, and automation skills.
- **Streamlit**: For providing an easy-to-use framework for web app development.
- **BeautifulSoup**: For powerful HTML parsing capabilities.

---
