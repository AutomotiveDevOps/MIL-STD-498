#!/usr/bin/env python3
"""
Convert HTML and Markdown files to StrictDoc format following proper grammar rules.

This script converts MIL-STD-498 document templates from HTML and Markdown formats
to StrictDoc (.sdoc) format, ensuring compliance with the StrictDoc grammar specification.

Author: Claude Sonnet 4 (claude-3-5-sonnet-20241022)
Generated via Cursor IDE (cursor.sh) with AI assistance
Model: Anthropic Claude 3.5 Sonnet
Generation timestamp: 2024-12-19
Context: Convert MIL-STD-498 documentation to StrictDoc format
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import html2text
from bs4 import BeautifulSoup
import yaml


class StrictDocConverter:
    """Convert HTML and Markdown files to StrictDoc format following grammar rules."""
    
    def __init__(self):
        self.requirement_counter = 1
        
    def clean_text_for_single_line(self, text: str) -> str:
        """Clean text for single-line fields according to StrictDoc grammar."""
        # Remove leading/trailing whitespace
        text = text.strip()
        
        # Ensure it starts with a non-space character (grammar requirement)
        if not text or text[0].isspace():
            text = text.lstrip()
            if not text:
                text = "No content provided"
        
        # Remove any newlines and excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove markdown table formatting that causes RST parsing errors
        # Remove pipe characters and table separators
        text = re.sub(r'\|\s*', '', text)  # Remove leading pipes
        text = re.sub(r'\s*\|', '', text)  # Remove trailing pipes
        text = re.sub(r'[-|]+\s*', '', text)  # Remove table separator lines
        
        # Clean up any remaining pipe characters
        text = text.replace('|', ' ')
        
        # Remove incomplete code blocks that cause RST parsing errors
        # Remove any text that starts with backticks but doesn't have proper closing
        text = re.sub(r'```[a-zA-Z]*\s*$', '', text)  # Remove incomplete opening code blocks
        text = re.sub(r'^\s*```\s*$', '', text)  # Remove standalone closing backticks
        
        # Remove any remaining backticks that might cause issues
        text = text.replace('```', '')
        text = text.replace('`', '')
        
        # Remove excessive whitespace again
        text = re.sub(r'\s+', ' ', text)
        
        # Final check: ensure the field is not empty
        if not text.strip():
            text = "No content provided"
        
        return text
    
    def clean_text_for_multiline(self, text: str) -> str:
        """Clean text for multiline fields according to StrictDoc grammar."""
        # Remove leading/trailing whitespace
        text = text.strip()
        
        # Ensure it starts with a non-space character
        if not text or text[0].isspace():
            text = text.lstrip()
            if not text:
                text = "No content provided"
        
        # Remove excessive whitespace but preserve structure
        lines = text.split('\n')
        cleaned_lines = []
        for line in lines:
            # Remove leading list markers and excessive indentation
            line = re.sub(r'^[\s]*[-*+]\s*', '', line)
            line = line.strip()
            if line:
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def extract_headings_from_html(self, html_content: str) -> List[Dict[str, Any]]:
        """Extract headings and content from HTML using BeautifulSoup."""
        soup = BeautifulSoup(html_content, 'html.parser')
        headings = []
        
        # Find all heading tags (h1-h6)
        for heading_tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            heading_text = heading_tag.get_text(strip=True)
            if not heading_text:
                continue
                
            # Get content following this heading until the next heading
            content = []
            current = heading_tag.next_sibling
            
            while current and not (hasattr(current, 'name') and current.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                if hasattr(current, 'get_text'):
                    text = current.get_text(strip=True)
                    if text:
                        content.append(text)
                elif isinstance(current, str) and current.strip():
                    content.append(current.strip())
                current = current.next_sibling
            
            headings.append({
                'title': heading_text,
                'content': ' '.join(content) if content else heading_text,
                'level': int(heading_tag.name[1])
            })
        
        return headings
    
    def extract_headings_from_markdown(self, md_content: str) -> List[Dict[str, Any]]:
        """Extract headings and content from Markdown."""
        headings = []
        lines = md_content.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Check for heading patterns (# ## ### etc.)
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if heading_match:
                level = len(heading_match.group(1))
                title = heading_match.group(2).strip()
                
                # Collect content until next heading
                content_lines = []
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()
                    if re.match(r'^(#{1,6})\s+', next_line):
                        break
                    if next_line:
                        content_lines.append(next_line)
                    j += 1
                
                content = ' '.join(content_lines) if content_lines else title
                
                headings.append({
                    'title': title,
                    'content': content,
                    'level': level
                })
            
            i += 1
        
        return headings
    
    def create_requirement_block(self, heading: Dict[str, Any], source_file: str) -> str:
        """Create a properly formatted REQUIREMENT block following StrictDoc grammar."""
        uid = f"REQ-{self.requirement_counter:03d}"
        self.requirement_counter += 1
        
        # Clean the title for single-line field
        title = self.clean_text_for_single_line(heading['title'])
        
        # Clean the content for single-line field (truncate if too long)
        content = self.clean_text_for_single_line(heading['content'])
        
        # Truncate content if it's too long for a single line
        if len(content) > 500:
            content = content[:497] + "..."
        
        # Build the block as a list of lines to guarantee correct newlines
        lines = [
            "[REQUIREMENT]",
            f"UID: {uid}",
            "STATUS: Draft",
            f"TITLE: {title}",
            f"STATEMENT: {content}",
            f"RATIONALE: Converted from {source_file} heading."
        ]
        return '\n'.join(lines)
    
    def convert_html_to_strictdoc(self, html_file: Path, output_file: Path) -> None:
        """Convert HTML file to StrictDoc format."""
        print(f"Converting {html_file} to {output_file}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract headings and content
        headings = self.extract_headings_from_html(html_content)
        
        if not headings:
            print(f"Warning: No headings found in {html_file}")
            return
        
        # Create document header with grammar definition
        doc_title = html_file.stem
        strictdoc_content = f"""[DOCUMENT]
