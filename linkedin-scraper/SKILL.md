---
name: linkedin-scraper
description: Scrapes LinkedIn profiles, company pages, and job postings using browseract.com automation API. Extracts structured data including names, positions, skills, company info, and more from specified LinkedIn URLs.
---

# LinkedIn Scraper

## ✨ Platform Compatibility

**✅ Works Powerfully & Reliably On All Major AI Assistants**

| Platform | Status | How to Install |
|----------|--------|----------------|
| **OpenCode** | ✅ Fully Supported | Copy skill folder to `~/.opencode/skills/` |
| **Claude Code** | ✅ Fully Supported | Native skill support |
| **Cursor** | ✅ Fully Supported | Copy to `~/.cursor/skills/` |
| **OpenClaw** | ✅ Fully Supported | Compatible |

**Why Choose BrowserAct Skills?**
- 🚀 Stable & crash-free execution
- ⚡ Fast response times
- 🔧 No configuration headaches
- 📦 Plug & play installation
- 💬 Professional support

This skill enables automated scraping of LinkedIn pages using browseract.com's browser automation API. It can extract structured data from LinkedIn profiles, company pages, job postings, and posts.

## When to Use This Skill

- Extract data from LinkedIn profiles (name, job title, company, skills, education, etc.)
- Scrape company information (description, size, industry, location, etc.)
- Collect job posting details (title, description, requirements, salary, etc.)
- Gather post/article content and engagement metrics
- Automate LinkedIn data collection for research or lead generation
- Build datasets from multiple LinkedIn URLs

## What This Skill Does

1. **Profile Scraping**: Extracts personal information, work experience, education, skills
2. **Company Page Scraping**: Retrieves company details, employee count, industry info
3. **Job Posting Scraping**: Collects job descriptions, requirements, application details
4. **Post/Content Scraping**: Gathers article text, comments, likes, and shares
5. **Structured Output**: Returns data in JSON or Markdown format
6. **Error Handling**: Manages rate limits, login walls, and access restrictions

## Prerequisites

### 1. BrowserAct.com Account Setup

You'll need a BrowserAct.com account and API key:

