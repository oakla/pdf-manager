# PDF Manager

A collection of tools for managing PDFs. This project provides command-line utilities to perform various operations on PDF files.

## Features

### Title Synchronization
The primary tool synchronizes PDF titles with their filenames, making it easier to organize and identify PDF files.

## Installation

### Requirements
- Python 3.8 or higher
- pip

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

The main entry point is through the `pdf_manager.cli` module:

```bash
python -m pdf_manager.cli --help
```

### Sync PDF Titles

Use the `sync-titles` command to update PDF titles to match their filenames:

#### Sync specific files:
```bash
python -m pdf_manager.cli sync-titles file1.pdf file2.pdf file3.pdf
```

#### Sync all PDFs in a directory:
```bash
python -m pdf_manager.cli sync-titles --directory /path/to/pdfs
```

#### Sync all PDFs recursively:
```bash
python -m pdf_manager.cli sync-titles --directory /path/to/pdfs --recursive
```

### Examples

1. **Sync a single PDF file:**
   ```bash
   python -m pdf_manager.cli sync-titles important_document.pdf
   ```
   This will change the PDF's title metadata to "important_document"

2. **Sync all PDFs in current directory:**
   ```bash
   python -m pdf_manager.cli sync-titles --directory .
   ```

3. **Sync all PDFs in a directory tree:**
   ```bash
   python -m pdf_manager.cli sync-titles --directory /home/user/documents --recursive
   ```

## How It Works

The title synchronization tool:

1. **Reads PDF metadata** using the pypdf library
2. **Extracts the filename** (without extension) as the new title
3. **Updates the PDF's title metadata** while preserving other metadata
4. **Saves the changes** back to the original file

**Note:** The tool creates a temporary file during processing to ensure data safety, then replaces the original file only after successful processing.

## Project Structure

```
pdf-manager/
├── pdf_manager/
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # Command-line interface
│   └── title_sync.py        # Title synchronization functionality
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Project configuration
├── main.py                 # Alternative entry point
└── README.md              # This file
```

## Development

### Adding New Tools

To add new PDF management tools:

1. Create a new module in the `pdf_manager` package
2. Add the corresponding command to `cli.py`
3. Update this README with usage instructions

### Testing

Create test PDFs and run the tools to verify functionality:

```bash
# Create test directory
mkdir test_pdfs

# Run the sync tool
python -m pdf_manager.cli sync-titles --directory test_pdfs
```

## Dependencies

- **pypdf** (3.17.4+): For reading and writing PDF files
- **click** (8.1.7+): For creating the command-line interface

## Future Enhancements

Planned tools for this collection:
- PDF merging and splitting
- Metadata bulk editing
- Page manipulation (rotation, extraction)
- Text extraction and search
- Bookmark management

## License

This project is open source. See the project repository for license details.