TITLE: {doc_title}

[GRAMMAR]
ELEMENTS:
- TAG: REQUIREMENT
  FIELDS:
  - TITLE: UID
    TYPE: String
    REQUIRED: True
  - TITLE: STATUS
    TYPE: String
    REQUIRED: True
  - TITLE: TITLE
    TYPE: String
    REQUIRED: True
  - TITLE: STATEMENT
    TYPE: String
    REQUIRED: True
  - TITLE: RATIONALE
    TYPE: String
    REQUIRED: True

"""
        
        # Add requirements for each heading
        for heading in headings:
            requirement_block = self.create_requirement_block(heading, html_file.name)
            strictdoc_content += requirement_block + "\n\n"
        
        # Write the StrictDoc file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(strictdoc_content)
        
        print(f"Created {output_file} with {len(headings)} requirements")
    
    def convert_markdown_to_strictdoc(self, md_file: Path, output_file: Path) -> None:
        """Convert Markdown file to StrictDoc format."""
        print(f"Converting {md_file} to {output_file}")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Extract headings and content
        headings = self.extract_headings_from_markdown(md_content)
        
        if not headings:
            print(f"Warning: No headings found in {md_file}")
            return
        
        # Create document header with grammar definition
        doc_title = md_file.stem
        strictdoc_content = f"""[DOCUMENT]
TITLE: {doc_title}

[GRAMMAR]
ELEMENTS:
- TAG: REQUIREMENT
  FIELDS:
  - TITLE: UID
    TYPE: String
    REQUIRED: True
  - TITLE: STATUS
    TYPE: String
    REQUIRED: True
  - TITLE: TITLE
    TYPE: String
    REQUIRED: True
  - TITLE: STATEMENT
    TYPE: String
    REQUIRED: True
  - TITLE: RATIONALE
    TYPE: String
    REQUIRED: True

