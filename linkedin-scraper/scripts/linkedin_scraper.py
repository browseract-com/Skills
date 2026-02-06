#!/usr/bin/env python3
"""
LinkedIn Scraper - BrowserAct Skill

This script scrapes LinkedIn profiles, company pages, and job postings
using the BrowserAct MCP server.

Template ID: 77973967694128706
"""

import os
import json
import time
import argparse
from datetime import datetime
from typing import Optional
import requests


BROWSERACT_API_KEY = os.environ.get("BROWSERACT_API_KEY")
BROWSERACT_MCP_TOKEN = os.environ.get("BROWSERACT_MCP_TOKEN")
MCP_SERVER_URL = "https://mcp.browseract.com/77973967694128706/mcp/"


def detect_url_type(url: str) -> str:
    """Detect the type of LinkedIn URL."""
    if "/in/" in url or "/pub/" in url:
        return "profile"
    elif "/company/" in url:
        return "company"
    elif "/jobs/view/" in url:
        return "job"
    elif "/posts/" in url or "/feed/update/" in url:
        return "post"
    else:
        return "unknown"


def execute_mcp_request(payload: dict) -> dict:
    """Execute a request to the BrowserAct MCP server."""
    response = requests.post(
        MCP_SERVER_URL,
        headers={
            "Authorization": f"Bearer {BROWSERACT_MCP_TOKEN}",
            "Content-Type": "application/json"
        },
        json=payload,
        timeout=60000
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"MCP request failed: {response.status_code} - {response.text}")


def scrape_linkedin_profile(url: str, include_skills: bool = True, include_education: bool = True) -> dict:
    """
    Scrape a LinkedIn profile.

    Args:
        url: LinkedIn profile URL
        include_skills: Whether to extract skills
        include_education: Whether to extract education history

    Returns:
        Dictionary containing profile data
    """
    payload = {
        "url": url,
        "type": "profile",
        "options": {
            "extract_skills": include_skills,
            "extract_education": include_education,
            "scroll_to_load": True,
            "wait_for_content": True
        }
    }

    return execute_mcp_request(payload)


def scrape_linkedin_company(url: str, include_employees: bool = True, include_posts: bool = True) -> dict:
    """
    Scrape a LinkedIn company page.

    Args:
        url: LinkedIn company page URL
        include_employees: Whether to extract employee info
        include_posts: Whether to extract recent posts

    Returns:
        Dictionary containing company data
    """
    payload = {
        "url": url,
        "type": "company",
        "options": {
            "extract_employees": include_employees,
            "extract_posts": include_posts,
            "max_posts": 5,
            "scroll_to_load": True
        }
    }

    return execute_mcp_request(payload)


def scrape_linkedin_job(url: str, include_salary: bool = True) -> dict:
    """
    Scrape a LinkedIn job posting.

    Args:
        url: LinkedIn job posting URL
        include_salary: Whether to extract salary info

    Returns:
        Dictionary containing job data
    """
    payload = {
        "url": url,
        "type": "job",
        "options": {
            "extract_salary": include_salary,
            "parse_requirements": True,
            "scroll_to_load": True
        }
    }

    return execute_mcp_request(payload)


def detect_url_type(url: str) -> str:
    """Detect the type of LinkedIn URL."""
    if "/in/" in url or "/pub/" in url:
        return "profile"
    elif "/company/" in url:
        return "company"
    elif "/jobs/view/" in url:
        return "job"
    elif "/posts/" in url or "/feed/update/" in url:
        return "post"
    else:
        return "unknown"


