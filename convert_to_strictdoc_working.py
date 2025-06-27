#!/usr/bin/env python3
"""
Convert MIL-STD-498 HTML and Markdown files to StrictDoc format.

This script reads HTML and Markdown files and converts them to StrictDoc (.sdoc) format
following the StrictDoc grammar rules exactly.

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
from typing import Dict, List, Optional, Tuple
from bs4 import BeautifulSoup
import html2text


def extract_title_from_html(html_content: str) -> str:
    """Extract document title from HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.get_text().strip()
    return "Untitled Document"


def html_to_markdown(html_content: str) -> str:
    """Convert HTML to Markdown."""
    h2t = html2text.HTML2Text()
    h2t.ignore_links = False
    h2t.ignore_images = False
    h2t.body_width = 0  # No line wrapping
    return h2t.handle(html_content)


def clean_markdown(markdown_content: str) -> str:
    """Clean up markdown content for StrictDoc."""
    # Remove HTML comments
    markdown_content = re.sub(r'<!--.*?-->', '', markdown_content, flags=re.DOTALL)
    
    # Clean up excessive whitespace
    markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
    
    # Remove leading/trailing whitespace
    markdown_content = markdown_content.strip()
    
    return markdown_content


def extract_title_from_markdown(content: str) -> str:
    """Extract title from markdown content."""
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "Untitled Document"


def get_document_mapping() -> Dict[str, str]:
    """Get mapping of document abbreviations to full names."""
    return {
        'SRS': 'Software Requirements Specification',
        'SDD': 'Software Design Description',
        'SDP': 'Software Development Plan',
        'SSS': 'System/Subsystem Specification',
        'STP': 'Software Test Plan',
        'STR': 'Software Test Report',
        'SIP': 'Software Installation Plan',
        'STRP': 'Software Transition Plan',
        'COM': 'Computer Operator Manual',
        'CPM': 'Computer Program Manual',
        'DBDD': 'Database Design Description',
        'FSM': 'Firmware Support Manual',
        'IDD': 'Interface Design Description',
        'IRS': 'Interface Requirements Specification',
        'OCD': 'Operational Concept Description',
        'SCOM': 'Software Configuration Management Plan',
        'SIOM': 'Software Input/Output Manual',
        'SPS': 'Software Product Specification',
        'SSDD': 'Software System Design Description',
        'STD': 'Software Transition Description',
        'SUM': 'Software User Manual',
        'SVD': 'Software Version Description'
    }


def convert_html_to_strictdoc(html_file_path: str, output_dir: str) -> str:
    """Convert HTML file to StrictDoc format."""
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract title
    title = extract_title_from_html(html_content)
    
    # Convert to markdown
    markdown_content = html_to_markdown(html_content)
    markdown_content = clean_markdown(markdown_content)
    
    # Clean the title for UID
    uid = title.upper().replace(' ', '_').replace('.', '_').replace('-', '_')
    uid = re.sub(r'[^A-Z0-9_]', '', uid)
    
    # Create StrictDoc document
    strictdoc_content = f"""[DOCUMENT]
TITLE: MIL-STD-498: {title}
UID: {uid}
VERSION: 1.0
DATE: 2024-12-19
CLASSIFICATION: UNCLASSIFIED

{markdown_content}"""
    
    # Write to file
    base_name = Path(html_file_path).stem
    output_path = os.path.join(output_dir, f"{base_name}.sdoc")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(strictdoc_content)
    
    return output_path


