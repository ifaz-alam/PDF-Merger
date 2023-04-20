import os
from natsort import natsorted
from PyPDF2 import PdfReader, PdfMerger

def merge_pdfs():
    # Get all the PDF filenames in the PDFS directory
    pdf_dir = "Files"
    pdf_files = natsorted([f for f in os.listdir(pdf_dir) if f.endswith('.pdf')])

    # Create a PdfMerger object
    merger = PdfMerger()

    # Append each PDF to the PdfMerger object
    for pdf in pdf_files:
        merger.append(PdfReader(os.path.join(pdf_dir, pdf)), outline_item=pdf[:-4])
    output_file = input("Desired name of output file: ")
    # Write the merged PDF to a file
    with open(f"{output_file}.pdf", "wb") as output_file:
        merger.write(output_file)

    print("PDF files merged successfully!")

if __name__ == "__main__":
    merge_pdfs()
