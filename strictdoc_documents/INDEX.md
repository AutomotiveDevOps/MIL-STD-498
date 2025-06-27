# MIL-STD-498 StrictDoc Documents Index

This directory contains MIL-STD-498 document templates converted to StrictDoc format.

## Document Types

### HTML-based conversions:
- [Computer Operator Manual](strictdoc_documents/COM.sdoc)
- [Computer Program Manual](strictdoc_documents/CPM.sdoc)
- [Database Design Description](strictdoc_documents/DBDD.sdoc)
- [Firmware Support Manual](strictdoc_documents/FSM.sdoc)
- [Interface Design Description](strictdoc_documents/IDD.sdoc)
- [Interface Requirements Specification](strictdoc_documents/IRS.sdoc)
- [Operational Concept Description](strictdoc_documents/OCD.sdoc)
- [Software Configuration Management Plan](strictdoc_documents/SCOM.sdoc)
- [Software Design Description](strictdoc_documents/SDD.sdoc)
- [Software Development Plan](strictdoc_documents/SDP.sdoc)
- [Software Input/Output Manual](strictdoc_documents/SIOM.sdoc)
- [Software Installation Plan](strictdoc_documents/SIP.sdoc)
- [Software Product Specification](strictdoc_documents/SPS.sdoc)
- [Software Requirements Specification](strictdoc_documents/SRS.sdoc)
- [Software System Design Description](strictdoc_documents/SSDD.sdoc)
- [System/Subsystem Specification](strictdoc_documents/SSS.sdoc)
- [Software Transition Description](strictdoc_documents/STD.sdoc)
- [Software Test Plan](strictdoc_documents/STP.sdoc)
- [Software Test Report](strictdoc_documents/STR.sdoc)
- [Software Transition Plan](strictdoc_documents/STRP.sdoc)
- [Software User Manual](strictdoc_documents/SUM.sdoc)
- [Software Version Description](strictdoc_documents/SVD.sdoc)

### Markdown-based conversions:
- [Computer Operator Manual (MD)](strictdoc_documents/COM_md.sdoc)
- [Computer Program Manual (MD)](strictdoc_documents/CPM_md.sdoc)
- [Database Design Description (MD)](strictdoc_documents/DBDD_md.sdoc)
- [Firmware Support Manual (MD)](strictdoc_documents/FSM_md.sdoc)
- [Interface Design Description (MD)](strictdoc_documents/IDD_md.sdoc)
- [Interface Requirements Specification (MD)](strictdoc_documents/IRS_md.sdoc)
- [Operational Concept Description (MD)](strictdoc_documents/OCD_md.sdoc)
- [Software Configuration Management Plan (MD)](strictdoc_documents/SCOM_md.sdoc)
- [Software Design Description (MD)](strictdoc_documents/SDD_md.sdoc)
- [Software Development Plan (MD)](strictdoc_documents/SDP_md.sdoc)
- [Software Input/Output Manual (MD)](strictdoc_documents/SIOM_md.sdoc)
- [Software Installation Plan (MD)](strictdoc_documents/SIP_md.sdoc)
- [Software Product Specification (MD)](strictdoc_documents/SPS_md.sdoc)
- [Software Requirements Specification (MD)](strictdoc_documents/SRS_md.sdoc)
- [Software System Design Description (MD)](strictdoc_documents/SSDD_md.sdoc)
- [System/Subsystem Specification (MD)](strictdoc_documents/SSS_md.sdoc)
- [Software Transition Description (MD)](strictdoc_documents/STD_md.sdoc)
- [Software Test Plan (MD)](strictdoc_documents/STP_md.sdoc)
- [Software Transition Plan (MD)](strictdoc_documents/STRP_md.sdoc)
- [Software Test Report (MD)](strictdoc_documents/STR_md.sdoc)
- [Software User Manual (MD)](strictdoc_documents/SUM_md.sdoc)
- [Software Version Description (MD)](strictdoc_documents/SVD_md.sdoc)


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

