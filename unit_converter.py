import tkinter as tk

# Define the conversion functions
def convert():
    input_value = float(input_entry.get())
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()

    # Define the conversion rates
    conversion_rates = {
        ("Miles", "Kilometers"): 1.60934,
        ("Kilometers", "Miles"): 0.621371,
        ("Pounds", "Kilograms"): 0.453592,
        ("Kilograms", "Pounds"): 2.20462,
        ("Inches", "Centimeters"): 2.54,
        ("Centimeters", "Inches"): 0.393701,
    }

    # Check if conversion is valid
    if (from_unit, to_unit) not in conversion_rates:
        result_label.config(text="Invalid Conversion")
        return

    # Perform the conversion
    result_value = input_value * conversion_rates[(from_unit, to_unit)]
    result_label.config(text=f"{result_value} {to_unit}")

# Create main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("250x175")
root.resizable(False, False)

# Create the widgets
input_label = tk.Label(root, text="Value: ")
input_entry = tk.Entry(root)
from_unit_label = tk.Label(root, text="From:")
from_unit_var = tk.StringVar(root)
from_unit_var.set("Choose Unit From")
from_unit_option = tk.OptionMenu(root, from_unit_var, *["Miles", "Kilometers", "Pounds", "Kilograms", "Inches", "Centimeters"])
to_unit_label = tk.Label(root, text="To:")
to_unit_var = tk.StringVar(root)
to_unit_var.set("Choose Unit To")
to_unit_option = tk.OptionMenu(root, to_unit_var, *["Miles", "Kilometers", "Pounds", "Kilograms", "Inches", "Centimeters"])
convert_button = tk.Button(root, text="Convert", command=convert)
result_label = tk.Label(root, text="")

# Add the widgets to the window
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry.grid(row=0, column=1, padx=5, pady=5)
from_unit_label.grid(row=1, column=0, padx=5, pady=5)
from_unit_option.grid(row=1, column=1, padx=5, pady=5)
to_unit_label.grid(row=2, column=0, padx=5, pady=5)
to_unit_option.grid(row=2, column=1, padx=5, pady=5)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()