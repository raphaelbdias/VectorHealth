// data/corpusFiles.ts
export type CorpusFile = {
  family: string;          // "ohrs" | "ajcc" | "waittimes" etc
  chapter: string;         // e.g. "Chapter I – ALR"
  appendixCode?: string;   // "Appendix 1.33"
  path: string;            // relative path under corpus/
  label: string;           // nice human label
};

export const CORPUS_FILES: CorpusFile[] = [
  // OHRS core appendices
  {
    family: "ohrs",
    chapter: "OHRS Core",
    appendixCode: "Appendix A",
    path: "corpus/ohrs/Appendix_A_v12.docx",
    label: "OHRS Appendix A v12 – Functional Centre Accounts",
  },
  {
    family: "ohrs",
    chapter: "OHRS Core",
    appendixCode: "Appendix B",
    path: "corpus/ohrs/Appendix_B_v12.pdf",
    label: "OHRS Appendix B v12 – Balance Sheet Accounts",
  },
  {
    family: "ohrs",
    chapter: "OHRS Core",
    appendixCode: "Appendix C",
    path: "corpus/ohrs/Appendix_C_v12.pdf",
    label: "OHRS Appendix C v12 – Statistical Accounts",
  },
  {
    family: "ohrs",
    chapter: "OHRS Core",
    appendixCode: "Appendix D",
    path: "corpus/ohrs/Appendix_D_v12.pdf",
    label: "OHRS Appendix D v12 – Workload & Earned Hours",
  },
  {
    family: "ohrs",
    chapter: "OHRS Core",
    appendixCode: "Appendix 1.1",
    path: "corpus/ohrs/CCO_DBK_Appendix_1-1-2_MAR_22.xlsx",
    label: "OHRS Functional Centres (DBK 1-1-2)",
  },
  {
    family: "ohrs",
    chapter: "OHRS Core",
    appendixCode: "Appendix A",
    path: "corpus/ohrs/CCO_DBK_Appendix_A_SEP_25.xlsx",
    label: "MOHLTC Master Numbering System (DBK A)",
  },

  // AJCC / staging
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.26.1",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-26-1_APR10.xlsx",
    label: "AJCC 6 – Valid Cancer Stages for ICD-10-CA",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.26.2",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-26-2_APR10.pdf",
    label: "AJCC Sixth Edition – Improvements and Changes",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.29.1–1.29.2",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-29-1_APR_21.xls",
    label: "AJCC 6 Stage Validation – ICDO3/Site/Stage (1-29-1)",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.29.2",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-29-2_APR_21.xls",
    label: "AJCC 6 Stage Validation – Stage Table (1-29-2)",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.30.1",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-30-1_APR_21.xls",
    label: "AJCC 7 Stage Validation – Site Group (1-30-1)",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.30.3",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-30-3_APR_21.xls",
    label: "AJCC 7 Stage Validation – Stage (1-30-3)",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.30.2",
    path: "corpus/ajcc/CCO_DBK_Appendix_1_30-2_AUG14.xls",
    label: "AJCC 7 Stage Validation – ICDO3 (1-30-2)",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.31.1",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-31-1_APR_21.xlsx",
    label: "AJCC 8 – Chapter Key/Number & Description (1-31-1)",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.31.2",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-31-2_JUN_25.xlsx",
    label: "AJCC 8 – ICDO3 Topography/Histology vs Chapter (1-31-2)",
  },
  {
    family: "ajcc",
    chapter: "Chapter I – ALR / AJCC",
    appendixCode: "Appendix 1.31.3",
    path: "corpus/ajcc/CCO_DBK_Appendix_1-31-3_APR_21.xlsx",
    label: "AJCC 8 – Valid Cancer Stage by Chapter (1-31-3)",
  },

  // Then similar entries for:
  //  - corpus/icd (1-18, 1-24, 1-36, 1-3, etc.)
  //  - corpus/mis (1-15, 1-20, 1-21)
  //  - corpus/admin (1.13, 1.34, 1.4, Appendix B)
  //  - corpus/cco (1.9, 1.19, 1-43, etc.)
  //  - corpus/waittimes (1.33, 1.45, ALC, WTIS specs)
  //  - corpus/pathology (4.1, 4.2, 4.4a/b, SPCSM)
  //  - corpus/pet (13.x)
  //  - corpus/sso (12A–12G docs)
  //  - corpus/ndfp (3.1)
  //  - corpus/orrs (if you add those later)
];
