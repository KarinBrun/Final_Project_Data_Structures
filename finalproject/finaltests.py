# Name: Final Project
# Author: Karin Brun
# Created: 11/20/2023
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
# Description: Unit tests for final project
#
# Academic Honesty: I attest that this is my original work.
#                   I have not used unauthorized source code,
#                   either modified or unmodified. I have not
#                   given other fellow student(s) access to my program.

import unittest
# imports classes from other files
from finalproject.queuecode import PatientQueue
from finalproject.linkedlistcode import *
from finalproject.validation import *


# tests say which method they test and which file it attaches to
class FinalProjectTests(unittest.TestCase):
    def test_patient_queue_add_patient(self):
        test_queue = PatientQueue()
        test_queue.add_patient("Sally", 3)
        test_queue.add_patient("Bob", 1)
        test_queue.add_patient("George", 2)
        expected = "Bob - Severe\nSally - Mild\nGeorge - Moderate\n"
        self.assertEqual(expected, f"{test_queue}")

    def test_queue_invalid_add_patient(self):
        test_queue = PatientQueue()
        with self.assertRaises(InvalidInputCharacters):
            test_queue.add_patient(".", 1)
        with self.assertRaises(InvalidInputCharacters):
            test_queue.add_patient("Bob", 7)

    def test_patient_queue_next_in_line(self):
        test_queue = PatientQueue()
        test_queue.add_patient("Sally", 3)
        test_queue.add_patient("Bob", 1)
        test_queue.add_patient("George", 2)
        expected = (1, 'Bob')
        self.assertEqual(expected, test_queue.next_in_line())

    def test_patient_queue_remove_patient(self):
        test_queue = PatientQueue()
        test_queue.add_patient("Sally", 3)
        test_queue.add_patient("Bob", 1)
        test_queue.add_patient("George", 2)
        test_queue.remove_patient()
        expected = "George - Moderate\nSally - Mild\n"
        self.assertEqual(expected, f"{test_queue}")

    def test_room_assign_patient(self):
        test_room = Room(12)
        test_room.assign_patient("Bob", 1)
        expected = "Bob"
        self.assertEqual(expected, test_room.patient)
        self.assertTrue(30 <= test_room.est_time <= 150)

    def test_room_invalid_assign_patient(self):
        room_1 = Room(1)
        with self.assertRaises(InvalidInputCharacters):
            room_1.assign_patient(".", 3)
        with self.assertRaises(InvalidInputCharacters):
            room_1.assign_patient("Sally", 7)

    def test_room_clear_room(self):
        test_room = Room(13, "Ned", 20)
        test_room.clear_room()
        expected = ""
        expected_time = 0
        self.assertEqual(expected, test_room.patient)
        self.assertEqual(expected_time, test_room.est_time)

    def test_room_available_room(self):
        test_room1 = Room()
        test_room2 = Room(14, "Sally", 50)
        self.assertTrue(test_room1.available_room())
        self.assertFalse(test_room2.available_room())

    def test_room_update_time(self):
        test_room = Room(15, "George", 10)
        test_room.update_time(6)
        expected = 4
        self.assertEqual(expected, test_room.est_time)
        test_room.update_time(12)
        expected = 0
        expected_patient = ""
        self.assertEqual(expected, test_room.est_time)
        self.assertEqual(expected_patient, test_room.patient)

    def test_room_list_add_room(self):
        room_list1 = RoomList()
        room_1 = Room(1)
        room_2 = Room(2, "Bob", 50)
        room_3 = Room(3)
        room_4 = Room(4, "Ned", 20)
        room_list1.add_room(room_1)
        room_list1.add_room(room_2)
        room_list1.add_room(room_3)
        room_list1.add_room(room_4)
        expected = "[Room: 1, Patient: , Estimated time until open: 0\n" \
                   " -> Room: 2, Patient: Bob, Estimated time until open: 50\n" \
                   " -> Room: 3, Patient: , Estimated time until open: 0\n" \
                   " -> Room: 4, Patient: Ned, Estimated time until open: 20\n]"
        self.assertEqual(expected, f"{room_list1}")

    def test_room_list_patient_to_room(self):
        room_list1 = RoomList()
        room_1 = Room(1)
        room_2 = Room(2, "Bob", 50)
        room_list1.add_room(room_1)
        room_list1.add_room(room_2)
        expected = "Patient has been assigned to room."
        self.assertEqual(expected, room_list1.patient_to_room("Sally", 3))
        expected = "No room available."
        self.assertEqual(expected, room_list1.patient_to_room("Susan", 1))

    def test_room_list_invalid_patient_to_room(self):
        room_list1 = RoomList()
        room_1 = Room(1)
        room_list1.add_room(room_1)
        with self.assertRaises(InvalidInputCharacters):
            room_list1.patient_to_room(".", 3)
        with self.assertRaises(InvalidInputCharacters):
            room_list1.patient_to_room("Sally", 7)

    def test_room_list_update_rooms(self):
        room_list1 = RoomList()
        room_1 = Room(1, "Harry", 10)
        room_2 = Room(2, "Bob", 50)
        room_list1.add_room(room_1)
        room_list1.add_room(room_2)
        expected = "[Room: 1, Patient: , Estimated time until open: 0\n" \
                   " -> Room: 2, Patient: Bob, Estimated time until open: 40\n]"
        room_list1.update_rooms(10)
        self.assertEqual(expected, f"{room_list1}")


if __name__ == '__main__':
    unittest.main()
