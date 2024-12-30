# Importing libraries
import pandas as pd
import time
from datetime import datetime
import threading
import os
import keyboard
import sys

# Edit settings here
cut_off = 85  # percentage required to clear cut-off
time_qn = 42  # desired time in seconds under which each question should be marked
exam_correct_marks = 1
exam_wrong_marks = -0.25

# Matrix: Each row represents a section, and columns represent its attributes
sections_matrix = [
    # [0.name, 1.totals, 2.time, 3.correct_marks, 4.wrong_marks]
    ["English", 30, 1200, 1, -0.25],
    ["Quant", 35, 1200, 1, -0.25],
    ["Reasoning", 35, 1200, 1, -0.25]
]

# Initializing [0.marks, 1.corrects, 2.wrongs, 3.skips, 4.attempts] for each section
results_matrix = [[0, 0, 0, 0, 0] for _ in sections_matrix]  
totals = 0
duration = 0
marks = 0
corrects = 0
wrongs = 0
percentage = 0
accuracy = 0
avg_time = 0
no_sections = len(sections_matrix)

# Defining function to save results
def save_results(section, subsection, percentage, accuracy, avg_time):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Create a dictionary of the result data
    result_data = {
        'Timestamp': timestamp,
        'Section': section,
        'Subsection': subsection,
        'Score %': percentage,
        'Accuracy %': accuracy,
        'Avg Time Per Qn (s)': avg_time
    }
    # Convert the dictionary to a pandas DataFrame
    result_df = pd.DataFrame([result_data])
    # Define the file path where the results will be saved
    file_path = "exam_results.csv"
    # Check if the file exists
    try:
        # If file doesn't exist, create a new file with headers
        if not os.path.exists(file_path):
            result_df.to_csv(file_path, mode='w', header=True, index=False)
        else:
            # If file exists, append the result without writing headers
            result_df.to_csv(file_path, mode='a', header=False, index=False)
    except Exception as e:
        print(f"Error writing to CSV: {e}")

# Defining main page
def main():
    # Resetting for new session
    results_matrix = [[0, 0, 0, 0, 0] for _ in sections_matrix]  
    totals = 0
    duration = 0
    marks = 0
    corrects = 0
    wrongs = 0
    percentage = 0
    accuracy = 0
    avg_time = 0
    clear_console()
    print("\n---Welcome to the Exam Practice Tracker!---")
    print("1. Exam Mode")
    print("2. Sectional Mode")
    print("3. Questions Mode")
    choice = int(input("Enter your choice (1 or 2 or 3): "))
    if choice == 1:
        exam_mode()
    elif choice == 2:
        sectional_mode()
    elif choice == 3:
        questions_mode()
    else:
        print("\nInvalid choice. Please enter 1 or 2 or 3.\n")
        main()

# Defining exam mode
def exam_mode():
    print("\n--- Exam Mode ---")
    for i in range(no_sections):   
        section_countdown(i)
    print("\nExam completed! Enter results...")
    # Calculations and Result
    for i in range(no_sections):
        print(f"\nHow many did you attempt in {sections_matrix[i][0]}: ")
        results_matrix[i][4] = int(input())
        print(f"\nHow many were wrong in {sections_matrix[i][0]}: ")
        results_matrix[i][2] = int(input())
    for i in range(no_sections):
        calculate(sections_matrix[i][0], "Assorted", sections_matrix[i][2], sections_matrix[i][1], results_matrix[i][4], results_matrix[i][2], sections_matrix[i][3], sections_matrix[i][4],1)
    print(f"\n Overall")
    for i in range(no_sections):
        totals += sections_matrix[i][1]
        duration += sections_matrix[i][2]
        attempts += results_matrix[i][4]
        wrongs += results_matrix[i][2]
    calculate("Overall", "Assorted", duration, totals, attempts, wrongs, exam_correct_marks, exam_wrong_marks, 0)
    input("\nPress Enter to restart...")
    main()

# Defining sectional mode
def sectional_mode():
    print("\n--- Sectional Mode ---")
    for i, section in enumerate(sections_matrix, 1):
        print(f"{i}. {section[0]}")
    m = int(input("Select a section using index number: "))
    if m in range(1, no_sections + 1):
        n=m-1
    else:
        print("\nInvalid choice. Please choose a valid section.\n")
        main()
    section_countdown(n)
    attempts = int(input("Number of Attempted: "))
    wrongs = int(input("How many wrong: "))
    calculate(sections_matrix[n][0], "Assorted", sections_matrix[n][2], sections_matrix[n][1], attempts, wrongs, sections_matrix[n][3], sections_matrix[n][4],1)
    input("\nPress Enter to restart...")
    main()
    