def format_profile_output(data: dict) -> str:
    """Format profile data as markdown."""
    personal_info = data.get("personal_info", {})
    experience = data.get("experience", [])
    education = data.get("education", [])
    skills = data.get("skills", [])

    output = f"## LinkedIn Profile\n\n"
    output += f"**URL**: {data.get('url', 'N/A')}\n\n"

    output += "### Basic Information\n"
    output += f"- **Name**: {personal_info.get('name', 'N/A')}\n"
    output += f"- **Headline**: {personal_info.get('headline', 'N/A')}\n"
    output += f"- **Location**: {personal_info.get('location', 'N/A')}\n"
    output += f"- **Connections**: {personal_info.get('connections', 'N/A')}\n\n"

    if experience:
        output += "### Experience\n"
        for exp in experience[:5]:
            output += f"- **{exp.get('title', 'N/A')}** at {exp.get('company', 'N/A')}\n"
            output += f"  - {exp.get('duration', 'N/A')}\n"
            output += f"  - {exp.get('location', 'N/A')}\n\n"

    if education:
        output += "### Education\n"
        for edu in education[:3]:
            output += f"- **{edu.get('degree', 'N/A')}** - {edu.get('institution', 'N/A')}\n"
            output += f"  - {edu.get('field', 'N/A')} ({edu.get('duration', 'N/A')})\n\n"

    if skills:
        output += "### Top Skills\n"
        for skill in skills[:10]:
            output += f"- {skill.get('name', 'N/A')} ({skill.get('endorsements', 'N/A')} endorsements)\n"

    return output


def format_company_output(data: dict) -> str:
    """Format company data as markdown."""
    basic_info = data.get("basic_info", {})

    output = f"## LinkedIn Company\n\n"
    output += f"**URL**: {data.get('url', 'N/A')}\n\n"

    output += "### Basic Information\n"
    output += f"- **Name**: {basic_info.get('name', 'N/A')}\n"
    output += f"- **Industry**: {basic_info.get('industry', 'N/A')}\n"
    output += f"- **Size**: {basic_info.get('size', 'N/A')}\n"
    output += f"- **Headquarters**: {basic_info.get('headquarters', 'N/A')}\n"
    output += f"- **Website**: {basic_info.get('website', 'N/A')}\n\n"

    if data.get("about"):
        output += "### About\n"
        output += f"{data.get('about')}\n\n"

    return output


def format_job_output(data: dict) -> str:
    """Format job data as markdown."""
    job_details = data.get("job_details", {})

    output = f"## LinkedIn Job Posting\n\n"
    output += f"**URL**: {data.get('url', 'N/A')}\n\n"

    output += "### Job Details\n"
    output += f"- **Title**: {job_details.get('title', 'N/A')}\n"
    output += f"- **Company**: {job_details.get('company', 'N/A')}\n"
    output += f"- **Location**: {job_details.get('location', 'N/A')}\n"
    output += f"- **Type**: {job_details.get('employment_type', 'N/A')}\n"
    output += f"- **Level**: {job_details.get('experience_level', 'N/A')}\n"
    output += f"- **Posted**: {job_details.get('posted_date', 'N/A')}\n"
    output += f"- **Applicants**: {job_details.get('applicants', 'N/A')}\n\n"

    return output


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="LinkedIn Scraper - Extract data from LinkedIn profiles, companies, and jobs")
    parser.add_argument("url", help="LinkedIn URL to scrape")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown", help="Output format")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--include-skills", action="store_true", default=True, help="Include skills (profiles)")
    parser.add_argument("--include-education", action="store_true", default=True, help="Include education (profiles)")
    parser.add_argument("--include-salary", action="store_true", default=True, help="Include salary (jobs)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()

    if not BROWSERACT_MCP_TOKEN:
        print("Error: BROWSERACT_MCP_TOKEN environment variable not set")
        print("Get your token from: https://www.browseract.com/reception/integrations")
        return 1

    url_type = detect_url_type(args.url)

    if url_type == "unknown":
        print(f"Error: Could not detect LinkedIn URL type: {args.url}")
        return 1

    try:
        if args.verbose:
            print(f"Scraping LinkedIn {url_type}: {args.url}")

        if url_type == "profile":
            data = scrape_linkedin_profile(args.url, args.include_skills, args.include_education)
            output = format_profile_output(data) if args.format == "markdown" else json.dumps(data, indent=2)
        elif url_type == "company":
            data = scrape_linkedin_company(args.url)
            output = format_company_output(data) if args.format == "markdown" else json.dumps(data, indent=2)
        elif url_type == "job":
            data = scrape_linkedin_job(args.url, args.include_salary)
            output = format_job_output(data) if args.format == "markdown" else json.dumps(data, indent=2)
        else:
            print(f"Error: Unsupported URL type: {url_type}")
            return 1

        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            if args.verbose:
                print(f"Output saved to: {args.output}")
        else:
            print(output)

        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
