# MIL-STD-498 Documentation Repository

This repository contains a complete collection of MIL-STD-498 (Military Standard 498) document templates in multiple formats. MIL-STD-498 is a United States military standard that defines the software development and documentation process for software systems.

## 🌐 Live Documentation Site

The documentation is automatically generated and published to GitHub Pages: **[https://automotivedevops.github.io/MIL-STD-498/](https://automotivedevops.github.io/MIL-STD-498/)**

## 📁 Repository Structure

### Source Documents

- **`html/`** - Original MIL-STD-498 HTML templates (22 files)
  - Source templates from [kkovacs.eu](http://kkovacs.eu/free-project-management-template-mil-std-498)
  - Well-structured XHTML 1.0 Transitional format
  - Consistent document structure across all templates

- **`md/`** - Markdown versions of HTML templates (22 files)
  - Converted from HTML using Pandoc
  - Maintains document structure and hierarchy
  - Some formatting artifacts from HTML conversion

### StrictDoc Generated Files

- **`strictdoc_md/`** - StrictDoc (.sdoc) files generated from Markdown sources (22 files)
  - Each Markdown heading becomes a separate `[REQUIREMENT]` block
  - Proper grammar compliance with StrictDoc specification
  - Generated HTML: `https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/`

- **`strictdoc_html/`** - StrictDoc (.sdoc) files generated from HTML sources (22 files)
  - Each HTML heading becomes a separate `[REQUIREMENT]` block
  - Proper grammar compliance with StrictDoc specification
  - Generated HTML: `https://automotivedevops.github.io/MIL-STD-498/strictdoc_html/html/strictdoc_html/`

### Legacy Files

- **`strictdoc_documents/`** - Legacy StrictDoc files (22 files)
  - Older conversion format (not actively maintained)
  - Contains `.md.sdoc` files from previous conversion attempts

### Output Directories

- **`final_output/`** - HTML output from Markdown-based StrictDoc files
- **`final_output_html/`** - HTML output from HTML-based StrictDoc files
- **`test_output/`** - Test HTML output for validation
- **`output/`** - Legacy output directory

## 📋 Document Types

### Requirements Documents
- **[SRS](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SRS.html.md.html)** - Software Requirements Specification
  - Defines software requirements and acceptance criteria
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SRS.html)

- **[SSS](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SSS.html.md.html)** - System/Subsystem Specification
  - System-level requirements and specifications
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SSS.html)

- **[IRS](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/IRS.html.md.html)** - Interface Requirements Specification
  - Interface requirements between system components
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/IRS.html)

### Design Documents
- **[SDD](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SDD.html.md.html)** - Software Design Description
  - Software architectural and detailed design
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SDD.html)

- **[SSDD](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SSDD.html.md.html)** - System/Subsystem Design Description
  - System-level design descriptions
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SSDD.html)

- **[IDD](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/IDD.html.md.html)** - Interface Design Description
  - Interface design specifications
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/IDD.html)

- **[DBDD](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/DBDD.html.md.html)** - Database Design Description
  - Database design and structure
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/DBDD.html)

### Planning Documents
- **[SDP](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SDP.html.md.html)** - Software Development Plan
  - Comprehensive software development planning
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SDP.html)

- **[STP](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/STP.html.md.html)** - Software Test Plan
  - Software testing strategy and procedures
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/STP.html)

- **[SIP](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SIP.html.md.html)** - Software Installation Plan
  - Software installation procedures
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SIP.html)

- **[SCOM](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SCOM.html.md.html)** - Software Configuration Management Plan
  - Configuration management planning
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SCOM.html)

### Testing Documents
- **[STR](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/STR.html.md.html)** - Software Test Report
  - Test execution results and reports
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/STR.html)

### User Documentation
- **[COM](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/COM.html.md.html)** - Computer Operator Manual
  - Computer system operation manual
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/COM.html)

- **[CPM](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/CPM.html.md.html)** - Computer Program Manual
  - Computer program usage manual
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/CPM.html)

- **[SUM](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SUM.html.md.html)** - Software User Manual
  - Software user manual
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SUM.html)

