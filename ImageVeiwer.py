from tkinter import Tk, Label, Toplevel
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter as tk

def open_image():
    # Create a new tkinter window
    root = Tk()
    root.title("Image")

    # Open the file dialog and get the path of the selected image file
    image_path = askopenfilename()

    # Open the image using PIL
    image = Image.open(image_path)

    # Convert the PIL image to a PhotoImage object
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = Label(root, image=photo)
    label.image = photo  # Keep a reference to the image object to prevent it from being garbage collected
    label.pack()

    # Create a new top-level window to display the data
    coords_window = Toplevel(root)
    coords_window.title("Data")
    coords_window.geometry("200x50")  # Set the size of the window
    coords_label = Label(coords_window, text="")
    coords_label.pack()
    color_label = Label(coords_window, text="")
    color_label.pack()


    # Update the coordinates label whenever the mouse is moved over the image
    def update_coords(event):
        # Get the color of the pixel under the mouse cursor
        r, g, b = image.getpixel((event.x, event.y))
        color = f"rgb({r}, {g}, {b})"

        coords_label.config(text=f"({event.x}, {event.y})")
        color_label.config(text=f"{color}")

    label.bind("<Motion>", update_coords)

    # Start the tkinter main loop
    root.mainloop()

# Call the function
open_image()
