# Name: Final Project
# Author: Karin Brun
# Created: 11/06/2023
#
# Course: CIS 152 - Data Structure
# Version: 1.0
# OS: Linux Ubuntu
# IDE: PyCharm EDU
#
# Copyright:  This is my own original work
#             based on specifications issued
#             by our instructor
#
# Description: GUI code for final project
#
# Academic Honesty: I attest that this is my original work.
#                   I have not used unauthorized source code,
#                   either modified or unmodified. I have not
#                   given other fellow student(s) access to my program.

from finalproject.queuecode import *
from finalproject.linkedlistcode import *
from finalproject.validation import *
import tkinter
from tkinter import ttk
import tkinter.font as font


# updates room ui components. if empty colors the room light green, if full colors the room light red
def update_rooms():
    room_gui = room_list.get_room(0)
    if room_gui.available_room():
        frame_room1["bg"] = "light green"
        label_rm_num1["bg"] = "light green"
        label_p_name1["bg"] = "light green"
        label_rm_time1["bg"] = "light green"
    else:
        frame_room1["bg"] = "tomato1"
        label_rm_num1["bg"] = "tomato1"
        label_p_name1["bg"] = "tomato1"
        label_rm_time1["bg"] = "tomato1"
    label_p_name1["text"] = room_gui.patient
    label_rm_time1["text"] = room_gui.est_time

    room_gui = room_list.get_room(1)
    if room_gui.available_room():
        frame_room2["bg"] = "light green"
        label_rm_num2["bg"] = "light green"
        label_p_name2["bg"] = "light green"
        label_rm_time2["bg"] = "light green"
    else:
        frame_room2["bg"] = "tomato1"
        label_rm_num2["bg"] = "tomato1"
        label_p_name2["bg"] = "tomato1"
        label_rm_time2["bg"] = "tomato1"
    label_p_name2["text"] = room_gui.patient
    label_rm_time2["text"] = room_gui.est_time

    room_gui = room_list.get_room(2)
    if room_gui.available_room():
        frame_room3["bg"] = "light green"
        label_rm_num3["bg"] = "light green"
        label_p_name3["bg"] = "light green"
        label_rm_time3["bg"] = "light green"
    else:
        frame_room3["bg"] = "tomato1"
        label_rm_num3["bg"] = "tomato1"
        label_p_name3["bg"] = "tomato1"
        label_rm_time3["bg"] = "tomato1"
    label_p_name3["text"] = room_gui.patient
    label_rm_time3["text"] = room_gui.est_time

    room_gui = room_list.get_room(3)
    if room_gui.available_room():
        frame_room4["bg"] = "light green"
        label_rm_num4["bg"] = "light green"
        label_p_name4["bg"] = "light green"
        label_rm_time4["bg"] = "light green"
    else:
        frame_room4["bg"] = "tomato1"
        label_rm_num4["bg"] = "tomato1"
        label_p_name4["bg"] = "tomato1"
        label_rm_time4["bg"] = "tomato1"
    label_p_name4["text"] = room_gui.patient
    label_rm_time4["text"] = room_gui.est_time


# updates time on rooms every second
def update_time(self):
    room_list.update_rooms(1)
    if not patient_list.empty():
        patient = patient_list.next_in_line()
        if room_list.patient_to_room(patient[1], patient[0]) == "Patient has been assigned to room.":
            patient_list.remove_patient()
            label_patient_queue["text"] = f"{patient_list}"
    update_rooms()
    self.after(1000, update_time, window)


# adds patient to room or queue based on availability from text box and triage from drop down
def click_add_patient():
    try:
        patient_name = p_name_text.get()
        validate_string_input(patient_name)
        priority = 3
        match priority_box.get():
            case "Mild":
                priority = 3
            case "Moderate":
                priority = 2
            case "Severe":
                priority = 1
        if room_list.patient_to_room(patient_name, priority) == "Patient has been assigned to room.":
            update_rooms()
        else:
            patient_list.add_patient(patient_name, priority)
        p_name_text.set("")
        label_patient_queue["text"] = f"{patient_list}"
    except InvalidInputCharacters:
        p_name_text.set(" ")
        new_window = tkinter.Toplevel(window)
        new_window.title("Invalid Characters")
        new_window.geometry("500x45")
        label = tkinter.Label(new_window, text="Invalid Character Input for Name.", font=myFont)
        label.pack()


# ui code for base window
window = tkinter.Tk()
window.minsize(950, 535)
window.title("ER Patient and Room Tracker")
myFont = font.Font(size=12)

