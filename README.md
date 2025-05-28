# Face Recognition Based Attendance Management System (FAMS)

## 📌 Overview

The **Face Recognition Based Attendance Management System (FAMS)** is a Python desktop application developed using `Tkinter`, `OpenCV`, and `MySQL`. It automates the attendance process using facial recognition technology to identify students and log their attendance, thereby reducing manual intervention and improving reliability and efficiency in institutional environments.

This project features both **automatic** and **manual** attendance recording modes and offers a user-friendly interface for managing student information and attendance records.


## 🧾 Abstract
The **Face Recognition-Based Attendance Management System (FAMS)** is an intelligent attendance tracking solution designed to automate and streamline the attendance recording process in academic institutions and organizations. Leveraging the power of computer vision and machine learning, this system employs facial recognition technology to identify individuals and mark their attendance with minimal human intervention.

Traditional attendance methods are time-consuming, error-prone, and vulnerable to manipulation (e.g., proxy attendance). To address these shortcomings, FAMS uses a webcam to capture real-time facial images and match them against a pre-trained dataset of registered students. The system utilizes the Local Binary Pattern Histogram (LBPH) algorithm, known for its robustness in real-world face recognition scenarios, to perform accurate identification.

The application is built using Python, with a user-friendly Tkinter GUI interface that allows users to:

Register new students by capturing facial images and storing metadata.

Train a face recognition model using the captured dataset.

Automatically recognize students during class sessions and record attendance.

Manually add attendance in case of technical constraints or unregistered individuals.

Export attendance records to CSV format for further use or reporting.

All attendance data is stored in a MySQL database for structured storage, and CSV files are generated for easy access and offline record-keeping. A secured admin panel enables authorized personnel to view registered student data and monitor attendance history.

By integrating OpenCV for real-time image processing, Pandas for data handling, and MySQL for database operations, FAMS delivers a complete and efficient attendance solution. The system reduces manual workload, enhances accuracy, ensures integrity, and paves the way for adopting intelligent automation in educational and corporate environments.


## 🧰 Tech Stack

- **Frontend**: Tkinter (Python GUI)
- **Backend**: Python
- **Database**: MySQL
- **Libraries Used**:
  - `OpenCV` – for image capturing and facial recognition
  - `Pandas` – for handling data
  - `PIL` – for image processing
  - `NumPy` – numerical operations
  - `pymysql` – MySQL connectivity


## 🎯 Features

- 📷 **Image Capture**: Capture 70+ facial samples of each student for model training.
- 🧠 **Model Training**: Train an LBPH (Local Binary Pattern Histogram) classifier.
- 🧍‍♂️ **Face Recognition**: Automatically recognize students and record their attendance.
- 📝 **Manual Entry**: GUI to manually enter attendance in case of recognition failure or absence of training.
- 📊 **Admin Panel**: View registered student details.
- 📁 **CSV Export**: Export attendance records to CSV files.
- 🛡️ **Authentication**: Simple admin authentication to view sensitive data.
- 🖥️ **Multi-Window GUI**: Separate interfaces for each major task.


## 📂 Project Structure

Face-Recognition-Attendance/

- TrainingImage/ # Captured student face images
 TrainingImageLabel/ # Trained LBPH model saved here
- StudentDetails/ # CSV storing enrollment and name
- Attendance/ # Auto & manual attendance CSVs
- AMS.py # Main application file
- haarcascade_frontalface_default.xml # OpenCV model for face detection
- README.md


## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MySQL server running on localhost
- Required Python libraries:
  ```bash
  pip install opencv-python-headless numpy pillow pandas pymysql
Database Setup
Ensure MySQL server is running.

The app automatically creates the database face_reco_fill and required tables on execution.

No need to manually configure the DB.

## 🧑‍💻 How to Use
1. Register a Student
Enter enrollment number and name.

![Screenshot 2025-05-28 220000](https://github.com/user-attachments/assets/f1b2958a-3fd4-4eda-93e1-e6e7e5c45600)


Click "Take Images" to capture training images.

2. Train the Model
After registration, click "Train Images" to train the recognition model.

3. Mark Attendance
For auto-mode, click "Automatic Attendance", enter subject, and let the camera recognize faces.

![Screenshot 2025-05-28 220055](https://github.com/user-attachments/assets/ae15fbe4-8b0b-4c14-97d1-47102f121115)

![Screenshot 2025-05-28 220250](https://github.com/user-attachments/assets/e28761f6-8831-4759-b23f-636143d8238a)

![Screenshot 2025-05-28 220321](https://github.com/user-attachments/assets/aedbe186-7def-4ae2-b9c1-2a4df02b37c8)


For manual-mode, click "Manually Fill Attendance", enter details manually.

![Screenshot 2025-05-28 220725](https://github.com/user-attachments/assets/175affae-ffe8-4a49-9247-1bf7da739ef5)

![Screenshot 2025-05-28 220747](https://github.com/user-attachments/assets/a04e12e1-ebf7-49cc-8d5a-a7577d8c4bed)



4. Admin Access
Use "Check Registered Students" to view all registered entries.

Username: Kumaraswamy

Password: Kumar@117

![Screenshot 2025-05-28 220839](https://github.com/user-attachments/assets/600b838f-4278-4fcc-b128-dd8ef4162db3)

![Screenshot 2025-05-28 220914](https://github.com/user-attachments/assets/62999b56-d4e9-4c20-9e72-d41b8e73b889)


## 📁 Output
All attendance records are saved as .csv in the Attendance/ directory.

Trained models and student data are stored locally.

## 💡 Future Enhancements
Integrate cloud storage for better scalability.

Add email/SMS notifications for attendance reports.

Improve GUI aesthetics and responsiveness.

Mobile support or web deployment.

## 🤝 Contributions
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 🛡️ License
This project is open-source and available under the MIT License.

## 📬 Contact
For queries, reach out via GitHub Issues or email: khandapukumar117@gmail.com

## 🧾 Acknowledgments
Thanks to the developers and open-source contributors whose tools and documentation made this possible.
