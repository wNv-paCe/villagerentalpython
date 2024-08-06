import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

class VillageRentalsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Village Rentals")
        self.root.geometry("1000x600")
        self.create_menu()
        self.show_welcome_message()

    # Menu for user to choose what action that would like to do with this application
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        equipment_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Equipment", menu=equipment_menu)
        equipment_menu.add_command(label="Add Equipment", command=self.add_equipment)
        equipment_menu.add_command(label="Delete Equipment", command=self.delete_equipment)
        equipment_menu.add_command(label="View All Equipment", command=self.view_all_equipment)

        customer_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Customer", menu=customer_menu)
        customer_menu.add_command(label="Add Customer", command=self.add_customer)
        customer_menu.add_command(label="View All Customers", command=self.view_all_customers)

        rental_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Rental", menu=rental_menu)
        rental_menu.add_command(label="Process Rental", command=self.process_rental)

    # Connexting to the database (SQL)
    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',  # No password for local server
                database='villagerentals'
            )
            return conn
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))
            return None

    # Adding a new equipment
    # Get equipment from user's input
    def add_equipment(self):
        self.clear_frame()
        tk.Label(self.root, text="Add Equipment", font=('Arial', 16)).pack(pady=10)

        tk.Label(self.root, text="Equipment ID").pack()
        self.equipment_id_entry = tk.Entry(self.root)
        self.equipment_id_entry.pack()

        tk.Label(self.root, text="Category ID").pack()
        self.category_id_entry = tk.Entry(self.root)
        self.category_id_entry.pack()

        tk.Label(self.root, text="Name").pack()
        self.equipment_name_entry = tk.Entry(self.root)
        self.equipment_name_entry.pack()

        tk.Label(self.root, text="Description").pack()
        self.equipment_description_entry = tk.Entry(self.root)
        self.equipment_description_entry.pack()

        tk.Label(self.root, text="Daily Rental Rate").pack()
        self.daily_rental_rate_entry = tk.Entry(self.root)
        self.daily_rental_rate_entry.pack()

        tk.Button(self.root, text="Add Equipment", command=self.save_equipment).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.go_back).pack(pady=10)

    # Saveing the new added equipment into the databse
    # Save data from user's input (Equipment Detail)
    def save_equipment(self):
        equipment_id = self.equipment_id_entry.get()
        category_id = self.category_id_entry.get()
        name = self.equipment_name_entry.get()
        description = self.equipment_description_entry.get()
        daily_rate = self.daily_rental_rate_entry.get()

        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO rentalequipment (id, category_id, equipment_name, description, daily_rate) VALUES (%s, %s, %s, %s, %s)", 
                           (equipment_id, category_id, name, description, daily_rate))
            conn.commit()
            cursor.close()
            conn.close()

        messagebox.showinfo("Success", "Equipment added successfully!")
        self.clear_frame()

    # Deleting an exist equipment
    # By user's input
    def delete_equipment(self):
        self.clear_frame()
        tk.Label(self.root, text="Delete Equipment", font=('Arial', 16)).pack(pady=10)

        tk.Label(self.root, text="Equipment ID").pack()
        self.del_equipment_id_entry = tk.Entry(self.root)
        self.del_equipment_id_entry.pack()

        tk.Button(self.root, text="Delete Equipment", command=self.remove_equipment).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.go_back).pack(pady=10)

    # Delete the desire data from the database
    def remove_equipment(self):
        equipment_id = self.del_equipment_id_entry.get()
        
        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rentalequipment WHERE id = %s", (equipment_id,))
            conn.commit()
            cursor.close()
            conn.close()

        messagebox.showinfo("Success", "Equipment deleted successfully!")
        self.clear_frame()

    # Adding a new customer information
    # From user's input
    def add_customer(self):
        self.clear_frame()
        tk.Label(self.root, text="Add Customer", font=('Arial', 16)).pack(pady=10)

        tk.Label(self.root, text="Customer ID").pack()
        self.customer_id_entry = tk.Entry(self.root)
        self.customer_id_entry.pack()

        tk.Label(self.root, text="First Name").pack()
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack()

        tk.Label(self.root, text="Last Name").pack()
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.pack()

        tk.Label(self.root, text="Contact Phone").pack()
        self.contact_phone_entry = tk.Entry(self.root)
        self.contact_phone_entry.pack()

        tk.Label(self.root, text="Email").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        tk.Button(self.root, text="Add Customer", command=self.save_customer).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.go_back).pack(pady=10)

    # Saving a new customer information into the database
    def save_customer(self):
        customer_id = self.customer_id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        contact_phone = self.contact_phone_entry.get()
        email = self.email_entry.get()

        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customerinfo (id, last_name, first_name, contact_phone, email) VALUES (%s, %s, %s, %s, %s)", 
                       (customer_id, last_name, first_name, contact_phone, email))
            conn.commit()
            cursor.close()
            conn.close()

        messagebox.showinfo("Success", "Customer added successfully!")
        self.clear_frame()

    # Showing all exist customer from the database
    def view_all_customers(self):
        self.clear_frame()
        tk.Label(self.root, text="All Customers", font=('Arial', 16)).pack(pady=10)

        tree = ttk.Treeview(self.root, columns=("ID", "First Name", "Last Name", "Phone", "Email"), show='headings')
        tree.heading("ID", text="Customer ID")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Phone", text="Contact Phone")
        tree.heading("Email", text="Email")
        tree.pack()

        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, last_name, first_name, contact_phone, email FROM customerinfo")
            records = cursor.fetchall()
            for row in records:
                tree.insert("", "end", values=row)
            cursor.close()
            conn.close()

        tk.Button(self.root, text="Back", command=self.go_back).pack(pady=10)

    # Showing all the exist equipment from the database
    def view_all_equipment(self):
        self.clear_frame()
        tk.Label(self.root, text="All Equipment", font=('Arial', 16)).pack(pady=10)

        tree = ttk.Treeview(self.root, columns=("ID", "Category", "Name", "Description", "Daily Rate"), show='headings')
        tree.heading("ID", text="Equipment ID")
        tree.heading("Category", text="Category ID")
        tree.heading("Name", text="Name")
        tree.heading("Description", text="Description")
        tree.heading("Daily Rate", text="Daily Rate")
        tree.pack()

        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, category_id, equipment_name, description, daily_rate FROM rentalequipment")
            records = cursor.fetchall()
            for row in records:
                tree.insert("", "end", values=row)
            cursor.close()
            conn.close()

        tk.Button(self.root, text="Back", command=self.go_back).pack(pady=10)

    # Starting a rental process
    # From user's input
    def process_rental(self):
        self.clear_frame()
        tk.Label(self.root, text="Process Rental", font=('Arial', 16)).pack(pady=10)

        tk.Label(self.root, text="Rental ID").pack()
        self.rental_id_entry = tk.Entry(self.root)
        self.rental_id_entry.pack()

        tk.Label(self.root, text="Customer ID").pack()
        self.rental_customer_id_entry = tk.Entry(self.root)
        self.rental_customer_id_entry.pack()

        tk.Label(self.root, text="Customer Last Name").pack()
        self.rental_last_name_entry = tk.Entry(self.root)
        self.rental_last_name_entry.pack()

        tk.Label(self.root, text="Equipment ID").pack()
        self.rental_equipment_id_entry = tk.Entry(self.root)
        self.rental_equipment_id_entry.pack()

        tk.Label(self.root, text="Rental Date (YYYY-MM-DD)").pack()
        self.rental_date_entry = tk.Entry(self.root)
        self.rental_date_entry.pack()

        tk.Label(self.root, text="Return Date (YYYY-MM-DD)").pack()
        self.return_date_entry = tk.Entry(self.root)
        self.return_date_entry.pack()

        tk.Label(self.root, text="Cost of Rental").pack()
        self.cost_label = tk.Label(self.root, text="")
        self.cost_label.pack()

        tk.Button(self.root, text="Calculate Cost", command=self.calculate_rental_cost).pack(pady=10)
        tk.Button(self.root, text="Process Rental", command=self.save_rental).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.go_back).pack(pady=10)

    # Saving a new rental detail to the database
    def save_rental(self):
        rental_id = self.rental_id_entry.get()
        customer_id = self.rental_customer_id_entry.get()
        last_name = self.rental_last_name_entry.get()
        equipment_id = self.rental_equipment_id_entry.get()
        rental_date = self.rental_date_entry.get()
        return_date = self.return_date_entry.get()
        cost = self.cost_label.cget("text")

        # Get the current system date and time
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO rentalinfo (id, customer_id, equipment_id, date, rental_date, return_date, cost)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (rental_id, customer_id, equipment_id, current_date, rental_date, return_date, cost))
            conn.commit()
            cursor.close()
            conn.close()

        messagebox.showinfo("Success", "Rental processed successfully!")
        self.clear_frame()

    # Calculate the toal code of the current rental
    def calculate_rental_cost(self):
        equipment_id = self.rental_equipment_id_entry.get()
        rental_date = self.rental_date_entry.get()
        return_date = self.return_date_entry.get()

        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT daily_rate FROM rentalequipment WHERE id = %s", (equipment_id,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if result:
                daily_rate = result[0]
                rental_days = (datetime.strptime(return_date, "%Y-%m-%d") - datetime.strptime(rental_date, "%Y-%m-%d")).days
                total_cost = rental_days * daily_rate
                self.cost_label.config(text=f"{total_cost:.2f}")
            else:
                messagebox.showerror("Error", "Equipment ID not found!")

    # "Welcome" message will be showed to the user
    def show_welcome_message(self):
        tk.Label(self.root, text="Welcome to Village Rentals!", font=('Arial', 24)).pack(pady=20)
        tk.Label(self.root, text="Please use the menu to navigate through the options.", font=('Arial', 16)).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Move to the previous page when user press on this function button
    def go_back(self):
        self.clear_frame()
        self.create_menu()
        self.show_welcome_message()

if __name__ == "__main__":
    root = tk.Tk()
    app = VillageRentalsApp(root)
    root.mainloop()



