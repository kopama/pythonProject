import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("My pizza")

frame = tkinter.Frame(window)
frame.pack()





#user information
user_info_frame =tkinter.LabelFrame(frame, text="Customer Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="last Name")
last_name_label.grid(row=0, column=1)
tel_name_label = tkinter.Label(user_info_frame, text="Phone Number")
tel_name_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame, text="First Name")
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame, text="last Name")
last_name_entry.grid(row=1, column=1)
tel_name_entry = tkinter.Entry(user_info_frame, text="Phone Number")
tel_name_entry.grid(row=1, column=2)

#Pizza information
pizza_info_frame = tkinter.LabelFrame(frame, text="Choose your Pizza")
pizza_info_frame.grid(row= 1, column=2, padx=20, pady=20)

pizza_label = tkinter.Label(pizza_info_frame, text="Pizza Name")
pizza_combobox = ttk.Combobox(pizza_info_frame, values=["Hot pizza_ $15", "Beef pizza_ $17", "Chiken pizza_ $21", "Chiken pizza_ $15"])
pizza_label.grid(row=0, column=0)
pizza_combobox.grid(row=1, column=0)

sauce_label = tkinter.Label(pizza_info_frame, text="Select sauce")
sauce_combobox = ttk.Combobox(pizza_info_frame, values=["BBQ_ + $2", "red pizza sauce_ + $0", "american sauce_ + $1.5"])
sauce_label.grid(row=1, column=1)
sauce_combobox.grid(row=3, column=1)

#payement information
banq_frame = tkinter.LabelFrame(frame)
banq_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

payement_label = tkinter.Label(banq_frame, text = " Payement information")
payement_check = tkinter.Checkbutton(banq_frame, text="Pay with cash at delivery")
payement_label.grid(row=0, column=0)
payement_check.grid(row=1, column=0)

payement_label = tkinter.Label(banq_frame, text = " Payement information")
payement_check = tkinter.Checkbutton(banq_frame, text="Call 002458689 to pay with debit card")
payement_label.grid(row=0, column=0)
payement_check.grid(row=2, column=0)

#Customer adress information
user_info_frame =tkinter.LabelFrame(frame, text="Customer Adress")
user_info_frame.grid(row= 3, column=2, padx=20, pady=20)

first_adress_label = tkinter.Label(user_info_frame, text="Adress")
first_adress_label.grid(row=0, column=0)
last_city_label = tkinter.Label(user_info_frame, text="City")
last_city_label.grid(row=0, column=1)
tel_state_label = tkinter.Label(user_info_frame, text="State")
tel_state_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame, text="Adress")
first_name_entry.grid(row=3, column=0)
last_name_entry = tkinter.Entry(user_info_frame, text="City")
last_name_entry.grid(row=3, column=1)
tel_name_entry = tkinter.Entry(user_info_frame, text="State")
tel_name_entry.grid(row=3, column=2)

#Place ordor button
button = tkinter.Button(frame, text="Place your order")
button.grid(row=4, column=0, sticky="news", padx=20, pady=20)






window.mainloop()