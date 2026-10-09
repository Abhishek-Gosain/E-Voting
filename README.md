# E-Voting System

A desktop-assisted electronic voting project built with Python, OpenCV, SQLite, and an HTML/CSS web interface. The project explores voter registration, face recognition, voting workflows, result viewing, and feedback management.

## Features

* **Voter Registration:** Capture facial images and store voter details.
* **Face Recognition:** Use OpenCV-based face recognition as part of the voting workflow.
* **Voting Interface:** Browse candidates and explore voting-related functionality.
* **Results:** View election results through the project's result module.
* **Feedback:** Collect and store user feedback.
* **Database:** Use SQLite for voter information, votes, and feedback.
* **Web Interface:** HTML, CSS, and Bootstrap-based pages.

## Tech Stack

* **Language:** Python
* **Computer Vision:** OpenCV, NumPy
* **Image Processing:** Pillow
* **Database:** SQLite
* **Frontend:** HTML, CSS, Bootstrap
* **GUI:** Tkinter

## Project Structure

```text
e-voting-system/
├── Run from home.html/
│   ├── home.html
│   ├── login.html
│   ├── reg.html
│   ├── vote.html
│   ├── result.html
│   └── ...other web assets
├── Classifiers/
├── trainer/
├── vote.py
├── registration.py
├── result.py
├── feedback.py
├── image.py
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure above is illustrative. Update it to match the files actually included in the repository.*

## Installation

1. Install Python 3 and Git.

2. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   cd e-voting-system
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Open the `Run from home.html` folder and launch `home.html` in a browser to explore the web interface.

6. Run the Python modules separately only after reviewing their configuration, required files, and database setup.

## Learning Outcomes

This project provided practical exposure to Python application development, computer vision, facial image processing, database operations, and web interface development.

## Important Limitations

This is an educational project, not a production-ready election system. Face recognition can produce false matches, and the application requires security, privacy, authentication, vote-integrity, and database-validation improvements before any real-world use.

Do not use real voter information or biometric data in a public demonstration.

## License

Add a license after verifying that you have permission to redistribute all source code, images, fonts, and other assets included in the repository.
