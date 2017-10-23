'''
FUNC:A_1tys_2_1_1_45
PDB:1tys
EC:2.1.1.45
RESI:glu,tyr,ser,arg,asp
LOCI:a-58,94,146,166,169;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[11.28, 9.78, 9.02, 9.4, 7.65, 8.11, 7.1, 5.75], [12.03, 10.55, 9.75, 10.23, 8.4, 8.98, 7.96, 6.67]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 11.28), ('CB', 'SER', 'CG', 'TYR', 9.78), ('CB', 'SER', 'CD1', 'TYR', 9.02), ('CB', 'SER', 'CD2', 'TYR', 9.4), ('CB', 'SER', 'CE1', 'TYR', 7.65), ('CB', 'SER', 'CE2', 'TYR', 8.11), ('CB', 'SER', 'CZ', 'TYR', 7.1), ('CB', 'SER', 'OH', 'TYR', 5.75)], [('OG', 'SER', 'CB', 'TYR', 12.03), ('OG', 'SER', 'CG', 'TYR', 10.55), ('OG', 'SER', 'CD1', 'TYR', 9.75), ('OG', 'SER', 'CD2', 'TYR', 10.23), ('OG', 'SER', 'CE1', 'TYR', 8.4), ('OG', 'SER', 'CE2', 'TYR', 8.98), ('OG', 'SER', 'CZ', 'TYR', 7.96), ('OG', 'SER', 'OH', 'TYR', 6.67)]]}
ARG_TYR = { 
	'distances':
		[[15.18, 13.9, 12.75, 14.05, 11.61, 13.05, 11.78, 10.8], [14.21, 12.88, 11.81, 12.9, 10.61, 11.84, 10.63, 9.59], [14.31, 13.01, 12.03, 12.97, 10.87, 11.92, 10.82, 9.82], [13.47, 12.12, 11.26, 11.95, 10.07, 10.86, 9.85, 8.82], [13.95, 12.55, 11.79, 12.21, 10.55, 11.02, 10.12, 8.97], [15.24, 13.83, 13.07, 13.46, 11.8, 12.24, 11.35, 10.15], [13.23, 11.81, 11.2, 11.34, 9.95, 10.12, 9.35, 8.2]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'TYR', 15.18), ('CB', 'ARG', 'CG', 'TYR', 13.9), ('CB', 'ARG', 'CD1', 'TYR', 12.75), ('CB', 'ARG', 'CD2', 'TYR', 14.05), ('CB', 'ARG', 'CE1', 'TYR', 11.61), ('CB', 'ARG', 'CE2', 'TYR', 13.05), ('CB', 'ARG', 'CZ', 'TYR', 11.78), ('CB', 'ARG', 'OH', 'TYR', 10.8)], [('CG', 'ARG', 'CB', 'TYR', 14.21), ('CG', 'ARG', 'CG', 'TYR', 12.88), ('CG', 'ARG', 'CD1', 'TYR', 11.81), ('CG', 'ARG', 'CD2', 'TYR', 12.9), ('CG', 'ARG', 'CE1', 'TYR', 10.61), ('CG', 'ARG', 'CE2', 'TYR', 11.84), ('CG', 'ARG', 'CZ', 'TYR', 10.63), ('CG', 'ARG', 'OH', 'TYR', 9.59)], [('CD', 'ARG', 'CB', 'TYR', 14.31), ('CD', 'ARG', 'CG', 'TYR', 13.01), ('CD', 'ARG', 'CD1', 'TYR', 12.03), ('CD', 'ARG', 'CD2', 'TYR', 12.97), ('CD', 'ARG', 'CE1', 'TYR', 10.87), ('CD', 'ARG', 'CE2', 'TYR', 11.92), ('CD', 'ARG', 'CZ', 'TYR', 10.82), ('CD', 'ARG', 'OH', 'TYR', 9.82)], [('NE', 'ARG', 'CB', 'TYR', 13.47), ('NE', 'ARG', 'CG', 'TYR', 12.12), ('NE', 'ARG', 'CD1', 'TYR', 11.26), ('NE', 'ARG', 'CD2', 'TYR', 11.95), ('NE', 'ARG', 'CE1', 'TYR', 10.07), ('NE', 'ARG', 'CE2', 'TYR', 10.86), ('NE', 'ARG', 'CZ', 'TYR', 9.85), ('NE', 'ARG', 'OH', 'TYR', 8.82)], [('CZ', 'ARG', 'CB', 'TYR', 13.95), ('CZ', 'ARG', 'CG', 'TYR', 12.55), ('CZ', 'ARG', 'CD1', 'TYR', 11.79), ('CZ', 'ARG', 'CD2', 'TYR', 12.21), ('CZ', 'ARG', 'CE1', 'TYR', 10.55), ('CZ', 'ARG', 'CE2', 'TYR', 11.02), ('CZ', 'ARG', 'CZ', 'TYR', 10.12), ('CZ', 'ARG', 'OH', 'TYR', 8.97)], [('NH1', 'ARG', 'CB', 'TYR', 15.24), ('NH1', 'ARG', 'CG', 'TYR', 13.83), ('NH1', 'ARG', 'CD1', 'TYR', 13.07), ('NH1', 'ARG', 'CD2', 'TYR', 13.46), ('NH1', 'ARG', 'CE1', 'TYR', 11.8), ('NH1', 'ARG', 'CE2', 'TYR', 12.24), ('NH1', 'ARG', 'CZ', 'TYR', 11.35), ('NH1', 'ARG', 'OH', 'TYR', 10.15)], [('NH2', 'ARG', 'CB', 'TYR', 13.23), ('NH2', 'ARG', 'CG', 'TYR', 11.81), ('NH2', 'ARG', 'CD1', 'TYR', 11.2), ('NH2', 'ARG', 'CD2', 'TYR', 11.34), ('NH2', 'ARG', 'CE1', 'TYR', 9.95), ('NH2', 'ARG', 'CE2', 'TYR', 10.12), ('NH2', 'ARG', 'CZ', 'TYR', 9.35), ('NH2', 'ARG', 'OH', 'TYR', 8.2)]]}
ARG_SER = { 
	'distances':
		[[8.16, 8.26], [6.93, 7.28], [7.51, 8.16], [6.7, 7.6], [6.55, 7.44], [7.36, 8.02], [6.11, 7.2]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'SER', 8.16), ('CB', 'ARG', 'OG', 'SER', 8.26)], [('CG', 'ARG', 'CB', 'SER', 6.93), ('CG', 'ARG', 'OG', 'SER', 7.28)], [('CD', 'ARG', 'CB', 'SER', 7.51), ('CD', 'ARG', 'OG', 'SER', 8.16)], [('NE', 'ARG', 'CB', 'SER', 6.7), ('NE', 'ARG', 'OG', 'SER', 7.6)], [('CZ', 'ARG', 'CB', 'SER', 6.55), ('CZ', 'ARG', 'OG', 'SER', 7.44)], [('NH1', 'ARG', 'CB', 'SER', 7.36), ('NH1', 'ARG', 'OG', 'SER', 8.02)], [('NH2', 'ARG', 'CB', 'SER', 6.11), ('NH2', 'ARG', 'OG', 'SER', 7.2)]]}
TYR_ASP = { 
	'distances':
		[[17.89, 18.92, 19.92, 18.79], [16.47, 17.53, 18.55, 17.41], [16.08, 17.24, 18.23, 17.21], [15.72, 16.7, 17.75, 16.5], [14.85, 16.04, 17.05, 16.04], [14.45, 15.46, 16.53, 15.26], [13.99, 15.11, 16.16, 15.03], [12.77, 13.94, 15.0, 13.88]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 17.89), ('CB', 'TYR', 'CG', 'ASP', 18.92), ('CB', 'TYR', 'OD1', 'ASP', 19.92), ('CB', 'TYR', 'OD2', 'ASP', 18.79)], [('CG', 'TYR', 'CB', 'ASP', 16.47), ('CG', 'TYR', 'CG', 'ASP', 17.53), ('CG', 'TYR', 'OD1', 'ASP', 18.55), ('CG', 'TYR', 'OD2', 'ASP', 17.41)], [('CD1', 'TYR', 'CB', 'ASP', 16.08), ('CD1', 'TYR', 'CG', 'ASP', 17.24), ('CD1', 'TYR', 'OD1', 'ASP', 18.23), ('CD1', 'TYR', 'OD2', 'ASP', 17.21)], [('CD2', 'TYR', 'CB', 'ASP', 15.72), ('CD2', 'TYR', 'CG', 'ASP', 16.7), ('CD2', 'TYR', 'OD1', 'ASP', 17.75), ('CD2', 'TYR', 'OD2', 'ASP', 16.5)], [('CE1', 'TYR', 'CB', 'ASP', 14.85), ('CE1', 'TYR', 'CG', 'ASP', 16.04), ('CE1', 'TYR', 'OD1', 'ASP', 17.05), ('CE1', 'TYR', 'OD2', 'ASP', 16.04)], [('CE2', 'TYR', 'CB', 'ASP', 14.45), ('CE2', 'TYR', 'CG', 'ASP', 15.46), ('CE2', 'TYR', 'OD1', 'ASP', 16.53), ('CE2', 'TYR', 'OD2', 'ASP', 15.26)], [('CZ', 'TYR', 'CB', 'ASP', 13.99), ('CZ', 'TYR', 'CG', 'ASP', 15.11), ('CZ', 'TYR', 'OD1', 'ASP', 16.16), ('CZ', 'TYR', 'OD2', 'ASP', 15.03)], [('OH', 'TYR', 'CB', 'ASP', 12.77), ('OH', 'TYR', 'CG', 'ASP', 13.94), ('OH', 'TYR', 'OD1', 'ASP', 15.0), ('OH', 'TYR', 'OD2', 'ASP', 13.88)]]}
ARG_GLU = { 
	'distances':
		[[20.31, 19.11, 17.87, 17.68, 17.18], [19.32, 18.07, 16.84, 16.74, 16.08], [19.86, 18.54, 17.37, 17.38, 16.54], [18.92, 17.56, 16.42, 16.51, 15.52], [18.85, 17.51, 16.32, 16.43, 15.36], [19.82, 18.51, 17.28, 17.35, 16.32], [17.93, 16.56, 15.4, 15.59, 14.4]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 20.31), ('CB', 'ARG', 'CG', 'GLU', 19.11), ('CB', 'ARG', 'CD', 'GLU', 17.87), ('CB', 'ARG', 'OE1', 'GLU', 17.68), ('CB', 'ARG', 'OE2', 'GLU', 17.18)], [('CG', 'ARG', 'CB', 'GLU', 19.32), ('CG', 'ARG', 'CG', 'GLU', 18.07), ('CG', 'ARG', 'CD', 'GLU', 16.84), ('CG', 'ARG', 'OE1', 'GLU', 16.74), ('CG', 'ARG', 'OE2', 'GLU', 16.08)], [('CD', 'ARG', 'CB', 'GLU', 19.86), ('CD', 'ARG', 'CG', 'GLU', 18.54), ('CD', 'ARG', 'CD', 'GLU', 17.37), ('CD', 'ARG', 'OE1', 'GLU', 17.38), ('CD', 'ARG', 'OE2', 'GLU', 16.54)], [('NE', 'ARG', 'CB', 'GLU', 18.92), ('NE', 'ARG', 'CG', 'GLU', 17.56), ('NE', 'ARG', 'CD', 'GLU', 16.42), ('NE', 'ARG', 'OE1', 'GLU', 16.51), ('NE', 'ARG', 'OE2', 'GLU', 15.52)], [('CZ', 'ARG', 'CB', 'GLU', 18.85), ('CZ', 'ARG', 'CG', 'GLU', 17.51), ('CZ', 'ARG', 'CD', 'GLU', 16.32), ('CZ', 'ARG', 'OE1', 'GLU', 16.43), ('CZ', 'ARG', 'OE2', 'GLU', 15.36)], [('NH1', 'ARG', 'CB', 'GLU', 19.82), ('NH1', 'ARG', 'CG', 'GLU', 18.51), ('NH1', 'ARG', 'CD', 'GLU', 17.28), ('NH1', 'ARG', 'OE1', 'GLU', 17.35), ('NH1', 'ARG', 'OE2', 'GLU', 16.32)], [('NH2', 'ARG', 'CB', 'GLU', 17.93), ('NH2', 'ARG', 'CG', 'GLU', 16.56), ('NH2', 'ARG', 'CD', 'GLU', 15.4), ('NH2', 'ARG', 'OE1', 'GLU', 15.59), ('NH2', 'ARG', 'OE2', 'GLU', 14.4)]]}
TYR_GLU = { 
	'distances':
		[[10.99, 9.68, 9.63, 10.19, 9.29], [11.0, 9.61, 9.26, 9.77, 8.76], [11.74, 10.39, 9.87, 10.2, 9.4], [10.56, 9.09, 8.67, 9.31, 7.99], [12.04, 10.68, 9.93, 10.18, 9.34], [10.9, 9.42, 8.75, 9.3, 7.91], [11.65, 10.22, 9.39, 9.75, 8.63], [12.25, 10.85, 9.84, 10.09, 9.0]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 10.99), ('CB', 'TYR', 'CG', 'GLU', 9.68), ('CB', 'TYR', 'CD', 'GLU', 9.63), ('CB', 'TYR', 'OE1', 'GLU', 10.19), ('CB', 'TYR', 'OE2', 'GLU', 9.29)], [('CG', 'TYR', 'CB', 'GLU', 11.0), ('CG', 'TYR', 'CG', 'GLU', 9.61), ('CG', 'TYR', 'CD', 'GLU', 9.26), ('CG', 'TYR', 'OE1', 'GLU', 9.77), ('CG', 'TYR', 'OE2', 'GLU', 8.76)], [('CD1', 'TYR', 'CB', 'GLU', 11.74), ('CD1', 'TYR', 'CG', 'GLU', 10.39), ('CD1', 'TYR', 'CD', 'GLU', 9.87), ('CD1', 'TYR', 'OE1', 'GLU', 10.2), ('CD1', 'TYR', 'OE2', 'GLU', 9.4)], [('CD2', 'TYR', 'CB', 'GLU', 10.56), ('CD2', 'TYR', 'CG', 'GLU', 9.09), ('CD2', 'TYR', 'CD', 'GLU', 8.67), ('CD2', 'TYR', 'OE1', 'GLU', 9.31), ('CD2', 'TYR', 'OE2', 'GLU', 7.99)], [('CE1', 'TYR', 'CB', 'GLU', 12.04), ('CE1', 'TYR', 'CG', 'GLU', 10.68), ('CE1', 'TYR', 'CD', 'GLU', 9.93), ('CE1', 'TYR', 'OE1', 'GLU', 10.18), ('CE1', 'TYR', 'OE2', 'GLU', 9.34)], [('CE2', 'TYR', 'CB', 'GLU', 10.9), ('CE2', 'TYR', 'CG', 'GLU', 9.42), ('CE2', 'TYR', 'CD', 'GLU', 8.75), ('CE2', 'TYR', 'OE1', 'GLU', 9.3), ('CE2', 'TYR', 'OE2', 'GLU', 7.91)], [('CZ', 'TYR', 'CB', 'GLU', 11.65), ('CZ', 'TYR', 'CG', 'GLU', 10.22), ('CZ', 'TYR', 'CD', 'GLU', 9.39), ('CZ', 'TYR', 'OE1', 'GLU', 9.75), ('CZ', 'TYR', 'OE2', 'GLU', 8.63)], [('OH', 'TYR', 'CB', 'GLU', 12.25), ('OH', 'TYR', 'CG', 'GLU', 10.85), ('OH', 'TYR', 'CD', 'GLU', 9.84), ('OH', 'TYR', 'OE1', 'GLU', 10.09), ('OH', 'TYR', 'OE2', 'GLU', 9.0)]]}
ARG_ASP = { 
	'distances':
		[[13.8, 15.28, 16.07, 15.75], [13.05, 14.51, 15.39, 14.87], [13.78, 15.18, 16.12, 15.42], [13.24, 14.59, 15.61, 14.72], [12.35, 13.64, 14.68, 13.71], [12.1, 13.36, 14.35, 13.46], [11.99, 13.21, 14.31, 13.16]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 13.8), ('CB', 'ARG', 'CG', 'ASP', 15.28), ('CB', 'ARG', 'OD1', 'ASP', 16.07), ('CB', 'ARG', 'OD2', 'ASP', 15.75)], [('CG', 'ARG', 'CB', 'ASP', 13.05), ('CG', 'ARG', 'CG', 'ASP', 14.51), ('CG', 'ARG', 'OD1', 'ASP', 15.39), ('CG', 'ARG', 'OD2', 'ASP', 14.87)], [('CD', 'ARG', 'CB', 'ASP', 13.78), ('CD', 'ARG', 'CG', 'ASP', 15.18), ('CD', 'ARG', 'OD1', 'ASP', 16.12), ('CD', 'ARG', 'OD2', 'ASP', 15.42)], [('NE', 'ARG', 'CB', 'ASP', 13.24), ('NE', 'ARG', 'CG', 'ASP', 14.59), ('NE', 'ARG', 'OD1', 'ASP', 15.61), ('NE', 'ARG', 'OD2', 'ASP', 14.72)], [('CZ', 'ARG', 'CB', 'ASP', 12.35), ('CZ', 'ARG', 'CG', 'ASP', 13.64), ('CZ', 'ARG', 'OD1', 'ASP', 14.68), ('CZ', 'ARG', 'OD2', 'ASP', 13.71)], [('NH1', 'ARG', 'CB', 'ASP', 12.1), ('NH1', 'ARG', 'CG', 'ASP', 13.36), ('NH1', 'ARG', 'OD1', 'ASP', 14.35), ('NH1', 'ARG', 'OD2', 'ASP', 13.46)], [('NH2', 'ARG', 'CB', 'ASP', 11.99), ('NH2', 'ARG', 'CG', 'ASP', 13.21), ('NH2', 'ARG', 'OD1', 'ASP', 14.31), ('NH2', 'ARG', 'OD2', 'ASP', 13.16)]]}
ASP_GLU = { 
	'distances':
		[[16.73, 16.06, 14.57, 14.19, 13.89], [17.12, 16.54, 15.1, 14.74, 14.43], [17.77, 17.28, 15.84, 15.4, 15.25], [16.89, 16.28, 14.88, 14.63, 14.16]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 16.73), ('CB', 'ASP', 'CG', 'GLU', 16.06), ('CB', 'ASP', 'CD', 'GLU', 14.57), ('CB', 'ASP', 'OE1', 'GLU', 14.19), ('CB', 'ASP', 'OE2', 'GLU', 13.89)], [('CG', 'ASP', 'CB', 'GLU', 17.12), ('CG', 'ASP', 'CG', 'GLU', 16.54), ('CG', 'ASP', 'CD', 'GLU', 15.1), ('CG', 'ASP', 'OE1', 'GLU', 14.74), ('CG', 'ASP', 'OE2', 'GLU', 14.43)], [('OD1', 'ASP', 'CB', 'GLU', 17.77), ('OD1', 'ASP', 'CG', 'GLU', 17.28), ('OD1', 'ASP', 'CD', 'GLU', 15.84), ('OD1', 'ASP', 'OE1', 'GLU', 15.4), ('OD1', 'ASP', 'OE2', 'GLU', 15.25)], [('OD2', 'ASP', 'CB', 'GLU', 16.89), ('OD2', 'ASP', 'CG', 'GLU', 16.28), ('OD2', 'ASP', 'CD', 'GLU', 14.88), ('OD2', 'ASP', 'OE1', 'GLU', 14.63), ('OD2', 'ASP', 'OE2', 'GLU', 14.16)]]}
SER_GLU = { 
	'distances':
		[[14.71, 13.48, 12.17, 12.12, 11.35], [14.69, 13.57, 12.18, 11.96, 11.45]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 14.71), ('CB', 'SER', 'CG', 'GLU', 13.48), ('CB', 'SER', 'CD', 'GLU', 12.17), ('CB', 'SER', 'OE1', 'GLU', 12.12), ('CB', 'SER', 'OE2', 'GLU', 11.35)], [('OG', 'SER', 'CB', 'GLU', 14.69), ('OG', 'SER', 'CG', 'GLU', 13.57), ('OG', 'SER', 'CD', 'GLU', 12.18), ('OG', 'SER', 'OE1', 'GLU', 11.96), ('OG', 'SER', 'OE2', 'GLU', 11.45)]]}
SER_ASP = { 
	'distances':
		[[10.14, 11.51, 12.53, 11.66], [9.29, 10.72, 11.66, 11.03]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 10.14), ('CB', 'SER', 'CG', 'ASP', 11.51), ('CB', 'SER', 'OD1', 'ASP', 12.53), ('CB', 'SER', 'OD2', 'ASP', 11.66)], [('OG', 'SER', 'CB', 'ASP', 9.29), ('OG', 'SER', 'CG', 'ASP', 10.72), ('OG', 'SER', 'OD1', 'ASP', 11.66), ('OG', 'SER', 'OD2', 'ASP', 11.03)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'A_1tys_2_1_1_45')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_TYR, d, 'A_1tys_2_1_1_45')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_SER, d, 'A_1tys_2_1_1_45')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_ASP, d, 'A_1tys_2_1_1_45')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_GLU, d, 'A_1tys_2_1_1_45')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_GLU, d, 'A_1tys_2_1_1_45')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ARG_ASP, d, 'A_1tys_2_1_1_45')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_GLU, d, 'A_1tys_2_1_1_45')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_GLU, d, 'A_1tys_2_1_1_45')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_ASP, d, 'A_1tys_2_1_1_45')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'ARG_TYR' :  match2,
		'ARG_SER' :  match3,
		'TYR_ASP' :  match4,
		'ARG_GLU' :  match5,
		'TYR_GLU' :  match6,
		'ARG_ASP' :  match7,
		'ASP_GLU' :  match8,
		'SER_GLU' :  match9,
		'SER_ASP' :  match10}