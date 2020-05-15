import sqlite3
from tkinter import *

root = Tk()
root.title('F-DataBase')
root.iconbitmap('C:/Users/kevin/OneDrive/Desktop/fsociety-mask.ico')
root.geometry("400x400")

# Databases

# Create a Database or connect one
conn = sqlite3.connect('address_book.db')

# create a cursor 
c = conn.cursor()

'''
# Create a table
c.execute("""CREATE TABLE addresses (
            first_name text, 
            last_name text, 
            address text, 
            city text,
            state text,
            zipcode integer       
            )""")
'''


# create function to delete a record
def delete():
    # Create a Database or connect one
    conn = sqlite3.connect('address_book.db')
    # create a cursor
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid=" + id_box.get())

    # commit changes
    conn.commit()
    # close the connection
    conn.close()


# submit function
def submit():
    # Create a Database or connect one
    conn = sqlite3.connect('address_book.db')
    # create a cursor
    c = conn.cursor()

    # Insert into database table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # commit changes
    conn.commit()
    # close the connection
    conn.close()

    # clear the textboxes when something is submitted
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create query function
def query():
    # Create a Database or connect one
    conn = sqlite3.connect('address_book.db')
    # create a cursor
    c = conn.cursor()

    # query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # loop through results
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()
    # close the connection
    conn.close()


# create textbox
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

id_box = Entry(root, width=30)
id_box.grid(row=9, column=1)

# create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

city_label = Label(root, text="State")
city_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

id_box_label = Label(root, text="Input ID Number")
id_box_label.grid(row=9, column=0)

# create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=110)

# create a query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create an update button
from updateWindow import update

update_btn = Button(root, text="Update Record", command=update)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

# commit changes
conn.commit()

# close the connection
conn.close()

root.mainloop()
