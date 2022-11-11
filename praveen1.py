import os
#import tkinter as tk
import pyautogui
#from tkinter.filedialog import *
#from tkinter import filedialog






def screen():
    
    myScreen = pyautogui.screenshot()
    save_path = r'C:\Users\PRAVEENKUMAR\Desktop\p'
    myScreen.save(save_path+".png")