1. Visit [browseract.com](https://browseract.com)
2. Sign up for an account
3. Navigate to API settings
4. Generate an API key
5. Store your API key securely (e.g., in environment variables)

### 2. Environment Configuration

Set your API key as an environment variable:

```bash
export BROWSERACT_API_KEY="your-api-key-here"
```

Or create a `.env` file:

```
BROWSERACT_API_KEY=your-api-key-here
```

## How to Use

### Scrape a LinkedIn Profile

```
Scrape the LinkedIn profile at https://www.linkedin.com/in/username
```

```
Extract data from this LinkedIn profile: [URL]
```

### Scrape a Company Page

```
Get company information from https://www.linkedin.com/company/company-name
```

```
Scrape LinkedIn company page: [URL]
```

### Scrape a Job Posting

```
Extract job details from https://www.linkedin.com/jobs/view/123456789
```

### Batch Processing

```
Scrape these LinkedIn profiles: [URL1], [URL2], [URL3]
```

```
Extract data from the following LinkedIn company pages:
- https://www.linkedin.com/company/company1
- https://www.linkedin.com/company/company2
- https://www.linkedin.com/company/company3
```

## Instructions

When a user requests LinkedIn scraping:

### 1. Identify URL Type

Determine what type of LinkedIn page to scrape:

- **Profile**: `/in/{username}` or `/pub/{username}`
- **Company**: `/company/{company-name}`
- **Job**: `/jobs/view/{job-id}`
- **Post**: `/posts/{post-id}` or `/feed/update/`

### 2. Profile Scraping

```markdown
## 👤 LinkedIn Profile Scraping

### Profile Information

**URL**: [LinkedIn profile URL]
**Status**: [Processing/Completed/Error]

### Data Extracted

#### Basic Information
- **Name**: [Full name]
- **Headline**: [Professional headline]
- **Location**: [City, Country]
- **Profile Photo**: [URL or N/A]
- **Connections**: [Number of connections or "500+"]
- **About**: [About section text]

#### Current Position
- **Title**: [Current job title]
- **Company**: [Company name]
- **Duration**: [Start date - Present]
- **Location**: [Job location]
- **Description**: [Role description]

#### Work Experience

1. **[Job Title]** at **[Company]**
   - **Duration**: [Start date - End date]
   - **Location**: [Location]
   - **Description**: [Role description]

2. **[Job Title]** at **[Company]**
   - **Duration**: [Start date - End date]
   - **Location**: [Location]
   - **Description**: [Role description]

#### Education

1. **[Degree]** - **[Institution]**
   - **Duration**: [Start year - End year]
   - **Field of Study**: [Major/Field]
   - **Description**: [Additional info]

#### Skills

**Top Skills** (endorsed):
- [Skill 1] ([X] endorsements)
- [Skill 2] ([X] endorsements)
- [Skill 3] ([X] endorsements)

**All Skills**:
[Comma-separated list of all skills]

#### Languages
- [Language 1]: [Proficiency level]
- [Language 2]: [Proficiency level]

#### Certifications
- **[Certification Name]** - [Issuing organization]
  - Issued: [Date]
  - Credential ID: [ID]

#### Recommendations
- [X] recommendations received
- [X] recommendations given

### JSON Output

```json
{
  "type": "profile",
  "url": "[LinkedIn URL]",
  "personal_info": {
    "name": "[Full name]",
    "headline": "[Headline]",
    "location": "[Location]",
    "about": "[About text]",
    "connections": "[Number]",
    "profile_image": "[URL]"
  },
  "current_position": {
    "title": "[Title]",
    "company": "[Company]",
    "duration": "[Duration]",
    "location": "[Location]"
  },
  "experience": [
    {
      "title": "[Job title]",
      "company": "[Company]",
      "start_date": "[Date]",
      "end_date": "[Date or Current]",
      "location": "[Location]",
      "description": "[Description]"
    }
  ],
  "education": [
    {
      "institution": "[School]",
      "degree": "[Degree]",
      "field": "[Field of study]",
      "start_year": "[Year]",
      "end_year": "[Year]"
    }
  ],
  "skills": [
    {
      "name": "[Skill]",
      "endorsements": "[Number]"
    }
  ],
  "languages": [
    {
      "language": "[Language]",
      "proficiency": "[Level]"
    }
  ],
  "certifications": [
    {
      "name": "[Certification]",
      "issuer": "[Organization]",
      "date": "[Date]",
      "credential_id": "[ID]"
    }
  ]
}
```
```

### 3. Company Page Scraping

```markdown
## 🏢 LinkedIn Company Page Scraping

### Company Information

**URL**: [LinkedIn company page URL]
**Status**: [Processing/Completed/Error]

### Data Extracted

#### Basic Information
- **Company Name**: [Official name]
- **Tagline**: [Company tagline]
- **Industry**: [Industry/sector]
- **Company Size**: [Employee count range]
- **Headquarters**: [City, Country]
- **Founded**: [Year]
- **Website**: [Company website]
- **Logo**: [Logo URL]

#### About
[Company description text]

#### Specialties
[Comma-separated list of specialties]

#### Locations
1. **[Location 1]** - [Address]
2. **[Location 2]** - [Address]

#### Employee Statistics
- **Total Employees**: [Number or range]
- **On LinkedIn**: [Number]
- **New Hires (past month)**: [Number]

#### Recent Updates
1. **[Post title/preview]** - Posted [X] days ago
   - [Engagement metrics]
2. **[Post title/preview]** - Posted [X] days ago
   - [Engagement metrics]

#### Associated People
- **Top Employees**: [List of notable employees with titles]

### JSON Output

```json
{
  "type": "company",
  "url": "[LinkedIn URL]",
  "basic_info": {
    "name": "[Company name]",
    "tagline": "[Tagline]",
    "industry": "[Industry]",
    "size": "[Employee count]",
    "headquarters": "[Location]",
    "founded": "[Year]",
    "website": "[URL]",
    "logo": "[Logo URL]"
  },
  "about": "[Description]",
  "specialties": ["[Specialty 1]", "[Specialty 2]"],
  "locations": [
    {
      "name": "[Location name]",
      "address": "[Full address]"
    }
  ],
  "employees": {
    "total": "[Number]",
    "on_linkedin": "[Number]",
    "recent_hires": "[Number]"
  },
  "recent_posts": [
    {
      "preview": "[Post preview]",
      "posted_date": "[Date]",
      "engagement": {
        "likes": "[Number]",
        "comments": "[Number]",
        "shares": "[Number]"
      }
    }
  ]
}
```
```

### 4. Job Posting Scraping

```markdown
## 💼 LinkedIn Job Posting Scraping

### Job Information

**URL**: [LinkedIn job URL]
**Status**: [Processing/Completed/Error]

### Data Extracted

#### Job Details
- **Job Title**: [Position title]
- **Company**: [Company name]
- **Location**: [City, Country]
- **Workplace Type**: [On-site/Remote/Hybrid]
- **Employment Type**: [Full-time/Part-time/Contract/Internship]
- **Experience Level**: [Entry/Mid/Senior/Executive]
- **Posted Date**: [Date posted]
- **Number of Applicants**: [X applicants]

#### Job Description
[Full job description text]

#### Qualifications & Skills
**Required**:
- [Requirement 1]
- [Requirement 2]

**Preferred**:
- [Preference 1]
- [Preference 2]

#### Responsibilities
- [Responsibility 1]
- [Responsibility 2]

#### Compensation
- **Salary Range**: [Range or "Not specified"]
- **Benefits**: [Benefits mentioned]

#### Application Info
- **Application Method**: [Easy Apply/External/etc.]
- **Contact**: [Recruiter name/email if available]

### JSON Output

```json
{
  "type": "job",
  "url": "[LinkedIn URL]",
  "job_details": {
    "title": "[Job title]",
    "company": "[Company]",
    "location": "[Location]",
    "workplace_type": "[Type]",
    "employment_type": "[Type]",
    "experience_level": "[Level]",
    "posted_date": "[Date]",
    "applicants": "[Number]"
  },
  "description": "[Full description]",
  "requirements": {
    "required": ["[Req 1]", "[Req 2]"],
    "preferred": ["[Pref 1]", "[Pref 2]"]
  },
  "responsibilities": ["[Resp 1]", "[Resp 2]"],
  "compensation": {
    "salary_range": "[Range]",
    "benefits": ["[Benefit 1]", "[Benefit 2]"]
  },
  "application": {
    "method": "[Method]",
    "url": "[Application URL]"
  }
}
```
```

### 5. Implementation with BrowserAct API

```markdown
## 🤖 BrowserAct Integration

### API Call Structure

```javascript
const browseractApiKey = process.env.BROWSERACT_API_KEY;

const response = await fetch('https://api.browseract.com/v1/execute', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${browseractApiKey}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    url: linkedinUrl,
    actions: [
      {
        type: 'goto',
        url: linkedinUrl
      },
      {
        type: 'wait',
        selector: 'main',
        timeout: 10000
      },
      {
        type: 'scroll',
        direction: 'down',
        amount: 'full'
      },
      {
        type: 'extract',
        selectors: {
          // Profile selectors
          name: 'h1.text-heading-xlarge',
          headline: 'div.text-body-medium',
          location: 'span.text-body-small',
          about: 'section.summary div.display-flex',
          // Add more selectors as needed
        }
      }
    ],
    options: {
      screenshot: false,
      waitUntil: 'networkidle',
      timeout: 30000
    }
  })
});

