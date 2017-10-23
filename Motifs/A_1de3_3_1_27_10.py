'''
FUNC:A_1de3_3_1_27_10
PDB:1de3
EC:3.1.27.10
RESI:his,glu,his
LOCI:a-50,96,137;
'''
import motifFunctions as cmd
HIS_HIS = { 
	'distances':
		[[16.76, 15.23, 14.59, 14.41, 13.28, 13.16, 19.25, 18.9, 17.46, 16.9], [15.25, 13.72, 13.08, 12.92, 11.77, 11.66, 17.76, 17.39, 15.94, 15.4], [14.67, 13.14, 12.38, 12.47, 11.11, 11.17, 17.29, 16.87, 15.4, 14.97], [14.38, 12.87, 12.33, 11.98, 11.02, 10.77, 16.8, 16.45, 15.02, 14.39], [13.38, 11.85, 11.11, 11.17, 9.84, 9.88, 15.99, 15.55, 14.08, 13.65], [13.18, 11.65, 11.07, 10.83, 9.77, 9.59, 15.66, 15.27, 13.82, 13.25], [16.68, 15.19, 14.66, 14.36, 13.43, 13.22, 19.05, 18.54, 17.07, 16.35], [17.32, 15.81, 15.2, 15.01, 13.95, 13.82, 19.77, 19.28, 17.81, 17.16], [17.6, 16.08, 15.5, 15.22, 14.21, 14.01, 20.03, 19.64, 18.19, 17.53], [17.58, 16.09, 15.63, 15.12, 14.33, 13.98, 19.87, 19.52, 18.11, 17.35], [16.76, 15.25, 14.67, 14.38, 13.38, 13.18, 16.68, 17.32, 17.6, 17.58], [15.23, 13.72, 13.14, 12.87, 11.85, 11.65, 15.19, 15.81, 16.08, 16.09], [14.59, 13.08, 12.38, 12.33, 11.11, 11.07, 14.66, 15.2, 15.5, 15.63], [14.41, 12.92, 12.47, 11.98, 11.17, 10.83, 14.36, 15.01, 15.22, 15.12], [13.28, 11.77, 11.11, 11.02, 9.84, 9.77, 13.43, 13.95, 14.21, 14.33], [13.16, 11.66, 11.17, 10.77, 9.88, 9.59, 13.22, 13.82, 14.01, 13.98], [19.25, 17.76, 17.29, 16.8, 15.99, 15.66, 19.05, 19.77, 20.03, 19.87], [18.9, 17.39, 16.87, 16.45, 15.55, 15.27, 18.54, 19.28, 19.64, 19.52], [17.46, 15.94, 15.4, 15.02, 14.08, 13.82, 17.07, 17.81, 18.19, 18.11], [16.9, 15.4, 14.97, 14.39, 13.65, 13.25, 16.35, 17.16, 17.53, 17.35]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 16.76), ('CB', 'HIS', 'CG', 'HIS', 15.23), ('CB', 'HIS', 'ND1', 'HIS', 14.59), ('CB', 'HIS', 'CD2', 'HIS', 14.41), ('CB', 'HIS', 'CE1', 'HIS', 13.28), ('CB', 'HIS', 'NE2', 'HIS', 13.16), ('CB', 'HIS', 'O', 'HIS', 19.25), ('CB', 'HIS', 'C', 'HIS', 18.9), ('CB', 'HIS', 'CA', 'HIS', 17.46), ('CB', 'HIS', 'N', 'HIS', 16.9)], [('CG', 'HIS', 'CB', 'HIS', 15.25), ('CG', 'HIS', 'CG', 'HIS', 13.72), ('CG', 'HIS', 'ND1', 'HIS', 13.08), ('CG', 'HIS', 'CD2', 'HIS', 12.92), ('CG', 'HIS', 'CE1', 'HIS', 11.77), ('CG', 'HIS', 'NE2', 'HIS', 11.66), ('CG', 'HIS', 'O', 'HIS', 17.76), ('CG', 'HIS', 'C', 'HIS', 17.39), ('CG', 'HIS', 'CA', 'HIS', 15.94), ('CG', 'HIS', 'N', 'HIS', 15.4)], [('ND1', 'HIS', 'CB', 'HIS', 14.67), ('ND1', 'HIS', 'CG', 'HIS', 13.14), ('ND1', 'HIS', 'ND1', 'HIS', 12.38), ('ND1', 'HIS', 'CD2', 'HIS', 12.47), ('ND1', 'HIS', 'CE1', 'HIS', 11.11), ('ND1', 'HIS', 'NE2', 'HIS', 11.17), ('ND1', 'HIS', 'O', 'HIS', 17.29), ('ND1', 'HIS', 'C', 'HIS', 16.87), ('ND1', 'HIS', 'CA', 'HIS', 15.4), ('ND1', 'HIS', 'N', 'HIS', 14.97)], [('CD2', 'HIS', 'CB', 'HIS', 14.38), ('CD2', 'HIS', 'CG', 'HIS', 12.87), ('CD2', 'HIS', 'ND1', 'HIS', 12.33), ('CD2', 'HIS', 'CD2', 'HIS', 11.98), ('CD2', 'HIS', 'CE1', 'HIS', 11.02), ('CD2', 'HIS', 'NE2', 'HIS', 10.77), ('CD2', 'HIS', 'O', 'HIS', 16.8), ('CD2', 'HIS', 'C', 'HIS', 16.45), ('CD2', 'HIS', 'CA', 'HIS', 15.02), ('CD2', 'HIS', 'N', 'HIS', 14.39)], [('CE1', 'HIS', 'CB', 'HIS', 13.38), ('CE1', 'HIS', 'CG', 'HIS', 11.85), ('CE1', 'HIS', 'ND1', 'HIS', 11.11), ('CE1', 'HIS', 'CD2', 'HIS', 11.17), ('CE1', 'HIS', 'CE1', 'HIS', 9.84), ('CE1', 'HIS', 'NE2', 'HIS', 9.88), ('CE1', 'HIS', 'O', 'HIS', 15.99), ('CE1', 'HIS', 'C', 'HIS', 15.55), ('CE1', 'HIS', 'CA', 'HIS', 14.08), ('CE1', 'HIS', 'N', 'HIS', 13.65)], [('NE2', 'HIS', 'CB', 'HIS', 13.18), ('NE2', 'HIS', 'CG', 'HIS', 11.65), ('NE2', 'HIS', 'ND1', 'HIS', 11.07), ('NE2', 'HIS', 'CD2', 'HIS', 10.83), ('NE2', 'HIS', 'CE1', 'HIS', 9.77), ('NE2', 'HIS', 'NE2', 'HIS', 9.59), ('NE2', 'HIS', 'O', 'HIS', 15.66), ('NE2', 'HIS', 'C', 'HIS', 15.27), ('NE2', 'HIS', 'CA', 'HIS', 13.82), ('NE2', 'HIS', 'N', 'HIS', 13.25)], [('O', 'HIS', 'CB', 'HIS', 16.68), ('O', 'HIS', 'CG', 'HIS', 15.19), ('O', 'HIS', 'ND1', 'HIS', 14.66), ('O', 'HIS', 'CD2', 'HIS', 14.36), ('O', 'HIS', 'CE1', 'HIS', 13.43), ('O', 'HIS', 'NE2', 'HIS', 13.22), ('O', 'HIS', 'O', 'HIS', 19.05), ('O', 'HIS', 'C', 'HIS', 18.54), ('O', 'HIS', 'CA', 'HIS', 17.07), ('O', 'HIS', 'N', 'HIS', 16.35)], [('C', 'HIS', 'CB', 'HIS', 17.32), ('C', 'HIS', 'CG', 'HIS', 15.81), ('C', 'HIS', 'ND1', 'HIS', 15.2), ('C', 'HIS', 'CD2', 'HIS', 15.01), ('C', 'HIS', 'CE1', 'HIS', 13.95), ('C', 'HIS', 'NE2', 'HIS', 13.82), ('C', 'HIS', 'O', 'HIS', 19.77), ('C', 'HIS', 'C', 'HIS', 19.28), ('C', 'HIS', 'CA', 'HIS', 17.81), ('C', 'HIS', 'N', 'HIS', 17.16)], [('CA', 'HIS', 'CB', 'HIS', 17.6), ('CA', 'HIS', 'CG', 'HIS', 16.08), ('CA', 'HIS', 'ND1', 'HIS', 15.5), ('CA', 'HIS', 'CD2', 'HIS', 15.22), ('CA', 'HIS', 'CE1', 'HIS', 14.21), ('CA', 'HIS', 'NE2', 'HIS', 14.01), ('CA', 'HIS', 'O', 'HIS', 20.03), ('CA', 'HIS', 'C', 'HIS', 19.64), ('CA', 'HIS', 'CA', 'HIS', 18.19), ('CA', 'HIS', 'N', 'HIS', 17.53)], [('N', 'HIS', 'CB', 'HIS', 17.58), ('N', 'HIS', 'CG', 'HIS', 16.09), ('N', 'HIS', 'ND1', 'HIS', 15.63), ('N', 'HIS', 'CD2', 'HIS', 15.12), ('N', 'HIS', 'CE1', 'HIS', 14.33), ('N', 'HIS', 'NE2', 'HIS', 13.98), ('N', 'HIS', 'O', 'HIS', 19.87), ('N', 'HIS', 'C', 'HIS', 19.52), ('N', 'HIS', 'CA', 'HIS', 18.11), ('N', 'HIS', 'N', 'HIS', 17.35)], [('CB', 'HIS', 'CB', 'HIS', 16.76), ('CB', 'HIS', 'CG', 'HIS', 15.25), ('CB', 'HIS', 'ND1', 'HIS', 14.67), ('CB', 'HIS', 'CD2', 'HIS', 14.38), ('CB', 'HIS', 'CE1', 'HIS', 13.38), ('CB', 'HIS', 'NE2', 'HIS', 13.18), ('CB', 'HIS', 'O', 'HIS', 16.68), ('CB', 'HIS', 'C', 'HIS', 17.32), ('CB', 'HIS', 'CA', 'HIS', 17.6), ('CB', 'HIS', 'N', 'HIS', 17.58)], [('CG', 'HIS', 'CB', 'HIS', 15.23), ('CG', 'HIS', 'CG', 'HIS', 13.72), ('CG', 'HIS', 'ND1', 'HIS', 13.14), ('CG', 'HIS', 'CD2', 'HIS', 12.87), ('CG', 'HIS', 'CE1', 'HIS', 11.85), ('CG', 'HIS', 'NE2', 'HIS', 11.65), ('CG', 'HIS', 'O', 'HIS', 15.19), ('CG', 'HIS', 'C', 'HIS', 15.81), ('CG', 'HIS', 'CA', 'HIS', 16.08), ('CG', 'HIS', 'N', 'HIS', 16.09)], [('ND1', 'HIS', 'CB', 'HIS', 14.59), ('ND1', 'HIS', 'CG', 'HIS', 13.08), ('ND1', 'HIS', 'ND1', 'HIS', 12.38), ('ND1', 'HIS', 'CD2', 'HIS', 12.33), ('ND1', 'HIS', 'CE1', 'HIS', 11.11), ('ND1', 'HIS', 'NE2', 'HIS', 11.07), ('ND1', 'HIS', 'O', 'HIS', 14.66), ('ND1', 'HIS', 'C', 'HIS', 15.2), ('ND1', 'HIS', 'CA', 'HIS', 15.5), ('ND1', 'HIS', 'N', 'HIS', 15.63)], [('CD2', 'HIS', 'CB', 'HIS', 14.41), ('CD2', 'HIS', 'CG', 'HIS', 12.92), ('CD2', 'HIS', 'ND1', 'HIS', 12.47), ('CD2', 'HIS', 'CD2', 'HIS', 11.98), ('CD2', 'HIS', 'CE1', 'HIS', 11.17), ('CD2', 'HIS', 'NE2', 'HIS', 10.83), ('CD2', 'HIS', 'O', 'HIS', 14.36), ('CD2', 'HIS', 'C', 'HIS', 15.01), ('CD2', 'HIS', 'CA', 'HIS', 15.22), ('CD2', 'HIS', 'N', 'HIS', 15.12)], [('CE1', 'HIS', 'CB', 'HIS', 13.28), ('CE1', 'HIS', 'CG', 'HIS', 11.77), ('CE1', 'HIS', 'ND1', 'HIS', 11.11), ('CE1', 'HIS', 'CD2', 'HIS', 11.02), ('CE1', 'HIS', 'CE1', 'HIS', 9.84), ('CE1', 'HIS', 'NE2', 'HIS', 9.77), ('CE1', 'HIS', 'O', 'HIS', 13.43), ('CE1', 'HIS', 'C', 'HIS', 13.95), ('CE1', 'HIS', 'CA', 'HIS', 14.21), ('CE1', 'HIS', 'N', 'HIS', 14.33)], [('NE2', 'HIS', 'CB', 'HIS', 13.16), ('NE2', 'HIS', 'CG', 'HIS', 11.66), ('NE2', 'HIS', 'ND1', 'HIS', 11.17), ('NE2', 'HIS', 'CD2', 'HIS', 10.77), ('NE2', 'HIS', 'CE1', 'HIS', 9.88), ('NE2', 'HIS', 'NE2', 'HIS', 9.59), ('NE2', 'HIS', 'O', 'HIS', 13.22), ('NE2', 'HIS', 'C', 'HIS', 13.82), ('NE2', 'HIS', 'CA', 'HIS', 14.01), ('NE2', 'HIS', 'N', 'HIS', 13.98)], [('O', 'HIS', 'CB', 'HIS', 19.25), ('O', 'HIS', 'CG', 'HIS', 17.76), ('O', 'HIS', 'ND1', 'HIS', 17.29), ('O', 'HIS', 'CD2', 'HIS', 16.8), ('O', 'HIS', 'CE1', 'HIS', 15.99), ('O', 'HIS', 'NE2', 'HIS', 15.66), ('O', 'HIS', 'O', 'HIS', 19.05), ('O', 'HIS', 'C', 'HIS', 19.77), ('O', 'HIS', 'CA', 'HIS', 20.03), ('O', 'HIS', 'N', 'HIS', 19.87)], [('C', 'HIS', 'CB', 'HIS', 18.9), ('C', 'HIS', 'CG', 'HIS', 17.39), ('C', 'HIS', 'ND1', 'HIS', 16.87), ('C', 'HIS', 'CD2', 'HIS', 16.45), ('C', 'HIS', 'CE1', 'HIS', 15.55), ('C', 'HIS', 'NE2', 'HIS', 15.27), ('C', 'HIS', 'O', 'HIS', 18.54), ('C', 'HIS', 'C', 'HIS', 19.28), ('C', 'HIS', 'CA', 'HIS', 19.64), ('C', 'HIS', 'N', 'HIS', 19.52)], [('CA', 'HIS', 'CB', 'HIS', 17.46), ('CA', 'HIS', 'CG', 'HIS', 15.94), ('CA', 'HIS', 'ND1', 'HIS', 15.4), ('CA', 'HIS', 'CD2', 'HIS', 15.02), ('CA', 'HIS', 'CE1', 'HIS', 14.08), ('CA', 'HIS', 'NE2', 'HIS', 13.82), ('CA', 'HIS', 'O', 'HIS', 17.07), ('CA', 'HIS', 'C', 'HIS', 17.81), ('CA', 'HIS', 'CA', 'HIS', 18.19), ('CA', 'HIS', 'N', 'HIS', 18.11)], [('N', 'HIS', 'CB', 'HIS', 16.9), ('N', 'HIS', 'CG', 'HIS', 15.4), ('N', 'HIS', 'ND1', 'HIS', 14.97), ('N', 'HIS', 'CD2', 'HIS', 14.39), ('N', 'HIS', 'CE1', 'HIS', 13.65), ('N', 'HIS', 'NE2', 'HIS', 13.25), ('N', 'HIS', 'O', 'HIS', 16.35), ('N', 'HIS', 'C', 'HIS', 17.16), ('N', 'HIS', 'CA', 'HIS', 17.53), ('N', 'HIS', 'N', 'HIS', 17.35)]]}
