# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:30:07 2023

@author: stani
"""

from Work import HabitTrackerApp

app = HabitTrackerApp()
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()