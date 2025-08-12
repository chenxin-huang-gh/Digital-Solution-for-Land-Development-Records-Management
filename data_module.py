"""This module is for manipulating the data sets. Since the original complete data
 sets are kept individually in the different institutions of Chinese governments and are
  confidential, I faked multiple partial data sets which are public with similar form and
   used to test my program.

Author : Chenxin Huang"""

# Import the pandas library, which is used for data manipulation and analysis.
import pandas as pd

# Define the data sets dictionary, which include the different information of one single construction project.
data = {
    'Project Name': ['Project A', 'Project B', 'Project C', 'Project D', 'Project E', 'Project F', 'Project G', 'Project H', 'Project I', 'Project J'],
    'City Planning Number': ['UPN001', 'UPN002', 'UPN003', 'UPN004', 'UPN005', 'UPN006', 'UPN007', 'UPN008', 'UPN009', 'UPN010'],
    'Land Supply Number': ['LSN001', 'LSN002', 'LSN003', 'LSN004', 'LSN005', 'LSN006', 'LSN007', 'LSN008', 'LSN009', 'LSN010'],
    'Building Permit Number': ['BCN001', 'BCN002', 'BCN003', 'BCN004', 'BCN005', 'BCN006', 'BCN007', 'BCN008', 'BCN009', 'BCN010'],
    'Cadastral Location': ['CL001', 'CL002', 'CL003', 'CL004', 'CL005', 'CL006', 'CL007', 'CL008', 'CL009', 'CL010'],
    'Real Estate Registration Name': ['RERN001', 'RERN002', 'RERN003', 'RERN004', 'RERN005', 'RERN006', 'RERN007', 'RERN008', 'RERN009', 'RERN010'],
    'Completion Status': ['Completed', 'In Progress', 'Completed', 'In Progress', 'Completed', 'In Progress', 'Completed', 'In Progress', 'Completed', 'In Progress'],
    'Street Address': ['Address 1', 'Address 2', 'Address 3', 'Address 4', 'Address 5', 'Address 6', 'Address 7', 'Address 8', 'Address 9', 'Address 10'],
    'Photo Filename': ['photoA.jpg', 'photoB.jpg', 'photoC.jpg', 'photoD.jpg', 'photoE.jpg', 'photoF.jpg', 'photoG.jpg', 'photoH.jpg', 'photoI.jpg', 'photoJ.jpg']
}

df = pd.DataFrame(data)
# Address to pixel mapping for the map.
address_to_pixel = {
    'Address 1': (270, 153),
    'Address 2': (298, 450),
    'Address 3': (198, 580),
    'Address 4': (400, 450),
    'Address 5': (430, 362),
    'Address 6': (610, 450),
    'Address 7': (695, 350),
    'Address 8': (695, 482),
    'Address 9': (584, 265),
    'Address 10': (350, 289)
}