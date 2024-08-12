# PDF Text Extraction 

## Prerequisites

To run the script successfully, you need to install the following dependencies:

1. **Poppler**: Required for converting PDF pages into images.
2. **Tesseract OCR**: Required for performing OCR on the images to extract text.

### 1. Installing Poppler

**Poppler** is a PDF rendering library that `pdf2image` uses to convert PDF pages to images.

#### On Linux
Install Poppler using your package manager:
***sudo apt-get install poppler-utils***

#### On macOS
Install Poppler using Homebrew:
***brew install poppler***

#### On Windows

1. Download the Poppler binaries from Poppler's official website.
2. Extract the contents and add the directory containing pdftoppm.exe to your system’s PATH environment variable.

### 2. Installing Tesseract OCR

**Tesseract OCR** is an open-source OCR engine used for extracting text from images.

#### On Linux
Install Tesseract OCR using your package manager:
***sudo apt-get install tesseract-ocr***
 
#### On macOS
Install Tesseract OCR using Homebrew:
***brew install tesseract***

#### On Windows
1. Download the Tesseract installer from the Tesseract GitHub releases page.
2. Run the installer and follow the setup instructions.
3. Optionally, add the Tesseract executable directory to your system's PATH environment variable.