"""
import asyncio
from pyppeteer import launch

async def scrape_links():
    # Launch a headless Chromium browser
    browser = await launch(headless=True)

    # Create a new page
    page = await browser.newPage()

    # Navigate to the URL
    url = "https://www.nutritionix.com/brand/burger-king/products/513fbc1283aa2dc80c00000a"  # Replace with the actual URL
    await page.goto(url)

    # Wait for the page to load
    await page.waitForSelector("tr.item-row")

    # Extract href attributes from <tr> elements with class "item-row"
    hrefs = await page.evaluate('''() => {
        const hrefs = [];
        const rows = document.querySelectorAll("tr.item-row");
        for (const row of rows) {
            const anchor = row.querySelector("a");
            if (anchor) {
                hrefs.push(anchor.getAttribute("href"));
            }
        }
        return hrefs;
    }''')

    # Print the extracted hrefs
    for href in hrefs:
        print(href)

    # Close the browser
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(scrape_links())







import asyncio
from pyppeteer import launch

async def extract_text_from_divs():
    # Launch a headless Chromium browser
    browser = await launch(headless=True)

    # Create a new page
    page = await browser.newPage()

    # Navigate to the URL of the web page containing the <div> elements
    url = "https://www.nutritionix.com/i/burger-king/16-piece-chicken-nuggets/bd9d8414c0f945e71c6f5f24"  # Replace with the actual URL
    await page.goto(url)

    # Wait for the <div> elements to be visible
    await page.waitForSelector("div.nf-line")

    # Extract and print text from each <div> element
    div_elements = await page.evaluate('''() => {
        const divElements = document.querySelectorAll("div.nf-line");
        return Array.from(divElements, element => element.textContent.trim());
    }''')

    for index, text in enumerate(div_elements):
        print(f"{text}")

    # Close the browser
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(extract_text_from_divs())
"""
import csv

# Sample data for chicken nuggets
# Create and write data to a CSV file
with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ["Menu Item", "Total Fat (g)", "Saturated Fat (g)", "Trans Fat (g)", "Cholesterol (mg)", 
                "Sodium (mg)", "Total Carbohydrates (g)", "Dietary Fiber (g)", "Sugars (g)", "Protein (g)"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write header row
    writer.writeheader()

for _ in range(10):
    item_data = {
        "Menu Item": "Chicken Nuggets",
        "Total Fat (g)": "15",
        "Saturated Fat (g)": "3.5",
        "Trans Fat (g)": "0",
        "Cholesterol (mg)": "30",
        "Sodium (mg)": "800",
        "Total Carbohydrates (g)": "20",
        "Dietary Fiber (g)": "1",
        "Sugars (g)": "0",
        "Protein (g)": "10",
    }
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(item_data)

print("Data saved to 'chicken_nuggets.csv' file.")
