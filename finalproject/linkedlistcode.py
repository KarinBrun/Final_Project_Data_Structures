# Name: Final Project
# Author: Karin Brun
# Created: 10/28/2023
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
# Description: Linked list code for final project
#
# Academic Honesty: I attest that this is my original work.
#                   I have not used unauthorized source code,
#                   either modified or unmodified. I have not
#                   given other fellow student(s) access to my program.

import random
# imports linked list python library
from structlinks.DataStructures import LinkedList
from finalproject.validation import *


# linked list class RoomList
class RoomList:
    def __init__(self):
        self.llist = LinkedList()

    def __str__(self):
        return f"{self.llist}"

    # adds a room to the linked list
    def add_room(self, room):
        self.llist.append(room)

    # adds a patient to a room in linked list
    def patient_to_room(self, patient, priority):
        try:
            validate_numeric_priority(priority)
            validate_string_input(patient)
            patient_assigned = False
            for room in self.llist:
                if room.available_room() is True:
                    room.assign_patient(patient, priority)
                    patient_assigned = True
                    break
            if patient_assigned is True:
                return "Patient has been assigned to room."
            else:
                return "No room available."
        except InvalidInputCharacters:
            raise InvalidInputCharacters

    # updates the time remaining on a room in linked list
    def update_rooms(self, time_difference):
        for room in self.llist:
            room.update_time(time_difference)

    # returns the room at a given index of the linked list
    def get_room(self, room_index):
        return self.llist[room_index]


# class for room object
class Room:
    def __init__(self, room_num=None, patient="", est_time=0):
        self.room_num = room_num
        self.patient = patient
        self.est_time = est_time

    def __str__(self):
        return f"Room: {self.room_num}, Patient: {self.patient}, Estimated time until open: {self.est_time}\n"

    # assigns a patient and priority(triage) to a room
    def assign_patient(self, patient, priority):
        try:
            validate_numeric_priority(priority)
            validate_string_input(patient)
            self.patient = patient
            self.est_time = (4 - priority) * random.randrange(10, 50, 10)
        except InvalidInputCharacters:
            raise InvalidInputCharacters

    # clears room to default
    def clear_room(self):
        self.patient = ""
        self.est_time = 0

    # when estimated time reaches 0, makes the room available again
    def available_room(self):
        if self.est_time == 0:
            return True
        else:
            return False

    # updates time based on the time count given when room will be available
    def update_time(self, time_difference):
        self.est_time -= time_difference
        if self.est_time <= 0:
            self.clear_room()
