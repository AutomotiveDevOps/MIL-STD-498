#!/usr/bin/env python3
"""
Convert MIL-STD-498 HTML and Markdown files to StrictDoc format.

This script reads HTML and Markdown files and converts them to StrictDoc (.sdoc) format
following the StrictDoc grammar rules.

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


class HTMLToStrictDocConverter:
    """Convert HTML files to StrictDoc format."""
    
    def __init__(self):
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0  # No line wrapping
        
    def extract_title_from_html(self, html_content: str) -> str:
        """Extract document title from HTML."""
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.get_text().strip()
        return "Untitled Document"
    
    def html_to_markdown(self, html_content: str) -> str:
        """Convert HTML to Markdown."""
        return self.h2t.handle(html_content)
    
    def clean_markdown(self, markdown_content: str) -> str:
        """Clean up markdown content for StrictDoc."""
        # Remove HTML comments
        markdown_content = re.sub(r'<!--.*?-->', '', markdown_content, flags=re.DOTALL)
        
        # Clean up excessive whitespace
        markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
        
        # Remove leading/trailing whitespace
        markdown_content = markdown_content.strip()
        
        return markdown_content
    
    def convert_html_to_strictdoc(self, html_file_path: str, output_dir: str) -> str:
        """Convert HTML file to StrictDoc format."""
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract title
        title = self.extract_title_from_html(html_content)
        
        # Convert to markdown
        markdown_content = self.html_to_markdown(html_content)
        markdown_content = self.clean_markdown(markdown_content)
        
        # Create StrictDoc content
        strictdoc_content = self.create_strictdoc_content(title, markdown_content)
        
        # Write to file
        base_name = Path(html_file_path).stem
        output_path = os.path.join(output_dir, f"{base_name}.sdoc")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(strictdoc_content)
        
        return output_path
    
    def create_strictdoc_content(self, title: str, content: str) -> str:
        """Create StrictDoc formatted content."""
        # Convert markdown content to StrictDoc sections
        sections = self.convert_markdown_to_sections(content)
        
        # Create StrictDoc document
        strictdoc_content = f"""[DOCUMENT]
TITLE: MIL-STD-498: {title}
UID: {title.upper().replace(' ', '_')}
VERSION: 1.0
DATE: 2024-12-19
CLASSIFICATION: UNCLASSIFIED

OPTIONS:
  ENABLE_MID: On
  MARKUP: RST
  AUTO_LEVELS: On
  LAYOUT: Default
  VIEW_STYLE: Simple
  NODE_IN_TOC: True

"""
        
        # Add sections
        for section in sections:
            strictdoc_content += section + "\n"
        
        return strictdoc_content
    
    def convert_markdown_to_sections(self, content: str) -> List[str]:
        """Convert markdown content to StrictDoc sections."""
        sections = []
        lines = content.split('\n')
        current_section = None
        current_content = []
        
        for line in lines:
            # Check if this is a heading
            if line.startswith('# '):
                # Save previous section if exists
                if current_section:
                    sections.append(self.create_section(current_section, current_content))
                
                # Start new section
                current_section = line[2:].strip()
                current_content = []
            elif line.startswith('## '):
                # Subsection - treat as content for now
                current_content.append(line)
            elif line.startswith('### '):
                # Sub-subsection - treat as content for now
                current_content.append(line)
            else:
                # Regular content
                current_content.append(line)
        
        # Add final section
        if current_section:
            sections.append(self.create_section(current_section, current_content))
        
        return sections
    
    def create_section(self, title: str, content: List[str]) -> str:
        """Create a StrictDoc section."""
        # Clean up content
        content_text = '\n'.join(content).strip()
        
        # Create section
        section = f"""[SECTION]
