"""
From Prompting to Instruction Tuning - Student Template

Name: Mandi Schmuhl
Date: 10/25/2026

Instructions:
- Complete all TODO sections.
- Replace example outputs with YOUR actual results.
- Add at least ONE failure case.
- Be thoughtful in your analysis — this is the most important part.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class ExperimentResult:
    task_name: str
    prompt_type: str
    prompt_text: str
    model_output: str
    followed_instructions: bool
    notes: str


# -----------------------------
# PRINTING FUNCTIONS
# -----------------------------
def print_result(result: ExperimentResult) -> None:
    print("=" * 70)
    print(f"Task: {result.task_name}")
    print(f"Prompt Type: {result.prompt_type}")

    print("\nPrompt:")
    print(result.prompt_text)

    print("\nModel Output:")
    print(result.model_output)

    print(f"\nFollowed Instructions: {result.followed_instructions}")
    print(f"Notes: {result.notes}")
    print("=" * 70)
    print()


def compare_results(prompt_only: ExperimentResult, instruction_tuned: ExperimentResult) -> None:
    print("#" * 70)
    print(f"COMPARISON FOR TASK: {prompt_only.task_name}")
    print("#" * 70)

    print("\nPrompt-Only Output:")
    print(prompt_only.model_output)

    print("\nInstruction-Tuned Output:")
    print(instruction_tuned.model_output)

    print("\nAnalysis:")

    # TODO: Write your comparison analysis here
    if prompt_only.task_name == "Translation":
        print(
            "The instruction-tuned version followed the expected translation pattern more consistently. The examples helped reinforce the format of the response.")

    elif prompt_only.task_name == "Summarization":
        print(
            "The instruction-tuned version produced a shorter and more focused summary. The examples clarified the expected level of detail.")

    elif prompt_only.task_name == "Explain to a Child":
        print(
            "The instruction-tuned version used simpler language and was more appropriate for a young audience. The examples helped guide the style of the response.")

    print()


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main() -> None:
    results: List[ExperimentResult] = []

    # ===================================================
    # TASK 1 (REQUIRED)
    # ===================================================

    # TODO: Replace with your own prompt
    prompt_only_1 = ExperimentResult(
        task_name="Translation",
        prompt_type="Prompt-Only",
        prompt_text="Translate to Spanish: How are you?",
        model_output="¿Cómo estás?",
        followed_instructions=True,
        notes="The model correctly translated the phrase into Spanish."
    )

    instruction_1 = ExperimentResult(
        task_name="Translation",
        prompt_type="Instruction-Tuned",
        prompt_text=(
            "Instruction: Translate to Spanish\n"
            "Input: Hello\n"
            "Output: Hola\n\n"
            "Instruction: Translate to Spanish\n"
            "Input: Good morning\n"
            "Output: Buenos días\n\n"
            "Instruction: Translate to Spanish\n"
            "Input: How are you?\n"
            "Output:"
        ),
        model_output="¿Cómo estás?",
        followed_instructions=True,
        notes="The model followed the examples and produced the correct translation."
    )

    results.append(prompt_only_1)
    results.append(instruction_1)

    # ===================================================
    # TASK 2 (REQUIRED)
    # ===================================================

    prompt_only_2 = ExperimentResult(
        task_name="Summarization",
        prompt_type="Prompt-Only",
        prompt_text="Summarize this paragraph: Artificial intelligence is increasingly used by businesses to automate tasks, analyze large amounts of data, and improve customer service.",
        model_output="Businesses use AI to automate tasks, analyze data, and improve customer service.",
        followed_instructions=True,
        notes="The model created an accurate summary."
    )

    instruction_2 = ExperimentResult(
        task_name="Summarization",
        prompt_type="Instruction-Tuned",
        prompt_text="""
    Instruction: Summarize the paragraph in one sentence.

    Input:
    Dogs are loyal animals and are often considered human companions.

    Output:
    Dogs are loyal companions.

    Instruction: Summarize the paragraph in one sentence.

    Input:
    Artificial intelligence is increasingly used by businesses to automate tasks, analyze large amounts of data, and improve customer service.

    Output:
    """,
        model_output="Businesses use AI to automate work, analyze data, and improve customer service.",
        followed_instructions=True,
        notes="The summary was shorter and more focused after adding examples."
    )

    results.append(prompt_only_2)
    results.append(instruction_2)

    # ===================================================
    # TASK 3 (REQUIRED)
    # ===================================================

    prompt_only_3 = ExperimentResult(
        task_name="Explain to a Child",
        prompt_type="Prompt-Only",
        prompt_text="Explain gravity to a 6-year-old.",
        model_output="Gravity is a force that pulls things toward the Earth.",
        followed_instructions=True,
        notes="The explanation was correct but somewhat formal."
    )

    instruction_3 = ExperimentResult(
        task_name="Explain to a Child",
        prompt_type="Instruction-Tuned",
        prompt_text="""
    Instruction: Explain a topic to a 6-year-old.

    Input:
    What is rain?

    Output:
    Rain is water that falls from clouds when they get full.

    Instruction: Explain a topic to a 6-year-old.

    Input:
    What is gravity?

    Output:
    """,
        model_output="Gravity is like an invisible hand that keeps your feet on the ground and makes things fall down instead of floating away.",
        followed_instructions=True,
        notes="The explanation used simpler language and was easier for a child to understand."
    )

    results.append(prompt_only_3)
    results.append(instruction_3)

    # ===================================================
    # REQUIRED FAILURE CASE
    # ===================================================

    failure_case = ExperimentResult(
        task_name="Failure Case",
        prompt_type="Instruction-Tuned",
        prompt_text="""
    Instruction: Answer reasoning questions carefully.

    Input:
    A bat and a ball cost $1.10 total.
    The bat costs $1.00 more than the ball.
    How much does the ball cost?

    Output:
    """,
        model_output="10 cents",
        followed_instructions=False,
        notes=(
            "The correct answer is 5 cents. The model followed the format of the instructions "
            "but still produced the wrong answer. This shows that instruction tuning improves "
            "instruction following but does not guarantee correct reasoning."
        )
    )

    results.append(failure_case)

    # ===================================================
    # PRINT RESULTS
    # ===================================================
    print("\nALL RESULTS\n")

    for result in results:
        print_result(result)

    # ===================================================
    # COMPARISONS
    # ===================================================
    compare_results(prompt_only_1, instruction_1)
    compare_results(prompt_only_2, instruction_2)
    compare_results(prompt_only_3, instruction_3)


if __name__ == "__main__":
    main()