- **[SIOM](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SIOM.html.md.html)** - Software Input/Output Manual
  - Input/output procedures manual
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SIOM.html)

### Transition & Installation
- **[STRP](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/STRP.html.md.html)** - Software Transition Plan
  - Software transition planning
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/STRP.html)

- **[SVD](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SVD.html.md.html)** - Software Version Description
  - Version description and release notes
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SVD.html)

### Support Documentation
- **[FSM](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/FSM.html.md.html)** - Firmware Support Manual
  - Firmware support procedures
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/FSM.html)

- **[OCD](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/OCD.html.md.html)** - Operational Concept Description
  - Operational concept descriptions
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/OCD.html)

### Additional Documents
- **[SPS](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/SPS.html.md.html)** - Software Product Specification
  - Software product specifications
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/SPS.html)

- **[STD](https://automotivedevops.github.io/MIL-STD-498/strictdoc_md/html/strictdoc_md/STD.html.md.html)** - Software Transition Document
  - Software transition documentation
  - Original: [HTML](https://automotivedevops.github.io/MIL-STD-498/original_html/STD.html)

## 🚀 GitHub Pages Deployment

This repository uses GitHub Actions to automatically:

1. **Generate HTML documentation** from StrictDoc files
2. **Copy original MIL-STD-498 HTML files**
3. **Create a comprehensive index page** with navigation
4. **Deploy everything to GitHub Pages**

### Workflow Details
- **Trigger**: Push to `master` branch or manual dispatch
- **Build**: Uses Python 3.12 with StrictDoc
- **Dependencies**: StrictDoc, BeautifulSoup4, html2text
- **Output**: Complete documentation site with navigation

## 🛠️ Local Development

### Prerequisites
- Python 3.12+
- Virtual environment (recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/AutomotiveDevOps/MIL-STD-498.git
cd MIL-STD-498

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install strictdoc beautifulsoup4 html2text

# Generate HTML documentation locally
python3 convert_to_strictdoc_final.py
venv/bin/strictdoc export --formats=html --output-dir=docs/ strictdoc_md/
```

## 📖 Usage

### Viewing Documentation
- **Online**: Visit [https://automotivedevops.github.io/MIL-STD-498/](https://automotivedevops.github.io/MIL-STD-498/)
- **Local**: Open `docs/index.html` in your browser after generation

### Using StrictDoc Files
The StrictDoc (.sdoc) files can be used with StrictDoc to generate various output formats:

```bash
# Generate HTML
venv/bin/strictdoc export --formats=html --output-dir=output/ strictdoc_md/

# Generate PDF
venv/bin/strictdoc export --formats=pdf --output-dir=output/ strictdoc_md/

# Generate ReqIF
venv/bin/strictdoc export --formats=reqifspec --output-dir=output/ strictdoc_md/
```

## 🔄 Automation

The repository includes automated workflows for:
- **Documentation Generation**: Converts StrictDoc files to HTML
- **GitHub Pages Deployment**: Publishes documentation automatically
- **Index Generation**: Creates comprehensive navigation

## 📄 License

This project contains MIL-STD-498 templates. Please refer to the original MIL-STD-498 standard for licensing information.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For questions or issues, please open an issue on GitHub.

## 📚 Source Attribution

- **Original HTML**: Sourced from [kkovacs.eu](http://kkovacs.eu/free-project-management-template-mil-std-498)
- **Markdown conversion**: Performed using [Pandoc](http://johnmacfarlane.net/pandoc/)
- **Standard reference**: [MIL-STD-498 on Wikipedia](https://en.wikipedia.org/wiki/MIL-STD-498)
- **StrictDoc**: [StrictDoc Documentation](https://strictdoc.readthedocs.io/)

## 📊 Repository Status

- **Current state**: Clean working tree, all changes committed
- **Documentation**: Complete set of MIL-STD-498 templates
- **Formats**: HTML, Markdown, and StrictDoc versions available
- **Maintenance**: Repository is stable and well-maintained
- **Automation**: Fully automated documentation generation and deployment 