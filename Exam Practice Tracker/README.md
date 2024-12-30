# Exam Practice Tracker

This Python program helps you track and evaluate your performance while practicing for exams. It allows you to simulate exams, track time and accuracy for each section, and store results for later review.

## Disclaimer

Please note that this program is **not a real exam simulation**. It is designed to help you **track your progress** while practicing exam questions and recording your results. The purpose is to provide insights into your performance, helping you identify areas for improvement and gauge how efficiently you are tackling practice questions. It is not intended to replicate the exact experience of taking an official exam under timed conditions.

## Features

- **Exam Mode**: Simulate a full exam, tracking performance across different sections.
- **Sectional Mode**: Track performance for individual sections of the exam.
- **Questions Mode**: Track performance for specific questions, including time taken and accuracy.
- **Result Calculation**: Displays detailed results, including score, percentage, accuracy, and time per question.
- **Result Saving**: Saves the exam results to a CSV file for future reference and analysis.
Since all historical data is saved in a CSV file, you can easily analyze it later to uncover insights and trends. By examining past results, you can identify areas for improvement, track your progress over time, and make data-driven decisions about how to adjust your study routine. You can use tools like Excel, Google Sheets, or Python (with libraries like pandas) to explore and visualize your performance patterns across different exams, sections, or topics.

## Installation

### Prerequisites

Ensure that you have Python 3.x installed. You will also need the following Python packages:
- `pandas` (for saving results to a CSV file)
- `keyboard` (for skip funciton in timer)

### Installing Dependencies

To install the required dependencies, run:

```bash
pip install pandas
pip install keyboard
```

### Running the Program

1. Download or clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the program with:

```bash
python exam_practice_tracker.py
```

## How to Use

Upon running the program, you will be prompted to choose between three modes:
1. **Exam Mode**: This will simulate a full exam with different sections and time limits.
2. **Sectional Mode**: This will allow you to track performance for a specific section.
3. **Questions Mode**: Track performance for individual questions, including time taken and accuracy.

After completing the session in any mode, the program will calculate and display the results, such as your score, percentage, and time per question. You will also have the option to save your results to a CSV file.

## Customizing the Program for Other Exams

The program is designed to be easily customizable for other exams with different marking structures and sections. Below are the parts of the code you need to modify:

### 1. **Marking Scheme**:
   In the exam mode, the marking structure for correct and incorrect answers is defined in the variables:
   - `exam_correct_marks`: The marks awarded for each correct answer (default is 1).
   - `exam_wrong_marks`: The penalty for each wrong answer (default is -0.25).
  In sectional and questions mode, the marking structure is defined in the `sections_matrix`.

### 2. **Sections and Attributes**:
   The exam sections, number of questions, and time limits are defined in the `sections_matrix` variable. Each section is represented by a list in the format:

   ```python
   ["Section Name", Total Questions, Total Time in Seconds, Marks for Correct Answer, Marks for Incorrect Answer]
   ```

   Here's the default `sections_matrix`:
   ```python
   sections_matrix = [
       ["English", 30, 1200, 1, -0.25],
       ["Quant", 35, 1200, 1, -0.25],
       ["Reasoning", 35, 1200, 1, -0.25]
   ]
   ```

   - **Section Name**: The name of the section (e.g., "English", "Math").
   - **Total Questions**: The total number of questions in the section.
   - **Total Time**: The time allowed for the section (in seconds). For example, 1200 seconds is 20 minutes.
   - **Marks for Correct Answer**: The marks awarded for each correct answer.
   - **Marks for Incorrect Answer**: The penalty for each incorrect answer.

   To add or modify sections for your exam, simply adjust the `sections_matrix` list. For example, if your exam has sections for "General Knowledge" and "Verbal Reasoning", you could change it to:

   ```python
   sections_matrix = [
       ["General Knowledge", 40, 1800, 1, -0.25],
       ["Verbal Reasoning", 35, 1200, 1, -0.25]
   ]
   ```

### 3. **Cut-off and Time per Question**:
   You can adjust the minimum percentage required to pass the exam and the time threshold for each question:
   - `cut_off = 85`  # Percentage required to clear the cut-off (default is 85%).
   - `time_qn = 42`  # Time in seconds under which each question should be marked (default is 42 seconds).

   For example:
   ```python
   cut_off = 80  # Lower cut-off percentage for another exam
   time_qn = 35  # Set a faster time per question
   ```

### 4. **Result Saving**:
   The program saves results to a CSV file (`exam_results.csv`). You can modify the file path if you prefer saving the results elsewhere. This is done in the `save_results` function.

## Files
- `exam_practice_tracker.py`: The main program file.
- `exam_results.csv`: This file stores your exam results, including timestamp, section, subsection, score, accuracy, and average time per question.

## Example Output

```bash
--- Results ---
Section: Quant
Subsection: Assorted
Duration: 15 min
Score: 30/35 marks
Percentage: 85%
Accuracy: 90%
Average Time per Question: 25s
Congratulations! You most likely will clear the cut-off
Congratulations! You are finishing in time
```
