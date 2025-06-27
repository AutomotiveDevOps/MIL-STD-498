# MIL-STD-498 StrictDoc Documents Index

This directory contains MIL-STD-498 document templates converted to StrictDoc format.

## Document Types

### HTML-based conversions:
- Software Requirements Specification (SRS.sdoc)
- Software Design Description (SDD.sdoc)
- Software Development Plan (SDP.sdoc)
- System/Subsystem Specification (SSS.sdoc)
- Software Test Plan (STP.sdoc)
- Software Test Report (STR.sdoc)
- Software Installation Plan (SIP.sdoc)
- Software Transition Plan (STRP.sdoc)
- Computer Operator Manual (COM.sdoc)
- Computer Program Manual (CPM.sdoc)
- Database Design Description (DBDD.sdoc)
- Firmware Support Manual (FSM.sdoc)
- Interface Design Description (IDD.sdoc)
- Interface Requirements Specification (IRS.sdoc)
- Operational Concept Description (OCD.sdoc)
- Software Configuration Management Plan (SCOM.sdoc)
- Software Input/Output Manual (SIOM.sdoc)
- Software Product Specification (SPS.sdoc)
- Software System Design Description (SSDD.sdoc)
- Software Transition Description (STD.sdoc)
- Software User Manual (SUM.sdoc)
- Software Version Description (SVD.sdoc)

### Markdown-based conversions:
- Software Requirements Specification (SRS_md.sdoc)
- Software Design Description (SDD_md.sdoc)
- Software Development Plan (SDP_md.sdoc)
- System/Subsystem Specification (SSS_md.sdoc)
- Software Test Plan (STP_md.sdoc)
- Software Test Report (STR_md.sdoc)
- Software Installation Plan (SIP_md.sdoc)
- Software Transition Plan (STRP_md.sdoc)
- Computer Operator Manual (COM_md.sdoc)
- Computer Program Manual (CPM_md.sdoc)
- Database Design Description (DBDD_md.sdoc)
- Firmware Support Manual (FSM_md.sdoc)
- Interface Design Description (IDD_md.sdoc)
- Interface Requirements Specification (IRS_md.sdoc)
- Operational Concept Description (OCD_md.sdoc)
- Software Configuration Management Plan (SCOM_md.sdoc)
- Software Input/Output Manual (SIOM_md.sdoc)
- Software Product Specification (SPS_md.sdoc)
- Software System Design Description (SSDD_md.sdoc)
- Software Transition Description (STD_md.sdoc)
- Software User Manual (SUM_md.sdoc)
- Software Version Description (SVD_md.sdoc)

## Conversion Information

- **Total documents**: 44
- **HTML conversions**: 22
- **Markdown conversions**: 22
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

## Notes

These are basic StrictDoc documents with document headers only. The content from the original HTML/Markdown files can be added as needed for specific projects.
