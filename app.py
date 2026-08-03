import os
import gradio as gr
import requests
import pandas as pd
from pathlib import Path

from agent import GAIAAgent


DEFAULT_API_URL = "https://agents-course-unit4-scoring.hf.space"


def download_file(task_id, file_name):
    if not file_name:
        return None

    folder = Path("files")
    folder.mkdir(exist_ok=True)

    path = folder / file_name

    # Reuse downloaded files
    if path.exists():
        return str(path)

    url = f"{DEFAULT_API_URL}/files/{task_id}"

    response = requests.get(url, timeout=60)
    response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)

    return str(path)


def run_and_submit_all():

    api_url = DEFAULT_API_URL

    questions_url = f"{api_url}/questions"
    submit_url = f"{api_url}/submit"

    # -------------------------------------------------
    # HF Space information
    # -------------------------------------------------
    space_id = os.getenv("SPACE_ID")

    if space_id:
        agent_code = (
            f"https://huggingface.co/spaces/{space_id}/tree/main"
        )
    else:
        agent_code = "local"

    # IMPORTANT:
    # Replace this with your HF username if running locally.
    # When deployed as a Space, use OAuth username.
    username = os.getenv(
        "HF_USERNAME",
        "local_test"
    )

    # -------------------------------------------------
    # Initialize agent
    # -------------------------------------------------
    try:
        agent = GAIAAgent()

    except Exception as e:
        return (
            f"Agent initialization failed: {e}",
            pd.DataFrame()
        )


    # -------------------------------------------------
    # Fetch questions
    # -------------------------------------------------
    try:
        response = requests.get(
            questions_url,
            timeout=30
        )

        response.raise_for_status()

        questions_data = response.json()

    except Exception as e:
        return (
            f"Question download failed: {e}",
            pd.DataFrame()
        )


    results_log = []
    answers_payload = []


    # -------------------------------------------------
    # Run agent
    # -------------------------------------------------
    for item in questions_data:

        task_id = item.get("task_id")
        question = item.get("question")

        if not task_id or question is None:
            continue


        try:

            file_path = download_file(
                task_id,
                item.get("file_name")
            )


            answer = agent(
                question,
                file_path
            )


        except Exception as e:

            print(
                f"Task failed {task_id}: {e}"
            )

            # Do not submit exception text
            answer = ""


        answers_payload.append(
            {
                "task_id": task_id,
                "submitted_answer": answer
            }
        )


        results_log.append(
            {
                "Task ID": task_id,
                "Question": question,
                "Submitted Answer": answer
            }
        )


    if not answers_payload:

        return (
            "No answers generated.",
            pd.DataFrame(results_log)
        )


    # -------------------------------------------------
    # Submit
    # -------------------------------------------------

    submission_data = {
        "username": username.strip(),
        "agent_code": agent_code,
        "answers": answers_payload
    }


    try:

        response = requests.post(
            submit_url,
            json=submission_data,
            timeout=300
        )

        response.raise_for_status()

        result = response.json()


        status = (
            "Submission Successful!\n\n"
            f"User: {result.get('username')}\n"
            f"Score: {result.get('score')}%\n"
            f"Correct: "
            f"{result.get('correct_count')}/"
            f"{result.get('total_attempted')}\n"
            f"Message: {result.get('message')}"
        )


    except requests.exceptions.HTTPError as e:

        status = (
            f"Submission failed: "
            f"{e.response.status_code}\n"
            f"{e.response.text}"
        )


    except Exception as e:

        status = (
            f"Submission failed: {e}"
        )


    return (
        status,
        pd.DataFrame(results_log)
    )



# -------------------------------------------------
# Gradio UI
# -------------------------------------------------

with gr.Blocks() as demo:

    gr.Markdown(
        "# GAIA Agent Evaluation Runner"
    )


    run_button = gr.Button(
        "Run Evaluation & Submit"
    )


    status_output = gr.Textbox(
        label="Status",
        lines=8
    )


    results_table = gr.DataFrame(
        label="Results"
    )


    run_button.click(
        fn=run_and_submit_all,
        outputs=[
            status_output,
            results_table
        ]
    )



if __name__ == "__main__":

    demo.launch(
        debug=True,
        share=False
    )