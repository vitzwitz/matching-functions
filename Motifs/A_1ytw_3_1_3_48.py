'''
FUNC:A_1ytw_3_1_3_48
PDB:1ytw
EC:3.1.3.48
RESI:glu,asp,his,cys,arg,thr
LOCI:a-290,356,402,403,409,410;
'''
import motifFunctions as cmd
THR_HIS = { 
	'distances':
		[[7.65, 8.96, 9.55, 10.03, 10.8, 11.07], [6.43, 7.66, 8.18, 8.78, 9.42, 9.75], [7.66, 9.06, 9.88, 9.98, 11.09, 11.16]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'HIS', 7.65), ('CB', 'THR', 'CG', 'HIS', 8.96), ('CB', 'THR', 'ND1', 'HIS', 9.55), ('CB', 'THR', 'CD2', 'HIS', 10.03), ('CB', 'THR', 'CE1', 'HIS', 10.8), ('CB', 'THR', 'NE2', 'HIS', 11.07)], [('OG1', 'THR', 'CB', 'HIS', 6.43), ('OG1', 'THR', 'CG', 'HIS', 7.66), ('OG1', 'THR', 'ND1', 'HIS', 8.18), ('OG1', 'THR', 'CD2', 'HIS', 8.78), ('OG1', 'THR', 'CE1', 'HIS', 9.42), ('OG1', 'THR', 'NE2', 'HIS', 9.75)], [('CG2', 'THR', 'CB', 'HIS', 7.66), ('CG2', 'THR', 'CG', 'HIS', 9.06), ('CG2', 'THR', 'ND1', 'HIS', 9.88), ('CG2', 'THR', 'CD2', 'HIS', 9.98), ('CG2', 'THR', 'CE1', 'HIS', 11.09), ('CG2', 'THR', 'NE2', 'HIS', 11.16)]]}
THR_ASP = { 
	'distances':
		[[13.23, 12.88, 12.19, 13.5], [12.76, 12.48, 11.94, 13.02], [14.7, 14.32, 13.63, 14.9]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 13.23), ('CB', 'THR', 'CG', 'ASP', 12.88), ('CB', 'THR', 'OD1', 'ASP', 12.19), ('CB', 'THR', 'OD2', 'ASP', 13.5)], [('OG1', 'THR', 'CB', 'ASP', 12.76), ('OG1', 'THR', 'CG', 'ASP', 12.48), ('OG1', 'THR', 'OD1', 'ASP', 11.94), ('OG1', 'THR', 'OD2', 'ASP', 13.02)], [('CG2', 'THR', 'CB', 'ASP', 14.7), ('CG2', 'THR', 'CG', 'ASP', 14.32), ('CG2', 'THR', 'OD1', 'ASP', 13.63), ('CG2', 'THR', 'OD2', 'ASP', 14.9)]]}
HIS_ASP = { 
	'distances':
		[[14.57, 14.32, 14.17, 14.48], [14.81, 14.66, 14.67, 14.76], [13.95, 13.86, 13.98, 13.88], [15.99, 15.91, 15.95, 15.98], [14.7, 14.69, 14.91, 14.65], [15.91, 15.89, 16.07, 15.89]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 14.57), ('CB', 'HIS', 'CG', 'ASP', 14.32), ('CB', 'HIS', 'OD1', 'ASP', 14.17), ('CB', 'HIS', 'OD2', 'ASP', 14.48)], [('CG', 'HIS', 'CB', 'ASP', 14.81), ('CG', 'HIS', 'CG', 'ASP', 14.66), ('CG', 'HIS', 'OD1', 'ASP', 14.67), ('CG', 'HIS', 'OD2', 'ASP', 14.76)], [('ND1', 'HIS', 'CB', 'ASP', 13.95), ('ND1', 'HIS', 'CG', 'ASP', 13.86), ('ND1', 'HIS', 'OD1', 'ASP', 13.98), ('ND1', 'HIS', 'OD2', 'ASP', 13.88)], [('CD2', 'HIS', 'CB', 'ASP', 15.99), ('CD2', 'HIS', 'CG', 'ASP', 15.91), ('CD2', 'HIS', 'OD1', 'ASP', 15.95), ('CD2', 'HIS', 'OD2', 'ASP', 15.98)], [('CE1', 'HIS', 'CB', 'ASP', 14.7), ('CE1', 'HIS', 'CG', 'ASP', 14.69), ('CE1', 'HIS', 'OD1', 'ASP', 14.91), ('CE1', 'HIS', 'OD2', 'ASP', 14.65)], [('NE2', 'HIS', 'CB', 'ASP', 15.91), ('NE2', 'HIS', 'CG', 'ASP', 15.89), ('NE2', 'HIS', 'OD1', 'ASP', 16.07), ('NE2', 'HIS', 'OD2', 'ASP', 15.89)]]}