TITLE: {title}
{content_text}
[/SECTION]"""
        
        return section


class MarkdownToStrictDocConverter:
    """Convert Markdown files to StrictDoc format."""
    
    def convert_markdown_to_strictdoc(self, markdown_file_path: str, output_dir: str) -> str:
        """Convert Markdown file to StrictDoc format."""
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Extract title from first heading
        title = self.extract_title_from_markdown(markdown_content)
        
        # Clean content
        cleaned_content = self.clean_markdown_content(markdown_content)
        
        # Create StrictDoc content
        strictdoc_content = self.create_strictdoc_content(title, cleaned_content)
        
        # Write to file
        base_name = Path(markdown_file_path).stem.replace('.html', '')
        output_path = os.path.join(output_dir, f"{base_name}.sdoc")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(strictdoc_content)
        
        return output_path
    
    def extract_title_from_markdown(self, content: str) -> str:
        """Extract title from markdown content."""
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                return line[2:].strip()
        return "Untitled Document"
    
    def clean_markdown_content(self, content: str) -> str:
        """Clean markdown content for StrictDoc."""
        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        
        # Clean up excessive whitespace
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Remove leading/trailing whitespace
        content = content.strip()
        
        return content
    
    def create_strictdoc_content(self, title: str, content: str) -> str:
        """Create StrictDoc formatted content."""
        # Convert markdown content to StrictDoc sections
        sections = self.convert_markdown_to_sections(content)
        
        # Create StrictDoc document
        strictdoc_content = f"""[DOCUMENT]
TITLE: MIL-STD-498: {title}
UID: {title.upper().replace(' ', '_')}
VERSION: 1.0
DATE: 2024-12-19
CLASSIFICATION: UNCLASSIFIED

OPTIONS:
  ENABLE_MID: On
  MARKUP: RST
  AUTO_LEVELS: On
  LAYOUT: Default
  VIEW_STYLE: Simple
  NODE_IN_TOC: True

"""
        
        # Add sections
        for section in sections:
            strictdoc_content += section + "\n"
        
        return strictdoc_content
    
    def convert_markdown_to_sections(self, content: str) -> List[str]:
        """Convert markdown content to StrictDoc sections."""
        sections = []
        lines = content.split('\n')
        current_section = None
        current_content = []
        
        for line in lines:
            # Check if this is a heading
            if line.startswith('# '):
                # Save previous section if exists
                if current_section:
                    sections.append(self.create_section(current_section, current_content))
                
                # Start new section
                current_section = line[2:].strip()
                current_content = []
            elif line.startswith('## '):
                # Subsection - treat as content for now
                current_content.append(line)
            elif line.startswith('### '):
                # Sub-subsection - treat as content for now
                current_content.append(line)
            else:
                # Regular content
                current_content.append(line)
        
        # Add final section
        if current_section:
            sections.append(self.create_section(current_section, current_content))
        
        return sections
    
    def create_section(self, title: str, content: List[str]) -> str:
        """Create a StrictDoc section."""
        # Clean up content
        content_text = '\n'.join(content).strip()
        
        # Create section
        section = f"""[SECTION]
TITLE: {title}
{content_text}
[/SECTION]"""
        
        return section


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


def main():
    """Main conversion function."""
    # Create output directory
    output_dir = "strictdoc_documents"
    os.makedirs(output_dir, exist_ok=True)
    
    # Get document mapping
    doc_mapping = get_document_mapping()
    
    # Initialize converters
    html_converter = HTMLToStrictDocConverter()
    md_converter = MarkdownToStrictDocConverter()
    
    # Get all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    converted_files = []
    
    for html_file in sorted(html_files):
        base_name = Path(html_file).stem
        md_file = f"{html_file}.md"
        
        print(f"Processing {html_file}...")
        
        # Convert HTML to StrictDoc
        try:
            output_path = html_converter.convert_html_to_strictdoc(html_file, output_dir)
            converted_files.append(output_path)
            print(f"  ✓ Converted {html_file} -> {output_path}")
        except Exception as e:
            print(f"  ✗ Error converting {html_file}: {e}")
        
        # Convert Markdown to StrictDoc (if exists)
        if os.path.exists(md_file):
            try:
                output_path = md_converter.convert_markdown_to_strictdoc(md_file, output_dir)
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


if __name__ == "__main__":
    main() 