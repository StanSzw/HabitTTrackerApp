# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:11:30 2023

@author: stani
"""
import tkinter as tk
from tkinter import messagebox
import datetime


#The class to count and manage statistics of the application
class StreakStatistics:
    def __init__(self, root, habits):
        self.root = root
        self.habits = habits


    #Display list of habits with missing check-off
    def show_broken_streaks(self):
        if not self.habits:
            messagebox.showinfo("No Habits", "There are no habits to show.")
            return

        missing_streaks_dialog = tk.Toplevel(self.root)
        missing_streaks_dialog.title("Missing Check-offs")
        missing_streaks_dialog.geometry("300x200")

        for habit, data in self.habits.items():
            completed_dates = data['completed_dates']
            periodicity = data['periodicity']
            streak_break_count = 0

            if not completed_dates:
                missing_checkoff_label = tk.Label(missing_streaks_dialog, text=f"Missing check-off: {habit}")
                missing_checkoff_label.pack()

            else:
                last_completed_date = datetime.datetime.strptime(completed_dates[-1], '%Y-%m-%d').date()
                while last_completed_date < datetime.date.today():
                    next_due_date = last_completed_date + datetime.timedelta(days=periodicity)
                    if next_due_date <= datetime.date.today():
                        streak_break_count += 1
                        last_completed_date = next_due_date
                    else:
                        break

                if streak_break_count > 0:
                    broken_streak_label = tk.Label(missing_streaks_dialog, text=f"Broken streak for {habit} ({streak_break_count} times).")
                    broken_streak_label.pack()
    
    #updateing the streak                
    def update_streak(self, habit):
            completed_dates = self.habits[habit]['completed_dates']
            current_streak = 0
            
            if completed_dates:
                last_completed_date = datetime.datetime.strptime(completed_dates[-1], '%Y-%m-%d').date()
                current_date = datetime.date.today()
                delta = current_date - last_completed_date
        
                if delta.days == 0 or delta.days % self.habits[habit]['periodicity'] == 0:
                    current_streak = 1
        
                    for i in range(len(completed_dates) - 2, -1, -1):
                        previous_date = datetime.datetime.strptime(completed_dates[i], '%Y-%m-%d').date()
                        if (last_completed_date - previous_date).days == 1:
                            current_streak += 1
                            last_completed_date = previous_date
                        else:
                            break
        
            self.habits[habit]['current_streak'] = current_streak
            
    #recounting habits streaks       
    def get_habit_streaks(self):
            habit_streaks = {}
            for habit, data in self.habits.items():
                if 'current_streak' in data:
                    current_streak = data['current_streak']
                else:
                    current_streak = 0
                habit_streaks[habit] = current_streak
            return habit_streaks
       
        
    #displaying the streak   
    def display_habit_streaks(self):
            habit_streaks = self.get_habit_streaks()
        
            habit_list = tk.Toplevel(self.root)
            habit_list.title("Habit Streaks")
            habit_list.geometry("200x300")
        
            listbox = tk.Listbox(habit_list)
            listbox.pack(fill=tk.BOTH, expand=True)
        
            for habit, streak in habit_streaks.items():
                listbox.insert(tk.END, f"{habit}: {streak}")
        
            
    #Display the longest streak     
    def get_longest_streak(self):
             longest_streak = 0
             for habit in self.habits.values():
                 if 'current_streak' in habit:
                     current_streak = habit['current_streak']
                     if current_streak > longest_streak:
                         longest_streak = current_streak
             messagebox.showinfo("Longest Streak", f"The longest streak is {longest_streak}.")      