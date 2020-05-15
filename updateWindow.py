from tkinter import *
import sqlite3

# function to save the changes made in the update window

# Create a Database or connect one

conn = sqlite3.connect('address_book.db')
# create a cursor
c = conn.cursor()


def save():
    # Create a Database or connect one
    conn = sqlite3.connect('address_book.db')
    # create a cursor
    c = conn.cursor()

    from database import id_box

    record_id = id_box.get()

    c.execute("""UPDATE addresses SET 
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid = :oid""",
              {'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'zipcode': zipcode_editor.get(),
               'oid': record_id
               })

    # commit changes
    conn.commit()
    # close the connection
    conn.close()

    # close window
    editor.destroy()


# create an update function to change a part of a record
def update():
    global editor
    editor = Tk()
    editor.title('Update Record')
    editor.iconbitmap('C:/Users/kevin/OneDrive/Desktop/fsociety-mask.ico')
    editor.geometry("400x400")

    # Create a Database or connect one
    conn = sqlite3.connect('address_book.db')
    # create a cursor
    c = conn.cursor()

    from database import id_box

    record_id = id_box.get()
    # query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # make text box global
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # create textbox for update window
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # create textbox labels for update window
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)

    city_label_editor = Label(editor, text="State")
    city_label_editor.grid(row=4, column=0)

    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    # loop through the results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # button to save changes
    save_btn = Button(editor, text="Update Record", command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=140)


# commit changes
conn.commit()
# close the connection
conn.close()
