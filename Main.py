import tkinter

import customtkinter
import cv2

import AI
import HandDetection

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x350")


def HandDetect():
    HandDetection.HandDetection();


def FacialRecognition():
    AI.AIENCODING()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

button = customtkinter.CTkButton(master=frame, text="FacialRecognition", command=FacialRecognition)
button.pack(pady=12, padx=10)

# create a second button
button2 = customtkinter.CTkButton(master=frame, text="HandDetection", command=HandDetect)
button2.pack(pady=12, padx=10)
root.mainloop()