HIS_GLU = { 
	'distances':
		[[8.09, 8.6, 9.74, 9.64, 10.86, 6.8, 7.74, 8.18, 7.87], [7.01, 7.34, 8.37, 8.18, 9.52, 6.05, 7.05, 7.4, 7.37], [7.16, 7.42, 8.17, 7.73, 9.39, 6.87, 7.78, 7.87, 7.88], [6.18, 6.28, 7.4, 7.37, 8.5, 4.93, 6.02, 6.54, 6.83], [6.48, 6.46, 7.04, 6.52, 8.26, 6.52, 7.4, 7.43, 7.73], [5.8, 5.62, 6.47, 6.24, 7.62, 5.33, 6.3, 6.58, 7.09], [5.94, 7.09, 8.3, 8.53, 9.25, 5.61, 5.85, 5.67, 4.82], [7.03, 8.08, 9.24, 9.33, 10.27, 6.48, 6.92, 6.88, 6.05], [7.89, 8.68, 9.94, 10.02, 10.98, 6.59, 7.29, 7.66, 7.06], [7.75, 8.44, 9.85, 10.14, 10.78, 5.86, 6.53, 7.22, 6.75], [13.42, 12.06, 10.9, 10.45, 10.58, 14.41, 14.65, 14.57, 15.85], [12.02, 10.66, 9.54, 9.03, 9.34, 12.98, 13.27, 13.2, 14.46], [11.67, 10.4, 9.26, 8.56, 9.25, 12.75, 13.1, 12.96, 14.12], [11.18, 9.76, 8.76, 8.39, 8.54, 11.93, 12.22, 12.27, 13.58], [10.58, 9.3, 8.27, 7.54, 8.4, 11.52, 11.94, 11.86, 13.02], [10.22, 8.82, 7.89, 7.39, 7.88, 10.94, 11.32, 11.37, 12.63], [15.61, 14.21, 13.09, 12.84, 12.56, 16.49, 16.64, 16.62, 17.97], [15.02, 13.67, 12.46, 12.18, 11.9, 16.12, 16.2, 16.07, 17.38], [13.58, 12.25, 11.02, 10.69, 10.51, 14.75, 14.85, 14.68, 15.97], [12.75, 11.4, 10.22, 10.08, 9.59, 13.84, 13.87, 13.74, 15.08]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 8.09), ('CB', 'HIS', 'CG', 'GLU', 8.6), ('CB', 'HIS', 'CD', 'GLU', 9.74), ('CB', 'HIS', 'OE1', 'GLU', 9.64), ('CB', 'HIS', 'OE2', 'GLU', 10.86), ('CB', 'HIS', 'O', 'GLU', 6.8), ('CB', 'HIS', 'C', 'GLU', 7.74), ('CB', 'HIS', 'CA', 'GLU', 8.18), ('CB', 'HIS', 'N', 'GLU', 7.87)], [('CG', 'HIS', 'CB', 'GLU', 7.01), ('CG', 'HIS', 'CG', 'GLU', 7.34), ('CG', 'HIS', 'CD', 'GLU', 8.37), ('CG', 'HIS', 'OE1', 'GLU', 8.18), ('CG', 'HIS', 'OE2', 'GLU', 9.52), ('CG', 'HIS', 'O', 'GLU', 6.05), ('CG', 'HIS', 'C', 'GLU', 7.05), ('CG', 'HIS', 'CA', 'GLU', 7.4), ('CG', 'HIS', 'N', 'GLU', 7.37)], [('ND1', 'HIS', 'CB', 'GLU', 7.16), ('ND1', 'HIS', 'CG', 'GLU', 7.42), ('ND1', 'HIS', 'CD', 'GLU', 8.17), ('ND1', 'HIS', 'OE1', 'GLU', 7.73), ('ND1', 'HIS', 'OE2', 'GLU', 9.39), ('ND1', 'HIS', 'O', 'GLU', 6.87), ('ND1', 'HIS', 'C', 'GLU', 7.78), ('ND1', 'HIS', 'CA', 'GLU', 7.87), ('ND1', 'HIS', 'N', 'GLU', 7.88)], [('CD2', 'HIS', 'CB', 'GLU', 6.18), ('CD2', 'HIS', 'CG', 'GLU', 6.28), ('CD2', 'HIS', 'CD', 'GLU', 7.4), ('CD2', 'HIS', 'OE1', 'GLU', 7.37), ('CD2', 'HIS', 'OE2', 'GLU', 8.5), ('CD2', 'HIS', 'O', 'GLU', 4.93), ('CD2', 'HIS', 'C', 'GLU', 6.02), ('CD2', 'HIS', 'CA', 'GLU', 6.54), ('CD2', 'HIS', 'N', 'GLU', 6.83)], [('CE1', 'HIS', 'CB', 'GLU', 6.48), ('CE1', 'HIS', 'CG', 'GLU', 6.46), ('CE1', 'HIS', 'CD', 'GLU', 7.04), ('CE1', 'HIS', 'OE1', 'GLU', 6.52), ('CE1', 'HIS', 'OE2', 'GLU', 8.26), ('CE1', 'HIS', 'O', 'GLU', 6.52), ('CE1', 'HIS', 'C', 'GLU', 7.4), ('CE1', 'HIS', 'CA', 'GLU', 7.43), ('CE1', 'HIS', 'N', 'GLU', 7.73)], [('NE2', 'HIS', 'CB', 'GLU', 5.8), ('NE2', 'HIS', 'CG', 'GLU', 5.62), ('NE2', 'HIS', 'CD', 'GLU', 6.47), ('NE2', 'HIS', 'OE1', 'GLU', 6.24), ('NE2', 'HIS', 'OE2', 'GLU', 7.62), ('NE2', 'HIS', 'O', 'GLU', 5.33), ('NE2', 'HIS', 'C', 'GLU', 6.3), ('NE2', 'HIS', 'CA', 'GLU', 6.58), ('NE2', 'HIS', 'N', 'GLU', 7.09)], [('O', 'HIS', 'CB', 'GLU', 5.94), ('O', 'HIS', 'CG', 'GLU', 7.09), ('O', 'HIS', 'CD', 'GLU', 8.3), ('O', 'HIS', 'OE1', 'GLU', 8.53), ('O', 'HIS', 'OE2', 'GLU', 9.25), ('O', 'HIS', 'O', 'GLU', 5.61), ('O', 'HIS', 'C', 'GLU', 5.85), ('O', 'HIS', 'CA', 'GLU', 5.67), ('O', 'HIS', 'N', 'GLU', 4.82)], [('C', 'HIS', 'CB', 'GLU', 7.03), ('C', 'HIS', 'CG', 'GLU', 8.08), ('C', 'HIS', 'CD', 'GLU', 9.24), ('C', 'HIS', 'OE1', 'GLU', 9.33), ('C', 'HIS', 'OE2', 'GLU', 10.27), ('C', 'HIS', 'O', 'GLU', 6.48), ('C', 'HIS', 'C', 'GLU', 6.92), ('C', 'HIS', 'CA', 'GLU', 6.88), ('C', 'HIS', 'N', 'GLU', 6.05)], [('CA', 'HIS', 'CB', 'GLU', 7.89), ('CA', 'HIS', 'CG', 'GLU', 8.68), ('CA', 'HIS', 'CD', 'GLU', 9.94), ('CA', 'HIS', 'OE1', 'GLU', 10.02), ('CA', 'HIS', 'OE2', 'GLU', 10.98), ('CA', 'HIS', 'O', 'GLU', 6.59), ('CA', 'HIS', 'C', 'GLU', 7.29), ('CA', 'HIS', 'CA', 'GLU', 7.66), ('CA', 'HIS', 'N', 'GLU', 7.06)], [('N', 'HIS', 'CB', 'GLU', 7.75), ('N', 'HIS', 'CG', 'GLU', 8.44), ('N', 'HIS', 'CD', 'GLU', 9.85), ('N', 'HIS', 'OE1', 'GLU', 10.14), ('N', 'HIS', 'OE2', 'GLU', 10.78), ('N', 'HIS', 'O', 'GLU', 5.86), ('N', 'HIS', 'C', 'GLU', 6.53), ('N', 'HIS', 'CA', 'GLU', 7.22), ('N', 'HIS', 'N', 'GLU', 6.75)], [('CB', 'HIS', 'CB', 'GLU', 13.42), ('CB', 'HIS', 'CG', 'GLU', 12.06), ('CB', 'HIS', 'CD', 'GLU', 10.9), ('CB', 'HIS', 'OE1', 'GLU', 10.45), ('CB', 'HIS', 'OE2', 'GLU', 10.58), ('CB', 'HIS', 'O', 'GLU', 14.41), ('CB', 'HIS', 'C', 'GLU', 14.65), ('CB', 'HIS', 'CA', 'GLU', 14.57), ('CB', 'HIS', 'N', 'GLU', 15.85)], [('CG', 'HIS', 'CB', 'GLU', 12.02), ('CG', 'HIS', 'CG', 'GLU', 10.66), ('CG', 'HIS', 'CD', 'GLU', 9.54), ('CG', 'HIS', 'OE1', 'GLU', 9.03), ('CG', 'HIS', 'OE2', 'GLU', 9.34), ('CG', 'HIS', 'O', 'GLU', 12.98), ('CG', 'HIS', 'C', 'GLU', 13.27), ('CG', 'HIS', 'CA', 'GLU', 13.2), ('CG', 'HIS', 'N', 'GLU', 14.46)], [('ND1', 'HIS', 'CB', 'GLU', 11.67), ('ND1', 'HIS', 'CG', 'GLU', 10.4), ('ND1', 'HIS', 'CD', 'GLU', 9.26), ('ND1', 'HIS', 'OE1', 'GLU', 8.56), ('ND1', 'HIS', 'OE2', 'GLU', 9.25), ('ND1', 'HIS', 'O', 'GLU', 12.75), ('ND1', 'HIS', 'C', 'GLU', 13.1), ('ND1', 'HIS', 'CA', 'GLU', 12.96), ('ND1', 'HIS', 'N', 'GLU', 14.12)], [('CD2', 'HIS', 'CB', 'GLU', 11.18), ('CD2', 'HIS', 'CG', 'GLU', 9.76), ('CD2', 'HIS', 'CD', 'GLU', 8.76), ('CD2', 'HIS', 'OE1', 'GLU', 8.39), ('CD2', 'HIS', 'OE2', 'GLU', 8.54), ('CD2', 'HIS', 'O', 'GLU', 11.93), ('CD2', 'HIS', 'C', 'GLU', 12.22), ('CD2', 'HIS', 'CA', 'GLU', 12.27), ('CD2', 'HIS', 'N', 'GLU', 13.58)], [('CE1', 'HIS', 'CB', 'GLU', 10.58), ('CE1', 'HIS', 'CG', 'GLU', 9.3), ('CE1', 'HIS', 'CD', 'GLU', 8.27), ('CE1', 'HIS', 'OE1', 'GLU', 7.54), ('CE1', 'HIS', 'OE2', 'GLU', 8.4), ('CE1', 'HIS', 'O', 'GLU', 11.52), ('CE1', 'HIS', 'C', 'GLU', 11.94), ('CE1', 'HIS', 'CA', 'GLU', 11.86), ('CE1', 'HIS', 'N', 'GLU', 13.02)], [('NE2', 'HIS', 'CB', 'GLU', 10.22), ('NE2', 'HIS', 'CG', 'GLU', 8.82), ('NE2', 'HIS', 'CD', 'GLU', 7.89), ('NE2', 'HIS', 'OE1', 'GLU', 7.39), ('NE2', 'HIS', 'OE2', 'GLU', 7.88), ('NE2', 'HIS', 'O', 'GLU', 10.94), ('NE2', 'HIS', 'C', 'GLU', 11.32), ('NE2', 'HIS', 'CA', 'GLU', 11.37), ('NE2', 'HIS', 'N', 'GLU', 12.63)], [('O', 'HIS', 'CB', 'GLU', 15.61), ('O', 'HIS', 'CG', 'GLU', 14.21), ('O', 'HIS', 'CD', 'GLU', 13.09), ('O', 'HIS', 'OE1', 'GLU', 12.84), ('O', 'HIS', 'OE2', 'GLU', 12.56), ('O', 'HIS', 'O', 'GLU', 16.49), ('O', 'HIS', 'C', 'GLU', 16.64), ('O', 'HIS', 'CA', 'GLU', 16.62), ('O', 'HIS', 'N', 'GLU', 17.97)], [('C', 'HIS', 'CB', 'GLU', 15.02), ('C', 'HIS', 'CG', 'GLU', 13.67), ('C', 'HIS', 'CD', 'GLU', 12.46), ('C', 'HIS', 'OE1', 'GLU', 12.18), ('C', 'HIS', 'OE2', 'GLU', 11.9), ('C', 'HIS', 'O', 'GLU', 16.12), ('C', 'HIS', 'C', 'GLU', 16.2), ('C', 'HIS', 'CA', 'GLU', 16.07), ('C', 'HIS', 'N', 'GLU', 17.38)], [('CA', 'HIS', 'CB', 'GLU', 13.58), ('CA', 'HIS', 'CG', 'GLU', 12.25), ('CA', 'HIS', 'CD', 'GLU', 11.02), ('CA', 'HIS', 'OE1', 'GLU', 10.69), ('CA', 'HIS', 'OE2', 'GLU', 10.51), ('CA', 'HIS', 'O', 'GLU', 14.75), ('CA', 'HIS', 'C', 'GLU', 14.85), ('CA', 'HIS', 'CA', 'GLU', 14.68), ('CA', 'HIS', 'N', 'GLU', 15.97)], [('N', 'HIS', 'CB', 'GLU', 12.75), ('N', 'HIS', 'CG', 'GLU', 11.4), ('N', 'HIS', 'CD', 'GLU', 10.22), ('N', 'HIS', 'OE1', 'GLU', 10.08), ('N', 'HIS', 'OE2', 'GLU', 9.59), ('N', 'HIS', 'O', 'GLU', 13.84), ('N', 'HIS', 'C', 'GLU', 13.87), ('N', 'HIS', 'CA', 'GLU', 13.74), ('N', 'HIS', 'N', 'GLU', 15.08)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_HIS, d, 'A_1de3_3_1_27_10')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLU, d, 'A_1de3_3_1_27_10')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_HIS' :  match1,
		'HIS_GLU' :  match2}