# Doc Loaders

This directory contains various document loaders for the LangChain project. These loaders are designed to facilitate the loading and processing of different types of documents, such as PDFs, text files, and web content.

## Contents

- **Text_loader.py**: Loads text files.
- **app.py**: Main application file for document loading.
- **directoryloader.py**: Loads documents from a specified directory.
- **pdf_loader_test.py**: Test file for PDF loading functionality.
- **poem.txt**: A sample text file for testing.
- **webloader.py**: Loads content from web sources.

## Installation

To use these loaders, you need to have Python installed along with the following dependencies:

```bash
pip install langchain
pip install PyPDF2
pip install requests
```

## Usage

### Text Loader

To load a text file, you can use the `Text_loader.py` script. Here's an example:

```python
from Text_loader import load_text

text = load_text('poem.txt')
print(text)
```

### PDF Loader

For loading PDF files, refer to the `pdf_loader_test.py` file for examples on how to use the PDF loader.

### Web Loader

To load content from a web source, use the `webloader.py` script. Example:

```python
from webloader import load_web_content

content = load_web_content('https://example.com')
print(content)
```

## Additional Information

- Ensure that the necessary permissions are set for accessing files and web resources.
- For more detailed usage examples, refer to the individual loader files.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. 