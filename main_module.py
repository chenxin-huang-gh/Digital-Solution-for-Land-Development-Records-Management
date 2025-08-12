""" This project is designed to match and manage the multiple information of each
construction project throughout all its stages from land auction to completion record,
providin a convenient and efficient way for the public and the staff of government
departments in the urban construction management to inquire about the project specifying
its location on the map and exact picture more intuitively.

Author: Chenxin Huang"""

import sys
from PyQt5.QtWidgets import QApplication
from building_consent_tool_module import BuildingConsentTool

def main():
    """ The main function to start the building consent tool project."""
    app = QApplication(sys.argv)
    window = BuildingConsentTool()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()