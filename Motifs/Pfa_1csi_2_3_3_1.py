'''
FUNC:Pfa_1csi_2_3_3_1
PDB:1csi
EC:2.3.3.1
RESI:his,his,asp
LOCI:a-274,320,375;
'''
import motifFunctions as cmd
ASP_HISI = { 
	'distances':
		[[12.27, 11.86, 12.92, 10.7, 12.53, 11.22, 14.61, 13.59, 12.29, 12.35], [12.03, 11.43, 12.35, 10.18, 11.8, 10.49, 14.38, 13.28, 12.07, 12.34], [12.91, 12.19, 13.02, 10.88, 12.35, 11.04, 15.37, 14.24, 13.06, 13.42], [11.13, 10.5, 11.39, 9.27, 10.85, 9.57, 13.37, 12.25, 11.1, 11.43], [14.41, 14.19, 15.34, 13.12, 15.05, 13.76, 16.84, 15.94, 14.53, 14.36], [13.24, 13.01, 14.16, 11.94, 13.89, 12.6, 15.74, 14.84, 13.41, 13.28], [12.61, 12.21, 13.27, 11.04, 12.88, 11.56, 15.18, 14.19, 12.82, 12.87], [11.58, 11.13, 12.17, 9.95, 11.76, 10.45, 14.32, 13.34, 11.95, 12.09]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HISI', 12.27), ('CB', 'ASP', 'CG', 'HISI', 11.86), ('CB', 'ASP', 'ND1', 'HISI', 12.92), ('CB', 'ASP', 'CD2', 'HISI', 10.7), ('CB', 'ASP', 'CE1', 'HISI', 12.53), ('CB', 'ASP', 'NE2', 'HISI', 11.22), ('CB', 'ASP', 'O', 'HISI', 14.61), ('CB', 'ASP', 'C', 'HISI', 13.59), ('CB', 'ASP', 'CA', 'HISI', 12.29), ('CB', 'ASP', 'N', 'HISI', 12.35)], [('CG', 'ASP', 'CB', 'HISI', 12.03), ('CG', 'ASP', 'CG', 'HISI', 11.43), ('CG', 'ASP', 'ND1', 'HISI', 12.35), ('CG', 'ASP', 'CD2', 'HISI', 10.18), ('CG', 'ASP', 'CE1', 'HISI', 11.8), ('CG', 'ASP', 'NE2', 'HISI', 10.49), ('CG', 'ASP', 'O', 'HISI', 14.38), ('CG', 'ASP', 'C', 'HISI', 13.28), ('CG', 'ASP', 'CA', 'HISI', 12.07), ('CG', 'ASP', 'N', 'HISI', 12.34)], [('OD1', 'ASP', 'CB', 'HISI', 12.91), ('OD1', 'ASP', 'CG', 'HISI', 12.19), ('OD1', 'ASP', 'ND1', 'HISI', 13.02), ('OD1', 'ASP', 'CD2', 'HISI', 10.88), ('OD1', 'ASP', 'CE1', 'HISI', 12.35), ('OD1', 'ASP', 'NE2', 'HISI', 11.04), ('OD1', 'ASP', 'O', 'HISI', 15.37), ('OD1', 'ASP', 'C', 'HISI', 14.24), ('OD1', 'ASP', 'CA', 'HISI', 13.06), ('OD1', 'ASP', 'N', 'HISI', 13.42)], [('OD2', 'ASP', 'CB', 'HISI', 11.13), ('OD2', 'ASP', 'CG', 'HISI', 10.5), ('OD2', 'ASP', 'ND1', 'HISI', 11.39), ('OD2', 'ASP', 'CD2', 'HISI', 9.27), ('OD2', 'ASP', 'CE1', 'HISI', 10.85), ('OD2', 'ASP', 'NE2', 'HISI', 9.57), ('OD2', 'ASP', 'O', 'HISI', 13.37), ('OD2', 'ASP', 'C', 'HISI', 12.25), ('OD2', 'ASP', 'CA', 'HISI', 11.1), ('OD2', 'ASP', 'N', 'HISI', 11.43)], [('O', 'ASP', 'CB', 'HISI', 14.41), ('O', 'ASP', 'CG', 'HISI', 14.19), ('O', 'ASP', 'ND1', 'HISI', 15.34), ('O', 'ASP', 'CD2', 'HISI', 13.12), ('O', 'ASP', 'CE1', 'HISI', 15.05), ('O', 'ASP', 'NE2', 'HISI', 13.76), ('O', 'ASP', 'O', 'HISI', 16.84), ('O', 'ASP', 'C', 'HISI', 15.94), ('O', 'ASP', 'CA', 'HISI', 14.53), ('O', 'ASP', 'N', 'HISI', 14.36)], [('C', 'ASP', 'CB', 'HISI', 13.24), ('C', 'ASP', 'CG', 'HISI', 13.01), ('C', 'ASP', 'ND1', 'HISI', 14.16), ('C', 'ASP', 'CD2', 'HISI', 11.94), ('C', 'ASP', 'CE1', 'HISI', 13.89), ('C', 'ASP', 'NE2', 'HISI', 12.6), ('C', 'ASP', 'O', 'HISI', 15.74), ('C', 'ASP', 'C', 'HISI', 14.84), ('C', 'ASP', 'CA', 'HISI', 13.41), ('C', 'ASP', 'N', 'HISI', 13.28)], [('CA', 'ASP', 'CB', 'HISI', 12.61), ('CA', 'ASP', 'CG', 'HISI', 12.21), ('CA', 'ASP', 'ND1', 'HISI', 13.27), ('CA', 'ASP', 'CD2', 'HISI', 11.04), ('CA', 'ASP', 'CE1', 'HISI', 12.88), ('CA', 'ASP', 'NE2', 'HISI', 11.56), ('CA', 'ASP', 'O', 'HISI', 15.18), ('CA', 'ASP', 'C', 'HISI', 14.19), ('CA', 'ASP', 'CA', 'HISI', 12.82), ('CA', 'ASP', 'N', 'HISI', 12.87)], [('N', 'ASP', 'CB', 'HISI', 11.58), ('N', 'ASP', 'CG', 'HISI', 11.13), ('N', 'ASP', 'ND1', 'HISI', 12.17), ('N', 'ASP', 'CD2', 'HISI', 9.95), ('N', 'ASP', 'CE1', 'HISI', 11.76), ('N', 'ASP', 'NE2', 'HISI', 10.45), ('N', 'ASP', 'O', 'HISI', 14.32), ('N', 'ASP', 'C', 'HISI', 13.34), ('N', 'ASP', 'CA', 'HISI', 11.95), ('N', 'ASP', 'N', 'HISI', 12.09)]]}
HIS_HIS = { 
	'distances':
		[[13.29, 12.45, 12.66, 11.59, 11.97, 11.28, 14.1, 12.99, 12.7, 13.42], [13.07, 12.08, 12.15, 11.16, 11.31, 10.65, 14.08, 12.93, 12.67, 13.54], [12.04, 10.97, 11.07, 9.98, 10.17, 9.44, 13.32, 12.13, 11.78, 12.7], [13.95, 12.86, 12.8, 11.95, 11.86, 11.29, 14.94, 13.8, 13.62, 14.57], [12.36, 11.16, 11.1, 10.14, 10.06, 9.4, 13.75, 12.55, 12.25, 13.29], [13.53, 12.33, 12.18, 11.38, 11.14, 10.59, 14.74, 13.57, 13.37, 14.42], [12.52, 11.89, 12.55, 10.85, 12.0, 10.96, 13.9, 12.78, 12.02, 12.41], [12.81, 12.06, 12.57, 11.04, 11.93, 10.98, 14.08, 12.94, 12.31, 12.84], [12.41, 11.69, 12.09, 10.81, 11.5, 10.7, 13.33, 12.23, 11.78, 12.37], [12.72, 12.19, 12.66, 11.43, 12.24, 11.48, 13.34, 12.32, 11.91, 12.33], [13.29, 13.07, 12.04, 13.95, 12.36, 13.53, 12.52, 12.81, 12.41, 12.72], [12.45, 12.08, 10.97, 12.86, 11.16, 12.33, 11.89, 12.06, 11.69, 12.19], [12.66, 12.15, 11.07, 12.8, 11.1, 12.18, 12.55, 12.57, 12.09, 12.66], [11.59, 11.16, 9.98, 11.95, 10.14, 11.38, 10.85, 11.04, 10.81, 11.43], [11.97, 11.31, 10.17, 11.86, 10.06, 11.14, 12.0, 11.93, 11.5, 12.24], [11.28, 10.65, 9.44, 11.29, 9.4, 10.59, 10.96, 10.98, 10.7, 11.48], [14.1, 14.08, 13.32, 14.94, 13.75, 14.74, 13.9, 14.08, 13.33, 13.34], [12.99, 12.93, 12.13, 13.8, 12.55, 13.57, 12.78, 12.94, 12.23, 12.32], [12.7, 12.67, 11.78, 13.62, 12.25, 13.37, 12.02, 12.31, 11.78, 11.91], [13.42, 13.54, 12.7, 14.57, 13.29, 14.42, 12.41, 12.84, 12.37, 12.33]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 13.29), ('CB', 'HIS', 'CG', 'HIS', 12.45), ('CB', 'HIS', 'ND1', 'HIS', 12.66), ('CB', 'HIS', 'CD2', 'HIS', 11.59), ('CB', 'HIS', 'CE1', 'HIS', 11.97), ('CB', 'HIS', 'NE2', 'HIS', 11.28), ('CB', 'HIS', 'O', 'HIS', 14.1), ('CB', 'HIS', 'C', 'HIS', 12.99), ('CB', 'HIS', 'CA', 'HIS', 12.7), ('CB', 'HIS', 'N', 'HIS', 13.42)], [('CG', 'HIS', 'CB', 'HIS', 13.07), ('CG', 'HIS', 'CG', 'HIS', 12.08), ('CG', 'HIS', 'ND1', 'HIS', 12.15), ('CG', 'HIS', 'CD2', 'HIS', 11.16), ('CG', 'HIS', 'CE1', 'HIS', 11.31), ('CG', 'HIS', 'NE2', 'HIS', 10.65), ('CG', 'HIS', 'O', 'HIS', 14.08), ('CG', 'HIS', 'C', 'HIS', 12.93), ('CG', 'HIS', 'CA', 'HIS', 12.67), ('CG', 'HIS', 'N', 'HIS', 13.54)], [('ND1', 'HIS', 'CB', 'HIS', 12.04), ('ND1', 'HIS', 'CG', 'HIS', 10.97), ('ND1', 'HIS', 'ND1', 'HIS', 11.07), ('ND1', 'HIS', 'CD2', 'HIS', 9.98), ('ND1', 'HIS', 'CE1', 'HIS', 10.17), ('ND1', 'HIS', 'NE2', 'HIS', 9.44), ('ND1', 'HIS', 'O', 'HIS', 13.32), ('ND1', 'HIS', 'C', 'HIS', 12.13), ('ND1', 'HIS', 'CA', 'HIS', 11.78), ('ND1', 'HIS', 'N', 'HIS', 12.7)], [('CD2', 'HIS', 'CB', 'HIS', 13.95), ('CD2', 'HIS', 'CG', 'HIS', 12.86), ('CD2', 'HIS', 'ND1', 'HIS', 12.8), ('CD2', 'HIS', 'CD2', 'HIS', 11.95), ('CD2', 'HIS', 'CE1', 'HIS', 11.86), ('CD2', 'HIS', 'NE2', 'HIS', 11.29), ('CD2', 'HIS', 'O', 'HIS', 14.94), ('CD2', 'HIS', 'C', 'HIS', 13.8), ('CD2', 'HIS', 'CA', 'HIS', 13.62), ('CD2', 'HIS', 'N', 'HIS', 14.57)], [('CE1', 'HIS', 'CB', 'HIS', 12.36), ('CE1', 'HIS', 'CG', 'HIS', 11.16), ('CE1', 'HIS', 'ND1', 'HIS', 11.1), ('CE1', 'HIS', 'CD2', 'HIS', 10.14), ('CE1', 'HIS', 'CE1', 'HIS', 10.06), ('CE1', 'HIS', 'NE2', 'HIS', 9.4), ('CE1', 'HIS', 'O', 'HIS', 13.75), ('CE1', 'HIS', 'C', 'HIS', 12.55), ('CE1', 'HIS', 'CA', 'HIS', 12.25), ('CE1', 'HIS', 'N', 'HIS', 13.29)], [('NE2', 'HIS', 'CB', 'HIS', 13.53), ('NE2', 'HIS', 'CG', 'HIS', 12.33), ('NE2', 'HIS', 'ND1', 'HIS', 12.18), ('NE2', 'HIS', 'CD2', 'HIS', 11.38), ('NE2', 'HIS', 'CE1', 'HIS', 11.14), ('NE2', 'HIS', 'NE2', 'HIS', 10.59), ('NE2', 'HIS', 'O', 'HIS', 14.74), ('NE2', 'HIS', 'C', 'HIS', 13.57), ('NE2', 'HIS', 'CA', 'HIS', 13.37), ('NE2', 'HIS', 'N', 'HIS', 14.42)], [('O', 'HIS', 'CB', 'HIS', 12.52), ('O', 'HIS', 'CG', 'HIS', 11.89), ('O', 'HIS', 'ND1', 'HIS', 12.55), ('O', 'HIS', 'CD2', 'HIS', 10.85), ('O', 'HIS', 'CE1', 'HIS', 12.0), ('O', 'HIS', 'NE2', 'HIS', 10.96), ('O', 'HIS', 'O', 'HIS', 13.9), ('O', 'HIS', 'C', 'HIS', 12.78), ('O', 'HIS', 'CA', 'HIS', 12.02), ('O', 'HIS', 'N', 'HIS', 12.41)], [('C', 'HIS', 'CB', 'HIS', 12.81), ('C', 'HIS', 'CG', 'HIS', 12.06), ('C', 'HIS', 'ND1', 'HIS', 12.57), ('C', 'HIS', 'CD2', 'HIS', 11.04), ('C', 'HIS', 'CE1', 'HIS', 11.93), ('C', 'HIS', 'NE2', 'HIS', 10.98), ('C', 'HIS', 'O', 'HIS', 14.08), ('C', 'HIS', 'C', 'HIS', 12.94), ('C', 'HIS', 'CA', 'HIS', 12.31), ('C', 'HIS', 'N', 'HIS', 12.84)], [('CA', 'HIS', 'CB', 'HIS', 12.41), ('CA', 'HIS', 'CG', 'HIS', 11.69), ('CA', 'HIS', 'ND1', 'HIS', 12.09), ('CA', 'HIS', 'CD2', 'HIS', 10.81), ('CA', 'HIS', 'CE1', 'HIS', 11.5), ('CA', 'HIS', 'NE2', 'HIS', 10.7), ('CA', 'HIS', 'O', 'HIS', 13.33), ('CA', 'HIS', 'C', 'HIS', 12.23), ('CA', 'HIS', 'CA', 'HIS', 11.78), ('CA', 'HIS', 'N', 'HIS', 12.37)], [('N', 'HIS', 'CB', 'HIS', 12.72), ('N', 'HIS', 'CG', 'HIS', 12.19), ('N', 'HIS', 'ND1', 'HIS', 12.66), ('N', 'HIS', 'CD2', 'HIS', 11.43), ('N', 'HIS', 'CE1', 'HIS', 12.24), ('N', 'HIS', 'NE2', 'HIS', 11.48), ('N', 'HIS', 'O', 'HIS', 13.34), ('N', 'HIS', 'C', 'HIS', 12.32), ('N', 'HIS', 'CA', 'HIS', 11.91), ('N', 'HIS', 'N', 'HIS', 12.33)], [('CB', 'HIS', 'CB', 'HIS', 13.29), ('CB', 'HIS', 'CG', 'HIS', 13.07), ('CB', 'HIS', 'ND1', 'HIS', 12.04), ('CB', 'HIS', 'CD2', 'HIS', 13.95), ('CB', 'HIS', 'CE1', 'HIS', 12.36), ('CB', 'HIS', 'NE2', 'HIS', 13.53), ('CB', 'HIS', 'O', 'HIS', 12.52), ('CB', 'HIS', 'C', 'HIS', 12.81), ('CB', 'HIS', 'CA', 'HIS', 12.41), ('CB', 'HIS', 'N', 'HIS', 12.72)], [('CG', 'HIS', 'CB', 'HIS', 12.45), ('CG', 'HIS', 'CG', 'HIS', 12.08), ('CG', 'HIS', 'ND1', 'HIS', 10.97), ('CG', 'HIS', 'CD2', 'HIS', 12.86), ('CG', 'HIS', 'CE1', 'HIS', 11.16), ('CG', 'HIS', 'NE2', 'HIS', 12.33), ('CG', 'HIS', 'O', 'HIS', 11.89), ('CG', 'HIS', 'C', 'HIS', 12.06), ('CG', 'HIS', 'CA', 'HIS', 11.69), ('CG', 'HIS', 'N', 'HIS', 12.19)], [('ND1', 'HIS', 'CB', 'HIS', 12.66), ('ND1', 'HIS', 'CG', 'HIS', 12.15), ('ND1', 'HIS', 'ND1', 'HIS', 11.07), ('ND1', 'HIS', 'CD2', 'HIS', 12.8), ('ND1', 'HIS', 'CE1', 'HIS', 11.1), ('ND1', 'HIS', 'NE2', 'HIS', 12.18), ('ND1', 'HIS', 'O', 'HIS', 12.55), ('ND1', 'HIS', 'C', 'HIS', 12.57), ('ND1', 'HIS', 'CA', 'HIS', 12.09), ('ND1', 'HIS', 'N', 'HIS', 12.66)], [('CD2', 'HIS', 'CB', 'HIS', 11.59), ('CD2', 'HIS', 'CG', 'HIS', 11.16), ('CD2', 'HIS', 'ND1', 'HIS', 9.98), ('CD2', 'HIS', 'CD2', 'HIS', 11.95), ('CD2', 'HIS', 'CE1', 'HIS', 10.14), ('CD2', 'HIS', 'NE2', 'HIS', 11.38), ('CD2', 'HIS', 'O', 'HIS', 10.85), ('CD2', 'HIS', 'C', 'HIS', 11.04), ('CD2', 'HIS', 'CA', 'HIS', 10.81), ('CD2', 'HIS', 'N', 'HIS', 11.43)], [('CE1', 'HIS', 'CB', 'HIS', 11.97), ('CE1', 'HIS', 'CG', 'HIS', 11.31), ('CE1', 'HIS', 'ND1', 'HIS', 10.17), ('CE1', 'HIS', 'CD2', 'HIS', 11.86), ('CE1', 'HIS', 'CE1', 'HIS', 10.06), ('CE1', 'HIS', 'NE2', 'HIS', 11.14), ('CE1', 'HIS', 'O', 'HIS', 12.0), ('CE1', 'HIS', 'C', 'HIS', 11.93), ('CE1', 'HIS', 'CA', 'HIS', 11.5), ('CE1', 'HIS', 'N', 'HIS', 12.24)], [('NE2', 'HIS', 'CB', 'HIS', 11.28), ('NE2', 'HIS', 'CG', 'HIS', 10.65), ('NE2', 'HIS', 'ND1', 'HIS', 9.44), ('NE2', 'HIS', 'CD2', 'HIS', 11.29), ('NE2', 'HIS', 'CE1', 'HIS', 9.4), ('NE2', 'HIS', 'NE2', 'HIS', 10.59), ('NE2', 'HIS', 'O', 'HIS', 10.96), ('NE2', 'HIS', 'C', 'HIS', 10.98), ('NE2', 'HIS', 'CA', 'HIS', 10.7), ('NE2', 'HIS', 'N', 'HIS', 11.48)], [('O', 'HIS', 'CB', 'HIS', 14.1), ('O', 'HIS', 'CG', 'HIS', 14.08), ('O', 'HIS', 'ND1', 'HIS', 13.32), ('O', 'HIS', 'CD2', 'HIS', 14.94), ('O', 'HIS', 'CE1', 'HIS', 13.75), ('O', 'HIS', 'NE2', 'HIS', 14.74), ('O', 'HIS', 'O', 'HIS', 13.9), ('O', 'HIS', 'C', 'HIS', 14.08), ('O', 'HIS', 'CA', 'HIS', 13.33), ('O', 'HIS', 'N', 'HIS', 13.34)], [('C', 'HIS', 'CB', 'HIS', 12.99), ('C', 'HIS', 'CG', 'HIS', 12.93), ('C', 'HIS', 'ND1', 'HIS', 12.13), ('C', 'HIS', 'CD2', 'HIS', 13.8), ('C', 'HIS', 'CE1', 'HIS', 12.55), ('C', 'HIS', 'NE2', 'HIS', 13.57), ('C', 'HIS', 'O', 'HIS', 12.78), ('C', 'HIS', 'C', 'HIS', 12.94), ('C', 'HIS', 'CA', 'HIS', 12.23), ('C', 'HIS', 'N', 'HIS', 12.32)], [('CA', 'HIS', 'CB', 'HIS', 12.7), ('CA', 'HIS', 'CG', 'HIS', 12.67), ('CA', 'HIS', 'ND1', 'HIS', 11.78), ('CA', 'HIS', 'CD2', 'HIS', 13.62), ('CA', 'HIS', 'CE1', 'HIS', 12.25), ('CA', 'HIS', 'NE2', 'HIS', 13.37), ('CA', 'HIS', 'O', 'HIS', 12.02), ('CA', 'HIS', 'C', 'HIS', 12.31), ('CA', 'HIS', 'CA', 'HIS', 11.78), ('CA', 'HIS', 'N', 'HIS', 11.91)], [('N', 'HIS', 'CB', 'HIS', 13.42), ('N', 'HIS', 'CG', 'HIS', 13.54), ('N', 'HIS', 'ND1', 'HIS', 12.7), ('N', 'HIS', 'CD2', 'HIS', 14.57), ('N', 'HIS', 'CE1', 'HIS', 13.29), ('N', 'HIS', 'NE2', 'HIS', 14.42), ('N', 'HIS', 'O', 'HIS', 12.41), ('N', 'HIS', 'C', 'HIS', 12.84), ('N', 'HIS', 'CA', 'HIS', 12.37), ('N', 'HIS', 'N', 'HIS', 12.33)]]}
