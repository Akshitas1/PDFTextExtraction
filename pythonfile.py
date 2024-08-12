import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import pandas as pd
import re

def process_pdfs(input_pdf_folder, output_excel_path):
    # Define regex patterns to extract data
    patterns = {
        'Contract #': re.compile(r'Contract #: (\d+)'),
        'Beginning Balance': re.compile(r'Beginning Balance:.*?\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)'),
        'Amount Withdrawn': re.compile(r'Amount Withdrawn \(1\):.*?\$\(([\d,\.]+)\)'),
        'Interest Credited': re.compile(r'^Interest Credited:.*?\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)'),
        'Contract Value': re.compile(r'Contract Value \(2\):.*?\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)')
    }

    # Initialize list to hold all extracted data
    all_extracted_data = []

    # Process each PDF file in the input folder
    for pdf_filename in os.listdir(input_pdf_folder):
        if pdf_filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_pdf_folder, pdf_filename)
            image_path = os.path.join('data/image_folder', pdf_filename.replace('.pdf', '_first_page.png'))

            # Convert the first page of the PDF to an image
            images = convert_from_path(pdf_path, first_page=0, last_page=1)
            first_page_image = images[0]
            first_page_image.save(image_path)

            # Perform OCR on the image
            image = Image.open(image_path)
            extracted_text = pytesseract.image_to_string(image)
            

            # Split text into lines
            lines = extracted_text.split('\n')

            # Initialize a dictionary to hold the extracted values
            extracted_data = {}

            # Loop through each line and apply regex patterns
            for line in lines:
                for key, pattern in patterns.items():
                    match = pattern.search(line)
                    if match:
                        extracted_data[key] = match.group(1)
                        # Print matched data for debugging
                        ##print(f'{key}: {match.group(1)}')

            # Append extracted data to the list
            if extracted_data:
                all_extracted_data.append(extracted_data)

    # Convert the list of dictionaries to a DataFrame
    df_combined = pd.DataFrame(all_extracted_data)

    # Save combined DataFrame to Excel
    df_combined.to_excel(output_excel_path, index=False)

    print("Processing complete. Data saved to Excel file.")

if __name__ == '__main__':
    input_pdf_folder = 'data/pdf_folder'
    output_excel_path = 'cleaned_data_combined.xlsx'
    process_pdfs(input_pdf_folder, output_excel_path)
