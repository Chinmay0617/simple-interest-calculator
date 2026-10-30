# Simple Interest Calculator

## 📌 Project Description
The Simple Interest Calculator is a Python-based application that calculates simple interest based on the principal amount, annual interest rate, and time period.

It helps users calculate interest and the total payable amount quickly and accurately.

## 🎯 Project Objective
The main objective of this project is to understand basic Python programming concepts and perform mathematical calculations using user input.

## 🧮 Formula

**Simple Interest = (P × R × T) / 100**

Where:
- P = Principal Amount
- R = Annual Rate of Interest
- T = Time Period in Years

**Total Amount = Principal + Simple Interest**

## 💻 Technologies Used
- Python 3
- Basic Mathematical Operations
- User Input and Output

## ⚙️ Features
- Accepts principal amount from the user.
- Accepts annual interest rate.
- Accepts time period in years.
- Calculates simple interest automatically.
- Displays the total amount.
- Easy-to-use command-line interface.

## 🚀 Python Source Code

```python
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in Years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)

total_amount = principal + simple_interest
print("Total Amount:", total_amount)
```

## 📊 Sample Output

```text
Enter Principal Amount: 1000
Enter Rate of Interest: 5
Enter Time in Years: 2

Simple Interest: 100.0
Total Amount: 1100.0
```

## ▶️ How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```bash
python simple_interest.py
```

5. Enter the required values to calculate simple interest.

## 📚 Learning Outcomes
- Understanding Python variables.
- Using input() and print() functions.
- Performing arithmetic operations.
- Understanding basic programming logic.

## 👨‍💻 Author
**Chinmay Sakhare**

## 📄 License
This project is created for educational and learning purposes.
