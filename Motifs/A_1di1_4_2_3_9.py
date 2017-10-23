'''
FUNC:A_1di1_4_2_3_9
PDB:1di1
EC:4.2.3.9
RESI:tyr,phe,phe,trp
LOCI:a-92,112,178,333;
'''
import motifFunctions as cmd
TYR_TRP = { 
	'distances':
		[[9.93, 10.3, 11.03, 10.37, 11.53, 11.17, 10.13, 11.71, 10.72, 11.49], [9.16, 9.49, 10.35, 9.39, 10.78, 10.25, 8.96, 10.71, 9.48, 10.34], [8.02, 8.2, 9.04, 8.05, 9.41, 8.87, 7.68, 9.34, 8.21, 9.02], [9.85, 10.22, 11.22, 10.0, 11.61, 10.94, 9.35, 11.29, 9.76, 10.73], [7.63, 7.72, 8.7, 7.32, 8.96, 8.2, 6.69, 8.54, 7.1, 8.02], [9.56, 9.88, 10.97, 9.48, 11.28, 10.45, 8.63, 10.69, 8.91, 9.97], [8.5, 8.69, 9.78, 8.17, 10.02, 9.12, 7.29, 9.33, 7.54, 8.6], [8.64, 8.74, 9.89, 8.01, 10.01, 8.95, 6.9, 9.0, 6.93, 8.06]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'TRP', 9.93), ('CB', 'TYR', 'CG', 'TRP', 10.3), ('CB', 'TYR', 'CD1', 'TRP', 11.03), ('CB', 'TYR', 'CD2', 'TRP', 10.37), ('CB', 'TYR', 'NE1', 'TRP', 11.53), ('CB', 'TYR', 'CE2', 'TRP', 11.17), ('CB', 'TYR', 'CE3', 'TRP', 10.13), ('CB', 'TYR', 'CZ2', 'TRP', 11.71), ('CB', 'TYR', 'CZ3', 'TRP', 10.72), ('CB', 'TYR', 'CH2', 'TRP', 11.49)], [('CG', 'TYR', 'CB', 'TRP', 9.16), ('CG', 'TYR', 'CG', 'TRP', 9.49), ('CG', 'TYR', 'CD1', 'TRP', 10.35), ('CG', 'TYR', 'CD2', 'TRP', 9.39), ('CG', 'TYR', 'NE1', 'TRP', 10.78), ('CG', 'TYR', 'CE2', 'TRP', 10.25), ('CG', 'TYR', 'CE3', 'TRP', 8.96), ('CG', 'TYR', 'CZ2', 'TRP', 10.71), ('CG', 'TYR', 'CZ3', 'TRP', 9.48), ('CG', 'TYR', 'CH2', 'TRP', 10.34)], [('CD1', 'TYR', 'CB', 'TRP', 8.02), ('CD1', 'TYR', 'CG', 'TRP', 8.2), ('CD1', 'TYR', 'CD1', 'TRP', 9.04), ('CD1', 'TYR', 'CD2', 'TRP', 8.05), ('CD1', 'TYR', 'NE1', 'TRP', 9.41), ('CD1', 'TYR', 'CE2', 'TRP', 8.87), ('CD1', 'TYR', 'CE3', 'TRP', 7.68), ('CD1', 'TYR', 'CZ2', 'TRP', 9.34), ('CD1', 'TYR', 'CZ3', 'TRP', 8.21), ('CD1', 'TYR', 'CH2', 'TRP', 9.02)], [('CD2', 'TYR', 'CB', 'TRP', 9.85), ('CD2', 'TYR', 'CG', 'TRP', 10.22), ('CD2', 'TYR', 'CD1', 'TRP', 11.22), ('CD2', 'TYR', 'CD2', 'TRP', 10.0), ('CD2', 'TYR', 'NE1', 'TRP', 11.61), ('CD2', 'TYR', 'CE2', 'TRP', 10.94), ('CD2', 'TYR', 'CE3', 'TRP', 9.35), ('CD2', 'TYR', 'CZ2', 'TRP', 11.29), ('CD2', 'TYR', 'CZ3', 'TRP', 9.76), ('CD2', 'TYR', 'CH2', 'TRP', 10.73)], [('CE1', 'TYR', 'CB', 'TRP', 7.63), ('CE1', 'TYR', 'CG', 'TRP', 7.72), ('CE1', 'TYR', 'CD1', 'TRP', 8.7), ('CE1', 'TYR', 'CD2', 'TRP', 7.32), ('CE1', 'TYR', 'NE1', 'TRP', 8.96), ('CE1', 'TYR', 'CE2', 'TRP', 8.2), ('CE1', 'TYR', 'CE3', 'TRP', 6.69), ('CE1', 'TYR', 'CZ2', 'TRP', 8.54), ('CE1', 'TYR', 'CZ3', 'TRP', 7.1), ('CE1', 'TYR', 'CH2', 'TRP', 8.02)], [('CE2', 'TYR', 'CB', 'TRP', 9.56), ('CE2', 'TYR', 'CG', 'TRP', 9.88), ('CE2', 'TYR', 'CD1', 'TRP', 10.97), ('CE2', 'TYR', 'CD2', 'TRP', 9.48), ('CE2', 'TYR', 'NE1', 'TRP', 11.28), ('CE2', 'TYR', 'CE2', 'TRP', 10.45), ('CE2', 'TYR', 'CE3', 'TRP', 8.63), ('CE2', 'TYR', 'CZ2', 'TRP', 10.69), ('CE2', 'TYR', 'CZ3', 'TRP', 8.91), ('CE2', 'TYR', 'CH2', 'TRP', 9.97)], [('CZ', 'TYR', 'CB', 'TRP', 8.5), ('CZ', 'TYR', 'CG', 'TRP', 8.69), ('CZ', 'TYR', 'CD1', 'TRP', 9.78), ('CZ', 'TYR', 'CD2', 'TRP', 8.17), ('CZ', 'TYR', 'NE1', 'TRP', 10.02), ('CZ', 'TYR', 'CE2', 'TRP', 9.12), ('CZ', 'TYR', 'CE3', 'TRP', 7.29), ('CZ', 'TYR', 'CZ2', 'TRP', 9.33), ('CZ', 'TYR', 'CZ3', 'TRP', 7.54), ('CZ', 'TYR', 'CH2', 'TRP', 8.6)], [('OH', 'TYR', 'CB', 'TRP', 8.64), ('OH', 'TYR', 'CG', 'TRP', 8.74), ('OH', 'TYR', 'CD1', 'TRP', 9.89), ('OH', 'TYR', 'CD2', 'TRP', 8.01), ('OH', 'TYR', 'NE1', 'TRP', 10.01), ('OH', 'TYR', 'CE2', 'TRP', 8.95), ('OH', 'TYR', 'CE3', 'TRP', 6.9), ('OH', 'TYR', 'CZ2', 'TRP', 9.0), ('OH', 'TYR', 'CZ3', 'TRP', 6.93), ('OH', 'TYR', 'CH2', 'TRP', 8.06)]]}
