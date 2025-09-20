"""Command line interface for PDF Manager."""

import click
from pathlib import Path
from typing import List
from .title_sync import sync_pdf_titles, find_pdf_files, update_pdf_title


@click.group()
@click.version_option()
def cli():
    """PDF Manager - A collection of tools for managing PDFs."""
    pass


@cli.command("sync-titles")
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--directory', '-d', type=click.Path(exists=True, file_okay=False),
              help='Directory containing PDF files to process')
@click.option('--recursive', '-r', is_flag=True, 
              help='Process PDFs recursively in subdirectories')
def sync_titles(files, directory, recursive):
    """Sync PDF titles to match their filenames.
    
    You can either specify individual PDF files or use --directory to process
    all PDFs in a directory.
    """
    pdf_files = []
    
    # Collect files from arguments
    for file_path in files:
        file_path = Path(file_path)
        if file_path.suffix.lower() == '.pdf':
            pdf_files.append(str(file_path))
        else:
            click.echo(f"Skipping non-PDF file: {file_path}")
    
    # Collect files from directory
    if directory:
        if recursive:
            dir_pdfs = [str(p) for p in Path(directory).rglob("*.pdf")]
        else:
            dir_pdfs = find_pdf_files(directory)
        pdf_files.extend(dir_pdfs)
    
    if not pdf_files:
        click.echo("No PDF files found to process.")
        return
    
    # Show files to be processed
    click.echo(f"Found {len(pdf_files)} PDF files to process:")
    for pdf_file in pdf_files:
        filename = Path(pdf_file).stem
        click.echo(f"  {pdf_file} -> title: '{filename}'")
    
    # Ask for confirmation
    if click.confirm('\nDo you want to proceed?'):
        success_count = sync_pdf_titles(pdf_files)
        click.echo(f"\nCompleted! Successfully updated {success_count} out of {len(pdf_files)} files.")
    else:
        click.echo("Operation cancelled.")


if __name__ == '__main__':
    cli()