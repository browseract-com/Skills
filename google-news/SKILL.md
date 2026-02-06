---
name: google-news-api
description: Automated news data collection using BrowserAct's Google News API template. Retrieve structured news articles with a single command. Ideal for tracking industry trends, monitoring PR coverage, and conducting news research.
---

# Google News Scraping Skill

This skill provides automated news data collection through BrowserAct's Google News API template. Execute a single command to retrieve structured news articles including headlines, sources, publication dates, and author information.

## Input Parameters

Configure the following parameters when invoking the script:

### 1. Search_Keywords

- **Type**: `string`
- **Description**: Keywords or phrases to search on Google News. Supports company names, industry terms, competitor names, and topic keywords.
- **Examples**: `AI startups`, `Tesla`, `SpaceX`, `artificial intelligence`, `climate change`

### 2. Publish_date

- **Type**: `string`
- **Description**: Filter news articles by publication date range.
- **Valid Values**:
  - `any time`: All time periods
  - `past hours`: Past few hours (best for breaking news)
  - `past 24 hours`: Past 24 hours (recommended for daily monitoring)
  - `past week`: Past 7 days (ideal for short-term trend analysis)
  - `past month`: Past 30 days (medium-term analysis)
  - `past year`: Past 365 days (long-term research and historical data)
- **Default**: `past week`

### 3. Datelimit

- **Type**: `number`
- **Description**: Maximum number of news articles to retrieve per request.
- **Default**: `30`
- **Recommendations**:
  - `10-30`: Real-time monitoring and breaking news
  - `50-100`: Comprehensive research and trend analysis
  - `100+`: Large-scale data collection

## API Key Configuration

If the `BROWSERACT_API_KEY` environment variable is not configured, the script will exit with an error message.

**Agent Action Required**:
> "BrowserAct API Key is not configured. Please obtain your API key from the [BrowserAct Console](https://www.browseract.com/reception/integrations) and provide it in this session."

## Execution Methods

### Direct Script Execution

Execute the standalone script for immediate results:

```bash
python ./scripts/google_news_api.py "search keywords" "time range" limit
```

### Example Usage

```bash
# Basic search (past week, default 30 articles)
python ./scripts/google_news_api.py "artificial intelligence"

# Custom time range
python ./scripts/google_news_api.py "Bitcoin" "past 24 hours"

# Custom limit
python ./scripts/google_news_api.py "Tesla" "past week" 50

# Full parameters
python ./scripts/google_news_api.py "climate change" "past month" 100
```

## Output Structure

Upon successful execution, the script parses and displays results from the API response:

```json
{
  "headline": "Article title",
  "source": "Publisher name",
  "news_link": "URL to article",
  "published_time": "ISO 8601 timestamp",
  "author": "Author name (if available)"
}
```

### Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `headline` | string | News article title |
| `source` | string | Publisher or news outlet name |
| `news_link` | string | Direct URL to the article |
| `published_time` | string | Publication timestamp (ISO 8601 format) |
| `author` | string | Author name (may be null for some articles) |

## Error Handling

The script handles common error scenarios:

- **Missing API Key**: Exits with setup instructions
- **Connection Errors**: Retries with exponential backoff
- **API Errors**: Displays error code and message
- **Timeout**: Configurable timeout with graceful failure

## Rate Limiting

Recommended usage patterns to avoid rate limiting:

- **Minimum Interval**: 3-5 seconds between requests
- **Batch Size**: Maximum 100 articles per request
- **Daily Limit**: Monitor API quota in BrowserAct dashboard

## Use Cases

### Industry Trend Monitoring

Track developments in specific industries or technologies:

```
Monitor news about cloud computing trends
```

### Competitive Intelligence

Stay informed about competitor activities:

```
Find news about competitor company XYZ
```

### PR and Brand Monitoring

Track media coverage and brand mentions:

```
Monitor brand mentions for company ABC
```

### Breaking News Detection

Identify emerging stories and viral content:

```
Get news about major tech announcements from the past 24 hours
```

### Academic Research

Collect historical news data for analysis:

```
Research news about renewable energy from the past year
```

## Integration with AI Agents

This skill is designed for seamless integration with AI coding assistants:

```python
from scripts.google_news_api import run_google_news_task

# Execute within an agent workflow
result = run_google_news_task(
    api_key="your-api-key",
    keywords="artificial intelligence",
    date_range="past week",
    limit=30
)

# Process results in your agent
if result:
    # Parse and analyze news data
    pass
```

## Dependencies

Required Python packages:

- `requests` - HTTP library for API calls
- Python 3.7 or higher

Install dependencies:

```bash
pip install requests
```

## Related Skills

- `amazon-competitor-analyzer` - Amazon product competitive analysis
- `web-scraper` - General-purpose web scraping
- `data-analyzer` - Data analysis and visualization

## Resources

- [BrowserAct Documentation](https://browseract.com/docs)
- [BrowserAct API Console](https://www.browseract.com/reception/integrations)
- [Google News](https://news.google.com)
- [Google News Search Operators](https://support.google.com/news/publishers/answer/42657)

---

**Skill Version**: 1.0.0  
**Last Updated**: 2026-02-06  
**Compatibility**: BrowserAct API v2
