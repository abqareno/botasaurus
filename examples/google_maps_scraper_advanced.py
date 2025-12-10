"""
Advanced Google Maps Scraper - Extract 40+ Properties
======================================================

This example demonstrates how to extract comprehensive data from Google Maps,
including 40+ properties for each place such as:
- Basic information (name, category, address, coordinates)
- Contact details (phone, website, email)
- Ratings and reviews
- Business hours and status
- Service options (delivery, takeout, dine-in, reservations)
- Accessibility features
- Payment options
- Amenities
- And much more!

Usage:
    python google_maps_scraper_advanced.py
"""

from botasaurus.browser import browser, Driver
from botasaurus.request import request, Request
import urllib.parse
import re
import json


@browser(
    block_images=True,
    parallel=5,
    reuse_driver=True,
)
def scrape_place_details(driver: Driver, link):
    """
    Scrape detailed information from a Google Maps place page.
    Extracts 40+ properties including business info, contact details, hours, etc.
    """
    
    def scrape_place_data():
        driver.get(link)
        
        # Accept Cookies for European users
        if driver.is_in_page("https://consent.google.com/"):
            agree_button_selector = 'form:nth-child(2) > div > div > button'
            driver.click(agree_button_selector)
            driver.get(link)
        
        # Helper function to safely extract text
        def safe_text(selector):
            try:
                return driver.text(selector)
            except:
                return None
        
        # Helper function to safely extract link
        def safe_link(selector):
            try:
                return driver.link(selector)
            except:
                return None
        
        # Helper function to safely get element
        def safe_element(selector):
            try:
                return driver.get_element_or_none(selector)
            except:
                return None
        
        # 1. BASIC INFORMATION
        # Title/Name of the place
        title = safe_text('h1.DUwDvf')
        
        # Subtitle/Category (e.g., "Restaurant", "Hotel", "Coffee Shop")
        category = safe_text('button[jsaction*="category"]')
        
        # Short description/tagline
        description = safe_text('div.WeS02d.fontBodyMedium')
        
        # 2. RATINGS AND REVIEWS
        # Overall rating (e.g., 4.5)
        rating = safe_text("div.F7nice > span[role='img']")
        
        # Number of reviews
        reviews_text = safe_text("div.F7nice > span:last-child")
        reviews_count = None
        if reviews_text:
            # Extract number from text like "(1,234)"
            reviews_count = int(''.join(filter(str.isdigit, reviews_text))) if reviews_text else None
        
        # User ratings total (alternative selector)
        user_ratings_total_text = safe_text("button[jsaction*='pane.reviewChart']")
        user_ratings_total = None
        if user_ratings_total_text:
            user_ratings_total = int(''.join(filter(str.isdigit, user_ratings_total_text)))
        
        # 3. CONTACT INFORMATION
        # Phone number
        phone = None
        phone_element = safe_element("button[data-item-id*='phone:tel:']")
        if phone_element:
            phone_data = phone_element.get_attribute("data-item-id")
            if phone_data:
                phone = phone_data.replace("phone:tel:", "")
        
        # Website URL
        website = safe_link("a[data-item-id='authority']")
        
        # Email (if available in the description or contact info)
        email = None
        page_text = driver.page_source
        email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', page_text)
        if email_match:
            email = email_match.group(0)
        
        # 4. LOCATION INFORMATION
        # Full address
        address = safe_text("button[data-item-id='address']")
        
        # Plus Code
        plus_code = safe_text("button[data-item-id*='plus_code']")
        
        # Latitude and Longitude (extracted from URL)
        latitude = None
        longitude = None
        coordinates_match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', link)
        if coordinates_match:
            latitude = float(coordinates_match.group(1))
            longitude = float(coordinates_match.group(2))
        
        # Place ID (extracted from URL)
        place_id = None
        place_id_match = re.search(r'!1s(0x[0-9a-fA-F:]+)', link)
        if place_id_match:
            place_id = place_id_match.group(1)
        
        # CID (Customer ID - another identifier)
        cid = None
        cid_match = re.search(r'!1s([0-9]+)!', link)
        if cid_match:
            cid = cid_match.group(1)
        
        # 5. BUSINESS HOURS AND STATUS
        # Business status (Open/Closed)
        business_status = safe_text("span[class*='ZDu9vd'] span[class*='fontBodyMedium']")
        
        # Opening hours - try to get full schedule
        opening_hours = None
        hours_button = safe_element("button[data-item-id*='oh']")
        if hours_button:
            try:
                hours_button.click()
                driver.short_wait()
                # Extract hours from the expanded panel
                hours_elements = driver.select_all("table.eK4R0e tr")
                if hours_elements:
                    opening_hours = {}
                    for row in hours_elements:
                        day = safe_text("td:first-child", row)
                        hours = safe_text("td:last-child", row)
                        if day and hours:
                            opening_hours[day] = hours
                # Close the hours panel
                driver.press(driver.esc)
            except:
                pass
        
        # 6. PRICING
        # Price level (e.g., "$$" or "Moderate")
        price_level = safe_text("span[aria-label*='Price']")
        
        # 7. SERVICE OPTIONS
        # These are usually shown as chips/tags
        service_options = {}
        
        # Delivery
        delivery = None
        delivery_element = safe_element("span[aria-label*='Delivery']")
        if delivery_element:
            delivery = "Yes" if "Yes" in delivery_element.get_attribute("aria-label") else "No"
        service_options['delivery'] = delivery
        
        # Takeout
        takeout = None
        takeout_element = safe_element("span[aria-label*='Takeout']")
        if takeout_element:
            takeout = "Yes" if "Yes" in takeout_element.get_attribute("aria-label") else "No"
        service_options['takeout'] = takeout
        
        # Dine-in
        dine_in = None
        dine_in_element = safe_element("span[aria-label*='Dine-in']")
        if dine_in_element:
            dine_in = "Yes" if "Yes" in dine_in_element.get_attribute("aria-label") else "No"
        service_options['dine_in'] = dine_in
        
        # Reservations
        reservations = None
        reservations_element = safe_element("span[aria-label*='Reservations']")
        if reservations_element:
            reservations = "Yes" if "Yes" in reservations_element.get_attribute("aria-label") else "No"
        service_options['reservations'] = reservations
        
        # 8. ACCESSIBILITY
        # Wheelchair accessible entrance
        wheelchair_accessible = None
        wheelchair_element = safe_element("span[aria-label*='Wheelchair']")
        if wheelchair_element:
            wheelchair_accessible = "Yes" if "accessible" in wheelchair_element.get_attribute("aria-label").lower() else "No"
        
        # 9. AMENITIES AND FEATURES
        # Extract all amenity/feature labels
        amenities = []
        amenity_elements = driver.select_all("div[class*='AeaXub'] div[class*='fontBodyMedium']")
        if amenity_elements:
            for elem in amenity_elements:
                amenity_text = elem.get_attribute("innerText")
                if amenity_text and amenity_text.strip():
                    amenities.append(amenity_text.strip())
        
        # 10. POPULAR TIMES
        # Check if popular times are available
        popular_times_available = driver.exists("div[aria-label*='Popular times']")
        
        # 11. PHOTOS
        # Count of photos
        photos_count = None
        photos_button = safe_element("button[jsaction*='photo']")
        if photos_button:
            photos_text = photos_button.get_attribute("aria-label")
            if photos_text:
                photos_match = re.search(r'(\d+)\s+photo', photos_text)
                if photos_match:
                    photos_count = int(photos_match.group(1))
        
        # 12. ADDITIONAL BUSINESS INFORMATION
        # Owner/Claimed status
        claimed = driver.exists("button[aria-label*='Claimed']")
        
        # Years in business
        years_in_business = safe_text("button[aria-label*='In business']")
        
        # Owner reply rate
        owner_response = safe_text("div[class*='mgr77e'] div[class*='fontBodyMedium']")
        
        # 13. ORDERING AND BOOKING LINKS
        # Menu link
        menu_link = safe_link("a[data-item-id='menu']")
        
        # Order online link
        order_link = safe_link("a[data-item-id*='order']")
        
        # Book a table link
        booking_link = safe_link("a[data-item-id*='reserve']")
        
        # 14. SOCIAL MEDIA AND OTHER LINKS
        # Try to find social media links in the page
        social_links = {}
        page_links = driver.get_all_links("a")
        for link_url in page_links:
            if link_url:
                if 'facebook.com' in link_url:
                    social_links['facebook'] = link_url
                elif 'instagram.com' in link_url:
                    social_links['instagram'] = link_url
                elif 'twitter.com' in link_url or 'x.com' in link_url:
                    social_links['twitter'] = link_url
                elif 'linkedin.com' in link_url:
                    social_links['linkedin'] = link_url
        
        # 15. REVIEW HIGHLIGHTS
        # Extract review snippets/highlights
        review_highlights = []
        highlight_elements = driver.select_all("div[class*='jJc9Ad'] span[class*='fontBodyMedium']")
        if highlight_elements:
            for elem in highlight_elements[:5]:  # Get first 5 highlights
                highlight_text = elem.get_attribute("innerText")
                if highlight_text and highlight_text.strip():
                    review_highlights.append(highlight_text.strip())
        
        # 16. VERIFIED INFORMATION
        # Check for verified badge
        verified = driver.exists("span[aria-label*='Verified']")
        
        # 17. PLACE TYPE
        # Establishment type (from structured data if available)
        place_types = []
        try:
            # Try to extract from JSON-LD structured data
            scripts = driver.select_all("script[type='application/ld+json']")
            for script in scripts:
                script_text = script.get_attribute("innerHTML")
                if script_text:
                    try:
                        data = json.loads(script_text)
                        if isinstance(data, dict) and '@type' in data:
                            place_types.append(data['@type'])
                    except:
                        pass
        except:
            pass
        
        # 18. TIMEZONE
        timezone = safe_text("div[class*='fontBodyMedium'] span[aria-label*='timezone']")
        
        # 19. TEMPORARILY CLOSED
        temporarily_closed = "Temporarily closed" in (business_status or "")
        
        # 20. PERMANENTLY CLOSED
        permanently_closed = "Permanently closed" in (business_status or "")
        
        # Construct comprehensive data dictionary with 40+ properties
        place_data = {
            # Basic Information (1-5)
            '1_title': title,
            '2_category': category,
            '3_description': description,
            '4_link': link,
            '5_place_id': place_id,
            
            # Ratings and Reviews (6-9)
            '6_rating': rating,
            '7_reviews_count': reviews_count,
            '8_user_ratings_total': user_ratings_total,
            '9_review_highlights': review_highlights,
            
            # Contact Information (10-13)
            '10_phone': phone,
            '11_website': website,
            '12_email': email,
            '13_social_links': social_links,
            
            # Location (14-19)
            '14_address': address,
            '15_latitude': latitude,
            '16_longitude': longitude,
            '17_plus_code': plus_code,
            '18_cid': cid,
            '19_timezone': timezone,
            
            # Business Status and Hours (20-24)
            '20_business_status': business_status,
            '21_opening_hours': opening_hours,
            '22_temporarily_closed': temporarily_closed,
            '23_permanently_closed': permanently_closed,
            '24_popular_times_available': popular_times_available,
            
            # Pricing (25)
            '25_price_level': price_level,
            
            # Service Options (26-29)
            '26_delivery': service_options.get('delivery'),
            '27_takeout': service_options.get('takeout'),
            '28_dine_in': service_options.get('dine_in'),
            '29_reservations': service_options.get('reservations'),
            
            # Accessibility (30)
            '30_wheelchair_accessible': wheelchair_accessible,
            
            # Amenities (31)
            '31_amenities': amenities,
            
            # Media and Visuals (32)
            '32_photos_count': photos_count,
            
            # Business Credibility (33-36)
            '33_claimed': claimed,
            '34_verified': verified,
            '35_years_in_business': years_in_business,
            '36_owner_response': owner_response,
            
            # Ordering and Booking (37-39)
            '37_menu_link': menu_link,
            '38_order_link': order_link,
            '39_booking_link': booking_link,
            
            # Additional Properties (40-42)
            '40_place_types': place_types,
            '41_all_amenities_count': len(amenities) if amenities else 0,
            '42_has_social_media': len(social_links) > 0,
        }
        
        # Print summary of extracted data
        non_null_count = sum(1 for v in place_data.values() if v not in [None, [], {}, '', False])
        print(f"Extracted {non_null_count}/42 properties for: {title}")
        
        return place_data
    
    return scrape_place_data()


