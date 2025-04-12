#!/usr/bin/env python3
#(c) Izudin Dzafic, 2023
import sys
import numpy as np
import matplotlib.pyplot as plt

args = len(sys.argv)-1
if args != 1:
    print('Missing input file name!')
    sys.exit()
    
# set dark background
plt.style.use('dark_background')
# Read the file and extract the relevant lines
lines = []
header = []
with open(sys.argv[1], 'r') as file:
    foundSolutionData = False
    headerLoaded = False
    firstHeaderLine = False
    secondHeaderLine = False
    for line in file:
        if foundSolutionData and firstHeaderLine and not headerLoaded:
            header = line.strip().split()
            headerLoaded = True
            print('Header is loaded')
        elif foundSolutionData:
            if not firstHeaderLine:
                if line.startswith('------'):
                    firstHeaderLine = True
                    continue
                else:
                    print('File is not formated properly! First line (--------) is not available!')
                    sys.exit()
            if not secondHeaderLine:       
                if line.startswith('------'):
                    secondHeaderLine = True
                    continue
                else:
                    print('File is not formated properly! Second line (--------) is not available!')
                    sys.exit()             
            if line.startswith('----'):
                print('Detected end of SOLUTION DATA')
                break
            lines.append(line)
        elif line.strip() == 'SOLUTION DATA':
            foundSolutionData = True
            print('Detected SOLUTION DATA')

# Parse the data
data = np.loadtxt(lines, dtype=float)

# Check if data is empty
if data.size == 0:
    print("No data found in the file.")
else:
    # Extract the columns
    columns_indices = [42, 43, 44, 45, 46, 47, 78, 79, 80]
    t = data[:, 0]
    columns = data[:, columns_indices].T
    
    # Plot the data
    for i, column in enumerate(columns):
        plt.plot(t, column, label=header[columns_indices[i]])

    # Add labels and legend
    if len(header) <= 11:
        xLbl = header[0]
        yLbl = ', '.join([header[i] for i in selected_column_indices]) 
        plt.xlabel(xLbl)
        plt.ylabel(yLbl)     
    else:
        plt.xlabel('Time (t) [s]')
        plt.ylabel('Multiple Values')
        
    plt.legend()
    
    # show grid
    plt.grid(linestyle='dotted', linewidth=1)
    
    # Display the plot
    plt.show()