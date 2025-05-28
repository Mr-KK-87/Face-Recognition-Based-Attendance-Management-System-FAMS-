import tkinter as tk
from tkinter import messagebox
import cv2
import csv
import os
import numpy as np
from PIL import Image, ImageTk
import datetime
import time
import pymysql

# Ensure all required packages are installed
def check_dependencies():
    try:
        import pymysql
        import cv2
        import numpy as np
    except ModuleNotFoundError as e:
        print(f"Missing module: {e.name}. Please install it using 'pip install {e.name}'")
        exit(1)

check_dependencies()

# Window Configuration
window = tk.Tk()
window.title("FAMS - Face Recognition Based Attendance Management System")
window.geometry('1280x720')
window.configure(background='grey80')

# Database Connection Helper Function
def connect_db(db_name):
    try:
        return pymysql.connect(host='localhost', user='root', password='', db=db_name)
    except pymysql.MySQLError as e:
        print("Database Connection Error:", e)
        return None

# Function to Manually Fill Attendance
def manually_fill():
    sb = tk.Toplevel()
    sb.title("Enter subject name...")
    sb.geometry('580x320')
    sb.configure(background='grey80')
    
    def fill_attendance():
        subject = sub_entry.get().strip()
        if not subject:
            messagebox.showerror("Error", "Please enter a subject name!")
            return
        
        ts = time.time()
        date_for_db = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        db_table_name = f"{subject}_{date_for_db}_Time_{time_stamp.replace(':', '_')}"
        
        connection = connect_db('manually_fill_attendance')
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {db_table_name} (
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        ENROLLMENT VARCHAR(100) NOT NULL,
                        NAME VARCHAR(50) NOT NULL,
                        DATE VARCHAR(20) NOT NULL,
                        TIME VARCHAR(20) NOT NULL
                    )
                """)
                connection.commit()
            except pymysql.MySQLError as e:
                print("Error creating table:", e)
    
    tk.Label(sb, text="Enter Subject:", width=15, height=2, fg="black", bg="grey80", font=('times', 15, 'bold')).place(x=30, y=100)
    sub_entry = tk.Entry(sb, width=20, font=('times', 23))
    sub_entry.place(x=250, y=105)
    tk.Button(sb, text="Fill Attendance", command=fill_attendance, bg="SkyBlue1", font=('times', 15, 'bold')).place(x=250, y=160)
    sb.mainloop()

# Function to Train the Model
def training():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    def get_images_and_labels(path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        face_samples, ids = [], []
        for image_path in image_paths:
            pil_image = Image.open(image_path).convert('L')
            image_np = np.array(pil_image, 'uint8')
            face_id = int(os.path.split(image_path)[-1].split(".")[1])
            faces = detector.detectMultiScale(image_np)
            for (x, y, w, h) in faces:
                face_samples.append(image_np[y:y+h, x:x+w])
                ids.append(face_id)
        return face_samples, ids
    
    try:
        faces, ids = get_images_and_labels("TrainingImage")
        recognizer.train(faces, np.array(ids))
        recognizer.save("TrainingImageLabel/Trainner.yml")
        messagebox.showinfo("Success", "Model Trained Successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Training Failed: {e}")

# GUI Layout
message = tk.Label(window, text="Face Recognition-Based Attendance Management System", bg="black", fg="white", width=50, height=3, font=('times', 30, 'bold'))
message.place(x=80, y=20)

train_img_btn = tk.Button(window, text="Train Images", command=training, bg="SkyBlue1", width=20, height=3, font=('times', 15, 'bold'))
train_img_btn.place(x=390, y=500)

manual_attendance_btn = tk.Button(window, text="Manually Fill Attendance", command=manually_fill, bg="SkyBlue1", width=20, height=3, font=('times', 15, 'bold'))
manual_attendance_btn.place(x=990, y=500)

window.mainloop()
