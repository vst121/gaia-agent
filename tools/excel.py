from smolagents import tool
import pandas as pd


@tool
def read_excel(path: str) -> str:
    """
    Read an Excel workbook.

    Args:
        path: Local path to the Excel (.xlsx) file.

    Returns:
        The contents of the workbook as formatted text.
    """

    try:
        # Read all sheets
        sheets = pd.read_excel(path, sheet_name=None)

        output = []

        for sheet_name, df in sheets.items():
            output.append(f"=== Sheet: {sheet_name} ===")
            output.append(df.to_string(index=False))
            output.append("")

        return "\n".join(output)

    except Exception as e:
        return f"Error reading Excel file: {e}"