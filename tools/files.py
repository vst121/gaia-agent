from smolagents import tool
from pathlib import Path
from pypdf import PdfReader
import pandas as pd


@tool
def read_text_file(path: str) -> str:
    """
    Read the contents of a text file.

    Args:
        path: The local file path of the text file to read.

    Returns:
        The text content of the file.
    """

    try:
        return Path(path).read_text(encoding="utf-8")

    except Exception as e:
        return f"Error reading file: {e}"


@tool
def read_pdf(path: str) -> str:
    """
    Extract text from a PDF document.

    Args:
        path: The local file path of the PDF document.

    Returns:
        The extracted text from the PDF.
    """

    try:
        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text

    except Exception as e:
        return f"Error reading PDF: {e}"


@tool
def read_csv(path: str) -> str:
    """
    Read data from a CSV file.

    Args:
        path: The local file path of the CSV file.

    Returns:
        The CSV contents converted into text.
    """

    try:
        df = pd.read_csv(path)
        return df.to_string()

    except Exception as e:
        return f"Error reading CSV: {e}"