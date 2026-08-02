from smolagents import tool
from pathlib import Path


@tool
def list_files(folder: str) -> str:
    """
    List files available inside a folder.

    Args:
        folder: The folder path to inspect.

    Returns:
        A list of files inside the folder.
    """

    try:
        files = []

        for file in Path(folder).rglob("*"):
            if file.is_file():
                files.append(str(file))

        if not files:
            return "No files found."

        return "\n".join(files)

    except Exception as e:
        return f"Error listing files: {e}"