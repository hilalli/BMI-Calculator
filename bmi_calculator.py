import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # converting cm to meters
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_var.set(f"BMI: {bmi} - {category}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height.")


# Creating main window
root = tk.Tk()
root.title("BMI Calculator")

# Adding input fields
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5)
entry_weight = tk.Entry(frame)
entry_weight.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Height (cm):").grid(row=1, column=0, padx=5, pady=5)
entry_height = tk.Entry(frame)
entry_height.grid(row=1, column=1, padx=5, pady=5)

# Adding Calculate button
button_calculate = tk.Button(frame, text="Calculate BMI", command=calculate_bmi)
button_calculate.grid(row=2, columnspan=2, pady=10)

# Adding result display
result_var = tk.StringVar()
label_result = tk.Label(frame, textvariable=result_var, font="lucida 12 bold")
label_result.grid(row=3, columnspan=2, pady=10)

# Running the main loop
root.mainloop()