@browser(
    data=["restaurants in bangalore"],
    block_images=True,
)
def scrape_places_links(driver: Driver, query):
    """
    Search for places on Google Maps and extract all place links.
    """
    
    # Visit Google Maps
    def visit_google_maps():
        encoded_query = urllib.parse.quote_plus(query)
        url = f'https://www.google.com/maps/search/{encoded_query}'
        driver.get(url)
        
        # Accept Cookies for European users
        if driver.is_in_page("https://consent.google.com/"):
            agree_button_selector = 'form:nth-child(2) > div > div > button'
            driver.click(agree_button_selector)
            driver.google_get(url)
    
    # Scroll to the end of the places list to get all the places
    def scroll_to_end_of_places_list():
        end_of_list_detected = False
        
        while not end_of_list_detected:
            # Element that holds the list of places
            places_list_element_selector = '[role="feed"]'
            driver.scroll(places_list_element_selector)
            print('Scrolling...')
            
            # Check if we've reached the end of the list
            end_of_list_indicator_selector = "p.fontBodyMedium > span > span"
            if driver.exists(end_of_list_indicator_selector):
                end_of_list_detected = True
        
        print("Successfully scrolled to the end of the places list.")
    
    def extract_place_links():
        places_links_selector = '[role="feed"] > div > div > a'
        return driver.links(places_links_selector)
    
    visit_google_maps()
    scroll_to_end_of_places_list()
    
    # Get all place links
    places_links = extract_place_links()
    
    print(f"Found {len(places_links)} places")
    
    # Return the places links to be saved as a output/links file
    filename = 'links'
    return filename, places_links


if __name__ == "__main__":
    # Step 1: Scrape all place links from the search query
    links = scrape_places_links()
    
    # Step 2: Scrape detailed information (40+ properties) for each place
    # This will run in parallel with 5 browsers for faster scraping
    scrape_place_details(links)
    
    print("\n" + "="*60)
    print("Scraping completed!")
    print("Check the 'output' folder for results:")
    print("  - finished.json: All scraped data in JSON format")
    print("  - finished.csv: All scraped data in CSV format")
    print("="*60)
