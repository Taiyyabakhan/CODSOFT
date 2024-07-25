from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
import sys as system

def xuat_ra_file():
    """Export tasks to a file."""
    try:
        with open("list.txt", "a") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo('Success', 'Tasks exported to list.txt')
    except Exception as e:
        messagebox.showinfo('Error', f'File could not be written: {str(e)}')

def them_tac_vu():
    """Add a new task to the list and database."""
    task_string = task_field.get()
    if not task_string:
        messagebox.showinfo('Error', 'Task name is empty')
    else:
        tasks.append(task_string)
        the_cursor.execute('INSERT INTO tasks VALUES (?)', (task_string,))
        the_connection.commit()
        danh_sach_tac_vu()
        task_field.delete(0, 'end')

def danh_sach_tac_vu():
    """Display the list of tasks."""
    xoa_danh_sach()
    for task in tasks:
        task_listbox.insert('end', task)

def xoa_tac_vu():
    """Delete a selected task from the list and database."""
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            danh_sach_tac_vu()
            the_cursor.execute('DELETE FROM tasks WHERE title = ?', (the_value,))
            the_connection.commit()
    except Exception as e:
        messagebox.showinfo('Error', f'No task selected: {str(e)}')

def xoa_tat_ca():
    """Delete all tasks after user confirmation."""
    if messagebox.askyesno('Delete All', 'Are you sure?'):
        tasks.clear()
        the_cursor.execute('DELETE FROM tasks')
        the_connection.commit()
        danh_sach_tac_vu()

def xoa_danh_sach():
    """Clear the task listbox."""
    task_listbox.delete(0, 'end')

def close():
    """Close the application."""
    guiWindow.destroy()
    the_connection.close()

def doc_co_so_du_lieu():
    """Read tasks from the database."""
    tasks.clear()
    for row in the_cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("1000x500+500+50")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#A1C3D1")

    # SQLite database setup
    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')
    tasks = []

    # UI setup
    functions_frame = Frame(guiWindow, bg="black")
    functions_frame.pack(side="top", expand=True, fill="both")

    task_label = Label(functions_frame, text="Enter Task:", font=("Arial", 16, "bold"), bg="black", fg="white")
    task_label.place(x=20, y=30)

    task_field = Entry(functions_frame, font=("Arial", 16), width=61, fg="black", bg="white")
    task_field.place(x=180, y=30)

    add_button = Button(functions_frame, text="Add Task", width=15, bg='#5D3FD3', fg="white", font=("Arial", 16, "bold"), command=them_tac_vu)
    del_button = Button(functions_frame, text="Delete Task", width=15, bg='#5D3FD3', fg="white", font=("Arial", 16, "bold"), command=xoa_tac_vu)
    del_all_button = Button(functions_frame, text="Delete All Tasks", width=15, font=("Arial", 16, "bold"), bg='#5D3FD3', fg="white", command=xoa_tat_ca)
    export_file = Button(functions_frame, text="Export to txt", width=15, font=("Arial", 16, "bold"), bg='#5D3FD3', fg="white", command=xuat_ra_file)
    exit_button = Button(functions_frame, text="Exit", width=69, bg='#5D3FD3', fg="white", font=("Arial", 16, "bold"), command=close)

    add_button.place(x=10, y=80)
    del_button.place(x=250, y=80)
    del_all_button.place(x=490, y=80)
    export_file.place(x=730, y=80)
    exit_button.place(x=10, y=400)

    task_listbox = Listbox(functions_frame, width=120, height=10, font=("Arial", 14), selectmode='SINGLE', bg="white", fg="black", selectbackground="#5D3FD3", selectforeground="white")
    task_listbox.place(x=17, y=150)

    doc_co_so_du_lieu()
    danh_sach_tac_vu()

    guiWindow.mainloop()
    
    the_connection.commit()
    the_connection.close()
