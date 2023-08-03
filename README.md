<<<<<<< HEAD
# Project

This is the README file for the Django project. It provides an overview of the project, instructions for installation, usage, and other relevant information.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)


## Project Description

This project is a idea where we create tool that generate ads using openAI and lang chain.

## Installation

To run this Django project locally, follow the steps below:

1. Clone the repository:

   ```shell
   git clone https://github.com/accelmatic/ads-generator-tools.git
   ```

2. Navigate to the project directory:

   ```shell
   cd ads-generator-tools
   ```

3. Create a virtual environment:

   ```shell
   python3 -m venv env
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```shell
     source env/bin/activate
     ```

   - On Windows:

     ```shell
     env\Scripts\activate
     ```

5. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Perform database migrations:

   ```shell
   python manage.py makemigrations
   ``` 

   ```shell
   python manage.py migrate
   ```


## Usage

To start the Django development server, run the following command:

```shell
python manage.py runserver
```

Access the application in your web browser at `http://localhost:8000/` or server IP.
=======