ARG_ASP = { 
	'distances':
		[[9.07, 9.25, 8.67, 10.25], [7.93, 8.29, 7.76, 9.4], [6.89, 7.46, 7.22, 8.48], [6.27, 6.59, 6.42, 7.47], [5.67, 6.11, 6.3, 6.78], [5.66, 6.5, 6.94, 7.14], [5.65, 5.7, 6.01, 6.08]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 9.07), ('CB', 'ARG', 'CG', 'ASP', 9.25), ('CB', 'ARG', 'OD1', 'ASP', 8.67), ('CB', 'ARG', 'OD2', 'ASP', 10.25)], [('CG', 'ARG', 'CB', 'ASP', 7.93), ('CG', 'ARG', 'CG', 'ASP', 8.29), ('CG', 'ARG', 'OD1', 'ASP', 7.76), ('CG', 'ARG', 'OD2', 'ASP', 9.4)], [('CD', 'ARG', 'CB', 'ASP', 6.89), ('CD', 'ARG', 'CG', 'ASP', 7.46), ('CD', 'ARG', 'OD1', 'ASP', 7.22), ('CD', 'ARG', 'OD2', 'ASP', 8.48)], [('NE', 'ARG', 'CB', 'ASP', 6.27), ('NE', 'ARG', 'CG', 'ASP', 6.59), ('NE', 'ARG', 'OD1', 'ASP', 6.42), ('NE', 'ARG', 'OD2', 'ASP', 7.47)], [('CZ', 'ARG', 'CB', 'ASP', 5.67), ('CZ', 'ARG', 'CG', 'ASP', 6.11), ('CZ', 'ARG', 'OD1', 'ASP', 6.3), ('CZ', 'ARG', 'OD2', 'ASP', 6.78)], [('NH1', 'ARG', 'CB', 'ASP', 5.66), ('NH1', 'ARG', 'CG', 'ASP', 6.5), ('NH1', 'ARG', 'OD1', 'ASP', 6.94), ('NH1', 'ARG', 'OD2', 'ASP', 7.14)], [('NH2', 'ARG', 'CB', 'ASP', 5.65), ('NH2', 'ARG', 'CG', 'ASP', 5.7), ('NH2', 'ARG', 'OD1', 'ASP', 6.01), ('NH2', 'ARG', 'OD2', 'ASP', 6.08)]]}
ARG_GLU = { 
	'distances':
		[[12.6, 11.88, 10.4, 9.74, 10.05], [12.04, 11.15, 9.71, 9.04, 9.42], [10.53, 9.64, 8.22, 7.51, 8.02], [9.73, 8.88, 7.4, 6.9, 6.99], [8.42, 7.58, 6.09, 5.66, 5.69], [7.77, 6.87, 5.46, 4.74, 5.46], [7.99, 7.22, 5.76, 5.72, 5.0]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 12.6), ('CB', 'ARG', 'CG', 'GLU', 11.88), ('CB', 'ARG', 'CD', 'GLU', 10.4), ('CB', 'ARG', 'OE1', 'GLU', 9.74), ('CB', 'ARG', 'OE2', 'GLU', 10.05)], [('CG', 'ARG', 'CB', 'GLU', 12.04), ('CG', 'ARG', 'CG', 'GLU', 11.15), ('CG', 'ARG', 'CD', 'GLU', 9.71), ('CG', 'ARG', 'OE1', 'GLU', 9.04), ('CG', 'ARG', 'OE2', 'GLU', 9.42)], [('CD', 'ARG', 'CB', 'GLU', 10.53), ('CD', 'ARG', 'CG', 'GLU', 9.64), ('CD', 'ARG', 'CD', 'GLU', 8.22), ('CD', 'ARG', 'OE1', 'GLU', 7.51), ('CD', 'ARG', 'OE2', 'GLU', 8.02)], [('NE', 'ARG', 'CB', 'GLU', 9.73), ('NE', 'ARG', 'CG', 'GLU', 8.88), ('NE', 'ARG', 'CD', 'GLU', 7.4), ('NE', 'ARG', 'OE1', 'GLU', 6.9), ('NE', 'ARG', 'OE2', 'GLU', 6.99)], [('CZ', 'ARG', 'CB', 'GLU', 8.42), ('CZ', 'ARG', 'CG', 'GLU', 7.58), ('CZ', 'ARG', 'CD', 'GLU', 6.09), ('CZ', 'ARG', 'OE1', 'GLU', 5.66), ('CZ', 'ARG', 'OE2', 'GLU', 5.69)], [('NH1', 'ARG', 'CB', 'GLU', 7.77), ('NH1', 'ARG', 'CG', 'GLU', 6.87), ('NH1', 'ARG', 'CD', 'GLU', 5.46), ('NH1', 'ARG', 'OE1', 'GLU', 4.74), ('NH1', 'ARG', 'OE2', 'GLU', 5.46)], [('NH2', 'ARG', 'CB', 'GLU', 7.99), ('NH2', 'ARG', 'CG', 'GLU', 7.22), ('NH2', 'ARG', 'CD', 'GLU', 5.76), ('NH2', 'ARG', 'OE1', 'GLU', 5.72), ('NH2', 'ARG', 'OE2', 'GLU', 5.0)]]}
