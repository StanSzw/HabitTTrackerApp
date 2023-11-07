Habit Tracker ReadMe

This document introduces a Python application designed for habit tracking and management. It utilizes a graphical user interface (GUI) created with the Tkinter library. The application serves several functions, allowing you to:

Add New Habits: Easily add new habits to track, specifying their periodicity.

Check Off Habits: Mark habits as completed for the current day.

View Habit Statistics: Gain insights into your habits, including your current streaks, longest streak, missed check-offs, and habits organized by their periodicity.

Remove Habits: Remove habits from your list when they are no longer relevant.

Save Progress: Save your habit data and its progress to a JSON file for future reference.

Prerequisites:

Python 3.x
Tkinter library (usually included with Python)
How to Use:

Run the "HabitTrackerApp" class to launch the application.

The main window of the application opens, offering the following options:

"Add New Habit": Click to add a new habit, providing its name and periodicity (the time between repetitions).

"See My Habits": View a list of all your tracked habits.

"Check off Habit": Mark a habit as completed for the day.

"Statistics": Access various statistics about your habits, including current streaks, longest streak, missed check-offs, and habits grouped by periodicity.

"Remove Habit": Remove a habit from your list when necessary.

When you add a new habit, it gets saved, and you can start tracking it immediately.

Checking off a habit updates your progress, and you can monitor your streaks and other statistics in the "Statistics" menu.

You can remove a habit from your list using the "Remove Habit" option.

Your habits and their progress are automatically saved to a JSON file named "habits.json." This file is loaded when you run the application, ensuring you can continue tracking your habits even after closing the application.

Streak Statistics:

The application employs the "StreakStatistics" class to calculate and manage your streaks. It offers the following features:

Displaying a list of habits with missing check-offs.
Updating and displaying the current streak for each habit.
Determining and displaying the longest streak among your habits.
Data Storage:

Your habit data and progress are stored in a JSON file named "habits.json." This file is loaded when you start the application and is saved each time you add, check off, or remove habits. This ensures that your data persists across different application sessions.

Please note that the application assumes that habit periodicity is measured in days. For instance, if a habit has a periodicity of 7, you should check it off once a week.
