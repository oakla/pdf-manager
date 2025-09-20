"""Tool for synchronizing PDF titles with their filenames."""

import os
from pathlib import Path
from typing import List, Optional
from pypdf import PdfReader, PdfWriter
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def update_pdf_title(pdf_path: str, title: Optional[str] = None) -> bool:
    """
    Update the title metadata of a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        title: New title for the PDF. If None, uses the filename without extension.
        
    Returns:
        True if successful, False otherwise
    """
    try:
        pdf_path = Path(pdf_path)
        
        # Use filename without extension as title if not provided
        if title is None:
            title = pdf_path.stem
        
        # Read the existing PDF
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            writer = PdfWriter()
            
            # Copy all pages
            for page in reader.pages:
                writer.add_page(page)
            
            # Update metadata
            metadata = {}
            if reader.metadata:
                # Copy existing metadata
                for key, value in reader.metadata.items():
                    metadata[key] = value
            # Set the new title
            metadata['/Title'] = title
            writer.add_metadata(metadata)
            
            # Write to a temporary file first
            temp_path = pdf_path.with_suffix('.tmp.pdf')
            with open(temp_path, 'wb') as output_file:
                writer.write(output_file)
        
        # Replace the original file
        temp_path.replace(pdf_path)
        logger.info(f"Updated title of '{pdf_path}' to '{title}'")
        return True
        
    except Exception as e:
        logger.error(f"Failed to update title for '{pdf_path}': {e}")
        return False


def sync_pdf_titles(pdf_paths: List[str]) -> int:
    """
    Sync titles of multiple PDF files to match their filenames.
    
    Args:
        pdf_paths: List of paths to PDF files
        
    Returns:
        Number of successfully updated files
    """
    success_count = 0
    
    for pdf_path in pdf_paths:
        if update_pdf_title(pdf_path):
            success_count += 1
    
    logger.info(f"Successfully updated {success_count} out of {len(pdf_paths)} PDF files")
    return success_count


def find_pdf_files(directory: str) -> List[str]:
    """
    Find all PDF files in a directory.
    
    Args:
        directory: Directory path to search
        
    Returns:
        List of PDF file paths
    """
    directory_path = Path(directory)
    pdf_files = []
    
    if directory_path.is_dir():
        pdf_files = [str(p) for p in directory_path.glob("*.pdf")]
        logger.info(f"Found {len(pdf_files)} PDF files in '{directory}'")
    else:
        logger.error(f"Directory '{directory}' does not exist")
    
    return pdf_files