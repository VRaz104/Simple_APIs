import os
import sys
import tabula
import pandas as pd
def pdf_to_excel(pdf_path: str, excel_path: str) -> None:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    print(f"Extracting tables from: {pdf_path}")
    dfs = tabula.read_pdf(pdf_path, pages="all", guess=True, area='entire_page')
    if not dfs:
        print("No tables found in PDF.")
        return
    print(f"Writing {len(dfs)} tables to Excel: {excel_path}")
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        for i, df in enumerate(dfs, start=1):
            sheet_name = f"Table_{i}"
            sheet_name = sheet_name[:31]
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("Done.")
if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_pdf = sys.argv[1]
        output_excel = sys.argv[2]
    elif len(sys.argv) == 1:
        input_pdf = r"C:\Users\Razvan\Documents\PDF's\pdf-sample_0.pdf"
        output_excel = r"C:\Users\Razvan\Documents\PDF's\report.xlsx"
        print(f"Using default paths: {input_pdf} -> {output_excel}")
    else:
        print("Usage: python PDF_to_Excel_converter.py [input.pdf output.xlsx]")
        print("If no arguments provided, uses hardcoded paths")
        sys.exit(1)
    pdf_to_excel(input_pdf, output_excel)