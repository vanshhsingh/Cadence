import customtkinter
from tkinter import *
from PIL import Image, ImageDraw, ImageTk

app = customtkinter.CTk()
app.geometry("1200x600")
app.title("Cadence")

# background
canvas = Canvas(app, width=1500, height=800, bg="#404040", relief=FLAT, highlightthickness=0)
canvas.place(relx=0.5, rely=0, anchor=customtkinter.CENTER)
canvas.pack()

# Load the original image
original_image = Image.open("Cadence  KIVY\Image\Post.jpg")

# Resize the original image to the desired size
target_size = (300, 300)
original_image = original_image.resize(target_size, Image.LANCZOS)

# Create a circular mask
mask = Image.new("L", original_image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, original_image.size[0], original_image.size[1]), fill=255)

# Create a new image with the desired background color
background_color = "#404040"
background_image = Image.new("RGBA", original_image.size, background_color)

# Resize the circular image to match the resized original image
circular_image = Image.new("RGBA", original_image.size, 0)
circular_image.paste(original_image, mask=mask)

# Paste the circular image onto the background image
final_image = Image.alpha_composite(background_image, circular_image)

# Convert the final image to PhotoImage
final_image = ImageTk.PhotoImage(final_image)

# Create a CTkLabel with the final image
image_label = customtkinter.CTkLabel(app, image=final_image)
image_label.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)  # Center the circular image in the window

# background

frame = customtkinter.CTkFrame(master=app, width=1200, height=200, fg_color="#2D2D2D")
frame.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

# Add text above the frame
text_label = Label(app, text="Circles", fg="white", bg="#2D2D2D", font=("Arial", 25))
text_label.place(relx=0.5, rely=0.7, anchor='center')
text_label = Label(app, text="Post malone", fg="white", bg="#2D2D2D", font=("Arial", 14))
text_label.place(relx=0.5, rely=0.75, anchor='center')

# red bg
frame = customtkinter.CTkFrame(master=app, width=1200, height=200, fg_color="#832424")
frame.place(relx=0.5, rely=1, anchor=customtkinter.CENTER)

#play button
Button= customtkinter.CTkButton(master=app, text="play")
Button.place(relx = 0.5, rely=0.9, anchor=customtkinter.CENTER)
#previous button
Button= customtkinter.CTkButton(master=app, text="previous")
Button.place(relx = 0.3, rely=0.9, anchor=customtkinter.CENTER)
#next button
Button= customtkinter.CTkButton(master=app, text="next")
Button.place(relx = 0.7, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()
