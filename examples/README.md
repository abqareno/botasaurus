# Botasaurus Examples

This directory contains example scripts demonstrating various capabilities of Botasaurus.

## 🗺️ Google Maps Scraper Examples

Need help choosing? See the [Comparison Guide](COMPARISON.md) to pick the right scraper for your needs.

### Quick Start Example (Recommended for Beginners)

**File:** `google_maps_scraper_quick.py`

A simplified, easy-to-understand Google Maps scraper that extracts **20+ essential properties** from each place.

**Extracted Properties:**
- Title, Category, Address
- Latitude, Longitude, Place ID, Plus Code
- Rating, Reviews Count
- Phone, Website
- Business Status, Hours Text
- Price Level
- Service Options (Delivery, Takeout, Dine-in)
- Wheelchair Accessibility
- Photos Count
- Top 10 Amenities

**Usage:**
```bash
python examples/google_maps_scraper_quick.py
```

### Advanced Example (40+ Properties)

**File:** `google_maps_scraper_advanced.py`

A comprehensive Google Maps scraper that extracts **40+ properties** from each place.

### Total: 42 Properties

**Extracted Properties:**

#### Basic Information (5 properties)
- Title/Name
- Category (e.g., Restaurant, Hotel)
- Description
- Link
- Place ID

#### Ratings and Reviews (4 properties)
- Overall rating
- Reviews count
- User ratings total
- Review highlights

#### Contact Information (4 properties)
- Phone number
- Website URL
- Email address
- Social media links (Facebook, Instagram, Twitter, LinkedIn)

#### Location (6 properties)
- Full address
- Latitude
- Longitude
- Plus Code
- CID (Customer ID)
- Timezone

#### Business Status and Hours (5 properties)
- Business status (Open/Closed)
- Opening hours (full weekly schedule)
- Temporarily closed flag
- Permanently closed flag
- Popular times availability

#### Pricing (1 property)
- Price level

#### Service Options (4 properties)
- Delivery availability
- Takeout availability
- Dine-in availability
- Reservations availability

#### Accessibility (1 property)
- Wheelchair accessible entrance

#### Amenities (1 property)
- List of all amenities and features

#### Media and Visuals (1 property)
- Photos count

#### Business Credibility (4 properties)
- Claimed status
- Verified badge
- Years in business
- Owner response information

#### Ordering and Booking (3 properties)
- Menu link
- Order online link
- Booking/reservation link

#### Additional Properties (3 properties)
- Place types (from structured data)
- Amenities count
- Social media presence flag

## Common Features (Both Examples)

### Usage

```bash
# Install Botasaurus if you haven't already
pip install botasaurus

# Run the quick start scraper (20+ properties)
python examples/google_maps_scraper_quick.py

# OR run the advanced scraper (42 properties)
python examples/google_maps_scraper_advanced.py
```

### Features

- **Parallel Processing**: Scrapes multiple places simultaneously (5 browsers by default) for faster execution
- **Image Blocking**: Reduces bandwidth and speeds up scraping by blocking images
- **Cookie Handling**: Automatically accepts cookie consent for European users
- **Robust Extraction**: Uses safe extraction methods with fallbacks to handle missing data
- **Comprehensive Output**: Saves data in both JSON and CSV formats

### Output

After running, check the `output` folder for:
- `finished.json`: All scraped data in JSON format
- `finished.csv`: All scraped data in CSV format
- `links.json`: List of all place links found

### Customization

You can customize the scraper by:
- Changing the search query in the `data` parameter
- Adjusting the number of parallel browsers
- Modifying which properties to extract
- Adding additional selectors for other Google Maps features

### Notes

- The scraper automatically handles cookie consent popups for European users
- Some properties may be `None` if they're not available for a particular place
- The scraper follows best practices and uses Botasaurus's anti-detection features
- Image blocking is enabled to reduce costs when using proxies

For a complete reference of all 42 properties and their selectors, see [PROPERTIES_REFERENCE.md](PROPERTIES_REFERENCE.md).

### Requirements

- Python 3.7+
- Botasaurus framework
- Chrome/Chromium browser (automatically managed by Botasaurus)