PHE_PHE = { 
	'distances':
		[[13.06, 11.68, 11.58, 10.67, 10.48, 9.43, 9.32], [12.64, 11.24, 10.97, 10.39, 9.83, 9.15, 8.82], [12.29, 10.96, 10.73, 10.18, 9.69, 9.07, 8.79], [12.84, 11.38, 10.92, 10.65, 9.67, 9.35, 8.78], [12.14, 10.83, 10.43, 10.25, 9.41, 9.2, 8.72], [12.7, 11.25, 10.63, 10.71, 9.38, 9.47, 8.71], [12.35, 10.98, 10.38, 10.51, 9.24, 9.4, 8.68], [13.06, 12.64, 12.29, 12.84, 12.14, 12.7, 12.35], [11.68, 11.24, 10.96, 11.38, 10.83, 11.25, 10.98], [11.58, 10.97, 10.73, 10.92, 10.43, 10.63, 10.38], [10.67, 10.39, 10.18, 10.65, 10.25, 10.71, 10.51], [10.48, 9.83, 9.69, 9.67, 9.41, 9.38, 9.24], [9.43, 9.15, 9.07, 9.35, 9.2, 9.47, 9.4], [9.32, 8.82, 8.79, 8.78, 8.72, 8.71, 8.68]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'PHE', 13.06), ('CB', 'PHE', 'CG', 'PHE', 11.68), ('CB', 'PHE', 'CD1', 'PHE', 11.58), ('CB', 'PHE', 'CD2', 'PHE', 10.67), ('CB', 'PHE', 'CE1', 'PHE', 10.48), ('CB', 'PHE', 'CE2', 'PHE', 9.43), ('CB', 'PHE', 'CZ', 'PHE', 9.32)], [('CG', 'PHE', 'CB', 'PHE', 12.64), ('CG', 'PHE', 'CG', 'PHE', 11.24), ('CG', 'PHE', 'CD1', 'PHE', 10.97), ('CG', 'PHE', 'CD2', 'PHE', 10.39), ('CG', 'PHE', 'CE1', 'PHE', 9.83), ('CG', 'PHE', 'CE2', 'PHE', 9.15), ('CG', 'PHE', 'CZ', 'PHE', 8.82)], [('CD1', 'PHE', 'CB', 'PHE', 12.29), ('CD1', 'PHE', 'CG', 'PHE', 10.96), ('CD1', 'PHE', 'CD1', 'PHE', 10.73), ('CD1', 'PHE', 'CD2', 'PHE', 10.18), ('CD1', 'PHE', 'CE1', 'PHE', 9.69), ('CD1', 'PHE', 'CE2', 'PHE', 9.07), ('CD1', 'PHE', 'CZ', 'PHE', 8.79)], [('CD2', 'PHE', 'CB', 'PHE', 12.84), ('CD2', 'PHE', 'CG', 'PHE', 11.38), ('CD2', 'PHE', 'CD1', 'PHE', 10.92), ('CD2', 'PHE', 'CD2', 'PHE', 10.65), ('CD2', 'PHE', 'CE1', 'PHE', 9.67), ('CD2', 'PHE', 'CE2', 'PHE', 9.35), ('CD2', 'PHE', 'CZ', 'PHE', 8.78)], [('CE1', 'PHE', 'CB', 'PHE', 12.14), ('CE1', 'PHE', 'CG', 'PHE', 10.83), ('CE1', 'PHE', 'CD1', 'PHE', 10.43), ('CE1', 'PHE', 'CD2', 'PHE', 10.25), ('CE1', 'PHE', 'CE1', 'PHE', 9.41), ('CE1', 'PHE', 'CE2', 'PHE', 9.2), ('CE1', 'PHE', 'CZ', 'PHE', 8.72)], [('CE2', 'PHE', 'CB', 'PHE', 12.7), ('CE2', 'PHE', 'CG', 'PHE', 11.25), ('CE2', 'PHE', 'CD1', 'PHE', 10.63), ('CE2', 'PHE', 'CD2', 'PHE', 10.71), ('CE2', 'PHE', 'CE1', 'PHE', 9.38), ('CE2', 'PHE', 'CE2', 'PHE', 9.47), ('CE2', 'PHE', 'CZ', 'PHE', 8.71)], [('CZ', 'PHE', 'CB', 'PHE', 12.35), ('CZ', 'PHE', 'CG', 'PHE', 10.98), ('CZ', 'PHE', 'CD1', 'PHE', 10.38), ('CZ', 'PHE', 'CD2', 'PHE', 10.51), ('CZ', 'PHE', 'CE1', 'PHE', 9.24), ('CZ', 'PHE', 'CE2', 'PHE', 9.4), ('CZ', 'PHE', 'CZ', 'PHE', 8.68)], [('CB', 'PHE', 'CB', 'PHE', 13.06), ('CB', 'PHE', 'CG', 'PHE', 12.64), ('CB', 'PHE', 'CD1', 'PHE', 12.29), ('CB', 'PHE', 'CD2', 'PHE', 12.84), ('CB', 'PHE', 'CE1', 'PHE', 12.14), ('CB', 'PHE', 'CE2', 'PHE', 12.7), ('CB', 'PHE', 'CZ', 'PHE', 12.35)], [('CG', 'PHE', 'CB', 'PHE', 11.68), ('CG', 'PHE', 'CG', 'PHE', 11.24), ('CG', 'PHE', 'CD1', 'PHE', 10.96), ('CG', 'PHE', 'CD2', 'PHE', 11.38), ('CG', 'PHE', 'CE1', 'PHE', 10.83), ('CG', 'PHE', 'CE2', 'PHE', 11.25), ('CG', 'PHE', 'CZ', 'PHE', 10.98)], [('CD1', 'PHE', 'CB', 'PHE', 11.58), ('CD1', 'PHE', 'CG', 'PHE', 10.97), ('CD1', 'PHE', 'CD1', 'PHE', 10.73), ('CD1', 'PHE', 'CD2', 'PHE', 10.92), ('CD1', 'PHE', 'CE1', 'PHE', 10.43), ('CD1', 'PHE', 'CE2', 'PHE', 10.63), ('CD1', 'PHE', 'CZ', 'PHE', 10.38)], [('CD2', 'PHE', 'CB', 'PHE', 10.67), ('CD2', 'PHE', 'CG', 'PHE', 10.39), ('CD2', 'PHE', 'CD1', 'PHE', 10.18), ('CD2', 'PHE', 'CD2', 'PHE', 10.65), ('CD2', 'PHE', 'CE1', 'PHE', 10.25), ('CD2', 'PHE', 'CE2', 'PHE', 10.71), ('CD2', 'PHE', 'CZ', 'PHE', 10.51)], [('CE1', 'PHE', 'CB', 'PHE', 10.48), ('CE1', 'PHE', 'CG', 'PHE', 9.83), ('CE1', 'PHE', 'CD1', 'PHE', 9.69), ('CE1', 'PHE', 'CD2', 'PHE', 9.67), ('CE1', 'PHE', 'CE1', 'PHE', 9.41), ('CE1', 'PHE', 'CE2', 'PHE', 9.38), ('CE1', 'PHE', 'CZ', 'PHE', 9.24)], [('CE2', 'PHE', 'CB', 'PHE', 9.43), ('CE2', 'PHE', 'CG', 'PHE', 9.15), ('CE2', 'PHE', 'CD1', 'PHE', 9.07), ('CE2', 'PHE', 'CD2', 'PHE', 9.35), ('CE2', 'PHE', 'CE1', 'PHE', 9.2), ('CE2', 'PHE', 'CE2', 'PHE', 9.47), ('CE2', 'PHE', 'CZ', 'PHE', 9.4)], [('CZ', 'PHE', 'CB', 'PHE', 9.32), ('CZ', 'PHE', 'CG', 'PHE', 8.82), ('CZ', 'PHE', 'CD1', 'PHE', 8.79), ('CZ', 'PHE', 'CD2', 'PHE', 8.78), ('CZ', 'PHE', 'CE1', 'PHE', 8.72), ('CZ', 'PHE', 'CE2', 'PHE', 8.71), ('CZ', 'PHE', 'CZ', 'PHE', 8.68)]]}