CYS_THR = { 
	'distances':
		[[6.8, 5.84, 8.12], [5.9, 5.24, 7.24]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'THR', 6.8), ('CB', 'CYS', 'OG1', 'THR', 5.84), ('CB', 'CYS', 'CG2', 'THR', 8.12)], [('SG', 'CYS', 'CB', 'THR', 5.9), ('SG', 'CYS', 'OG1', 'THR', 5.24), ('SG', 'CYS', 'CG2', 'THR', 7.24)]]}
ASP_GLU = { 
	'distances':
		[[8.74, 7.34, 6.37, 6.6, 5.84], [9.33, 8.03, 7.06, 7.49, 6.2], [10.46, 9.2, 8.11, 8.42, 7.23], [8.86, 7.63, 6.86, 7.56, 5.88]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 8.74), ('CB', 'ASP', 'CG', 'GLU', 7.34), ('CB', 'ASP', 'CD', 'GLU', 6.37), ('CB', 'ASP', 'OE1', 'GLU', 6.6), ('CB', 'ASP', 'OE2', 'GLU', 5.84)], [('CG', 'ASP', 'CB', 'GLU', 9.33), ('CG', 'ASP', 'CG', 'GLU', 8.03), ('CG', 'ASP', 'CD', 'GLU', 7.06), ('CG', 'ASP', 'OE1', 'GLU', 7.49), ('CG', 'ASP', 'OE2', 'GLU', 6.2)], [('OD1', 'ASP', 'CB', 'GLU', 10.46), ('OD1', 'ASP', 'CG', 'GLU', 9.2), ('OD1', 'ASP', 'CD', 'GLU', 8.11), ('OD1', 'ASP', 'OE1', 'GLU', 8.42), ('OD1', 'ASP', 'OE2', 'GLU', 7.23)], [('OD2', 'ASP', 'CB', 'GLU', 8.86), ('OD2', 'ASP', 'CG', 'GLU', 7.63), ('OD2', 'ASP', 'CD', 'GLU', 6.86), ('OD2', 'ASP', 'OE1', 'GLU', 7.56), ('OD2', 'ASP', 'OE2', 'GLU', 5.88)]]}
