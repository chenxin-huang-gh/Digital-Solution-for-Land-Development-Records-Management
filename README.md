# Building Consent Tool
A Python-based desktop application for managing and visualizing building consent data throughout the full lifecycle of construction projects. The tool enables users to search for projects by multiple identifiers, view related details, see geographic locations on a map, and preview associated photos.

# Features
Flexible search: Project Name, City Planning Number, Land Supply Number, Building Permit Number, Cadastral Location, Real Estate Registration Name, Completion Status.

Map visualization: Highlights the project location on a satellite map.

Photo preview: Displays facade renderings or actual project photos.

Modular design: Code is organized into separate modules for easy maintenance and scalability.

# Project Structure
python
Copy
Edit
### .
├── building_consent_tool_module.py       # Main GUI & search functionality  
├── data_module.py                        # Data processing & mapping  
├── image_dialog_module.py                # Displays project photos in dialog  
├── main_module.py                        # Entry point for running the app  
├── map.png                               # Map image used for visualization  
├── photos/                               # Folder containing project photos  
└── __pycache__/                          # Compiled Python files (ignored)  

# Requirements
Python 3.8 or higher

PyQt5

Pandas

# Install dependencies:

bash
Copy
Edit
pip install PyQt5 pandas
How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
Run the main module:

bash
Copy
Edit
python main_module.py
Example Usage
Select a search keyword from the dropdown menu.

Enter the keyword in the search box.

View matched project details, map location (red dot), and associated images.

# Future Improvements
Support for larger, more complex datasets

User authentication with role-based permissions

Enhanced UI/UX with interactive map tools

Feedback and complaint tracking module

# License
This project is open-source under the MIT License.
