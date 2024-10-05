# Bank Record Storage System Using Blockchain

## Overview

The **Bank Record Storage System Using Blockchain** is a web application that utilizes blockchain technology to securely store and manage bank transaction records. This system allows users to add new records of transactions and view the complete ledger of transactions, ensuring transparency and security.

## Features

- Add transaction records (sender, receiver, amount)
- View the complete blockchain ledger
- Validate the integrity of the blockchain

## Technologies Used

- [Streamlit](https://streamlit.io/) for the web application interface
- Python for backend logic
- Blockchain concepts for secure data management

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Shreyasaraf01/Bank-Record-Storage-System.git
   
2. Navigate into the project directory:
   ```bash
   cd Bank-Record-Storage-System
   
3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
4. Activate the virtual environment:
   
   -> On Windows:
   ```bash
     venv\Scripts\activate 
     ```
   -> On macOS/Linux:
   ```bash
     source venv/bin/activate

6. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Running the Application
Once everything is set up, you can run the application using the following command:
```bash
streamlit run app.py
```
This will start a Streamlit server, and you can view the application in your web browser at http://localhost:8501.

## Usage
-> Enter the sender, receiver, and amount in the input fields.

-> Click "Add Block" to create a new transaction record.

-> View the blockchain ledger to see all transaction records.

-> You can validate the blockchain to ensure its integrity.
