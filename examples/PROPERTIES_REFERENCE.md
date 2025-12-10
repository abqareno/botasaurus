# Google Maps Properties Reference Guide

This document provides a comprehensive reference for all 40+ properties that can be extracted from Google Maps places using the Botasaurus examples.

## Property Categories

### 1. Basic Information (5 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `title` | Name of the business/place | "Joe's Coffee Shop" | `h1.DUwDvf` |
| `category` | Business category/type | "Coffee Shop" | `button[jsaction*="category"]` |
| `description` | Short tagline or description | "Cozy neighborhood cafe" | `div.WeS02d.fontBodyMedium` |
| `link` | Google Maps URL for the place | "https://www.google.com/maps/place/..." | Input parameter |
| `place_id` | Google's unique place identifier | "0x89c25856139b3d33" | Extracted from URL regex |

### 2. Ratings and Reviews (4 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `rating` | Average rating (1-5 stars) | "4.5" | `div.F7nice > span[role='img']` |
| `reviews_count` | Total number of reviews | 1234 | `div.F7nice > span:last-child` |
| `user_ratings_total` | Alternative count of ratings | 1250 | `button[jsaction*='pane.reviewChart']` |
| `review_highlights` | Array of review snippets | ["Great coffee", "Friendly staff"] | `div[class*='jJc9Ad'] span[class*='fontBodyMedium']` |

### 3. Contact Information (4 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `phone` | Phone number | "+1-555-0123" | `button[data-item-id*='phone:tel:']` |
| `website` | Business website URL | "https://joescoffee.com" | `a[data-item-id='authority']` |
| `email` | Email address (if available) | "info@joescoffee.com" | Regex search in page source |
| `social_links` | Social media profile URLs | {facebook: "...", instagram: "..."} | Extracted from all page links |

### 4. Location Information (6 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `address` | Full street address | "123 Main St, New York, NY 10001" | `button[data-item-id='address']` |
| `latitude` | Geographic latitude | 40.7589 | Extracted from URL regex |
| `longitude` | Geographic longitude | -73.9851 | Extracted from URL regex |
| `plus_code` | Google Plus Code | "Q25X+2M New York" | `button[data-item-id*='plus_code']` |
| `cid` | Customer ID (alternative identifier) | "12345678901234567890" | Extracted from URL regex |
| `timezone` | Local timezone | "America/New_York" | `div[class*='fontBodyMedium'] span[aria-label*='timezone']` |

### 5. Business Status and Hours (5 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `business_status` | Current open/closed status | "Open ⋅ Closes 10 PM" | `span[class*='ZDu9vd'] span[class*='fontBodyMedium']` |
| `opening_hours` | Weekly schedule dictionary | {Monday: "8 AM–10 PM", ...} | Extracted from `table.eK4R0e tr` after clicking hours button |
| `temporarily_closed` | Boolean flag | true/false | Parsed from business_status |
| `permanently_closed` | Boolean flag | true/false | Parsed from business_status |
| `popular_times_available` | Has popular times data | true/false | `driver.exists("div[aria-label*='Popular times']")` |

### 6. Pricing (1 property)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `price_level` | Price range indicator | "$$" or "Moderate" | `span[aria-label*='Price']` |

### 7. Service Options (4 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `delivery` | Delivery service available | "Yes" / "No" | `span[aria-label*='Delivery']` |
| `takeout` | Takeout available | "Yes" / "No" | `span[aria-label*='Takeout']` |
| `dine_in` | Dine-in available | "Yes" / "No" | `span[aria-label*='Dine-in']` |
| `reservations` | Accepts reservations | "Yes" / "No" | `span[aria-label*='Reservations']` |

### 8. Accessibility (1 property)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `wheelchair_accessible` | Wheelchair accessible entrance | "Yes" / "No" | `span[aria-label*='Wheelchair']` |

### 9. Amenities and Features (1 property)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `amenities` | List of all amenities | ["Free Wi-Fi", "Outdoor seating", ...] | `div[class*='AeaXub'] div[class*='fontBodyMedium']` |

