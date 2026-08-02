import os
import requests

from config import (
    QUESTIONS_ENDPOINT,
    RANDOM_ENDPOINT,
    FILES_ENDPOINT,
    FILES_DIR,
)


def get_questions():
    response = requests.get(QUESTIONS_ENDPOINT)
    response.raise_for_status()
    return response.json()


def get_random_question():
    response = requests.get(RANDOM_ENDPOINT)
    response.raise_for_status()
    return response.json()


def download_attachment(task):
    """
    Download the attachment for a GAIA task if it exists.

    Returns:
        Local file path or None.
    """

    file_name = task.get("file_name")

    if not file_name:
        return None

    task_id = task["task_id"]

    response = requests.get(
        f"{FILES_ENDPOINT}/{task_id}",
        stream=True,
    )

    response.raise_for_status()

    local_path = os.path.join(FILES_DIR, file_name)

    with open(local_path, "wb") as f:
        for chunk in response.iter_content(8192):
            f.write(chunk)

    return local_path