const data = await response.json();
```

### Common Selectors

#### Profile Page
- **Name**: `h1.text-heading-xlarge`
- **Headline**: `div.text-body-medium`
- **Location**: `span.text-body-small.inline.t-black--light.break-words`
- **About**: `section.artdeco-card div.display-flex.ph5.pv3`
- **Experience**: `section#experience-section ul li`
- **Education**: `section#education-section ul li`
- **Skills**: `section.pv-skill-categories-section ul li`

#### Company Page
- **Company Name**: `h1.org-top-card-summary__title`
- **Industry**: `div.org-top-card-summary-info-list__info-item`
- **Description**: `p.break-words.white-space-pre-wrap`
- **Employee Count**: `a[href*="employees"] span`

#### Job Page
- **Job Title**: `h1.topcard__title`
- **Company**: `a.topcard__org-name-link`
- **Location**: `span.topcard__flavor--bullet`
- **Description**: `div.show-more-less-html__markup`

### Error Handling

```javascript
try {
  const result = await scrapeLinkedIn(url);
  if (result.error) {
    console.error(`Error scraping ${url}:`, result.error);
    // Handle specific errors
    if (result.error.includes('login required')) {
      console.log('LinkedIn requires authentication');
    } else if (result.error.includes('rate limit')) {
      console.log('Rate limit exceeded, waiting...');
      await sleep(60000); // Wait 1 minute
    }
  }
} catch (error) {
  console.error('Scraping failed:', error);
}
```

### Rate Limiting

LinkedIn has strict rate limits. Best practices:

