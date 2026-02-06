# Google News Scraping Skill

AI Skill for automated news data collection using BrowserAct's Google News API template. Retrieve structured news data with just one command. Perfect for tracking industry trends, monitoring public relations, and conducting news research.

> News Automation Tool - Retrieve structured news data via the BrowserAct API with a single command.

**Note**: This skill requires a BrowserAct API key. News data retrieval is executed via browseract.com's API.

---

## Table of Contents

1. [Installation](#installation)
2. [API Key Setup](#api-key-setup)
3. [Quick Start](#quick-start)
4. [What This Skill Does](#what-this-skill-does)
5. [Usage Examples](#usage-examples)
6. [Python Usage](#python-usage)
7. [Output Formats](#output-formats)
8. [Configuration](#configuration)
9. [Architecture](#architecture)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)
12. [License](#license)

---

## Installation

### For Claude Code

```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill
cp -r google-news ~/.claude/skills/

# Or clone directly
git clone https://github.com/browseract-com/google-news-skills.git ~/.claude/skills/google-news
```

### For Cursor

```bash
# Create skills directory in Cursor's config folder
mkdir -p ~/.cursor/skills

# Copy the skill
cp -r google-news ~/.cursor/skills/
```

### For VS Code (VSCode with Copilot)

```bash
# Create skills directory
mkdir -p ~/.vscode/skills

# Copy the skill
cp -r google-news ~/.vscode/skills/
```

### For OpenCode

```bash
# Create skills directory
mkdir -p ~/.opencode/skills

# Copy the skill
cp -r google-news ~/.opencode/skills/
```

### For Generic AI Assistants

```bash
# Copy to preferred skills directory
mkdir -p ~/skills

# Copy the skill
cp -r google-news ~/skills/

# Set environment variable for skills path if needed
export SKILLS_PATH=~/skills
```

### Direct Clone from GitHub

```bash
# Clone the repository
git clone https://github.com/browseract-com/google-news-skills.git

# The skill is located at:
# google-news-skills/
```

---

## API Key Setup

### Step 1: Get Your BrowserAct API Key

1. Visit [browseract.com](https://browseract.com)
2. Sign up for an account
3. Navigate to [API Settings](https://www.browseract.com/reception/integrations)
4. Generate an API key
5. Copy your API key

### Step 2: Configure API Key

Choose one of the following methods:

#### Method A: Environment Variable (Recommended)

**macOS / Linux:**
```bash
# Add to your shell profile
echo 'export BROWSERACT_API_KEY="your-api-key-here"' >> ~/.zshrc

# Or set temporarily
export BROWSERACT_API_KEY="your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
setx BROWSERACT_API_KEY "your-api-key-here"
```

**Windows (PowerShell):**
```powershell
$env:BROWSERACT_API_KEY = "your-api-key-here"
```

#### Method B: .env File

Create a `.env` file in your project directory:

```bash
# .env
BROWSERACT_API_KEY=your-api-key-here
```

Load it in Python:

```python
from dotenv import load_dotenv
load_dotenv()  # Loads .env file
```

#### Method C: Claude Code Specific

```bash
# Create .env file in Claude Code config
mkdir -p ~/.claude
echo "BROWSERACT_API_KEY=your-api-key-here" > ~/.claude/.env
```

#### Method D: Cursor Specific

```bash
# Create .env file in Cursor settings
mkdir -p ~/.cursor
echo "BROWSERACT_API_KEY=your-api-key-here" > ~/.cursor/.env
```

#### Method E: Command Line Argument

```bash
python scripts/google_news_api.py "AI News" --api-key your-api-key-here
```

#### Method F: Python Code

```python
import os
os.environ["BROWSERACT_API_KEY"] = "your-api-key-here"
```

### Step 3: Verify Your API Key

```bash
# Test if API key is set
echo $BROWSERACT_API_KEY

# Or test with Python
python -c "import os; print('API Key set:', bool(os.getenv('BROWSERACT_API_KEY')))"
```

---

## Quick Start

### Step 1: Install the Skill

Choose your platform:

| Platform | Command |
|----------|---------|
| Claude Code | `cp -r google-news ~/.claude/skills/` |
| Cursor | `cp -r google-news ~/.cursor/skills/` |
| VS Code | `cp -r google-news ~/.vscode/skills/` |
| OpenCode | `cp -r google-news ~/.opencode/skills/` |

### Step 2: Configure API Key

```bash
export BROWSERACT_API_KEY="your-api-key"
```

### Step 3: Start Using

**In Claude Code or any supported AI assistant:**

```
Find news about AI technology trends
```

```
Track news about Tesla stock
```

**Or use Python directly:**

```bash
python scripts/google_news_api.py "AI technology"
```

---

## What This Skill Does

1. **Keyword Search** — Search Google News for specific topics, companies, or keywords

2. **Time Filtering** — Filter news by publication date (any time, past hours, past 24 hours, past week, past year)

3. **Volume Control** — Limit the number of news articles retrieved (default: 30)

4. **Structured Data** — Extract headlines, sources, links, publication times, and authors

5. **Real-time Monitoring** — Perfect for tracking breaking news and industry trends

6. **PR Monitoring** — Monitor public relations coverage and brand mentions

7. **Trend Analysis** — Collect data for short-term and long-term trend analysis

8. **Multi-source Aggregation** — Aggregate news from multiple publishers

---

## Usage Examples

### Basic News Search

```
Find news about AI technology
```

```
Search for Tesla news
```

### Time-Restricted Search

```
Get news about cryptocurrency from the past week
```

```
Find Apple company news from the past 24 hours
```

### Industry Monitoring

```
Track electric vehicle industry news
```

```
Monitor semiconductor industry trends
```

### Competitive Intelligence

```
Find news about competitor XYZ
```

```
Track market changes in cloud computing
```

### PR Monitoring

```
Monitor brand mentions for our company
```

```
Track crisis news coverage
```

### Deep Research

```
Get news about AI from the past year for research
```

```
Collect long-term trends in renewable energy
```

---

## Python Usage

### Command Line Interface

```bash
# Basic search (default: past week, 30 articles)
python scripts/google_news_api.py "AI technology"

# Custom time range
python scripts/google_news_api.py "Bitcoin" "past 24 hours"

# Custom limit
python scripts/google_news_api.py "Tesla" "past week" 50

# Show help
python scripts/google_news_api.py --help
```

### Programmatic Usage

```python
import os
from scripts.google_news_api import run_google_news_task

# Set API key
os.environ["BROWSERACT_API_KEY"] = "your-api-key"

# Basic search
result = run_google_news_task(
    api_key="your-api-key",
    keywords="AI technology",
    date_range="past week",
    limit=30
)

print(result)
```

### Advanced Usage

```python
import os
from scripts.google_news_api import run_google_news_task

# Set API key
os.environ["BROWSERACT_API_KEY"] = "your-api-key"

# Search with custom parameters
result = run_google_news_task(
    api_key="your-api-key",
    keywords="machine learning",
    date_range="past month",  # Custom time range
    limit=50  # More articles
)

if result:
    # Parse the JSON result
    import json
    data = json.loads(result)
    for article in data:
        print(f"Title: {article.get('headline')}")
        print(f"Source: {article.get('source')}")
        print(f"Link: {article.get('news_link')}")
        print(f"Date: {article.get('published_time')}")
        print("---")
```

---

## Output Formats

### JSON Output

```json
[
  {
    "headline": "AI Technology Advances in 2024",
    "source": "TechCrunch",
    "news_link": "https://techcrunch.com/2024/01/15/ai-advances",
    "published_time": "2024-01-15T10:30:00Z",
    "author": "John Doe"
  },
  {
    "headline": "Machine Learning Trends Analysis",
    "source": "The Verge",
    "news_link": "https://theverge.com/2024/01/14/ml-trends",
    "published_time": "2024-01-14T15:45:00Z",
    "author": "Jane Smith"
  }
]
```

### Print Format

When run from command line, results are printed in a readable format:

```
========================================
AI Technology News Results
========================================

Headline: AI Technology Advances in 2024
Source: TechCrunch
Published: 2024-01-15
Link: https://techcrunch.com/...
Author: John Doe

---
```

---

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|-----------|---------|-------------|
| `BROWSERACT_API_KEY` | Yes | - | Your BrowserAct API key |
| `WORKFLOW_TEMPLATE_ID` | No | 77638424152140851 | BrowserAct workflow template |

### Setting Variables

**Linux/macOS:**
```bash
export BROWSERACT_API_KEY="your-key"
export WORKFLOW_TEMPLATE_ID="77638424152140851"
```

**Windows:**
```cmd
set BROWSERACT_API_KEY=your-key
```

**In Python:**
```python
import os
os.environ["BROWSERACT_API_KEY"] = "your-key"
```

### Workflow Template ID

The skill uses BrowserAct workflow template: `77638424152140851`

You can find available templates at:
https://www.browseract.com/template?platformType=0

### Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `Search_Keywords` | string | Yes | - | Keywords to search |
| `Publish_date` | string | No | past week | Time range |
| `Datelimit` | number | No | 30 | Max articles |

### Publish Date Options

| Option | Description |
|--------|-------------|
| `any time` | All time |
| `past hours` | Past few hours (breaking news) |
| `past 24 hours` | Past 24 hours (daily monitoring) |
| `past week` | Past week (short-term trends) |
| `past month` | Past month (medium-term analysis) |
| `past year` | Past year (long-term research) |

---

## Architecture

### BrowserAct API Integration

The skill uses BrowserAct's workflow template system:

```
User Request → Extract Keywords → Submit Task → Poll Status → Retrieve Results
```

### API Endpoints Used

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v2/workflow/run-task-by-template` | POST | Submit scraping task |
| `/v2/workflow/get-task-status` | GET | Check task status |
| `/v2/workflow/get-task` | GET | Retrieve results |

### API Flow

1. **Submit Task**: POST to `/run-task-by-template` with keywords and parameters
2. **Poll Status**: GET `/get-task-status` every 3 seconds
3. **Get Results**: GET `/get-task` when status is "finished"

### Rate Limiting

Best practices for API usage:

- **Search frequency**: Wait 3-5 seconds between searches
- **Batch size**: Maximum 50 articles per search
- **Retry logic**: Automatic retry on minor connection issues
- **Caching**: Cache results for 1 hour to avoid duplicates

### Error Handling

```python
try:
    result = run_google_news_task(
        api_key="your-key",
        keywords="AI news",
        date_range="past week",
        limit=30
    )
except requests.exceptions.ConnectionError:
    print("Network error - check internet connection")
except Exception as e:
    print(f"Error: {e}")
```

---

## Troubleshooting

### Issue: API Call Failed

**Solutions:**
1. Verify API key is correctly set:
   ```bash
   echo $BROWSERACT_API_KEY
   ```
2. Check account has sufficient API quota
3. Validate keywords are not empty
4. Check network connectivity

### Issue: No Results

**Solutions:**
1. Try different keywords
2. Expand time range (e.g., from "past 24 hours" to "past week")
3. Check if Google News is accessible in your region
4. Verify keywords are spelled correctly

### Issue: Task Timeout

**Solutions:**
1. Reduce the `Datelimit` parameter
2. Shorten the time range
3. Check BrowserAct service status
4. Verify workflow template is available

### Issue: Incomplete Data

**Solutions:**
1. Some articles may not have all fields
2. Check internet connection during retrieval
3. Retry with smaller limit
4. Review API response for errors

### Issue: Anti-Scraping Triggered

**Solutions:**
1. Reduce search frequency
2. Increase delay between requests
3. Use smaller result limits
4. Contact BrowserAct support for rate limit adjustment

### Issue: Permission Denied (Linux/macOS)

```bash
# Fix Python script permissions
chmod +x scripts/google_news_api.py

# Or run with python directly
python scripts/google_news_api.py "AI news"
```

### Issue: Module Not Found

```bash
# Install dependencies
pip install requests python-dotenv

# Or if using uv
uv pip install requests python-dotenv
```

---

## Project Structure

```
google-news-skills/
├── README.md                           # This file
├── SKILL.md                            # Skill documentation
└── scripts/
    └── google_news_api.py             # Python implementation
```

---

## Related Skills

- [amazon-competitor-analyzer](https://github.com/browseract-com/Skills) — Amazon product competitive analysis
- [browser-use](https://github.com/browser-use/browser-use) — Browser automation
- [web-scraper](https://github.com/) — General web scraping
- [data-analyzer](https://github.com/) — Data analysis tools

---

## Resources

- [BrowserAct Documentation](https://browseract.com/docs)
- [BrowserAct Workflow Templates](https://www.browseract.com/template?platformType=0)
- [BrowserAct API Integration](https://www.browseract.com/reception/integrations)
- [Google News](https://news.google.com)
- [News API Alternatives](https://newsapi.org)

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Adding New Features

1. Update `SKILL.md` with new functionality documentation
2. Add tests if applicable
3. Update this README with new usage examples
4. Ensure backward compatibility

---

## License

MIT License

---

## Support

- [GitHub Issues](https://github.com/browseract-com/google-news-skills/issues)
- [BrowserAct Discord](https://discord.gg/browseract)
- [Email Support](mailto:support@browseract.com)

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-06  
**Compatibility**: BrowserAct API v2+  
**Supported Platforms**: Claude Code, Cursor, VS Code, OpenCode, Generic AI Assistants  
**Supported Sites**: Google News

---

## Changelog

### v1.0.0 (2026-02-06)

- Initial release
- Keyword-based news search
- Time range filtering
- Volume control
- Structured JSON output
- Multi-platform support
- Comprehensive API key setup documentation
