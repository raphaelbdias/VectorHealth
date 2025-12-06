// data/appendices.ts
export type AppendixItem = {
  code: string;        // e.g. "Appendix 1.33"
  title: string;       // e.g. "Wait Times Definitions"
  chapter: string;     // e.g. "Chapter I – ALR"
  notes?: string;      // optional extra info if needed later
};

export const APPENDICES: AppendixItem[] = [
  // Chapter I – ALR
  { code: "Appendix A", title: "MOHLTC Master Numbering System", chapter: "Chapter I – ALR" },
  { code: "Appendix B", title: "Province and State codes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.1", title: "OHRS Functional Centres", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.3", title: "ICDO3 TOPOGRAPHY with Laterality", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.4", title: "Province issuing HCN", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.5", title: "ICD10CA to ICD03", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.9", title: "CCO Staging Guidelines", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.10", title: "ICDO3 Stage Validation Table with valid Group Stage Values AJCC 6th ed.", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.11", title: "TNM Staging Fact Sheet", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.13", title: "Responsibility for Payment Codes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.14", title: "NHPIP Code List", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.15", title: "Body Region Codes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.16", title: "Analytic Case Flag", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.17", title: "HCP Specialty code list", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.18", title: "ICD10CA Master Code/Description list", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.18.1", title: "ICD10CA Diagnosis Codes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.18.2", title: "ICD10CA New and Deactivated Codes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.19", title: "Treatment Intent", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.20", title: "Measurement Units", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.21", title: "Systemic Treatment Routes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.22", title: "CCO Regimen and NCT List", chapter: "Chapter I – ALR" },
  { code: "Appendix 1-22-1", title: "CCO Regimen Codes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1-22-2", title: "Formulary Regimen NCT", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.23", title: "Basis of Diagnosis", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.24", title: "Diagnosis / Gender Incompatibilities Validation table", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.26", title: "Valid AJCC 6 Cancer Stages for ICD10CA", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.26.1", title: "AJCC Validation Table", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.26.2", title: "AJCC Sixth Edition Staging Manual Improvements and Changes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.27", title: "ICDO3 Topography/Gender Incompatibilities", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.28", title: "ICDO3 Topography/Morphology Incompatibilities", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.29", title: "AJCC 6 Stage validation tables", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.29.1", title: "Valid Cancer Stage - ICD03", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.29.2", title: "Valid Cancer Stage – Stage", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.30", title: "AJCC 7 Stage validation tables", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.30.1", title: "Valid Cancer Stage ICDO3 - Site Group Code And Description", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.30.2", title: "Valid Cancer Stage - ICD03", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.30.3", title: "Valid Cancer Stage - Stage", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.31", title: "AJCC 8 - Stage Validation Tables", chapter: "Chapter I – ALR" },
  { code: "Appendix 1-31-1", title: "AJCCv8 Stage Chapter Key/Number and Description", chapter: "Chapter I – ALR" },
  { code: "Appendix 1-31-2", title: "ICDO3 Topography/Histology and AJCCv8 Chapter Key/Number", chapter: "Chapter I – ALR" },
  { code: "Appendix 1-31-3", title: "AJCCv8 Chapter Key/Number and Valid Cancer Stage", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.33", title: "Wait Times Definitions", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.34", title: "Reporting Facilities", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.36", title: "ICDO3 Morphology Codes", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.38", title: "Non-IV Drug List for Systemic Therapy", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.39", title: "Clinical Practice Group Mapping", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.40", title: "ALR activity by Reporting Facility", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.42", title: "Radiation Incident Reporting", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.43", title: "STFM Drug Classification - Antineoplastic and Supportive Drug list", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.45", title: "PSO Wait Time Data Collection Resource Guide", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.46", title: "Radiation Treatment (RT) Protocol", chapter: "Chapter I – ALR" },
  { code: "Appendix 1.47", title: "T Suffix m-value Coding Details AJCC 8th edition", chapter: "Chapter I – ALR" },

  // Chapter IIC – WTIS
  { code: "WTIS – ALC Reference Manual", title: "ALC Reference Manual", chapter: "Chapter IIC – WTIS" },
  { code: "WTIS – Surgery Data Standardization Guide", title: "Surgery Data Standardization Guide", chapter: "Chapter IIC – WTIS" },
  { code: "WTIS – DI Guide", title: "Diagnostic Imaging Wait Time and Efficiencies Data Standardization Guide", chapter: "Chapter IIC – WTIS" },
  { code: "WTIS – HL7 (ALC/DI/Surgery)", title: "Complex HL7 Specifications (ALC, DI MRICT, Surgery)", chapter: "Chapter IIC – WTIS" },

  // Chapter III – NDFP
  { code: "Appendix 3.1", title: "NDFP/EBP Policies", chapter: "Chapter III – NDFP" },

  // Chapter IV – ePath
  { code: "Appendix 4.1", title: "CAP electronic Cancer Checklists", chapter: "Chapter IV – ePath" },
  { code: "Appendix 4.2", title: "ePath Service Level Principles", chapter: "Chapter IV – ePath" },
  { code: "Appendix 4.3", title: "Country Codes", chapter: "Chapter IV – ePath" },
  { code: "Appendix 4.4a", title: "CCO Pathology Reporting Valid Institution Codes", chapter: "Chapter IV – ePath" },
  { code: "Appendix 4.4b", title: "CCO Pathology Reporting Obsolete Institution Codes", chapter: "Chapter IV – ePath" },

  // Chapter VI – Brachytherapy
  { code: "Chapter VI Appendix A", title: "MOHLTC Master Numbering System", chapter: "Chapter VI – Brachytherapy" },

  // Chapter IX – CCC
  { code: "GI Endoscopy DSP", title: "GI Endoscopy DSP Data Dictionary", chapter: "Chapter IX – Colon Cancer Check" },

  // Chapter X – Symptom Management
  { code: "Chapter X Appendix A", title: "MOHLTC Master Numbering System", chapter: "Chapter X – Symptom Management" },

  // Chapter XI – MCC
  { code: "Appendix 11.1", title: "Hospital Name and Region", chapter: "Chapter XI – MCC" },
  { code: "Appendix 11.2", title: "Disease Site", chapter: "Chapter XI – MCC" },

  // Chapter XII – SSOIS
  { code: "Appendix 12A", title: "SSO Stem Cell Transplant", chapter: "Chapter XII – SSOIS" },
  { code: "Appendix 12B", title: "SSO Sarcoma Chemotherapy", chapter: "Chapter XII – SSOIS" },
  { code: "Appendix 12C", title: "SSO Sarcoma Pathology", chapter: "Chapter XII – SSOIS" },
  { code: "Appendix 12D", title: "SSO Sarcoma Prosthesis", chapter: "Chapter XII – SSOIS" },
  { code: "Appendix 12F", title: "SSO Neuroendocrine", chapter: "Chapter XII – SSOIS" },
  { code: "Appendix 12G", title: "SSO Interventional Radiology", chapter: "Chapter XII – SSOIS" },

  // Chapter XIII – PET
  { code: "Appendix 13.1", title: "Topography Codes", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.2", title: "Histology Codes", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.3", title: "Valid Stage Group Values", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.4", title: "Valid Stage T Values", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.5", title: "Valid Stage N Values", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.6", title: "Valid Stage M Values", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.7", title: "Prior Imaging Studies", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.8", title: "Body Region", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.9", title: "Biomarkers", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.10", title: "Supporting Document File Types", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.11", title: "PET Centres", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.12", title: "Source of Radiopharmaceutical", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.13", title: "Active Insured and Registry Indications", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.14", title: "Insured Registry Pre Scan Indicator Specific Information", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.15", title: "Insured and Registry Post Scan Indicator Specific Information", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.16", title: "Physicians Specialty", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.17", title: "PET Access Status Valid Values", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.18", title: "PET Registry Status Valid Values", chapter: "Chapter XIII – PET" },
  { code: "Appendix 13.19", title: "Registry and Insured Physician Post Scan Indicator Specific Information", chapter: "Chapter XIII – PET" },

  // Chapter XIV – ORRS
  { code: "ORRS R8", title: "ORRS Release 8 Data Dictionary & Electronic Submission Specifications", chapter: "Chapter XIV – ORRS" },
];