# size of grid in window for ui elements
window.rowconfigure([0, 1], minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

# initializes room list and populates with rooms
room_list = RoomList()
room_num = 101
for num in range(4):
    room = Room(room_num + num)
    room_list.add_room(room)

# room 1 gui code
room = room_list.get_room(0)
frame_room1 = tkinter.Frame(master=window, bg="light green", relief=tkinter.GROOVE, borderwidth=2)
label_rm_num1 = tkinter.Label(master=frame_room1, bg="light green", font=myFont, text=f"Room {room.room_num}")
label_rm_num1.pack()
label_p_name1 = tkinter.Label(master=frame_room1, bg="light green", font=myFont, text=f"{room.patient}")
label_p_name1.pack(fill=tkinter.Y, expand=True)
label_rm_time1 = tkinter.Label(master=frame_room1, bg="light green", font=myFont, text=f"{room.est_time}")
label_rm_time1.pack(side=tkinter.BOTTOM)
frame_room1.grid(row=0, column=0, ipadx=80, ipady=50, padx=5, pady=5, sticky="nsew")

# room 2 gui code
room = room_list.get_room(1)
frame_room2 = tkinter.Frame(master=window, bg="light green", relief=tkinter.GROOVE, borderwidth=2)
label_rm_num2 = tkinter.Label(master=frame_room2, bg="light green", font=myFont, text=f"Room {room.room_num}")
label_rm_num2.pack()
label_p_name2 = tkinter.Label(master=frame_room2, bg="light green", font=myFont, text=f"{room.patient}")
label_p_name2.pack(fill=tkinter.Y, expand=True)
label_rm_time2 = tkinter.Label(master=frame_room2, bg="light green", font=myFont, text=f"{room.est_time}")
label_rm_time2.pack(side=tkinter.BOTTOM)
frame_room2.grid(row=0, column=1, ipadx=80, ipady=50, padx=5, pady=5, sticky="nsew")

# room 3 gui code
room = room_list.get_room(2)
frame_room3 = tkinter.Frame(master=window, bg="light green", relief=tkinter.GROOVE, borderwidth=2)
label_rm_num3 = tkinter.Label(master=frame_room3, bg="light green", font=myFont, text=f"Room {room.room_num}")
label_rm_num3.pack()
label_p_name3 = tkinter.Label(master=frame_room3, bg="light green", font=myFont, text=f"{room.patient}")
label_p_name3.pack(fill=tkinter.Y, expand=True)
label_rm_time3 = tkinter.Label(master=frame_room3, bg="light green", font=myFont, text=f"{room.est_time}")
label_rm_time3.pack(side=tkinter.BOTTOM)
frame_room3.grid(row=1, column=0, ipadx=80, ipady=50, padx=5, pady=5, sticky="nsew")

# room 4 gui code
room = room_list.get_room(3)
frame_room4 = tkinter.Frame(master=window, bg="light green", relief=tkinter.GROOVE, borderwidth=2)
label_rm_num4 = tkinter.Label(master=frame_room4, bg="light green", font=myFont, text=f"Room {room.room_num}")
label_rm_num4.pack()
label_p_name4 = tkinter.Label(master=frame_room4, bg="light green", font=myFont, text=f"{room.patient}")
label_p_name4.pack(fill=tkinter.Y, expand=True)
label_rm_time4 = tkinter.Label(master=frame_room4, bg="light green", font=myFont, text=f"{room.est_time}")
label_rm_time4.pack(side=tkinter.BOTTOM)
frame_room4.grid(row=1, column=1, ipadx=80, ipady=50, padx=5, pady=5, sticky="nsew")

# patient text box entry and triage drop down gui code
frame_patients = tkinter.Frame(master=window)
frame_sub_patients1 = tkinter.Frame(master=frame_patients)
frame_sub_patients2 = tkinter.Frame(master=frame_patients)
label_p_name = tkinter.Label(master=frame_sub_patients1, font=myFont, text="Patient Name:")
label_p_name.pack(padx=10, pady=1)
p_name_text = tkinter.StringVar()
p_name_entry = tkinter.Entry(master=frame_sub_patients1, fg='black', bg='white', width=26, font=myFont, textvariable=p_name_text)
p_name_entry.pack(padx=15, pady=8)
label_priority = tkinter.Label(master=frame_sub_patients1, font=myFont, text="Triage Level:")
label_priority.pack()
priority_box = ttk.Combobox(master=frame_sub_patients1, width=10, values=['Mild', 'Moderate', 'Severe'])
priority_box.current(0)
priority_box.pack(padx=10, pady=1)
button_add_patient = tkinter.Button(master=frame_sub_patients2, text="Add Patient", font=myFont, command=click_add_patient)
button_add_patient.pack(side=tkinter.BOTTOM)
frame_sub_patients1.grid(row=0, column=0, padx=5)
frame_sub_patients2.grid(row=1, column=0, pady=10)
frame_patients.grid(row=2, column=0, columnspan=2)

# initializes a patient list
patient_list = PatientQueue()

# patient list gui code
frame_queue = tkinter.Frame(master=window)
frame_sub_queue = tkinter.Frame(master=frame_queue)
label_patient_name = tkinter.Label(master=frame_sub_queue, font=myFont, text="Patient Name")
label_patient_name.pack(side=tkinter.LEFT, padx=40)
label_triage = tkinter.Label(master=frame_sub_queue, font=myFont, text="Triage Level")
label_triage.pack(side=tkinter.LEFT, padx=20)
frame_sub_queue.grid(row=0, column=0)
label_patient_queue = tkinter.Label(master=frame_queue, font=myFont, text=f"{patient_list}")
label_patient_queue.grid(row=1, column=0)
frame_queue.grid(row=0, column=3, ipady=50)

# runs the gui
update_time(window)
window.mainloop()
