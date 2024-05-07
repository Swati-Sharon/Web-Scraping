# WebScraping
Simple weather web scraping

This python script scrapes weather information for a given location using Google search results. It utilizes the "requests_html" library for web scraping.

- Python 3.x
- `requests_html` library (install using `pip install requests-html`)

## Usage

1. Import `HTMLSession` from `requests_html` library.
2. Define a session object `s`.
3. Set the location query.
4. Construct the Google search URL with the location query.
5. Send a GET request to the constructed URL.
6. Extract weather information from the response HTML.
7. Print the temperature, condition, and time.

## Example

```python
from requests_html import HTMLSession

# Create a session
s = HTMLSession()

# Set the location query
query = 'New Delhi'

# Construct the Google search URL
url = f'https://www.google.com/search?q=weather+new+delhi+{query}'

# Send GET request with a specific user agent
r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})

# Extract weather information
temp = r.html.find('span#wob_tm', first=True).text
degree = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
condition = r.html.find('span#wob_dc', first=True).text
day_time = r.html.find('div.VQF4g', first=True).find('div#wob_dts', first=True).text

# Print weather information
print(temp, degree, condition, day_time)
```

## Notes:
The script relies on the structure of Google's search result page. If Google changes how they present weather information on their site, this script might stop working correctly.

