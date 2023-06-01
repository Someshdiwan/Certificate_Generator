from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
import os.path
from tkinter import messagebox

# Create a function to generate the certificate
def generate_certificate():
    # Get the student's name and score from the input fields
    name = student_name_field.get()
    score = score_field.get()
    date = date_field.get()

    # Create a certificate template
    template_file = "certificate_template.jpg"
    if not os.path.isfile(template_file):
        messagebox.showerror("Error", "Certificate template file not found.")
        return
    img = Image.open(template_file)

    # Add the student's name and score to the template
    draw = ImageDraw.Draw(img)
    font1 = ImageFont.truetype("C:/Certificate_Generator/anastasia-script.ttf", 50)
    font2 = ImageFont.truetype("C:/Certificate_Generator/Polaris.ttf", 50)
    draw.text((867,703 ), "{}".format(name), fill=(195, 154, 92), font=font1)
    draw.text((466, 1137), "{}".format(score), fill=(0, 0, 0), font=font2)
    draw.text((1372, 1133), "{}".format(date), fill=(0, 0, 0), font=font2)

    # Save the certificate as a jpg file with a filename based on the student's name
    filename = "{}_certificate.jpg".format(name)
    img.save(filename)

    # Update the status field to indicate the certificate has been generated
    output_field.delete(0, tk.END)
    output_field.insert(0, "Certificate generated as {}".format(filename))

    # Ask user if they want to open the certificate file
    open_file = messagebox.askyesno("Open File", "Do you want to open the certificate file?")

    # Open the certificate file using the default image viewer if user clicked "Yes"
    if open_file:
        os.startfile(filename)

# Create a window
window = tk.Tk()
window.title("Certificate Generator")

# Create input fields for the student's name and score
name_label = tk.Label(window, text="Student Name:")
name_label.grid(row=0, column=0)
student_name_field = tk.Entry(window)
student_name_field.grid(row=0, column=1)

score_label = tk.Label(window, text="Score:")
score_label.grid(row=1, column=0)
score_field = tk.Entry(window)
score_field.grid(row=1, column=1)

date_label = tk.Label(window, text="Date:")
date_label.grid(row=2, column=0)
date_field = tk.Entry(window)
date_field.grid(row=2, column=1)

# Create a button to generate the certificate
generate_button = tk.Button(window, text="Generate Certificate", command=generate_certificate)
generate_button.grid(row=3, column=0, columnspan=2)

# Create an output field to display a message indicating the certificate has been generated
output_label = tk.Label(window, text="Status:")
output_label.grid(row=4, column=0)
output_field = tk.Entry(window)
output_field.grid(row=4, column=1)

# Start the main loop
window.mainloop()