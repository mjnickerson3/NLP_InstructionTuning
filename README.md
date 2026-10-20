# NLP_InstructionTuning

## Overview

This project explores the difference between prompt-only behavior (zero-shot prompting) and instruction-tuned behavior (few-shot prompting) using a language model.

The goal of the project is to demonstrate how examples can help a model better understand instructions and produce responses that are more aligned with user expectations. Three different tasks were tested:

- Translation
- Summarization
- Explain to a Child

The project also includes a failure case to demonstrate that instruction tuning can improve instruction-following behavior but does not guarantee correct reasoning.

---

# Part 1: Prompt-Only Behavior

## Task 1: Translation

### Input Prompt

Translate to Spanish: How are you?

### Model Output

¿Cómo estás?

### Followed Instructions?

Yes

### Notes

The model correctly translated the phrase into Spanish.

---

## Task 2: Summarization

### Input Prompt

Summarize this paragraph:

Artificial intelligence is increasingly used by businesses to automate tasks, analyze large amounts of data, and improve customer service.

### Model Output

Businesses use AI to automate tasks, analyze data, and improve customer service.

### Followed Instructions?

Yes

### Notes

The model correctly summarized the paragraph and captured the main idea.

---

## Task 3: Explain to a Child

### Input Prompt

Explain gravity to a 6-year-old.

### Model Output

Gravity is a force that pulls things toward the Earth.

### Followed Instructions?

Yes

### Notes

The explanation was accurate but somewhat formal for a young child.

---

# Part 2: Simulated Instruction Tuning

## Task 1: Translation

### Model Output

¿Cómo estás?

### Performance Improved?

Slightly

### Differences

The response remained correct, but the examples reinforced the expected response format.

---

## Task 2: Summarization

### Model Output

Businesses use AI to automate work, analyze data, and improve customer service.

### Performance Improved?

Yes

### Differences

The instruction-tuned output was shorter and more focused.

---

## Task 3: Explain to a Child

### Model Output

Gravity is like an invisible hand that keeps your feet on the ground and makes things fall down instead of floating away.

### Performance Improved?

Yes

### Differences

The response used simpler language and was easier for a child to understand.

---

# Part 3: Comparison Analysis

## Translation Analysis

The translation task did not change much between the prompt-only and instruction-tuned versions. In both cases, the model translated the phrase correctly. Because translation is something language models are usually good at, the examples did not make a large difference in the final answer.

The biggest thing I noticed was that the examples gave the model a clear pattern to follow. Even though the response was the same, the instruction-tuned version seemed more focused on providing exactly what was asked for. Out of the three tasks, this one showed the least improvement because the model already handled it well without examples.

### Translation Results

<img width="804" height="900" alt="image" src="https://github.com/user-attachments/assets/573ab8f2-0d9f-4093-8f9e-e84194a0c0cf" />


---

## Summarization Analysis

The summarization task showed more improvement than the translation task. The prompt-only version gave a good summary, but the instruction-tuned version was shorter and more direct. The examples helped show what the expected summary should look like, which seemed to make the response more consistent.

I think examples helped more in this task because summarization can be done in different ways. By providing examples, the model had a better idea of the format and level of detail that was expected.

### Summarization Results

<img width="900" height="541" alt="image" src="https://github.com/user-attachments/assets/1d69cbc5-bbab-4304-94b2-6ec165915aaa" />


---

## Explain to a Child Analysis

This task showed the biggest improvement. The prompt-only version explained gravity correctly, but it sounded more like a definition than something meant for a six-year-old. The instruction-tuned version used simpler language and a comparison that made the idea easier to understand.

I think the examples helped because they showed the model who the audience was supposed to be. Instead of only explaining the concept, the model adjusted its wording to make it more kid-friendly. Out of all three tasks, this was the one where I saw the biggest difference between the prompt-only and instruction-tuned responses.

### Explain to a Child Results

<img width="900" height="754" alt="image" src="https://github.com/user-attachments/assets/b1aec3f5-156f-4124-bd99-728d3c0438c5" />


---

# Part 4: Failure Case

## Task

Reasoning Problem

### Model Output

10 cents

### Why It Failed

The correct answer is 5 cents.

The model appears to have relied on a shortcut rather than completing the full reasoning process. This demonstrates that instruction tuning can improve instruction following but does not guarantee correct reasoning.

### Failure Case Screenshot

<img width="900" height="223" alt="image" src="https://github.com/user-attachments/assets/cde198ac-6b2b-4dc6-813b-9fb381b88da6" />


---

# Part 5: Final Reflection

## Why do base models struggle to follow instructions?

Base models are trained to predict the next word in a sequence of text. Because they are not specifically trained to understand user intentions, they may not always produce responses that match what the user wants.

## How does instruction tuning improve performance?

Instruction tuning improves performance because it gives the model examples to learn from. The examples help guide the response and make it more likely that the model will follow the instructions correctly.

## Why do examples help guide the model?

Examples help guide the model by showing patterns it can follow. They provide information about formatting, style, tone, and level of detail.

## Why can models still fail even after instruction tuning?

Instruction tuning improves instruction-following behavior, but it does not guarantee reasoning accuracy.

## Do you think this process creates true understanding?

I don't think instruction tuning creates true understanding. I think it helps the model give better answers because it learns patterns from examples, but that is different from actually understanding a concept. The model can still make mistakes, like in the bat-and-ball example, which shows that following instructions and understanding something are not the same thing.
