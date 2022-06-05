
# TDC Assignment

- Simple login page with Google Authentication with some styling along with a responsive navbar.
- A styled form containing a name field and dropdown fields with the Hover to dropdown effect. 
- For a given name, display some set of dropdown values, and for another name display some other sets of values.
  - Eg: 
    - name: x, dropdown: [a, b, c]
    - name: b, dropdown: [k, l, m]


## Getting Started

### Dependencies
- Python version 3.6 or above
- Django Framework
- Boostrap 5

### Installing

1. Clone the repo

   ```
   git clone https://github.com/AJ-Walker/TDC-Assignment.git 
   ```
    
2. Create virtual environment and activate 

   ```
   # On Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install Packages for running this API

   ```
   pip install -r requirements.txt

   ```

4. Running Django server

  ```
  python manage.py runserver

  ```

5. Open a browser and go to **[http://localhost:8000/u/](http://localhost:8000/u/)**