ARG_HIS = { 
	'distances':
		[[10.72, 11.4, 11.24, 12.54, 12.28, 13.02], [11.95, 12.53, 12.21, 13.67, 13.18, 14.03], [11.85, 12.23, 11.72, 13.36, 12.59, 13.54], [11.13, 11.51, 10.92, 12.7, 11.82, 12.85], [11.24, 11.46, 10.7, 12.62, 11.49, 12.62], [12.01, 12.07, 11.22, 13.14, 11.87, 13.01], [10.94, 11.15, 10.33, 12.35, 11.14, 12.32]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 10.72), ('CB', 'ARG', 'CG', 'HIS', 11.4), ('CB', 'ARG', 'ND1', 'HIS', 11.24), ('CB', 'ARG', 'CD2', 'HIS', 12.54), ('CB', 'ARG', 'CE1', 'HIS', 12.28), ('CB', 'ARG', 'NE2', 'HIS', 13.02)], [('CG', 'ARG', 'CB', 'HIS', 11.95), ('CG', 'ARG', 'CG', 'HIS', 12.53), ('CG', 'ARG', 'ND1', 'HIS', 12.21), ('CG', 'ARG', 'CD2', 'HIS', 13.67), ('CG', 'ARG', 'CE1', 'HIS', 13.18), ('CG', 'ARG', 'NE2', 'HIS', 14.03)], [('CD', 'ARG', 'CB', 'HIS', 11.85), ('CD', 'ARG', 'CG', 'HIS', 12.23), ('CD', 'ARG', 'ND1', 'HIS', 11.72), ('CD', 'ARG', 'CD2', 'HIS', 13.36), ('CD', 'ARG', 'CE1', 'HIS', 12.59), ('CD', 'ARG', 'NE2', 'HIS', 13.54)], [('NE', 'ARG', 'CB', 'HIS', 11.13), ('NE', 'ARG', 'CG', 'HIS', 11.51), ('NE', 'ARG', 'ND1', 'HIS', 10.92), ('NE', 'ARG', 'CD2', 'HIS', 12.7), ('NE', 'ARG', 'CE1', 'HIS', 11.82), ('NE', 'ARG', 'NE2', 'HIS', 12.85)], [('CZ', 'ARG', 'CB', 'HIS', 11.24), ('CZ', 'ARG', 'CG', 'HIS', 11.46), ('CZ', 'ARG', 'ND1', 'HIS', 10.7), ('CZ', 'ARG', 'CD2', 'HIS', 12.62), ('CZ', 'ARG', 'CE1', 'HIS', 11.49), ('CZ', 'ARG', 'NE2', 'HIS', 12.62)], [('NH1', 'ARG', 'CB', 'HIS', 12.01), ('NH1', 'ARG', 'CG', 'HIS', 12.07), ('NH1', 'ARG', 'ND1', 'HIS', 11.22), ('NH1', 'ARG', 'CD2', 'HIS', 13.14), ('NH1', 'ARG', 'CE1', 'HIS', 11.87), ('NH1', 'ARG', 'NE2', 'HIS', 13.01)], [('NH2', 'ARG', 'CB', 'HIS', 10.94), ('NH2', 'ARG', 'CG', 'HIS', 11.15), ('NH2', 'ARG', 'ND1', 'HIS', 10.33), ('NH2', 'ARG', 'CD2', 'HIS', 12.35), ('NH2', 'ARG', 'CE1', 'HIS', 11.14), ('NH2', 'ARG', 'NE2', 'HIS', 12.32)]]}
ARG_CYS = { 
	'distances':
		[[5.69, 6.04], [6.55, 7.02], [6.3, 7.13], [5.5, 6.25], [5.88, 6.8], [6.85, 7.99], [5.93, 6.61]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYS', 5.69), ('CB', 'ARG', 'SG', 'CYS', 6.04)], [('CG', 'ARG', 'CB', 'CYS', 6.55), ('CG', 'ARG', 'SG', 'CYS', 7.02)], [('CD', 'ARG', 'CB', 'CYS', 6.3), ('CD', 'ARG', 'SG', 'CYS', 7.13)], [('NE', 'ARG', 'CB', 'CYS', 5.5), ('NE', 'ARG', 'SG', 'CYS', 6.25)], [('CZ', 'ARG', 'CB', 'CYS', 5.88), ('CZ', 'ARG', 'SG', 'CYS', 6.8)], [('NH1', 'ARG', 'CB', 'CYS', 6.85), ('NH1', 'ARG', 'SG', 'CYS', 7.99)], [('NH2', 'ARG', 'CB', 'CYS', 5.93), ('NH2', 'ARG', 'SG', 'CYS', 6.61)]]}
THR_GLU = { 
	'distances':
		[[15.52, 15.23, 13.78, 13.37, 13.18], [14.43, 14.25, 12.84, 12.42, 12.29], [16.76, 16.55, 15.13, 14.72, 14.52]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'GLU', 15.52), ('CB', 'THR', 'CG', 'GLU', 15.23), ('CB', 'THR', 'CD', 'GLU', 13.78), ('CB', 'THR', 'OE1', 'GLU', 13.37), ('CB', 'THR', 'OE2', 'GLU', 13.18)], [('OG1', 'THR', 'CB', 'GLU', 14.43), ('OG1', 'THR', 'CG', 'GLU', 14.25), ('OG1', 'THR', 'CD', 'GLU', 12.84), ('OG1', 'THR', 'OE1', 'GLU', 12.42), ('OG1', 'THR', 'OE2', 'GLU', 12.29)], [('CG2', 'THR', 'CB', 'GLU', 16.76), ('CG2', 'THR', 'CG', 'GLU', 16.55), ('CG2', 'THR', 'CD', 'GLU', 15.13), ('CG2', 'THR', 'OE1', 'GLU', 14.72), ('CG2', 'THR', 'OE2', 'GLU', 14.52)]]}
