# LinkedIn Scraper Skill

Automated LinkedIn data extraction using BrowserAct.com browser automation.

## Quick Start

### 1. Install the Skill

This skill is located at:
```
~/.opencode/skills/linkedin-scraper/
```

### 2. Set Up BrowserAct API Key

Get your API key from [browseract.com](https://browseract.com) and set it as an environment variable:

```bash
export BROWSERACT_API_KEY="your-api-key-here"
```

Or add to your `.env` file:
```
BROWSERACT_API_KEY=your-api-key-here
```

### 2.1 MCP Server Configuration (Optional)

This skill includes MCP (Model Context Protocol) server configuration for enhanced browser automation:

```json
{
  "mcp": {
    "enabled": true,
    "serverUrl": "https://mcp.browseract.com/77973967694128706/mcp/",
    "token": "${BROWSERACT_MCP_TOKEN}",
    "transport": "sse",
    "timeout": 60000,
    "retries": 3
  }
}
```

**⚠️ Security Notice:** The MCP token should be set via environment variable:
```bash
export BROWSERACT_MCP_TOKEN="your-mcp-token-here"
```

**MCP Features:**
- ✅ Persistent browser sessions
- ✅ Better handling of dynamic content
- ✅ Improved reliability for complex scraping tasks
- ✅ Automatic session recovery
- ✅ Enhanced rate limiting protection

### 3. Use the Skill

In OpenCode, simply ask:

```
Scrape the LinkedIn profile at https://www.linkedin.com/in/username
```

```
Extract company data from https://www.linkedin.com/company/company-name
```

## Supported LinkedIn URL Types

| Type | URL Pattern | Example |
|------|-------------|---------|
| Profile | `/in/{username}` | `https://www.linkedin.com/in/johndoe` |
| Company | `/company/{name}` | `https://www.linkedin.com/company/google` |
| Job Posting | `/jobs/view/{id}` | `https://www.linkedin.com/jobs/view/123456` |
| Post | `/posts/{id}` | `https://www.linkedin.com/posts/user_activity` |

## Features

- ✅ Extract profile information (name, headline, experience, education, skills)
- ✅ Scrape company pages (about, size, industry, locations)
- ✅ Collect job postings (description, requirements, salary)
- ✅ Structured JSON output
- ✅ Batch processing multiple URLs
- ✅ Error handling and retry logic
- ✅ Rate limiting compliance

## Data Extracted

### Profile
- Personal info (name, headline, location, about)
- Current position
- Work experience history
- Education background
- Skills with endorsements
- Languages
- Certifications
- Recommendations count

### Company Page
- Company name and tagline
- Industry and size
- Headquarters location
- Founded year
- Website
- Description
- Specialties
- Recent posts
- Employee statistics

### Job Posting
- Job title and company
- Location and workplace type
- Employment type and level
- Job description
- Requirements (required/preferred)
- Responsibilities
- Compensation details
- Application method

## Example Commands

### Single Profile
```
Scrape https://www.linkedin.com/in/satyanadella
```

### Multiple Profiles
```
Extract data from these LinkedIn profiles:
- https://www.linkedin.com/in/jeffweiner08
- https://www.linkedin.com/in/reidhoffman
- https://www.linkedin.com/in/williamhgates
```

### Company Information
```
Get company details from https://www.linkedin.com/company/microsoft
```

### Job Posting
```
Extract job details from https://www.linkedin.com/jobs/view/3847362911
```

## Output Formats

### Markdown (Default)
Human-readable formatted output with sections and subsections.

### JSON
Structured data for programmatic processing:

```json
{
  "type": "profile",
  "url": "https://www.linkedin.com/in/username",
  "personal_info": {
    "name": "John Doe",
    "headline": "Software Engineer at Tech Corp",
    "location": "San Francisco, CA",
    "about": "Passionate about technology..."
  },
  "experience": [...],
  "education": [...],
  "skills": [...]
}
```

## Configuration

Create a `config.json` file for custom settings:

```json
{
  "browseract": {
    "apiKey": "${BROWSERACT_API_KEY}",
    "timeout": 30000,
    "waitUntil": "networkidle",
    "screenshot": false
  },
  "scraping": {
    "delayBetweenRequests": 3000,
    "maxRetries": 3,
    "scrollToLoad": true
  },
  "output": {
    "format": "json",
    "saveToFile": true,
    "directory": "./linkedin-data"
  }
}
```

## Rate Limiting

To respect LinkedIn's rate limits:

- **Delay**: 2-5 seconds between requests (configurable)
- **Batch Size**: Process max 10 URLs at a time
- **Daily Limit**: Recommend < 100 requests per day
- **Proxies**: Use proxy rotation for larger volumes

## Legal & Ethical Considerations

⚠️ **Important Notice**

LinkedIn's Terms of Service prohibit automated data scraping. This skill is provided for:

- **Educational purposes** - Learning web scraping techniques
- **Personal research** - Non-commercial data collection
- **Proof of concept** - Testing automation capabilities

**Always:**
- Check LinkedIn's current Terms of Service
- Consider using LinkedIn's official APIs
- Only scrape publicly available data
- Respect rate limits
- Comply with data privacy laws (GDPR, CCPA, etc.)
- Get consent for storing personal data

**Better Alternatives:**
- [LinkedIn Official API](https://developer.linkedin.com/) - Authorized access
- Manual export - LinkedIn's built-in data export feature
- Commercial services - Licensed data providers

## Troubleshooting

### "API Key Not Found"
Set the `BROWSERACT_API_KEY` environment variable:
```bash
export BROWSERACT_API_KEY="your-key"
```

### "Login Required"
Some profiles require authentication. Use BrowserAct's authenticated sessions:
```javascript
{
  "cookies": [/* LinkedIn session cookies */]
}
```

### "Rate Limited"
Reduce request frequency or use proxies:
```json
{
  "scraping": {
    "delayBetweenRequests": 5000
  }
}
```

### Incomplete Data
Increase timeout or enable scrolling:
```json
{
  "browseract": {
    "timeout": 60000
  },
  "scraping": {
    "scrollToLoad": true
  }
}
```

## Development

### File Structure
```
linkedin-scraper/
├── SKILL.md           # Main skill instructions
├── README.md          # This file
├── config.json        # Configuration (optional)
└── examples/          # Example outputs
    ├── profile.json
    ├── company.json
    └── job.json
```

### Testing

Test with a known public profile:
```
Scrape https://www.linkedin.com/in/williamhgates
```

Expected output should include Bill Gates' profile information.

## Support

For issues or questions:

1. Check the [SKILL.md](./SKILL.md) documentation
2. Review [BrowserAct docs](https://browseract.com/docs)
3. Open an issue in the OpenCode repository
4. Check LinkedIn's structure hasn't changed

## Version History

- **v1.0.0** (2026-02-04) - Initial release
  - Profile scraping
  - Company page scraping
  - Job posting scraping
  - JSON output support
  - Rate limiting
  - Error handling

## License

This skill is provided as-is for educational purposes. Users are responsible for ensuring compliance with LinkedIn's Terms of Service and applicable laws.

## Disclaimer

This skill uses browser automation to extract publicly available LinkedIn data. The authors are not responsible for any misuse or violations of LinkedIn's Terms of Service. Use at your own risk and ensure compliance with all applicable laws and regulations.
