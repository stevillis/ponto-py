# Ponto Py - Controle de Ponto

## Overview

**Ponto Py** is a time tracking application built with Python and Streamlit. It allows users to track their working hours, calculate total hours worked, and visualize the balance of hours against required working hours.

## Features

- Reads time tracking data from an Excel file.
- Calculates total working hours based on entry and exit times.
- Displays the total hours worked and the balance against required hours in a user-friendly dashboard.
- Formats the output to show hours and minutes clearly.

## Requirements

To run this application, you will need:

- Python 3.7 or higher
- Streamlit
- Pandas
- OpenPyXL (for reading Excel files)

You can install the required packages using pip:
```bash
pip install requirements.txt
```

## Usage

1. Clone the Repository:
    ```bash
    git clone https://github.com/stevillis/ponto-py.git
    cd ponto-py
    ```

2. Prepare Your Data:
Ensure you have an Excel file named out.xlsx in the parent directory of your project. The Excel file should contain the following columns:
- Data: The date of the work entries.
- Entrada1, Saída1: Entry and exit times for the first shift.
- Entrada2, Saída2: Entry and exit times for the second shift.
- Entrada3, Saída3: Entry and exit times for any additional shifts (optional).

3. Run the Application:
Execute the following command in your terminal:
    ```bash
    streamlit run app.py
    ```

4. View Your Dashboard:
Open your web browser and navigate to http://localhost:8501 to view your dashboard.