TRP_PHE = { 
	'distances':
		[[15.59, 14.34, 13.83, 13.86, 12.79, 12.81, 12.24], [14.36, 13.16, 12.75, 12.65, 11.78, 11.67, 11.2], [14.12, 13.03, 12.69, 12.58, 11.86, 11.74, 11.36], [13.39, 12.15, 11.81, 11.52, 10.81, 10.48, 10.09], [13.03, 11.99, 11.76, 11.47, 11.02, 10.7, 10.46], [12.52, 11.37, 11.16, 10.74, 10.31, 9.83, 9.6], [13.34, 12.01, 11.65, 11.29, 10.55, 10.12, 9.71], [11.53, 10.38, 10.32, 9.62, 9.51, 8.72, 8.67], [12.42, 11.07, 10.84, 10.24, 9.75, 9.04, 8.77], [11.49, 10.23, 10.15, 9.35, 9.21, 8.28, 8.2], [21.11, 20.0, 19.12, 19.98, 18.21, 19.12, 18.2], [20.51, 19.33, 18.47, 19.22, 17.48, 18.29, 17.38], [21.05, 19.83, 19.03, 19.62, 17.99, 18.63, 17.78], [19.41, 18.19, 17.3, 18.1, 16.27, 17.13, 16.18], [20.4, 19.12, 18.33, 18.86, 17.24, 17.8, 16.95], [19.37, 18.09, 17.24, 17.89, 16.14, 16.84, 15.92], [18.55, 17.36, 16.39, 17.36, 15.39, 16.43, 15.41], [18.51, 17.18, 16.31, 16.95, 15.16, 15.85, 14.9], [17.63, 16.39, 15.4, 16.38, 14.34, 15.4, 14.34], [17.62, 16.31, 15.37, 16.17, 14.22, 15.11, 14.08]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'PHE', 15.59), ('CB', 'TRP', 'CG', 'PHE', 14.34), ('CB', 'TRP', 'CD1', 'PHE', 13.83), ('CB', 'TRP', 'CD2', 'PHE', 13.86), ('CB', 'TRP', 'CE1', 'PHE', 12.79), ('CB', 'TRP', 'CE2', 'PHE', 12.81), ('CB', 'TRP', 'CZ', 'PHE', 12.24)], [('CG', 'TRP', 'CB', 'PHE', 14.36), ('CG', 'TRP', 'CG', 'PHE', 13.16), ('CG', 'TRP', 'CD1', 'PHE', 12.75), ('CG', 'TRP', 'CD2', 'PHE', 12.65), ('CG', 'TRP', 'CE1', 'PHE', 11.78), ('CG', 'TRP', 'CE2', 'PHE', 11.67), ('CG', 'TRP', 'CZ', 'PHE', 11.2)], [('CD1', 'TRP', 'CB', 'PHE', 14.12), ('CD1', 'TRP', 'CG', 'PHE', 13.03), ('CD1', 'TRP', 'CD1', 'PHE', 12.69), ('CD1', 'TRP', 'CD2', 'PHE', 12.58), ('CD1', 'TRP', 'CE1', 'PHE', 11.86), ('CD1', 'TRP', 'CE2', 'PHE', 11.74), ('CD1', 'TRP', 'CZ', 'PHE', 11.36)], [('CD2', 'TRP', 'CB', 'PHE', 13.39), ('CD2', 'TRP', 'CG', 'PHE', 12.15), ('CD2', 'TRP', 'CD1', 'PHE', 11.81), ('CD2', 'TRP', 'CD2', 'PHE', 11.52), ('CD2', 'TRP', 'CE1', 'PHE', 10.81), ('CD2', 'TRP', 'CE2', 'PHE', 10.48), ('CD2', 'TRP', 'CZ', 'PHE', 10.09)], [('NE1', 'TRP', 'CB', 'PHE', 13.03), ('NE1', 'TRP', 'CG', 'PHE', 11.99), ('NE1', 'TRP', 'CD1', 'PHE', 11.76), ('NE1', 'TRP', 'CD2', 'PHE', 11.47), ('NE1', 'TRP', 'CE1', 'PHE', 11.02), ('NE1', 'TRP', 'CE2', 'PHE', 10.7), ('NE1', 'TRP', 'CZ', 'PHE', 10.46)], [('CE2', 'TRP', 'CB', 'PHE', 12.52), ('CE2', 'TRP', 'CG', 'PHE', 11.37), ('CE2', 'TRP', 'CD1', 'PHE', 11.16), ('CE2', 'TRP', 'CD2', 'PHE', 10.74), ('CE2', 'TRP', 'CE1', 'PHE', 10.31), ('CE2', 'TRP', 'CE2', 'PHE', 9.83), ('CE2', 'TRP', 'CZ', 'PHE', 9.6)], [('CE3', 'TRP', 'CB', 'PHE', 13.34), ('CE3', 'TRP', 'CG', 'PHE', 12.01), ('CE3', 'TRP', 'CD1', 'PHE', 11.65), ('CE3', 'TRP', 'CD2', 'PHE', 11.29), ('CE3', 'TRP', 'CE1', 'PHE', 10.55), ('CE3', 'TRP', 'CE2', 'PHE', 10.12), ('CE3', 'TRP', 'CZ', 'PHE', 9.71)], [('CZ2', 'TRP', 'CB', 'PHE', 11.53), ('CZ2', 'TRP', 'CG', 'PHE', 10.38), ('CZ2', 'TRP', 'CD1', 'PHE', 10.32), ('CZ2', 'TRP', 'CD2', 'PHE', 9.62), ('CZ2', 'TRP', 'CE1', 'PHE', 9.51), ('CZ2', 'TRP', 'CE2', 'PHE', 8.72), ('CZ2', 'TRP', 'CZ', 'PHE', 8.67)], [('CZ3', 'TRP', 'CB', 'PHE', 12.42), ('CZ3', 'TRP', 'CG', 'PHE', 11.07), ('CZ3', 'TRP', 'CD1', 'PHE', 10.84), ('CZ3', 'TRP', 'CD2', 'PHE', 10.24), ('CZ3', 'TRP', 'CE1', 'PHE', 9.75), ('CZ3', 'TRP', 'CE2', 'PHE', 9.04), ('CZ3', 'TRP', 'CZ', 'PHE', 8.77)], [('CH2', 'TRP', 'CB', 'PHE', 11.49), ('CH2', 'TRP', 'CG', 'PHE', 10.23), ('CH2', 'TRP', 'CD1', 'PHE', 10.15), ('CH2', 'TRP', 'CD2', 'PHE', 9.35), ('CH2', 'TRP', 'CE1', 'PHE', 9.21), ('CH2', 'TRP', 'CE2', 'PHE', 8.28), ('CH2', 'TRP', 'CZ', 'PHE', 8.2)], [('CB', 'TRP', 'CB', 'PHE', 21.11), ('CB', 'TRP', 'CG', 'PHE', 20.0), ('CB', 'TRP', 'CD1', 'PHE', 19.12), ('CB', 'TRP', 'CD2', 'PHE', 19.98), ('CB', 'TRP', 'CE1', 'PHE', 18.21), ('CB', 'TRP', 'CE2', 'PHE', 19.12), ('CB', 'TRP', 'CZ', 'PHE', 18.2)], [('CG', 'TRP', 'CB', 'PHE', 20.51), ('CG', 'TRP', 'CG', 'PHE', 19.33), ('CG', 'TRP', 'CD1', 'PHE', 18.47), ('CG', 'TRP', 'CD2', 'PHE', 19.22), ('CG', 'TRP', 'CE1', 'PHE', 17.48), ('CG', 'TRP', 'CE2', 'PHE', 18.29), ('CG', 'TRP', 'CZ', 'PHE', 17.38)], [('CD1', 'TRP', 'CB', 'PHE', 21.05), ('CD1', 'TRP', 'CG', 'PHE', 19.83), ('CD1', 'TRP', 'CD1', 'PHE', 19.03), ('CD1', 'TRP', 'CD2', 'PHE', 19.62), ('CD1', 'TRP', 'CE1', 'PHE', 17.99), ('CD1', 'TRP', 'CE2', 'PHE', 18.63), ('CD1', 'TRP', 'CZ', 'PHE', 17.78)], [('CD2', 'TRP', 'CB', 'PHE', 19.41), ('CD2', 'TRP', 'CG', 'PHE', 18.19), ('CD2', 'TRP', 'CD1', 'PHE', 17.3), ('CD2', 'TRP', 'CD2', 'PHE', 18.1), ('CD2', 'TRP', 'CE1', 'PHE', 16.27), ('CD2', 'TRP', 'CE2', 'PHE', 17.13), ('CD2', 'TRP', 'CZ', 'PHE', 16.18)], [('NE1', 'TRP', 'CB', 'PHE', 20.4), ('NE1', 'TRP', 'CG', 'PHE', 19.12), ('NE1', 'TRP', 'CD1', 'PHE', 18.33), ('NE1', 'TRP', 'CD2', 'PHE', 18.86), ('NE1', 'TRP', 'CE1', 'PHE', 17.24), ('NE1', 'TRP', 'CE2', 'PHE', 17.8), ('NE1', 'TRP', 'CZ', 'PHE', 16.95)], [('CE2', 'TRP', 'CB', 'PHE', 19.37), ('CE2', 'TRP', 'CG', 'PHE', 18.09), ('CE2', 'TRP', 'CD1', 'PHE', 17.24), ('CE2', 'TRP', 'CD2', 'PHE', 17.89), ('CE2', 'TRP', 'CE1', 'PHE', 16.14), ('CE2', 'TRP', 'CE2', 'PHE', 16.84), ('CE2', 'TRP', 'CZ', 'PHE', 15.92)], [('CE3', 'TRP', 'CB', 'PHE', 18.55), ('CE3', 'TRP', 'CG', 'PHE', 17.36), ('CE3', 'TRP', 'CD1', 'PHE', 16.39), ('CE3', 'TRP', 'CD2', 'PHE', 17.36), ('CE3', 'TRP', 'CE1', 'PHE', 15.39), ('CE3', 'TRP', 'CE2', 'PHE', 16.43), ('CE3', 'TRP', 'CZ', 'PHE', 15.41)], [('CZ2', 'TRP', 'CB', 'PHE', 18.51), ('CZ2', 'TRP', 'CG', 'PHE', 17.18), ('CZ2', 'TRP', 'CD1', 'PHE', 16.31), ('CZ2', 'TRP', 'CD2', 'PHE', 16.95), ('CZ2', 'TRP', 'CE1', 'PHE', 15.16), ('CZ2', 'TRP', 'CE2', 'PHE', 15.85), ('CZ2', 'TRP', 'CZ', 'PHE', 14.9)], [('CZ3', 'TRP', 'CB', 'PHE', 17.63), ('CZ3', 'TRP', 'CG', 'PHE', 16.39), ('CZ3', 'TRP', 'CD1', 'PHE', 15.4), ('CZ3', 'TRP', 'CD2', 'PHE', 16.38), ('CZ3', 'TRP', 'CE1', 'PHE', 14.34), ('CZ3', 'TRP', 'CE2', 'PHE', 15.4), ('CZ3', 'TRP', 'CZ', 'PHE', 14.34)], [('CH2', 'TRP', 'CB', 'PHE', 17.62), ('CH2', 'TRP', 'CG', 'PHE', 16.31), ('CH2', 'TRP', 'CD1', 'PHE', 15.37), ('CH2', 'TRP', 'CD2', 'PHE', 16.17), ('CH2', 'TRP', 'CE1', 'PHE', 14.22), ('CH2', 'TRP', 'CE2', 'PHE', 15.11), ('CH2', 'TRP', 'CZ', 'PHE', 14.08)]]}
