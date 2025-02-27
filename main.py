import pygame
import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog
from items import draggableText

tk.Tk().withdraw()
# Open file dialog to select a file
file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Excel 97-2003 files", "*.xls")])
if file_path:
    print("Selected file:", file_path)
    df = pd.read_excel(file_path)

# Ask user for the dimensions of the lanyard paper in inches
width_in = simpledialog.askfloat("Width", "Enter the width of the paper in inches")
height_in = simpledialog.askfloat("Height", "Enter the height of the paper in inches")

# Convert inches to pixels (assuming 96 pixels per inch)
width = int(width_in * 96)
height = int(height_in * 96)

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            for text in draggable_texts:
                text.handle_resize(event.w, event.h)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for text in draggable_texts:
                    text.change_font_size(text.font_size + 5)
            elif event.key == pygame.K_DOWN:
                for text in draggable_texts:
                    text.change_font_size(max(5, text.font_size - 5))
        for text in draggable_texts:
            text.handle_event(event)
    
    for text in draggable_texts:
        text.draw(screen)

    pygame.display.flip()

pygame.quit()