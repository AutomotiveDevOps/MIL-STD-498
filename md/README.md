# MIL-STD-498 Documentation

This repository contains MIL-STD-498 (Military Standard 498) document templates in multiple formats. MIL-STD-498 is a United States military standard that defines the software development and documentation process for software systems.

## 📚 Documentation

### 🌐 Live Documentation Site
The documentation is automatically generated and published to GitHub Pages:
**https://automotivedevops.github.io/MIL-STD-498/**

The site includes:
- **Original MIL-STD-498 HTML Files**: All 22 original HTML templates
- **StrictDoc Generated HTML**: HTML files generated from StrictDoc (.sdoc) templates
- **Comprehensive Index**: Organized navigation with descriptions for each document type

### 📁 Repository Contents

- **22 HTML files**: Original MIL-STD-498 document templates
- **22 Markdown files**: Converted versions of the HTML files using Pandoc
- **44 StrictDoc files**: MIL-STD-498 documents converted to StrictDoc format
- **GitHub Actions workflow**: Automated documentation generation and deployment

### 📋 Document Types

| Abbreviation | Document Type | Original HTML | Markdown | StrictDoc |
|--------------|---------------|---------------|----------|-----------|
| SRS | Software Requirements Specification | ✅ | ✅ | ✅ |
| SDD | Software Design Description | ✅ | ✅ | ✅ |
| SDP | Software Development Plan | ✅ | ✅ | ✅ |
| SSS | System/Subsystem Specification | ✅ | ✅ | ✅ |
| STP | Software Test Plan | ✅ | ✅ | ✅ |
| STR | Software Test Report | ✅ | ✅ | ✅ |
| SIP | Software Installation Plan | ✅ | ✅ | ✅ |
| STRP | Software Transition Plan | ✅ | ✅ | ✅ |
| COM | Computer Operator Manual | ✅ | ✅ | ✅ |
| CPM | Computer Program Manual | ✅ | ✅ | ✅ |
| DBDD | Database Design Description | ✅ | ✅ | ✅ |
| FSM | Firmware Support Manual | ✅ | ✅ | ✅ |
| IDD | Interface Design Description | ✅ | ✅ | ✅ |
| IRS | Interface Requirements Specification | ✅ | ✅ | ✅ |
| OCD | Operational Concept Description | ✅ | ✅ | ✅ |
| SCOM | Software Configuration Management Plan | ✅ | ✅ | ✅ |
| SIOM | Software Input/Output Manual | ✅ | ✅ | ✅ |
| SPS | Software Product Specification | ✅ | ✅ | ✅ |
| SSDD | Software System Design Description | ✅ | ✅ | ✅ |
| STD | Software Transition Description | ✅ | ✅ | ✅ |
| SUM | Software User Manual | ✅ | ✅ | ✅ |
| SVD | Software Version Description | ✅ | ✅ | ✅ |

## 🚀 GitHub Pages Deployment

This repository uses GitHub Actions to automatically:
1. Generate HTML documentation from StrictDoc files
2. Copy original MIL-STD-498 HTML files
3. Create a comprehensive index page
4. Deploy everything to GitHub Pages

### Workflow Details

- **Trigger**: Push to `main`/`master` branch or manual dispatch
- **Build**: Uses Python 3.12 with `uv` package manager
- **Dependencies**: StrictDoc, BeautifulSoup4, html2text
- **Output**: Complete documentation site with navigation

## 🛠️ Local Development

### Prerequisites
- Python 3.12+
- `uv` package manager

### Setup
```bash
# Clone the repository
git clone https://github.com/AutomotiveDevOps/MIL-STD-498.git
cd MIL-STD-498

# Create virtual environment and install dependencies
uv venv
uv pip install strictdoc beautifulsoup4 html2text

# Generate HTML documentation locally
cd strictdoc_documents
uv run strictdoc export --formats=html --output-dir=../docs/ .
```

## 📖 Usage

### Viewing Documentation
- **Online**: Visit https://automotivedevops.github.io/MIL-STD-498/
- **Local**: Open `docs/index.html` in your browser after generation

### Using StrictDoc Files
The StrictDoc (.sdoc) files can be used with StrictDoc to generate various output formats:

```bash
# Generate HTML
strictdoc export --formats=html --output-dir=output/ .

# Generate PDF
strictdoc export --formats=pdf --output-dir=output/ .

# Generate ReqIF
strictdoc export --formats=reqif-spec --output-dir=output/ .
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

