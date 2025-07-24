# finalproject
# FileReader Project

This project implements a custom Python class to read and manipulate files using modern Python features.  
It also includes a colorful countdown timer and code style/linting with Black and Pylint.
---
Features
- Decorator for colored terminal output.
- Colorful countdown timer function.
- Automated testing with pytest.
- Code formatting and linting with black and pylint.
- Continuous Integration with GitHub Actions.

---

Setup & Usage

All steps can be done through VS Code and GitHub Desktop.

1. Clone finalproject  with GitHub Desktop.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment:
    - Open the terminal in VS Code.
    - Run:
      
     “ python -m venv .venv”
     
    - Activate the environment:
      - Windows:
        
        .\.venv\Scripts\activate
        
      - Mac/Linux:
        
        source .venv/bin/activate
        

4. Install dependencies:
    
    pip install black pylint pytest
    

5. Run the main program:
    
    python main1.py
    

6. Run tests:
    
    pytest
    

7. Format your code:
    
    black .
    

8. Lint your code:
    
    pylint main1.py
    

---

GitHub Actions

Every time you push code, GitHub Actions will:
- Check your code formatting with Black.
- Lint your code with Pylint.

You can see the results under the *Actions* tab in your GitHub repository.

---

Project Files

- main1.py - Main code with all classes and features.
- Test_main1.py - All automated test cases.
- .github/workflows/ - CI configuration for Black & Pylint.

---

Authors

- Elie Hanna, Karim Mohamed Abdeldayem, Youssef Abdelrahman

---
