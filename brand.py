
import re
import math
from pyppeteer import launch

class RestaurantScraper:  # Corrected class name
    def __init__(self):
        self.browser = None
        self.page = None
        self.file = "links.txt"

    async def initialize(self, link):
        # Clear file
        with open(self.file, 'w') as file:
            pass

        # Launch a headless Chromium browser
        self.browser = await launch(headless=True)

        # Create a new page
        self.page = await self.browser.newPage()
        await self.page.setDefaultNavigationTimeout(60000)  # Increase the default navigation timeout


        # Goes to page
        await self.page.goto(link)

    async def close_browser(self):
        # Close the browser
        if self.browser:
            print("Closed browser")
            await self.browser.close()

    async def get_number_of_pages(self):
        try:
            # Wait for the element to appear
            await self.page.waitForSelector("pre.text-center.ng-binding")

            # Get the text inside the <pre> element
            text = await self.page.evaluate('''() => {
                const preElement = document.querySelector("pre.text-center.ng-binding");
                return preElement.textContent;
            }''')

            # Use regular expression to find all numbers in the string
            numbers = [int(num) for num in re.findall(r'\d+', text)]
            number = math.ceil(numbers[2] / numbers[1])
            print(number)
            return number

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    async def scrape_links(self, page_num):
        try:
            url = f"https://www.nutritionix.com/brands/restaurant?page={page_num}"
            await self.page.goto(url)
            print(url)

            # Wait for the page to load
            await self.page.waitForSelector(".brand-grid.ng-scope")

            # Extract links from the divs
            links = await self.page.evaluate(
                '''() => {
                    const links = [];
                    const divs = document.querySelectorAll('.brand-grid.ng-scope');
                    for (const div of divs) {
                        const anchor = div.querySelector('a');
                        if (anchor) {
                            links.push(anchor.getAttribute('href'));
                        }
                    }
                    return links;
                }'''
            )

            return links
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
