# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:34:38 2023

@author: stani
"""

import unittest
from Work import HabitTrackerApp

class TestHabitTrackerApp(unittest.TestCase):
    def setUp(self):
        self.app = HabitTrackerApp()
        self.app.title("Test Habit Tracker")
        self.app.geometry("300x200")
        
    #test add_habit method    
    def test_add_habit(self):
        self.app.add_habit("test_add_habit", 7, "2023-10-17 20:00:00")
        self.assertIn("test_add_habit", self.app.habits)
        self.assertEqual(self.app.habits["test_add_habit"]["periodicity"], 7)       
        self.assertEqual(self.app.habits["test_add_habit"]["created_day"], "2023-10-17 20:00:00")
       
    #test temove_habit method    
    def test_remove_habit_with_habits(self):
        self.app.habits = {"Habit1": "Details1", "Habit2": "Details2"}  
        with self.subTest(msg="With habits case"):
            self.app.remove_habit()
            
            
    def tearDown(self):
        if hasattr(self.app, 'habit_remove_dialog'):
            self.app.habit_remove_dialog.destroy()
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()

