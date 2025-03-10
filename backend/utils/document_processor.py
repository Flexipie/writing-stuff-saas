"""Document processing utilities for text extraction and chunking"""
import os
import uuid
import logging
import pypdf
from typing import List, Tuple, Optional
from io import BytesIO

# Set up logging
logger = logging.getLogger(__name__)

def extract_text_from_pdf(file_content: bytes) -> List[Tuple[int, str]]:
    """
    Extract text from a PDF file
    
    Args:
        file_content (bytes): Content of the PDF file
        
    Returns:
        List[Tuple[int, str]]: List of tuples containing page number and page text
    """
    try:
        pdf = pypdf.PdfReader(BytesIO(file_content))
        pages = []
        
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                pages.append((i + 1, text))  # Page numbers start from 1
            else:
                pages.append((i + 1, ""))  # Empty page
                
        return pages
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise e

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """
    Split text into chunks with overlap
    
    Args:
        text (str): Text to split
        chunk_size (int): Size of each chunk
        overlap (int): Overlap between chunks
        
    Returns:
        List[str]: List of text chunks
    """
    if not text:
        return []
    
    chunks = []
    start = 0
    
    while start < len(text):
        end = min(start + chunk_size, len(text))
        if end < len(text) and end - start == chunk_size:
            # Find the last period, comma, newline, or space to break at
            last_good_break = end
            for i in range(end - 1, start + chunk_size // 2, -1):
                if text[i] in ['.', ',', '\n', ' ']:
                    last_good_break = i + 1
                    break
            end = last_good_break
        
        chunks.append(text[start:end])
        start = end - overlap if end - overlap > start else end
        
        # If we can't make progress, prevent infinite loop
        if start >= len(text) or (start == end and end == len(text)):
            break
            
    return chunks

def process_document(file_content: bytes, file_type: str, 
                    chunk_size: int = 1000, overlap: int = 200) -> List[Tuple[int, str, int]]:
    """
    Process document content into chunks
    
    Args:
        file_content (bytes): Content of the file
        file_type (str): Type of the file (pdf, txt, etc.)
        chunk_size (int): Size of each chunk
        overlap (int): Overlap between chunks
        
    Returns:
        List[Tuple[int, str, int]]: List of tuples containing (page number, text chunk, chunk index)
    """
    chunks = []
    
    if file_type == 'pdf':
        pages = extract_text_from_pdf(file_content)
        chunk_index = 0
        
        for page_num, page_text in pages:
            page_chunks = chunk_text(page_text, chunk_size, overlap)
            for chunk in page_chunks:
                if chunk.strip():  # Only include non-empty chunks
                    chunks.append((page_num, chunk, chunk_index))
                    chunk_index += 1
    else:
        # For text files, treat as a single page
        text = file_content.decode('utf-8', errors='ignore')
        page_chunks = chunk_text(text, chunk_size, overlap)
        for i, chunk in enumerate(page_chunks):
            if chunk.strip():  # Only include non-empty chunks
                chunks.append((1, chunk, i))  # Page 1 for text files
                
    return chunks

def save_file_locally(file_content: bytes, user_id: int, filename: str) -> str:
    """
    Save file to local storage
    
    Args:
        file_content (bytes): Content of the file
        user_id (int): ID of the user
        filename (str): Original filename
        
    Returns:
        str: Path where the file was saved
    """
    # Create directory for user if it doesn't exist
    user_dir = os.path.join('uploads', str(user_id))
    os.makedirs(user_dir, exist_ok=True)
    
    # Save file
    file_path = os.path.join(user_dir, filename)
    with open(file_path, 'wb') as f:
        f.write(file_content)
        
    return file_path

def generate_chunk_id() -> str:
    """
    Generate a unique ID for a chunk
    
    Returns:
        str: Unique ID
    """
    return str(uuid.uuid4())