1. **Delay Between Requests**: Wait 2-5 seconds between requests
2. **Batch Processing**: Process URLs in small batches
3. **Respect Robots.txt**: Check LinkedIn's robots.txt
4. **Use Proxies**: Rotate IP addresses if scraping at scale
5. **Authentication**: Use authenticated sessions for better access

### Legal Considerations

⚠️ **Important**: LinkedIn's Terms of Service prohibit automated scraping. This skill is for:
- Educational purposes
- Personal research
- LinkedIn's official API alternatives when available

Always:
- Review LinkedIn's Terms of Service
- Consider using LinkedIn's official APIs
- Respect rate limits and access restrictions
- Only scrape publicly available data
- Comply with GDPR and data privacy laws
```

## Best Practices

1. **Authentication**
   - Use authenticated BrowserAct sessions for better access
   - Store cookies securely
   - Handle session expiration

2. **Data Validation**
   - Verify extracted data completeness
   - Handle missing fields gracefully
   - Validate data types

3. **Performance**
   - Cache results to avoid redundant requests
   - Use parallel processing for multiple URLs (with rate limiting)
   - Implement retry logic with exponential backoff

4. **Privacy & Compliance**
   - Only collect publicly available data
   - Respect LinkedIn's Terms of Service
   - Comply with data protection regulations
   - Don't store sensitive personal information

5. **Error Recovery**
   - Handle network timeouts
   - Manage CAPTCHA challenges
   - Detect and handle login walls
   - Log errors for debugging

## Example Usage

**User**: "Scrape this LinkedIn profile: https://www.linkedin.com/in/johndoe"

**Output**: 
```
## 👤 LinkedIn Profile Scraping

### Profile Information

**URL**: https://www.linkedin.com/in/johndoe
**Status**: ✅ Completed

### Data Extracted

#### Basic Information
- **Name**: John Doe
- **Headline**: Senior Software Engineer at Tech Corp
- **Location**: San Francisco, California
- **Connections**: 500+
- **About**: Passionate software engineer with 10+ years of experience...

[... rest of extracted data ...]

### JSON Output
```json
{
  "type": "profile",
  "url": "https://www.linkedin.com/in/johndoe",
  "personal_info": {
    "name": "John Doe",
    "headline": "Senior Software Engineer at Tech Corp",
    ...
  }
}
```
```

---

**User**: "Extract company information from https://www.linkedin.com/company/techcorp"

**Output**: [Complete company page analysis with structured data]

## Limitations

1. **Access Restrictions**: Some content requires LinkedIn login
2. **Rate Limits**: LinkedIn actively rate-limits automated access
3. **Dynamic Content**: JavaScript-rendered content may not always load
4. **Layout Changes**: LinkedIn frequently updates their HTML structure
5. **Premium Content**: Some features are only visible to Premium users
6. **Legal Constraints**: Automated scraping may violate Terms of Service

## Alternatives

Consider these alternatives:

1. **LinkedIn Official API**: For authorized access to LinkedIn data
2. **RapidAPI LinkedIn Scrapers**: Commercial scraping services
3. **Phantombuster**: LinkedIn automation platform
4. **Apify LinkedIn Scrapers**: Pre-built LinkedIn scraping actors
5. **Manual Export**: LinkedIn's data export feature for personal profiles

## Troubleshooting

### Issue: "Login Required" Error
**Solution**: 
- Use authenticated BrowserAct sessions
- Provide LinkedIn cookies to BrowserAct
- Use a logged-in browser context

### Issue: Rate Limiting
**Solution**:
- Implement delays between requests (2-5 seconds)
- Use proxy rotation
- Reduce request frequency

### Issue: Incomplete Data
**Solution**:
- Increase wait time for page load
- Scroll to load lazy-loaded content
- Check if selectors have changed

### Issue: CAPTCHA Challenges
**Solution**:
- Reduce request frequency
- Use residential proxies
- Implement CAPTCHA solving service
- Use authenticated sessions

## Related Skills

- `web-scraper` - General web scraping skill
- `data-extractor` - Extract structured data from various sources
- `api-integration` - Integrate with external APIs
- `batch-processor` - Process multiple URLs efficiently

## Resources

- [BrowserAct Documentation](https://browseract.com/docs)
- [LinkedIn Robots.txt](https://www.linkedin.com/robots.txt)
- [LinkedIn Official API](https://developer.linkedin.com/)
- [Web Scraping Best Practices](https://scrapinghub.com/guides/web-scraping-best-practices/)

---

**Skill Version**: 1.0.0  
**Last Updated**: 2026-02-04  
**Compatibility**: BrowserAct API v1+