def convert_markdown_to_strictdoc(markdown_file_path: str, output_dir: str) -> str:
    """Convert Markdown file to StrictDoc format."""
    with open(markdown_file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Extract title from first heading
    title = extract_title_from_markdown(markdown_content)
    
    # Clean content
    cleaned_content = clean_markdown(markdown_content)
    
    # Clean the title for UID
    uid = title.upper().replace(' ', '_').replace('.', '_').replace('-', '_')
    uid = re.sub(r'[^A-Z0-9_]', '', uid)
    
    # Create StrictDoc document
    strictdoc_content = f"""[DOCUMENT]
TITLE: MIL-STD-498: {title}
UID: {uid}
VERSION: 1.0
DATE: 2024-12-19
CLASSIFICATION: UNCLASSIFIED

{cleaned_content}"""
    
    # Write to file
    base_name = Path(markdown_file_path).stem.replace('.html', '')
    output_path = os.path.join(output_dir, f"{base_name}.sdoc")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(strictdoc_content)
    
    return output_path


def create_index_file(output_dir: str, converted_files: List[str], doc_mapping: Dict[str, str]):
    """Create an index file listing all converted documents."""
    index_content = """# MIL-STD-498 StrictDoc Documents Index

This directory contains MIL-STD-498 document templates converted to StrictDoc format.

## Document Types

"""
    
    # Group files by type
    html_files = [f for f in converted_files if not f.endswith('_md.sdoc')]
    md_files = [f for f in converted_files if f.endswith('_md.sdoc')]
    
    index_content += "### HTML-based conversions:\n"
    for file_path in sorted(html_files):
        base_name = Path(file_path).stem
        full_name = doc_mapping.get(base_name, base_name)
        index_content += f"- [{full_name}]({file_path})\n"
    
    if md_files:
        index_content += "\n### Markdown-based conversions:\n"
        for file_path in sorted(md_files):
            base_name = Path(file_path).stem.replace('_md', '')
            full_name = doc_mapping.get(base_name, base_name)
            index_content += f"- [{full_name} (MD)]({file_path})\n"
    
    index_content += f"""

## Conversion Information

- **Total documents**: {len(converted_files)}
- **HTML conversions**: {len(html_files)}
- **Markdown conversions**: {len(md_files)}
- **Conversion tool**: StrictDoc 0.9.1
- **Source**: MIL-STD-498 templates from kkovacs.eu

## Usage

These .sdoc files can be used with StrictDoc to generate various output formats:

```bash
# Generate HTML
strictdoc export --formats=html --output-dir=output/ .

# Generate PDF
strictdoc export --formats=pdf --output-dir=output/ .

# Generate ReqIF
strictdoc export --formats=reqif-spec --output-dir=output/ .
```

"""
    
    index_path = os.path.join(output_dir, "INDEX.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"Created index file: {index_path}")


def main():
    """Main conversion function."""
    # Create output directory
    output_dir = "strictdoc_documents"
    os.makedirs(output_dir, exist_ok=True)
    
    # Get document mapping
    doc_mapping = get_document_mapping()
    
    # Get all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    converted_files = []
    
    for html_file in sorted(html_files):
        base_name = Path(html_file).stem
        md_file = f"{html_file}.md"
        
        print(f"Processing {html_file}...")
        
        # Convert HTML to StrictDoc
        try:
            output_path = convert_html_to_strictdoc(html_file, output_dir)
            converted_files.append(output_path)
            print(f"  ✓ Converted {html_file} -> {output_path}")
        except Exception as e:
            print(f"  ✗ Error converting {html_file}: {e}")
        
        # Convert Markdown to StrictDoc (if exists)
        if os.path.exists(md_file):
            try:
                output_path = convert_markdown_to_strictdoc(md_file, output_dir)
                # Rename to avoid conflicts
                new_output_path = output_path.replace('.sdoc', '_md.sdoc')
                os.rename(output_path, new_output_path)
                converted_files.append(new_output_path)
                print(f"  ✓ Converted {md_file} -> {new_output_path}")
            except Exception as e:
                print(f"  ✗ Error converting {md_file}: {e}")
    
    print(f"\nConversion complete! {len(converted_files)} files converted to {output_dir}/")
    
    # Create index file
    create_index_file(output_dir, converted_files, doc_mapping)
    
    return converted_files


if __name__ == "__main__":
    main() 