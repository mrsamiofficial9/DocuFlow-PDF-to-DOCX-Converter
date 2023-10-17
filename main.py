import PyPDF2
from docx import Document

pdf_file_name = input("Enter PDF file path: ")
output_docx_file_name = input("Enter output DOCX file name (including .docx extension): ")


doc = Document()

with open(pdf_file_name, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    for page in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page)
        text = page_obj.extract_text()

        
        doc.add_paragraph(text)


doc.save(output_docx_file_name)

print(f"Conversion completed. Text from PDF has been saved to {output_docx_file_name}.")
