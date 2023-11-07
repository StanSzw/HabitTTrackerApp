

import unittest
import tkinter as tk
from StreakStat import StreakStatistics  # Import your actual module

class TestStreakStatistics(unittest.TestCase):

    def setUp(self):
        # Create a sample habit dictionary for testing
        self.sample_habits = {
            'Habit1': {'completed_dates': ['2023-10-10'], 'periodicity': 1},
            'Habit2': {'completed_dates': ['2023-10-10', '2023-10-15'], 'periodicity': 5},
            'Habit3': {'completed_dates': [], 'periodicity': 2},
        }
        self.root = tk.Tk()

   
    def test_update_streak(self):
        streak_stats = StreakStatistics(self.root, self.sample_habits)
        habit_to_test = 'Habit1'

        # Add a new completed date for 'Habit1'
        streak_stats.habits[habit_to_test]['completed_dates'].append('2023-10-11')
        streak_stats.update_streak(habit_to_test)

        # Verify that the current streak for 'Habit1' is updated
        self.assertEqual(streak_stats.habits[habit_to_test]['current_streak'], 2)
        
    def test_get_habit_streaks(self):
        streak_stats = StreakStatistics(self.root, self.sample_habits)
        habit_streaks = streak_stats.get_habit_streaks()

        # Verify that the habit streaks are calculated correctly
        self.assertEqual(habit_streaks, {'Habit1': 1, 'Habit2': 2, 'Habit3': 0})    

    

    def tearDown(self):
        self.root.destroy()

    

    

if __name__ == '__main__':
    unittest.main()
