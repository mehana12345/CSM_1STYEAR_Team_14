from tkinter import *
import random

# Create main window
root = Tk()
root.title("Random Quote Generator")
root.geometry("400x300")
root.config(bg="#f0f8ff")

# List of motivational quotes
quotes = [
    "Believe in yourself and all that you are.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Push yourself, because no one else is going to do it for you.",
    "Success is not for the lazy.",
    "Dream it. Wish it. Do it.",
    "Great things never come from comfort zones.",
    "Wake up with determination. Go to bed with satisfaction.",
    "It always seems impossible until it's done.",
    "Don’t stop when you’re tired. Stop when you’re done."
]

# Function to display a random quote
def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

# Title Label
title_label = Label(root, text="🌞 Daily Motivation Booster 💪", 
                    font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#333")
title_label.pack(pady=10)

# Quote display label
quote_label = Label(root, text="Click below to get inspired!", 
                    wraplength=350, font=("Arial", 12), bg="#f0f8ff", fg="#555")
quote_label.pack(pady=40)

# Button to show random quote
quote_button = Button(root, text="✨ Get Quote ✨", command=show_quote, 
                      font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
quote_button.pack()

# Run the Tkinter event loop
root.mainloop()
