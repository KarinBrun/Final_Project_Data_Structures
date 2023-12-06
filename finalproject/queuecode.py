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
# Description: Queue code for final project
#
# Academic Honesty: I attest that this is my original work.
#                   I have not used unauthorized source code,
#                   either modified or unmodified. I have not
#                   given other fellow student(s) access to my program.

# python library for priority queues
from queue import PriorityQueue
from finalproject.validation import *


# class for priority queue PatientQueue
class PatientQueue:
    def __init__(self):
        self.queue = PriorityQueue()

    def __str__(self):
        string = ""
        priority = ""
        for patient in self.queue.queue:
            match patient[0]:
                case 3:
                    priority = "Mild"
                case 2:
                    priority = "Moderate"
                case 1:
                    priority = "Severe"
            string += f"{patient[1]} - {priority}\n"
        return string

    # adds patient to priority queue
    def add_patient(self, patient, priority):
        try:
            validate_numeric_priority(priority)
            validate_string_input(patient)
            self.queue.put((priority, patient))
        except InvalidInputCharacters:
            raise InvalidInputCharacters

    # displays first patient in priority queue
    def next_in_line(self):
        return self.queue.queue[0]

    # removes first patient from priority queue and returns priority queue
    def remove_patient(self):
        return self.queue.get()

    # shows if queue is empty
    def empty(self):
        return self.queue.empty()
