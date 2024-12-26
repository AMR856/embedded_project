# Arduino Web IDE

<p align="center">
  <img src="./imgs/arduino_logo_1200x630-01.png" alt="Arduino Logo" />
</p>

## Steps to Run the Project

Follow the steps below to set up and run the Arduino Web IDE project.

### 1. Clone the Repository

Clone the repository from GitHub using the following command:

```bash
git clone https://github.com/AMR856/embedded_project.git
```

Switch to the `arduino_cli` branch:

```bash
git checkout arduino_cli
```

### 2. Set Up a Python Virtual Environment

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On Linux/MacOS:
  ```bash
  source venv/bin/activate
  ```

- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```

### 3. Install Backend Dependencies and Run the Server

Install the required dependencies for Flask:

```bash
pip install -r requirements.txt
```

Run the Flask server:

```bash
python app.py
```

### 4. Set Up and Run the Frontend

Navigate to the frontend directory:

```bash
cd ../frontend
```

Install the project dependencies:

```bash
npm install
```

Build the frontend project:

```bash
npm run build
```

Run the project in preview mode:

```bash
npm run preview
```

You can now access the Arduino Web IDE in your browser.
