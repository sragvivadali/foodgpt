import re
from pyppeteer import launch
from brand import RestaurantScraper  # Corrected import

async def scrape_links(link):
    scraper = RestaurantScraper()  # Corrected class name
    url = "https://www.nutritionix.com" + link  # Corrected URL formatting
    await scraper.initialize(url)
    num = await scraper.get_number_of_pages()

    for i in range(1, num + 1):  # Corrected loop range
        # Navigate to the URL
        url = "https://www.nutritionix.com" + link + f"?page={i}"  # Corrected URL formatting
        await scraper.page.goto(url)

        # Wait for the page to load
        await scraper.page.waitForSelector("tr.item-row")

        # Extract href attributes from <tr> elements with class "item-row"
        hrefs = await scraper.page.evaluate('''() => {
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
    await scraper.close_browser()

