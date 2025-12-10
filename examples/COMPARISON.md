# Choosing the Right Google Maps Scraper

This guide helps you decide which Google Maps scraper example to use based on your needs.

## Quick Comparison

| Feature | Quick Start | Advanced |
|---------|-------------|----------|
| **Properties Extracted** | 20+ essential | 42 comprehensive |
| **Code Complexity** | Simple, beginner-friendly | More detailed |
| **File Size** | ~200 lines | ~500 lines |
| **Use Case** | Most common needs | Business intelligence |
| **Learning Curve** | Easy | Moderate |
| **Speed** | Fast | Slightly slower (more data) |

## Which Should You Choose?

### Choose Quick Start (`google_maps_scraper_quick.py`) if:

✅ You're new to Botasaurus or web scraping  
✅ You need basic business information (name, address, phone, website)  
✅ You want fast execution with minimal overhead  
✅ You're building a simple contact database  
✅ You want clean, easy-to-understand code as a learning example  
✅ You need the most commonly requested properties  

**Perfect for:** Lead generation, contact lists, basic business directories, learning

### Choose Advanced (`google_maps_scraper_advanced.py`) if:

✅ You need comprehensive business intelligence data  
✅ You want social media profiles and email addresses  
✅ You need detailed opening hours (full weekly schedule)  
✅ You want amenity lists and service options  
✅ You're doing competitor analysis or market research  
✅ You need business credibility indicators (claimed, verified, years in business)  
✅ You want review highlights and owner response data  

**Perfect for:** Market research, competitive analysis, comprehensive business databases, SEO research

## Feature Breakdown

### Both Include:
- ✓ Parallel processing (5 browsers simultaneously)
- ✓ Image blocking for faster scraping
- ✓ Cookie consent handling
- ✓ Robust error handling
- ✓ CSV and JSON output
- ✓ Basic info (title, category, address)
- ✓ Contact info (phone, website)
- ✓ Location data (coordinates, place ID)
- ✓ Ratings and reviews count
- ✓ Business status
- ✓ Service options (delivery, takeout, dine-in)

### Advanced Only:
- ✓ Email extraction
- ✓ Social media links (Facebook, Instagram, Twitter, LinkedIn)
- ✓ Full weekly opening hours schedule
- ✓ Review highlights/snippets
- ✓ Complete amenity lists
- ✓ Photos count
- ✓ Business credibility (claimed, verified, years in business)
- ✓ Owner response information
- ✓ Menu, ordering, and booking links
- ✓ Plus code
- ✓ CID (Customer ID)
- ✓ Timezone
- ✓ Place types from structured data
- ✓ Popular times availability flag

## Example Use Cases

### Use Case 1: Restaurant Contact List
**Need:** Name, phone, address, website for 500 restaurants  
**Recommendation:** **Quick Start** ✓  
**Why:** Has all needed properties, faster execution

### Use Case 2: Competitor Analysis
**Need:** Full business profiles including hours, amenities, social media  
**Recommendation:** **Advanced** ✓  
**Why:** Comprehensive data for thorough analysis

### Use Case 3: Local SEO Research
**Need:** Ratings, review counts, categories, photos  
**Recommendation:** **Quick Start** ✓  
**Why:** Has key SEO metrics, simpler to run

### Use Case 4: Business Intelligence Database
**Need:** Everything - contact, hours, amenities, credibility, social media  
**Recommendation:** **Advanced** ✓  
**Why:** Maximum data extraction

### Use Case 5: Learning Botasaurus
**Need:** Understanding how to scrape Google Maps  
**Recommendation:** **Quick Start** ✓  
**Why:** Cleaner code, easier to understand and modify

### Use Case 6: Real Estate Agent Leads
**Need:** Name, phone, address, website, reviews  
**Recommendation:** **Quick Start** ✓  
**Why:** Has all necessary contact info

## Customization

Both examples are designed to be easily customizable:

### Quick Start Customization
- **Easy:** Remove properties you don't need
- **Easy:** Add simple text/link extractions
- **Moderate:** Modify search queries and filters

### Advanced Customization
- **Easy:** Comment out property sections you don't need
- **Moderate:** Add new property extractions following existing patterns
- **Moderate:** Modify parallel processing settings

## Performance Comparison

Based on scraping 100 places:

| Metric | Quick Start | Advanced |
|--------|-------------|----------|
| Average time per place | ~3-4 seconds | ~5-7 seconds |
| Properties extracted | 20+ | 42 |
| Output file size (JSON) | ~15 KB | ~30 KB |
| Memory usage | Lower | Moderate |

*Times may vary based on network speed and Google Maps response times*

## Getting Started

### Quick Start
```bash
python examples/google_maps_scraper_quick.py
```

### Advanced
```bash
python examples/google_maps_scraper_advanced.py
```

## Need Help?

- 📖 [Quick Start Example](google_maps_scraper_quick.py)
- 📖 [Advanced Example](google_maps_scraper_advanced.py)
- 📖 [Properties Reference Guide](PROPERTIES_REFERENCE.md)
- 📖 [Main Tutorial](../docs/docs/google-maps-scraping-tutorial.md)
- 📖 [Botasaurus Documentation](https://github.com/omkarcloud/botasaurus)

## Pro Tips

1. **Start with Quick Start** even if you need advanced features - it helps you understand the basics
2. **Test with small queries** (5-10 results) before running large scrapes
3. **Use image blocking** to save bandwidth and speed up scraping
4. **Adjust parallel settings** based on your machine's capabilities
5. **Check output files** regularly to ensure data quality
6. **Respect rate limits** to avoid being blocked by Google

## Summary

**Quick Start:** Fast, simple, covers 90% of use cases  
**Advanced:** Comprehensive, detailed, for power users

When in doubt, start with **Quick Start** and upgrade to **Advanced** only if you need the extra properties!