"""
        
        # Add requirements for each heading
        for heading in headings:
            requirement_block = self.create_requirement_block(heading, md_file.name)
            strictdoc_content += requirement_block + "\n\n"
        
        # Write the StrictDoc file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(strictdoc_content)
        
        print(f"Created {output_file} with {len(headings)} requirements")
    
    def convert_all_files(self) -> None:
        """Convert all HTML and Markdown files to StrictDoc format."""
        # Reset counter for each conversion run
        self.requirement_counter = 1
        
        # Convert HTML files
        html_dir = Path("html")
        strictdoc_html_dir = Path("strictdoc_html")
        strictdoc_html_dir.mkdir(exist_ok=True)
        
        for html_file in html_dir.glob("*.html"):
            output_file = strictdoc_html_dir / f"{html_file.stem}.html.sdoc"
            self.convert_html_to_strictdoc(html_file, output_file)
        
        # Reset counter for markdown conversion
        self.requirement_counter = 1
        
        # Convert Markdown files
        md_dir = Path("md")
        strictdoc_md_dir = Path("strictdoc_md")
        strictdoc_md_dir.mkdir(exist_ok=True)
        
        for md_file in md_dir.glob("*.md"):
            output_file = strictdoc_md_dir / f"{md_file.stem}.md.sdoc"
            self.convert_markdown_to_strictdoc(md_file, output_file)


def get_document_mapping() -> Dict[str, str]:
    """Get mapping of document codes to full names."""
    return {
        "COM": "Software Component Design Document (SCDD)",
        "CPM": "Computer Program Manual (CPM)",
        "DBDD": "Database Design Document (DBDD)",
        "ICD": "Interface Control Document (ICD)",
        "IDD": "Interface Design Document (IDD)",
        "IRS": "Interface Requirements Specification (IRS)",
        "PIDS": "Product Interface Design Specification (PIDS)",
        "PRS": "Product Requirements Specification (PRS)",
        "SDP": "Software Development Plan (SDP)",
        "SIP": "Software Installation Plan (SIP)",
        "SIVP": "Software Integration Test Plan (SIVP)",
        "SIVR": "Software Integration Test Report (SIVR)",
        "SMP": "Software Maintenance Plan (SMP)",
        "SOO": "Statement of Objectives (SOO)",
        "SOW": "Statement of Work (SOW)",
        "SPMP": "Software Project Management Plan (SPMP)",
        "SRS": "Software Requirements Specification (SRS)",
        "SSDD": "Software System Design Document (SSDD)",
        "STP": "Software Test Plan (STP)",
        "STR": "Software Test Report (STR)",
        "SVVP": "Software Verification and Validation Plan (SVVP)",
        "SVVR": "Software Verification and Validation Report (SVVR)",
        "SWS": "Software Specification (SWS)",
        "SIOM": "Software Input/Output Manual (SIOM)",
        "SUM": "Software User Manual (SUM)",
    }


def main():
    """Main conversion function."""
    converter = StrictDocConverter()
    converter.convert_all_files()
    print("Conversion completed!")
    
    # Create index file
    create_index_file()


def create_index_file():
    """Create an index file listing all converted documents."""
    index_content = """# MIL-STD-498 StrictDoc Documents Index

This index lists all MIL-STD-498 documents converted to StrictDoc format.

## Document Categories

"""
    
    # Get document mapping
    doc_mapping = get_document_mapping()
    
    # List HTML-based conversions
    strictdoc_html_dir = Path("strictdoc_html")
    if strictdoc_html_dir.exists():
        index_content += "### HTML-based conversions (strictdoc_html):\n"
        for sdoc_file in sorted(strictdoc_html_dir.glob("*.sdoc")):
            base_name = sdoc_file.stem.replace('.html', '')
            full_name = doc_mapping.get(base_name, base_name)
            index_content += f"- [{full_name}]({sdoc_file})\n"
        index_content += "\n"
    
    # List Markdown-based conversions
    strictdoc_md_dir = Path("strictdoc_md")
    if strictdoc_md_dir.exists():
        index_content += "### Markdown-based conversions (strictdoc_md):\n"
        for sdoc_file in sorted(strictdoc_md_dir.glob("*.sdoc")):
            base_name = sdoc_file.stem.replace('.md', '')
            full_name = doc_mapping.get(base_name, base_name)
            index_content += f"- [{full_name} (MD)]({sdoc_file})\n"
        index_content += "\n"
    
    # Write index file
    with open("STRICTDOC_INDEX.md", 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print("Created STRICTDOC_INDEX.md")


if __name__ == "__main__":
    main() 