TYR_PHE = { 
	'distances':
		[[14.85, 13.6, 12.39, 13.76, 11.24, 12.76, 11.45], [14.34, 13.0, 11.88, 13.0, 10.63, 11.9, 10.64], [13.56, 12.2, 11.16, 12.12, 9.91, 11.0, 9.81], [14.83, 13.44, 12.35, 13.36, 11.04, 12.19, 10.94], [13.28, 11.86, 10.94, 11.59, 9.62, 10.37, 9.29], [14.59, 13.15, 12.16, 12.91, 10.8, 11.65, 10.5], [13.83, 12.37, 11.47, 12.03, 10.1, 10.74, 9.67], [13.8, 12.31, 11.56, 11.8, 10.17, 10.44, 9.53], [16.84, 16.19, 15.67, 16.33, 15.3, 15.99, 15.47], [16.3, 15.57, 14.93, 15.77, 14.49, 15.36, 14.71], [16.47, 15.61, 14.92, 15.73, 14.34, 15.19, 14.48], [15.79, 15.13, 14.42, 15.46, 14.06, 15.13, 14.43], [16.14, 15.22, 14.42, 15.38, 13.76, 14.78, 13.96], [15.44, 14.72, 13.9, 15.11, 13.47, 14.73, 13.91], [15.62, 14.77, 13.89, 15.07, 13.31, 14.55, 13.66], [15.45, 14.55, 13.56, 14.9, 12.92, 14.33, 13.33]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'PHE', 14.85), ('CB', 'TYR', 'CG', 'PHE', 13.6), ('CB', 'TYR', 'CD1', 'PHE', 12.39), ('CB', 'TYR', 'CD2', 'PHE', 13.76), ('CB', 'TYR', 'CE1', 'PHE', 11.24), ('CB', 'TYR', 'CE2', 'PHE', 12.76), ('CB', 'TYR', 'CZ', 'PHE', 11.45)], [('CG', 'TYR', 'CB', 'PHE', 14.34), ('CG', 'TYR', 'CG', 'PHE', 13.0), ('CG', 'TYR', 'CD1', 'PHE', 11.88), ('CG', 'TYR', 'CD2', 'PHE', 13.0), ('CG', 'TYR', 'CE1', 'PHE', 10.63), ('CG', 'TYR', 'CE2', 'PHE', 11.9), ('CG', 'TYR', 'CZ', 'PHE', 10.64)], [('CD1', 'TYR', 'CB', 'PHE', 13.56), ('CD1', 'TYR', 'CG', 'PHE', 12.2), ('CD1', 'TYR', 'CD1', 'PHE', 11.16), ('CD1', 'TYR', 'CD2', 'PHE', 12.12), ('CD1', 'TYR', 'CE1', 'PHE', 9.91), ('CD1', 'TYR', 'CE2', 'PHE', 11.0), ('CD1', 'TYR', 'CZ', 'PHE', 9.81)], [('CD2', 'TYR', 'CB', 'PHE', 14.83), ('CD2', 'TYR', 'CG', 'PHE', 13.44), ('CD2', 'TYR', 'CD1', 'PHE', 12.35), ('CD2', 'TYR', 'CD2', 'PHE', 13.36), ('CD2', 'TYR', 'CE1', 'PHE', 11.04), ('CD2', 'TYR', 'CE2', 'PHE', 12.19), ('CD2', 'TYR', 'CZ', 'PHE', 10.94)], [('CE1', 'TYR', 'CB', 'PHE', 13.28), ('CE1', 'TYR', 'CG', 'PHE', 11.86), ('CE1', 'TYR', 'CD1', 'PHE', 10.94), ('CE1', 'TYR', 'CD2', 'PHE', 11.59), ('CE1', 'TYR', 'CE1', 'PHE', 9.62), ('CE1', 'TYR', 'CE2', 'PHE', 10.37), ('CE1', 'TYR', 'CZ', 'PHE', 9.29)], [('CE2', 'TYR', 'CB', 'PHE', 14.59), ('CE2', 'TYR', 'CG', 'PHE', 13.15), ('CE2', 'TYR', 'CD1', 'PHE', 12.16), ('CE2', 'TYR', 'CD2', 'PHE', 12.91), ('CE2', 'TYR', 'CE1', 'PHE', 10.8), ('CE2', 'TYR', 'CE2', 'PHE', 11.65), ('CE2', 'TYR', 'CZ', 'PHE', 10.5)], [('CZ', 'TYR', 'CB', 'PHE', 13.83), ('CZ', 'TYR', 'CG', 'PHE', 12.37), ('CZ', 'TYR', 'CD1', 'PHE', 11.47), ('CZ', 'TYR', 'CD2', 'PHE', 12.03), ('CZ', 'TYR', 'CE1', 'PHE', 10.1), ('CZ', 'TYR', 'CE2', 'PHE', 10.74), ('CZ', 'TYR', 'CZ', 'PHE', 9.67)], [('OH', 'TYR', 'CB', 'PHE', 13.8), ('OH', 'TYR', 'CG', 'PHE', 12.31), ('OH', 'TYR', 'CD1', 'PHE', 11.56), ('OH', 'TYR', 'CD2', 'PHE', 11.8), ('OH', 'TYR', 'CE1', 'PHE', 10.17), ('OH', 'TYR', 'CE2', 'PHE', 10.44), ('OH', 'TYR', 'CZ', 'PHE', 9.53)], [('CB', 'TYR', 'CB', 'PHE', 16.84), ('CB', 'TYR', 'CG', 'PHE', 16.19), ('CB', 'TYR', 'CD1', 'PHE', 15.67), ('CB', 'TYR', 'CD2', 'PHE', 16.33), ('CB', 'TYR', 'CE1', 'PHE', 15.3), ('CB', 'TYR', 'CE2', 'PHE', 15.99), ('CB', 'TYR', 'CZ', 'PHE', 15.47)], [('CG', 'TYR', 'CB', 'PHE', 16.3), ('CG', 'TYR', 'CG', 'PHE', 15.57), ('CG', 'TYR', 'CD1', 'PHE', 14.93), ('CG', 'TYR', 'CD2', 'PHE', 15.77), ('CG', 'TYR', 'CE1', 'PHE', 14.49), ('CG', 'TYR', 'CE2', 'PHE', 15.36), ('CG', 'TYR', 'CZ', 'PHE', 14.71)], [('CD1', 'TYR', 'CB', 'PHE', 16.47), ('CD1', 'TYR', 'CG', 'PHE', 15.61), ('CD1', 'TYR', 'CD1', 'PHE', 14.92), ('CD1', 'TYR', 'CD2', 'PHE', 15.73), ('CD1', 'TYR', 'CE1', 'PHE', 14.34), ('CD1', 'TYR', 'CE2', 'PHE', 15.19), ('CD1', 'TYR', 'CZ', 'PHE', 14.48)], [('CD2', 'TYR', 'CB', 'PHE', 15.79), ('CD2', 'TYR', 'CG', 'PHE', 15.13), ('CD2', 'TYR', 'CD1', 'PHE', 14.42), ('CD2', 'TYR', 'CD2', 'PHE', 15.46), ('CD2', 'TYR', 'CE1', 'PHE', 14.06), ('CD2', 'TYR', 'CE2', 'PHE', 15.13), ('CD2', 'TYR', 'CZ', 'PHE', 14.43)], [('CE1', 'TYR', 'CB', 'PHE', 16.14), ('CE1', 'TYR', 'CG', 'PHE', 15.22), ('CE1', 'TYR', 'CD1', 'PHE', 14.42), ('CE1', 'TYR', 'CD2', 'PHE', 15.38), ('CE1', 'TYR', 'CE1', 'PHE', 13.76), ('CE1', 'TYR', 'CE2', 'PHE', 14.78), ('CE1', 'TYR', 'CZ', 'PHE', 13.96)], [('CE2', 'TYR', 'CB', 'PHE', 15.44), ('CE2', 'TYR', 'CG', 'PHE', 14.72), ('CE2', 'TYR', 'CD1', 'PHE', 13.9), ('CE2', 'TYR', 'CD2', 'PHE', 15.11), ('CE2', 'TYR', 'CE1', 'PHE', 13.47), ('CE2', 'TYR', 'CE2', 'PHE', 14.73), ('CE2', 'TYR', 'CZ', 'PHE', 13.91)], [('CZ', 'TYR', 'CB', 'PHE', 15.62), ('CZ', 'TYR', 'CG', 'PHE', 14.77), ('CZ', 'TYR', 'CD1', 'PHE', 13.89), ('CZ', 'TYR', 'CD2', 'PHE', 15.07), ('CZ', 'TYR', 'CE1', 'PHE', 13.31), ('CZ', 'TYR', 'CE2', 'PHE', 14.55), ('CZ', 'TYR', 'CZ', 'PHE', 13.66)], [('OH', 'TYR', 'CB', 'PHE', 15.45), ('OH', 'TYR', 'CG', 'PHE', 14.55), ('OH', 'TYR', 'CD1', 'PHE', 13.56), ('OH', 'TYR', 'CD2', 'PHE', 14.9), ('OH', 'TYR', 'CE1', 'PHE', 12.92), ('OH', 'TYR', 'CE2', 'PHE', 14.33), ('OH', 'TYR', 'CZ', 'PHE', 13.33)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_TRP, d, 'A_1di1_4_2_3_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(PHE_PHE, d, 'A_1di1_4_2_3_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TRP_PHE, d, 'A_1di1_4_2_3_9')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_PHE, d, 'A_1di1_4_2_3_9')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_TRP' :  match1,
		'PHE_PHE' :  match2,
		'TRP_PHE' :  match3,
		'TYR_PHE' :  match4}