# Defining questions mode
def questions_mode():
    print("\n--- Questions Mode ---")
    for j in range(1, no_sections+1):
        print(f"{j}. {sections_matrix[j-1][0]}")
    m = int(input("Select a section: "))
    if m in range(1, no_sections+1):
        n=m-1
        section = sections_matrix[n][0]
        correct_marks = sections_matrix[n][3]
        wrong_marks = sections_matrix[n][4]
    else:
        section = "Assorted"
        correct_marks = float(input("Enter marks given for each correct answers: "))
        wrong_marks = float(input("Enter marks given for each wrong answers: "))
    subsection = input("Enter the subsection name: ")
    if subsection == "":
        subsection = "Assorted"
    input("Press Enter to start the timer in 5 seconds...")
    print("Starting in ")
    for k in range(5, 0, -1):
        print(f"{k}...", end="\n")
        time.sleep(1)
    print("Started")
    start_time = datetime.now()
    input("Press Enter to stop the timer...")
    stop_time = datetime.now()
    duration = int((stop_time - start_time).total_seconds())
    totals = int(input("Total number of questions: "))
    attempts = int(input("Number of Attempted: "))
    wrongs = int(input("How many wrong: "))
    calculate(section, subsection, duration, totals, attempts, wrongs, correct_marks, wrong_marks,1)
    input("\nPress Enter to restart...")
    main()        

# Section countdown
def section_countdown(t):
    input(f"Press Enter to start {sections_matrix[t][0]} in 5 seconds...")
    print("Starting in ")
    for j in range(5, 0, -1):
        sys.stdout.write(f"\r{j}...")
        sys.stdout.flush()
        time.sleep(1)
    print(f"\n{sections_matrix[t][0]} timer started! You have {int(sections_matrix[t][2]/60)} minutes.")
    print("Press Space to skip the remaining time.")
    skip_flag = [False]  # To indicate skip
    console_lock = threading.Lock()  # Ensure clean output
    def check_skip():
        while not skip_flag[0]:
            if keyboard.is_pressed("space"):
                with console_lock:
                    print(f"\nSkipping the remaining time for {sections_matrix[t][0]}...")
                skip_flag[0] = True
    # Start a separate thread for checking skip key press
    skip_thread = threading.Thread(target=check_skip)
    skip_thread.daemon = True
    skip_thread.start()
    # Countdown for the section
    remaining_time = sections_matrix[t][2]  # Total time in seconds
    while remaining_time > 0:
        if skip_flag[0]:
            with console_lock:
                print(f"Skipped the remaining time for {sections_matrix[t][0]}.")
            return
        mins, secs = divmod(remaining_time, 60)
        with console_lock:
            sys.stdout.write("\r" + " " * 50 + "\r")
            sys.stdout.write(f"Time left: {mins} minute(s) {secs} second(s)")
            sys.stdout.flush()
        time.sleep(1)
        remaining_time -= 1
    if not skip_flag[0]:
        print(f"\nTime is up for {sections_matrix[t][0]}!")

# Calcuate result function
def calculate(section, subsection, duration, totals, attempts, wrongs, correct_marks, wrong_marks, save):
    corrects = attempts - wrongs
    marks = (corrects * correct_marks) - (wrongs * wrong_marks)
    avg_time = int(duration / attempts) if attempts > 0 else 0
    accuracy = int((corrects / totals) * 100) if totals > 0 else 0
    percentage = int((marks / totals) * 100) if totals > 0 else 0
    print("\n--- Results ---")
    print(f"Section: {section}")
    print(f"Subsection: {subsection}")
    print(f"Duration: {int(duration/60)} min")
    print(f"Score: {marks}/{attempts} marks")
    print(f"Percentage: {percentage}%")
    print(f"Accuracy: {accuracy}%")
    print(f"Average Time per Question: {avg_time}s")
    if percentage > cut_off:
        print("Congratulations! You most likely will clear the cut-off")
    else:
        print("You will not clear the cut-off")
    if avg_time > time_qn:
        print("You are taking too much time per question")
    else:
        print("Congratulations! You are finishing in time")
    if save == 1:   
        save_results(section, subsection, percentage, accuracy, avg_time)

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/MacOS
    else:
        os.system('clear')

# Start the program
if __name__ == "__main__":
    main()
