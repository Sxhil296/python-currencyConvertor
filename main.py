from tkinter import *

# Define the convert function
def convert():
    # Get the currencies and amount
    from_currency = from_entry.get()
    to_currency = to_entry.get()
    amount = float(amount_entry.get())

    # Define the exchange rates
    rates = {"USD": 1.0, "EUR": 0.84, "JPY": 109.72, "GBP": 0.72, "INR":82.32}

    # Get the exchange rates
    from_rate = rates[from_currency]
    to_rate = rates[to_currency]

    # Convert the amount
    result = (to_rate / from_rate) * amount
    result_label.config(text=str(round(result, 2)) + " " + to_currency)

# Create a GUI
window = Tk()
window.title("Currency Converter")
window.geometry("400x300")

# Label for currency amount
amount_label = Label(window, text="Amount:", font=("Arial", 14))
amount_label.place(x=10, y=10)
amount_entry = Entry(window, font=("Arial", 14))
amount_entry.place(x=120, y=10)

# Label for the currency from
from_label = Label(window, text="From:", font=("Arial", 14))
from_label.place(x=10, y=50)
from_entry = Entry(window, font=("Arial", 14))
from_entry.place(x=120, y=50)

# Label for the currency to
to_label = Label(window, text="To:", font=("Arial", 14))
to_label.place(x=10, y=90)
to_entry = Entry(window, font=("Arial", 14))
to_entry.place(x=120, y=90)

# Label for the converted currency
result_label = Label(window, text="", font=("Arial", 14))
result_label.place(x=10, y=200)

# Button to convert the currency
convert_button = Button(window, text="Convert", font=("Arial", 14), command=convert)
convert_button.place(x=150, y=150)

window.mainloop()