HIS_GLU = { 
	'distances':
		[[13.85, 14.21, 13.11, 12.83, 12.69], [13.3, 13.82, 12.84, 12.54, 12.55], [11.99, 12.59, 11.69, 11.43, 11.43], [14.05, 14.69, 13.79, 13.46, 13.58], [12.04, 12.81, 12.05, 11.78, 11.92], [13.32, 14.09, 13.32, 13.01, 13.21]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 13.85), ('CB', 'HIS', 'CG', 'GLU', 14.21), ('CB', 'HIS', 'CD', 'GLU', 13.11), ('CB', 'HIS', 'OE1', 'GLU', 12.83), ('CB', 'HIS', 'OE2', 'GLU', 12.69)], [('CG', 'HIS', 'CB', 'GLU', 13.3), ('CG', 'HIS', 'CG', 'GLU', 13.82), ('CG', 'HIS', 'CD', 'GLU', 12.84), ('CG', 'HIS', 'OE1', 'GLU', 12.54), ('CG', 'HIS', 'OE2', 'GLU', 12.55)], [('ND1', 'HIS', 'CB', 'GLU', 11.99), ('ND1', 'HIS', 'CG', 'GLU', 12.59), ('ND1', 'HIS', 'CD', 'GLU', 11.69), ('ND1', 'HIS', 'OE1', 'GLU', 11.43), ('ND1', 'HIS', 'OE2', 'GLU', 11.43)], [('CD2', 'HIS', 'CB', 'GLU', 14.05), ('CD2', 'HIS', 'CG', 'GLU', 14.69), ('CD2', 'HIS', 'CD', 'GLU', 13.79), ('CD2', 'HIS', 'OE1', 'GLU', 13.46), ('CD2', 'HIS', 'OE2', 'GLU', 13.58)], [('CE1', 'HIS', 'CB', 'GLU', 12.04), ('CE1', 'HIS', 'CG', 'GLU', 12.81), ('CE1', 'HIS', 'CD', 'GLU', 12.05), ('CE1', 'HIS', 'OE1', 'GLU', 11.78), ('CE1', 'HIS', 'OE2', 'GLU', 11.92)], [('NE2', 'HIS', 'CB', 'GLU', 13.32), ('NE2', 'HIS', 'CG', 'GLU', 14.09), ('NE2', 'HIS', 'CD', 'GLU', 13.32), ('NE2', 'HIS', 'OE1', 'GLU', 13.01), ('NE2', 'HIS', 'OE2', 'GLU', 13.21)]]}
CYS_HIS = { 
	'distances':
		[[7.66, 8.19, 7.83, 9.44, 8.92, 9.81], [7.76, 8.64, 8.49, 9.96, 9.72, 10.53]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 7.66), ('CB', 'CYS', 'CG', 'HIS', 8.19), ('CB', 'CYS', 'ND1', 'HIS', 7.83), ('CB', 'CYS', 'CD2', 'HIS', 9.44), ('CB', 'CYS', 'CE1', 'HIS', 8.92), ('CB', 'CYS', 'NE2', 'HIS', 9.81)], [('SG', 'CYS', 'CB', 'HIS', 7.76), ('SG', 'CYS', 'CG', 'HIS', 8.64), ('SG', 'CYS', 'ND1', 'HIS', 8.49), ('SG', 'CYS', 'CD2', 'HIS', 9.96), ('SG', 'CYS', 'CE1', 'HIS', 9.72), ('SG', 'CYS', 'NE2', 'HIS', 10.53)]]}