### 10. Media and Visuals (1 property)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `photos_count` | Number of photos available | 245 | Extracted from `button[jsaction*='photo']` aria-label |

### 11. Business Credibility (4 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `claimed` | Business is claimed by owner | true/false | `driver.exists("button[aria-label*='Claimed']")` |
| `verified` | Business is verified | true/false | `driver.exists("span[aria-label*='Verified']")` |
| `years_in_business` | How long in business | "In business for 10 years" | `button[aria-label*='In business']` |
| `owner_response` | Owner response information | "Responds in a few hours" | `div[class*='mgr77e'] div[class*='fontBodyMedium']` |

### 12. Ordering and Booking Links (3 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `menu_link` | Link to menu | "https://..." | `a[data-item-id='menu']` |
| `order_link` | Online ordering link | "https://..." | `a[data-item-id*='order']` |
| `booking_link` | Reservation/booking link | "https://..." | `a[data-item-id*='reserve']` |

### 13. Additional Metadata (3 properties)

| Property | Description | Example | Selector/Method |
|----------|-------------|---------|----------------|
| `place_types` | Structured data types | ["Restaurant", "Establishment"] | Extracted from JSON-LD script tags |
| `all_amenities_count` | Count of amenities | 15 | `len(amenities)` |
| `has_social_media` | Has social media presence | true/false | `len(social_links) > 0` |

## Total: 42 Properties

## Property Availability

Not all properties are available for every place. The availability depends on:

1. **Business type**: Restaurants have more service options than offices
2. **Data completeness**: Some businesses provide more information than others
3. **Google's data**: Google may not have all information for every place
4. **Business status**: Closed businesses have limited data

## Using the Properties

### Quick Start (20+ Essential Properties)

For most use cases, the quick start example (`google_maps_scraper_quick.py`) provides all essential properties:

- Basic identification (title, category, place_id)
- Location (address, coordinates, plus_code)
- Contact (phone, website)
- Ratings (rating, reviews_count)
- Key business info (hours, price, services)

### Advanced (42 Comprehensive Properties)

For comprehensive business intelligence, use the advanced example (`google_maps_scraper_advanced.py`) which includes:

- All quick start properties
- Detailed business hours (full weekly schedule)
- Review highlights
- Social media links
- Email addresses
- Accessibility features
- Complete amenity lists
- Business credibility indicators
- Ordering/booking links

## Selector Stability

Google Maps occasionally updates its HTML structure. The selectors provided are current as of December 2024, but may need adjustment over time.

**Tips for maintaining selectors:**

1. Use class prefixes (`class*='...'`) instead of exact matches when possible
2. Prefer `aria-label` attributes as they're more stable
3. Use `data-item-id` attributes which rarely change
4. Have fallback methods for critical properties
5. Wrap extraction in try-catch blocks for resilience

## Examples of Use Cases

### Real Estate Leads
Extract: title, category, address, phone, website, rating, reviews_count

### Business Intelligence
Extract: All properties for comprehensive competitor analysis

### Local SEO Research
Extract: rating, reviews_count, category, amenities, photos_count

### Contact Databases
Extract: title, phone, website, email, social_links, address

### Service Availability Mapping
Extract: delivery, takeout, dine_in, wheelchair_accessible, opening_hours

## Performance Considerations

- **Parallel Processing**: Run 5+ browsers simultaneously for 5x speed increase
- **Image Blocking**: Reduces bandwidth by 60-80%
- **Selective Extraction**: Extract only needed properties for faster scraping
- **Caching**: Use Botasaurus caching for repeated scrapes

## Legal and Ethical Considerations

When scraping Google Maps:

1. Respect rate limits
2. Use official APIs when available
3. Don't overload Google's servers
4. Follow Google's Terms of Service
5. Use the data ethically and legally
6. Consider using the Google Places API for commercial use

## Further Reading

- [Botasaurus Documentation](https://github.com/omkarcloud/botasaurus)
- [Google Maps Scraping Tutorial](../docs/docs/google-maps-scraping-tutorial.md)
- [Google Places API](https://developers.google.com/maps/documentation/places/web-service)
