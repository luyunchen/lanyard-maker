import pygame
import pandas as pd
import tkinter as tk

from items import draggableText
from tkinter import filedialog, simpledialog


tk.Tk().withdraw()
# Open file dialog to select a file
file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Excel 97-2003 files", "*.xls")])
if file_path:
    print("Selected file:", file_path)
    df = pd.read_excel(file_path)

width_in = simpledialog.askfloat("Width", "Enter the width of the paper in inches")
height_in = simpledialog.askfloat("Height", "Enter the height of the paper in inches")
pygame.init()
width = int(width_in*120)
height = int(height_in*120)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lanyard Designer")
# Create draggable texts with different initial positions
draggable_texts = []
x_offset = 50
y_offset = 50
for i, columnName in enumerate(df.columns):
    x = (i % 5) * x_offset + 50  # Adjust the x position
    y = (i // 5) * y_offset + 50  # Adjust the y position
    draggable_texts.append(draggableText(columnName, x, y, 20))
# Main loop
running = True

while running:
    screen.fill((255, 255, 255))  # White background
    for text in draggable_texts:
        text.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for text in draggable_texts:
            text.handle_event(event)

    pygame.display.flip()

pygame.quit()
