import sys
from PIL import ImageTk, Image
import requests
from tkinter import messagebox
import json
from functools import partial
import tkinter.scrolledtext as scrolledtext
import os
import os.path

import tkinter as tk
import tkinter.ttk as ttk

size_x, size_y = {512, 384}


LOGIN_URL = "http://localhost:8000/api-token-auth/"




def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None