ARG_THR = { 
	'distances':
		[[7.41, 7.29, 8.85], [8.9, 8.77, 10.37], [9.67, 9.27, 11.15], [9.38, 8.86, 10.87], [10.26, 9.57, 11.71], [11.31, 10.57, 12.75], [10.37, 9.62, 11.78]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'THR', 7.41), ('CB', 'ARG', 'OG1', 'THR', 7.29), ('CB', 'ARG', 'CG2', 'THR', 8.85)], [('CG', 'ARG', 'CB', 'THR', 8.9), ('CG', 'ARG', 'OG1', 'THR', 8.77), ('CG', 'ARG', 'CG2', 'THR', 10.37)], [('CD', 'ARG', 'CB', 'THR', 9.67), ('CD', 'ARG', 'OG1', 'THR', 9.27), ('CD', 'ARG', 'CG2', 'THR', 11.15)], [('NE', 'ARG', 'CB', 'THR', 9.38), ('NE', 'ARG', 'OG1', 'THR', 8.86), ('NE', 'ARG', 'CG2', 'THR', 10.87)], [('CZ', 'ARG', 'CB', 'THR', 10.26), ('CZ', 'ARG', 'OG1', 'THR', 9.57), ('CZ', 'ARG', 'CG2', 'THR', 11.71)], [('NH1', 'ARG', 'CB', 'THR', 11.31), ('NH1', 'ARG', 'OG1', 'THR', 10.57), ('NH1', 'ARG', 'CG2', 'THR', 12.75)], [('NH2', 'ARG', 'CB', 'THR', 10.37), ('NH2', 'ARG', 'OG1', 'THR', 9.62), ('NH2', 'ARG', 'CG2', 'THR', 11.78)]]}
CYS_GLU = { 
	'distances':
		[[10.75, 10.46, 9.03, 8.61, 8.53], [11.9, 11.52, 10.09, 9.85, 9.36]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 10.75), ('CB', 'CYS', 'CG', 'GLU', 10.46), ('CB', 'CYS', 'CD', 'GLU', 9.03), ('CB', 'CYS', 'OE1', 'GLU', 8.61), ('CB', 'CYS', 'OE2', 'GLU', 8.53)], [('SG', 'CYS', 'CB', 'GLU', 11.9), ('SG', 'CYS', 'CG', 'GLU', 11.52), ('SG', 'CYS', 'CD', 'GLU', 10.09), ('SG', 'CYS', 'OE1', 'GLU', 9.85), ('SG', 'CYS', 'OE2', 'GLU', 9.36)]]}
CYS_ASP = { 
	'distances':
		[[9.3, 9.22, 8.99, 9.73], [9.7, 9.31, 8.84, 9.79]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 9.3), ('CB', 'CYS', 'CG', 'ASP', 9.22), ('CB', 'CYS', 'OD1', 'ASP', 8.99), ('CB', 'CYS', 'OD2', 'ASP', 9.73)], [('SG', 'CYS', 'CB', 'ASP', 9.7), ('SG', 'CYS', 'CG', 'ASP', 9.31), ('SG', 'CYS', 'OD1', 'ASP', 8.84), ('SG', 'CYS', 'OD2', 'ASP', 9.79)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_HIS, d, 'A_1ytw_3_1_3_48')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(THR_ASP, d, 'A_1ytw_3_1_3_48')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1ytw_3_1_3_48')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_ASP, d, 'A_1ytw_3_1_3_48')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_GLU, d, 'A_1ytw_3_1_3_48')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_THR, d, 'A_1ytw_3_1_3_48')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASP_GLU, d, 'A_1ytw_3_1_3_48')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ARG_HIS, d, 'A_1ytw_3_1_3_48')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ARG_CYS, d, 'A_1ytw_3_1_3_48')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(THR_GLU, d, 'A_1ytw_3_1_3_48')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(HIS_GLU, d, 'A_1ytw_3_1_3_48')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(CYS_HIS, d, 'A_1ytw_3_1_3_48')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(ARG_THR, d, 'A_1ytw_3_1_3_48')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(CYS_GLU, d, 'A_1ytw_3_1_3_48')
	if match14 == []:
		 flag = True
		 break
	match15 , totTime15 = cmd.detect(CYS_ASP, d, 'A_1ytw_3_1_3_48')
	if match15 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_HIS' :  match1,
		'THR_ASP' :  match2,
		'HIS_ASP' :  match3,
		'ARG_ASP' :  match4,
		'ARG_GLU' :  match5,
		'CYS_THR' :  match6,
		'ASP_GLU' :  match7,
		'ARG_HIS' :  match8,
		'ARG_CYS' :  match9,
		'THR_GLU' :  match10,
		'HIS_GLU' :  match11,
		'CYS_HIS' :  match12,
		'ARG_THR' :  match13,
		'CYS_GLU' :  match14,
		'CYS_ASP' :  match15}