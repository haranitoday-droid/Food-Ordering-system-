import tkinter as tk
from tkinter import messagebox

class FoodOrderingSystem:
    def __init__(self, master):
        self.master = master
        master.title("Food Ordering System")

        self.menu = {
            "Burger": 5.00,
            "Pizza": 8.00,
            "Pasta": 7.00,
            "Salad": 4.00,
            "Soda": 1.50
        }

        self.selected_items = []
        self.total_price = 0.0

        # Menu List
        self.menu_listbox = tk.Listbox(master)
        for item in self.menu.keys():
            self.menu_listbox.insert(tk.END, item)
        self.menu_listbox.pack()

        # Order Selected Button
        self.order_button = tk.Button(master, text="Order Selected", command=self.order_selected)
        self.order_button.pack()

        # Clear Order Button
        self.clear_button = tk.Button(master, text="Clear Order", command=self.clear_order)
        self.clear_button.pack()

        # Bill Button
        self.bill_button = tk.Button(master, text="Generate Bill", command=self.generate_bill)
        self.bill_button.pack()

        # Total Label
        self.total_label = tk.Label(master, text="Total: $0.00")
        self.total_label.pack()

    def order_selected(self):
        selected_index = self.menu_listbox.curselection()
        if selected_index:
            selected_item = self.menu_listbox.get(selected_index)
            self.selected_items.append(selected_item)
            item_price = self.menu[selected_item]
            self.total_price += item_price
            self.update_total_label()
            messagebox.showinfo("Order Placed", f"You have ordered: {selected_item}")

    def clear_order(self):
        self.selected_items.clear()
        self.total_price = 0.0
        self.update_total_label()
        messagebox.showinfo("Order Cleared", "All orders have been cleared.")

    def update_total_label(self):
        self.total_label.config(text=f"Total: ${self.total_price:.2f}")

    def generate_bill(self):
        if not self.selected_items:
            messagebox.showwarning("No Orders", "You have no items ordered.")
            return

        bill_details = "Your Bill:\n\n"
        for item in self.selected_items:
            bill_details += f"{item}: ${self.menu[item]:.2f}\n"
        bill_details += f"\nTotal: ${self.total_price:.2f}"

        messagebox.showinfo("Bill", bill_details)

if __name__ == "__main__":
    root = tk.Tk()
    food_ordering_system = FoodOrderingSystem(root)
    root.mainloop()