HIS_ASP = { 
	'distances':
		[[11.09, 9.9, 10.21, 9.0, 14.03, 13.6, 12.42, 12.52], [11.26, 9.93, 10.08, 9.03, 14.25, 13.75, 12.46, 12.4], [10.44, 9.07, 9.21, 8.13, 13.47, 12.87, 11.53, 11.34], [12.32, 10.92, 10.93, 10.09, 15.27, 14.78, 13.44, 13.34], [11.13, 9.69, 9.67, 8.82, 14.12, 13.48, 12.08, 11.77], [12.26, 10.8, 10.72, 9.98, 15.21, 14.64, 13.24, 13.0], [7.58, 6.62, 7.18, 5.87, 10.4, 10.06, 9.03, 9.41], [8.61, 7.5, 7.89, 6.7, 11.47, 11.12, 10.0, 10.27], [9.8, 8.72, 9.21, 7.78, 12.73, 12.29, 11.19, 11.33], [10.23, 9.37, 10.01, 8.45, 13.03, 12.65, 11.7, 11.96], [12.27, 12.03, 12.91, 11.13, 14.41, 13.24, 12.61, 11.58], [11.86, 11.43, 12.19, 10.5, 14.19, 13.01, 12.21, 11.13], [12.92, 12.35, 13.02, 11.39, 15.34, 14.16, 13.27, 12.17], [10.7, 10.18, 10.88, 9.27, 13.12, 11.94, 11.04, 9.95], [12.53, 11.8, 12.35, 10.85, 15.05, 13.89, 12.88, 11.76], [11.22, 10.49, 11.04, 9.57, 13.76, 12.6, 11.56, 10.45], [14.61, 14.38, 15.37, 13.37, 16.84, 15.74, 15.18, 14.32], [13.59, 13.28, 14.24, 12.25, 15.94, 14.84, 14.19, 13.34], [12.29, 12.07, 13.06, 11.1, 14.53, 13.41, 12.82, 11.95], [12.35, 12.34, 13.42, 11.43, 14.36, 13.28, 12.87, 12.09]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 11.09), ('CB', 'HIS', 'CG', 'ASP', 9.9), ('CB', 'HIS', 'OD1', 'ASP', 10.21), ('CB', 'HIS', 'OD2', 'ASP', 9.0), ('CB', 'HIS', 'O', 'ASP', 14.03), ('CB', 'HIS', 'C', 'ASP', 13.6), ('CB', 'HIS', 'CA', 'ASP', 12.42), ('CB', 'HIS', 'N', 'ASP', 12.52)], [('CG', 'HIS', 'CB', 'ASP', 11.26), ('CG', 'HIS', 'CG', 'ASP', 9.93), ('CG', 'HIS', 'OD1', 'ASP', 10.08), ('CG', 'HIS', 'OD2', 'ASP', 9.03), ('CG', 'HIS', 'O', 'ASP', 14.25), ('CG', 'HIS', 'C', 'ASP', 13.75), ('CG', 'HIS', 'CA', 'ASP', 12.46), ('CG', 'HIS', 'N', 'ASP', 12.4)], [('ND1', 'HIS', 'CB', 'ASP', 10.44), ('ND1', 'HIS', 'CG', 'ASP', 9.07), ('ND1', 'HIS', 'OD1', 'ASP', 9.21), ('ND1', 'HIS', 'OD2', 'ASP', 8.13), ('ND1', 'HIS', 'O', 'ASP', 13.47), ('ND1', 'HIS', 'C', 'ASP', 12.87), ('ND1', 'HIS', 'CA', 'ASP', 11.53), ('ND1', 'HIS', 'N', 'ASP', 11.34)], [('CD2', 'HIS', 'CB', 'ASP', 12.32), ('CD2', 'HIS', 'CG', 'ASP', 10.92), ('CD2', 'HIS', 'OD1', 'ASP', 10.93), ('CD2', 'HIS', 'OD2', 'ASP', 10.09), ('CD2', 'HIS', 'O', 'ASP', 15.27), ('CD2', 'HIS', 'C', 'ASP', 14.78), ('CD2', 'HIS', 'CA', 'ASP', 13.44), ('CD2', 'HIS', 'N', 'ASP', 13.34)], [('CE1', 'HIS', 'CB', 'ASP', 11.13), ('CE1', 'HIS', 'CG', 'ASP', 9.69), ('CE1', 'HIS', 'OD1', 'ASP', 9.67), ('CE1', 'HIS', 'OD2', 'ASP', 8.82), ('CE1', 'HIS', 'O', 'ASP', 14.12), ('CE1', 'HIS', 'C', 'ASP', 13.48), ('CE1', 'HIS', 'CA', 'ASP', 12.08), ('CE1', 'HIS', 'N', 'ASP', 11.77)], [('NE2', 'HIS', 'CB', 'ASP', 12.26), ('NE2', 'HIS', 'CG', 'ASP', 10.8), ('NE2', 'HIS', 'OD1', 'ASP', 10.72), ('NE2', 'HIS', 'OD2', 'ASP', 9.98), ('NE2', 'HIS', 'O', 'ASP', 15.21), ('NE2', 'HIS', 'C', 'ASP', 14.64), ('NE2', 'HIS', 'CA', 'ASP', 13.24), ('NE2', 'HIS', 'N', 'ASP', 13.0)], [('O', 'HIS', 'CB', 'ASP', 7.58), ('O', 'HIS', 'CG', 'ASP', 6.62), ('O', 'HIS', 'OD1', 'ASP', 7.18), ('O', 'HIS', 'OD2', 'ASP', 5.87), ('O', 'HIS', 'O', 'ASP', 10.4), ('O', 'HIS', 'C', 'ASP', 10.06), ('O', 'HIS', 'CA', 'ASP', 9.03), ('O', 'HIS', 'N', 'ASP', 9.41)], [('C', 'HIS', 'CB', 'ASP', 8.61), ('C', 'HIS', 'CG', 'ASP', 7.5), ('C', 'HIS', 'OD1', 'ASP', 7.89), ('C', 'HIS', 'OD2', 'ASP', 6.7), ('C', 'HIS', 'O', 'ASP', 11.47), ('C', 'HIS', 'C', 'ASP', 11.12), ('C', 'HIS', 'CA', 'ASP', 10.0), ('C', 'HIS', 'N', 'ASP', 10.27)], [('CA', 'HIS', 'CB', 'ASP', 9.8), ('CA', 'HIS', 'CG', 'ASP', 8.72), ('CA', 'HIS', 'OD1', 'ASP', 9.21), ('CA', 'HIS', 'OD2', 'ASP', 7.78), ('CA', 'HIS', 'O', 'ASP', 12.73), ('CA', 'HIS', 'C', 'ASP', 12.29), ('CA', 'HIS', 'CA', 'ASP', 11.19), ('CA', 'HIS', 'N', 'ASP', 11.33)], [('N', 'HIS', 'CB', 'ASP', 10.23), ('N', 'HIS', 'CG', 'ASP', 9.37), ('N', 'HIS', 'OD1', 'ASP', 10.01), ('N', 'HIS', 'OD2', 'ASP', 8.45), ('N', 'HIS', 'O', 'ASP', 13.03), ('N', 'HIS', 'C', 'ASP', 12.65), ('N', 'HIS', 'CA', 'ASP', 11.7), ('N', 'HIS', 'N', 'ASP', 11.96)], [('CB', 'HIS', 'CB', 'ASP', 12.27), ('CB', 'HIS', 'CG', 'ASP', 12.03), ('CB', 'HIS', 'OD1', 'ASP', 12.91), ('CB', 'HIS', 'OD2', 'ASP', 11.13), ('CB', 'HIS', 'O', 'ASP', 14.41), ('CB', 'HIS', 'C', 'ASP', 13.24), ('CB', 'HIS', 'CA', 'ASP', 12.61), ('CB', 'HIS', 'N', 'ASP', 11.58)], [('CG', 'HIS', 'CB', 'ASP', 11.86), ('CG', 'HIS', 'CG', 'ASP', 11.43), ('CG', 'HIS', 'OD1', 'ASP', 12.19), ('CG', 'HIS', 'OD2', 'ASP', 10.5), ('CG', 'HIS', 'O', 'ASP', 14.19), ('CG', 'HIS', 'C', 'ASP', 13.01), ('CG', 'HIS', 'CA', 'ASP', 12.21), ('CG', 'HIS', 'N', 'ASP', 11.13)], [('ND1', 'HIS', 'CB', 'ASP', 12.92), ('ND1', 'HIS', 'CG', 'ASP', 12.35), ('ND1', 'HIS', 'OD1', 'ASP', 13.02), ('ND1', 'HIS', 'OD2', 'ASP', 11.39), ('ND1', 'HIS', 'O', 'ASP', 15.34), ('ND1', 'HIS', 'C', 'ASP', 14.16), ('ND1', 'HIS', 'CA', 'ASP', 13.27), ('ND1', 'HIS', 'N', 'ASP', 12.17)], [('CD2', 'HIS', 'CB', 'ASP', 10.7), ('CD2', 'HIS', 'CG', 'ASP', 10.18), ('CD2', 'HIS', 'OD1', 'ASP', 10.88), ('CD2', 'HIS', 'OD2', 'ASP', 9.27), ('CD2', 'HIS', 'O', 'ASP', 13.12), ('CD2', 'HIS', 'C', 'ASP', 11.94), ('CD2', 'HIS', 'CA', 'ASP', 11.04), ('CD2', 'HIS', 'N', 'ASP', 9.95)], [('CE1', 'HIS', 'CB', 'ASP', 12.53), ('CE1', 'HIS', 'CG', 'ASP', 11.8), ('CE1', 'HIS', 'OD1', 'ASP', 12.35), ('CE1', 'HIS', 'OD2', 'ASP', 10.85), ('CE1', 'HIS', 'O', 'ASP', 15.05), ('CE1', 'HIS', 'C', 'ASP', 13.89), ('CE1', 'HIS', 'CA', 'ASP', 12.88), ('CE1', 'HIS', 'N', 'ASP', 11.76)], [('NE2', 'HIS', 'CB', 'ASP', 11.22), ('NE2', 'HIS', 'CG', 'ASP', 10.49), ('NE2', 'HIS', 'OD1', 'ASP', 11.04), ('NE2', 'HIS', 'OD2', 'ASP', 9.57), ('NE2', 'HIS', 'O', 'ASP', 13.76), ('NE2', 'HIS', 'C', 'ASP', 12.6), ('NE2', 'HIS', 'CA', 'ASP', 11.56), ('NE2', 'HIS', 'N', 'ASP', 10.45)], [('O', 'HIS', 'CB', 'ASP', 14.61), ('O', 'HIS', 'CG', 'ASP', 14.38), ('O', 'HIS', 'OD1', 'ASP', 15.37), ('O', 'HIS', 'OD2', 'ASP', 13.37), ('O', 'HIS', 'O', 'ASP', 16.84), ('O', 'HIS', 'C', 'ASP', 15.74), ('O', 'HIS', 'CA', 'ASP', 15.18), ('O', 'HIS', 'N', 'ASP', 14.32)], [('C', 'HIS', 'CB', 'ASP', 13.59), ('C', 'HIS', 'CG', 'ASP', 13.28), ('C', 'HIS', 'OD1', 'ASP', 14.24), ('C', 'HIS', 'OD2', 'ASP', 12.25), ('C', 'HIS', 'O', 'ASP', 15.94), ('C', 'HIS', 'C', 'ASP', 14.84), ('C', 'HIS', 'CA', 'ASP', 14.19), ('C', 'HIS', 'N', 'ASP', 13.34)], [('CA', 'HIS', 'CB', 'ASP', 12.29), ('CA', 'HIS', 'CG', 'ASP', 12.07), ('CA', 'HIS', 'OD1', 'ASP', 13.06), ('CA', 'HIS', 'OD2', 'ASP', 11.1), ('CA', 'HIS', 'O', 'ASP', 14.53), ('CA', 'HIS', 'C', 'ASP', 13.41), ('CA', 'HIS', 'CA', 'ASP', 12.82), ('CA', 'HIS', 'N', 'ASP', 11.95)], [('N', 'HIS', 'CB', 'ASP', 12.35), ('N', 'HIS', 'CG', 'ASP', 12.34), ('N', 'HIS', 'OD1', 'ASP', 13.42), ('N', 'HIS', 'OD2', 'ASP', 11.43), ('N', 'HIS', 'O', 'ASP', 14.36), ('N', 'HIS', 'C', 'ASP', 13.28), ('N', 'HIS', 'CA', 'ASP', 12.87), ('N', 'HIS', 'N', 'ASP', 12.09)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HISI, d, 'Pfa_1csi_2_3_3_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_HIS, d, 'Pfa_1csi_2_3_3_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'Pfa_1csi_2_3_3_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HISI' :  match1,
		'HIS_HIS' :  match2,
		'HIS_ASP' :  match3}