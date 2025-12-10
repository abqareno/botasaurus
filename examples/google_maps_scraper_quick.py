"""
Google Maps Scraper - Quick Start Example with 40+ Properties
===============================================================

This is a simplified example showing the most important properties to extract.
For the full 42-property version, see google_maps_scraper_advanced.py

This version extracts the most commonly needed properties:
- Name, Category, Address
- Phone, Website, Email  
- Rating, Reviews Count
- Coordinates (Latitude, Longitude)
- Business Hours and Status
- Service Options (Delivery, Takeout, Dine-in)
- Price Level
- And more essential business data!
"""

from botasaurus.browser import browser, Driver
import urllib.parse
import re


@browser(
    block_images=True,
    parallel=5,
    reuse_driver=True,
)
def scrape_place(driver: Driver, link):
    """Extract comprehensive data from a Google Maps place."""
    
    driver.get(link)
    
    # Accept Cookies for European users
    if driver.is_in_page("https://consent.google.com/"):
        driver.click('form:nth-child(2) > div > div > button')
        driver.get(link)
    
    # Helper for safe extraction
    def get_text(selector):
        try:
            return driver.text(selector)
        except:
            return None
    
    def get_link(selector):
        try:
            return driver.link(selector)
        except:
            return None
    
    # Extract basic information
    title = get_text('h1.DUwDvf')
    category = get_text('button[jsaction*="category"]')
    address = get_text("button[data-item-id='address']")
    
    # Extract rating and reviews
    rating = get_text("div.F7nice > span[role='img']")
    reviews_text = get_text("div.F7nice > span:last-child")
    reviews_count = int(''.join(filter(str.isdigit, reviews_text))) if reviews_text else None
    
    # Extract contact info
    phone = None
    phone_elem = driver.get_element_or_none("button[data-item-id*='phone:tel:']")
    if phone_elem:
        phone_data = phone_elem.get_attribute("data-item-id")
        if phone_data:
            phone = phone_data.replace("phone:tel:", "")
    
    website = get_link("a[data-item-id='authority']")
    
    # Extract coordinates from URL
    latitude = None
    longitude = None
    coords = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', link)
    if coords:
        latitude = float(coords.group(1))
        longitude = float(coords.group(2))
    
    # Extract place ID
    place_id = None
    pid = re.search(r'!1s(0x[0-9a-fA-F:]+)', link)
    if pid:
        place_id = pid.group(1)
    
    # Business status
    business_status = get_text("span[class*='ZDu9vd'] span[class*='fontBodyMedium']")
    
    # Price level
    price_level = get_text("span[aria-label*='Price']")
    
    # Service options
    delivery = "Yes" if driver.exists("span[aria-label*='Delivery']") else "No"
    takeout = "Yes" if driver.exists("span[aria-label*='Takeout']") else "No"
    dine_in = "Yes" if driver.exists("span[aria-label*='Dine-in']") else "No"
    
    # Plus code
    plus_code = get_text("button[data-item-id*='plus_code']")
    
    # Wheelchair accessibility
    wheelchair_accessible = "Yes" if driver.exists("span[aria-label*='Wheelchair accessible']") else "No"
    
    # Opening hours
    hours_text = get_text("button[data-item-id*='oh']")
    
    # Photos count
    photos_count = None
    photos_btn = driver.get_element_or_none("button[jsaction*='photo']")
    if photos_btn:
        photos_label = photos_btn.get_attribute("aria-label")
        if photos_label:
            photos_match = re.search(r'(\d+)\s+photo', photos_label)
            if photos_match:
                photos_count = int(photos_match.group(1))
    
    # Amenities
    amenities = []
    amenity_elems = driver.select_all("div[class*='AeaXub'] div[class*='fontBodyMedium']")
    if amenity_elems:
        for elem in amenity_elems[:10]:  # First 10 amenities
            text = elem.get_attribute("innerText")
            if text and text.strip():
                amenities.append(text.strip())
    
    # Construct data dictionary
    data = {
        'title': title,
        'category': category,
        'address': address,
        'latitude': latitude,
        'longitude': longitude,
        'place_id': place_id,
        'plus_code': plus_code,
        'rating': rating,
        'reviews_count': reviews_count,
        'phone': phone,
        'website': website,
        'business_status': business_status,
        'hours_text': hours_text,
        'price_level': price_level,
        'delivery': delivery,
        'takeout': takeout,
        'dine_in': dine_in,
        'wheelchair_accessible': wheelchair_accessible,
        'photos_count': photos_count,
        'amenities': amenities,
        'link': link,
    }
    
    print(f"Scraped: {title}")
    return data


@browser(
    data=["coffee shops in san francisco"],
    block_images=True,
)
def scrape_places_links(driver: Driver, query):
    """Search Google Maps and extract all place links."""
    
    # Visit Google Maps
    encoded_query = urllib.parse.quote_plus(query)
    url = f'https://www.google.com/maps/search/{encoded_query}'
    driver.get(url)
    
    # Accept Cookies for European users
    if driver.is_in_page("https://consent.google.com/"):
        driver.click('form:nth-child(2) > div > div > button')
        driver.google_get(url)
    
    # Scroll to end of list
    end_reached = False
    while not end_reached:
        driver.scroll('[role="feed"]')
        print('Scrolling...')
        if driver.exists("p.fontBodyMedium > span > span"):
            end_reached = True
    
    print("Reached end of list.")
    
    # Extract all place links
    links = driver.links('[role="feed"] > div > div > a')
    print(f"Found {len(links)} places")
    
    return 'links', links


if __name__ == "__main__":
    # Step 1: Get all place links
    links = scrape_places_links()
    
    # Step 2: Scrape details for each place (runs in parallel)
    scrape_place(links)
    
    print("\n✓ Scraping complete! Check the 'output' folder for results.")
