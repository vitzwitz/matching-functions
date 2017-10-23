'''
FUNC:A_2dln_6_3_2_4
PDB:2dln
EC:6.3.2.4
RESI:glu,ser,tyr,arg,gly
LOCI:a-15,150,216,255,276;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[9.48, 8.15, 8.3, 6.97, 7.38, 5.73, 5.99, 5.3], [9.77, 8.34, 8.2, 7.36, 7.08, 6.01, 5.82, 4.79]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 9.48), ('CB', 'SER', 'CG', 'TYR', 8.15), ('CB', 'SER', 'CD1', 'TYR', 8.3), ('CB', 'SER', 'CD2', 'TYR', 6.97), ('CB', 'SER', 'CE1', 'TYR', 7.38), ('CB', 'SER', 'CE2', 'TYR', 5.73), ('CB', 'SER', 'CZ', 'TYR', 5.99), ('CB', 'SER', 'OH', 'TYR', 5.3)], [('OG', 'SER', 'CB', 'TYR', 9.77), ('OG', 'SER', 'CG', 'TYR', 8.34), ('OG', 'SER', 'CD1', 'TYR', 8.2), ('OG', 'SER', 'CD2', 'TYR', 7.36), ('OG', 'SER', 'CE1', 'TYR', 7.08), ('OG', 'SER', 'CE2', 'TYR', 6.01), ('OG', 'SER', 'CZ', 'TYR', 5.82), ('OG', 'SER', 'OH', 'TYR', 4.79)]]}
GLU_GLY = { 
	'distances':
		[[13.16, 12.25, 10.78, 10.91], [13.55, 12.74, 11.22, 11.16], [12.8, 12.1, 10.56, 10.29], [11.78, 11.11, 9.57, 9.29], [13.28, 12.65, 11.11, 10.7]],
	'comparisons':
		[[('CB', 'GLU', 'O', 'GLY', 13.16), ('CB', 'GLU', 'C', 'GLY', 12.25), ('CB', 'GLU', 'CA', 'GLY', 10.78), ('CB', 'GLU', 'N', 'GLY', 10.91)], [('CG', 'GLU', 'O', 'GLY', 13.55), ('CG', 'GLU', 'C', 'GLY', 12.74), ('CG', 'GLU', 'CA', 'GLY', 11.22), ('CG', 'GLU', 'N', 'GLY', 11.16)], [('CD', 'GLU', 'O', 'GLY', 12.8), ('CD', 'GLU', 'C', 'GLY', 12.1), ('CD', 'GLU', 'CA', 'GLY', 10.56), ('CD', 'GLU', 'N', 'GLY', 10.29)], [('OE1', 'GLU', 'O', 'GLY', 11.78), ('OE1', 'GLU', 'C', 'GLY', 11.11), ('OE1', 'GLU', 'CA', 'GLY', 9.57), ('OE1', 'GLU', 'N', 'GLY', 9.29)], [('OE2', 'GLU', 'O', 'GLY', 13.28), ('OE2', 'GLU', 'C', 'GLY', 12.65), ('OE2', 'GLU', 'CA', 'GLY', 11.11), ('OE2', 'GLU', 'N', 'GLY', 10.7)]]}
GLU_TYR = { 
	'distances':
		[[12.2, 10.92, 10.72, 10.13, 9.72, 9.05, 8.81, 7.99], [12.39, 11.07, 10.95, 10.11, 9.89, 8.93, 8.79, 7.85], [12.91, 11.49, 11.21, 10.6, 10.01, 9.3, 8.95, 7.81], [12.06, 10.6, 10.23, 9.77, 8.98, 8.43, 7.95, 6.73], [14.11, 12.68, 12.36, 11.8, 11.13, 10.49, 10.1, 8.91]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 12.2), ('CB', 'GLU', 'CG', 'TYR', 10.92), ('CB', 'GLU', 'CD1', 'TYR', 10.72), ('CB', 'GLU', 'CD2', 'TYR', 10.13), ('CB', 'GLU', 'CE1', 'TYR', 9.72), ('CB', 'GLU', 'CE2', 'TYR', 9.05), ('CB', 'GLU', 'CZ', 'TYR', 8.81), ('CB', 'GLU', 'OH', 'TYR', 7.99)], [('CG', 'GLU', 'CB', 'TYR', 12.39), ('CG', 'GLU', 'CG', 'TYR', 11.07), ('CG', 'GLU', 'CD1', 'TYR', 10.95), ('CG', 'GLU', 'CD2', 'TYR', 10.11), ('CG', 'GLU', 'CE1', 'TYR', 9.89), ('CG', 'GLU', 'CE2', 'TYR', 8.93), ('CG', 'GLU', 'CZ', 'TYR', 8.79), ('CG', 'GLU', 'OH', 'TYR', 7.85)], [('CD', 'GLU', 'CB', 'TYR', 12.91), ('CD', 'GLU', 'CG', 'TYR', 11.49), ('CD', 'GLU', 'CD1', 'TYR', 11.21), ('CD', 'GLU', 'CD2', 'TYR', 10.6), ('CD', 'GLU', 'CE1', 'TYR', 10.01), ('CD', 'GLU', 'CE2', 'TYR', 9.3), ('CD', 'GLU', 'CZ', 'TYR', 8.95), ('CD', 'GLU', 'OH', 'TYR', 7.81)], [('OE1', 'GLU', 'CB', 'TYR', 12.06), ('OE1', 'GLU', 'CG', 'TYR', 10.6), ('OE1', 'GLU', 'CD1', 'TYR', 10.23), ('OE1', 'GLU', 'CD2', 'TYR', 9.77), ('OE1', 'GLU', 'CE1', 'TYR', 8.98), ('OE1', 'GLU', 'CE2', 'TYR', 8.43), ('OE1', 'GLU', 'CZ', 'TYR', 7.95), ('OE1', 'GLU', 'OH', 'TYR', 6.73)], [('OE2', 'GLU', 'CB', 'TYR', 14.11), ('OE2', 'GLU', 'CG', 'TYR', 12.68), ('OE2', 'GLU', 'CD1', 'TYR', 12.36), ('OE2', 'GLU', 'CD2', 'TYR', 11.8), ('OE2', 'GLU', 'CE1', 'TYR', 11.13), ('OE2', 'GLU', 'CE2', 'TYR', 10.49), ('OE2', 'GLU', 'CZ', 'TYR', 10.1), ('OE2', 'GLU', 'OH', 'TYR', 8.91)]]}
SER_GLY = { 
	'distances':
		[[12.95, 12.27, 10.9, 10.91], [11.88, 11.17, 9.74, 9.73]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 12.95), ('CB', 'SER', 'C', 'GLY', 12.27), ('CB', 'SER', 'CA', 'GLY', 10.9), ('CB', 'SER', 'N', 'GLY', 10.91)], [('OG', 'SER', 'O', 'GLY', 11.88), ('OG', 'SER', 'C', 'GLY', 11.17), ('OG', 'SER', 'CA', 'GLY', 9.74), ('OG', 'SER', 'N', 'GLY', 9.73)]]}
TYR_ARG = { 
	'distances':
		[[17.42, 17.25, 15.87, 15.08, 14.2, 13.94, 13.78], [16.21, 16.12, 14.79, 13.96, 13.0, 12.7, 12.55], [15.13, 15.06, 13.73, 12.99, 12.04, 11.64, 11.71], [16.24, 16.22, 14.96, 14.01, 12.99, 12.74, 12.4], [14.05, 14.09, 12.82, 12.05, 11.01, 10.55, 10.67], [15.26, 15.34, 14.15, 13.16, 12.07, 11.79, 11.43], [14.12, 14.24, 13.05, 12.15, 11.03, 10.64, 10.51], [13.23, 13.47, 12.38, 11.44, 10.25, 9.81, 9.69]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 17.42), ('CB', 'TYR', 'CG', 'ARG', 17.25), ('CB', 'TYR', 'CD', 'ARG', 15.87), ('CB', 'TYR', 'NE', 'ARG', 15.08), ('CB', 'TYR', 'CZ', 'ARG', 14.2), ('CB', 'TYR', 'NH1', 'ARG', 13.94), ('CB', 'TYR', 'NH2', 'ARG', 13.78)], [('CG', 'TYR', 'CB', 'ARG', 16.21), ('CG', 'TYR', 'CG', 'ARG', 16.12), ('CG', 'TYR', 'CD', 'ARG', 14.79), ('CG', 'TYR', 'NE', 'ARG', 13.96), ('CG', 'TYR', 'CZ', 'ARG', 13.0), ('CG', 'TYR', 'NH1', 'ARG', 12.7), ('CG', 'TYR', 'NH2', 'ARG', 12.55)], [('CD1', 'TYR', 'CB', 'ARG', 15.13), ('CD1', 'TYR', 'CG', 'ARG', 15.06), ('CD1', 'TYR', 'CD', 'ARG', 13.73), ('CD1', 'TYR', 'NE', 'ARG', 12.99), ('CD1', 'TYR', 'CZ', 'ARG', 12.04), ('CD1', 'TYR', 'NH1', 'ARG', 11.64), ('CD1', 'TYR', 'NH2', 'ARG', 11.71)], [('CD2', 'TYR', 'CB', 'ARG', 16.24), ('CD2', 'TYR', 'CG', 'ARG', 16.22), ('CD2', 'TYR', 'CD', 'ARG', 14.96), ('CD2', 'TYR', 'NE', 'ARG', 14.01), ('CD2', 'TYR', 'CZ', 'ARG', 12.99), ('CD2', 'TYR', 'NH1', 'ARG', 12.74), ('CD2', 'TYR', 'NH2', 'ARG', 12.4)], [('CE1', 'TYR', 'CB', 'ARG', 14.05), ('CE1', 'TYR', 'CG', 'ARG', 14.09), ('CE1', 'TYR', 'CD', 'ARG', 12.82), ('CE1', 'TYR', 'NE', 'ARG', 12.05), ('CE1', 'TYR', 'CZ', 'ARG', 11.01), ('CE1', 'TYR', 'NH1', 'ARG', 10.55), ('CE1', 'TYR', 'NH2', 'ARG', 10.67)], [('CE2', 'TYR', 'CB', 'ARG', 15.26), ('CE2', 'TYR', 'CG', 'ARG', 15.34), ('CE2', 'TYR', 'CD', 'ARG', 14.15), ('CE2', 'TYR', 'NE', 'ARG', 13.16), ('CE2', 'TYR', 'CZ', 'ARG', 12.07), ('CE2', 'TYR', 'NH1', 'ARG', 11.79), ('CE2', 'TYR', 'NH2', 'ARG', 11.43)], [('CZ', 'TYR', 'CB', 'ARG', 14.12), ('CZ', 'TYR', 'CG', 'ARG', 14.24), ('CZ', 'TYR', 'CD', 'ARG', 13.05), ('CZ', 'TYR', 'NE', 'ARG', 12.15), ('CZ', 'TYR', 'CZ', 'ARG', 11.03), ('CZ', 'TYR', 'NH1', 'ARG', 10.64), ('CZ', 'TYR', 'NH2', 'ARG', 10.51)], [('OH', 'TYR', 'CB', 'ARG', 13.23), ('OH', 'TYR', 'CG', 'ARG', 13.47), ('OH', 'TYR', 'CD', 'ARG', 12.38), ('OH', 'TYR', 'NE', 'ARG', 11.44), ('OH', 'TYR', 'CZ', 'ARG', 10.25), ('OH', 'TYR', 'NH1', 'ARG', 9.81), ('OH', 'TYR', 'NH2', 'ARG', 9.69)]]}
TYR_GLY = { 
	'distances':
		[[13.0, 12.23, 11.7, 12.6], [11.98, 11.2, 10.52, 11.33], [10.61, 9.83, 9.21, 10.08], [12.53, 11.75, 10.89, 11.55], [9.79, 9.0, 8.2, 8.94], [11.89, 11.12, 10.11, 10.63], [10.52, 9.75, 8.73, 9.27], [10.08, 9.36, 8.16, 8.48]],
	'comparisons':
		[[('CB', 'TYR', 'O', 'GLY', 13.0), ('CB', 'TYR', 'C', 'GLY', 12.23), ('CB', 'TYR', 'CA', 'GLY', 11.7), ('CB', 'TYR', 'N', 'GLY', 12.6)], [('CG', 'TYR', 'O', 'GLY', 11.98), ('CG', 'TYR', 'C', 'GLY', 11.2), ('CG', 'TYR', 'CA', 'GLY', 10.52), ('CG', 'TYR', 'N', 'GLY', 11.33)], [('CD1', 'TYR', 'O', 'GLY', 10.61), ('CD1', 'TYR', 'C', 'GLY', 9.83), ('CD1', 'TYR', 'CA', 'GLY', 9.21), ('CD1', 'TYR', 'N', 'GLY', 10.08)], [('CD2', 'TYR', 'O', 'GLY', 12.53), ('CD2', 'TYR', 'C', 'GLY', 11.75), ('CD2', 'TYR', 'CA', 'GLY', 10.89), ('CD2', 'TYR', 'N', 'GLY', 11.55)], [('CE1', 'TYR', 'O', 'GLY', 9.79), ('CE1', 'TYR', 'C', 'GLY', 9.0), ('CE1', 'TYR', 'CA', 'GLY', 8.2), ('CE1', 'TYR', 'N', 'GLY', 8.94)], [('CE2', 'TYR', 'O', 'GLY', 11.89), ('CE2', 'TYR', 'C', 'GLY', 11.12), ('CE2', 'TYR', 'CA', 'GLY', 10.11), ('CE2', 'TYR', 'N', 'GLY', 10.63)], [('CZ', 'TYR', 'O', 'GLY', 10.52), ('CZ', 'TYR', 'C', 'GLY', 9.75), ('CZ', 'TYR', 'CA', 'GLY', 8.73), ('CZ', 'TYR', 'N', 'GLY', 9.27)], [('OH', 'TYR', 'O', 'GLY', 10.08), ('OH', 'TYR', 'C', 'GLY', 9.36), ('OH', 'TYR', 'CA', 'GLY', 8.16), ('OH', 'TYR', 'N', 'GLY', 8.48)]]}
GLU_ARG = { 
	'distances':
		[[16.11, 16.92, 16.24, 15.43, 14.11, 13.39, 13.6], [15.72, 16.5, 15.87, 14.95, 13.63, 13.04, 12.98], [14.42, 15.26, 14.73, 13.82, 12.51, 11.92, 11.88], [13.46, 14.23, 13.62, 12.7, 11.38, 10.8, 10.77], [14.42, 15.36, 14.96, 14.09, 12.79, 12.2, 12.19]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 16.11), ('CB', 'GLU', 'CG', 'ARG', 16.92), ('CB', 'GLU', 'CD', 'ARG', 16.24), ('CB', 'GLU', 'NE', 'ARG', 15.43), ('CB', 'GLU', 'CZ', 'ARG', 14.11), ('CB', 'GLU', 'NH1', 'ARG', 13.39), ('CB', 'GLU', 'NH2', 'ARG', 13.6)], [('CG', 'GLU', 'CB', 'ARG', 15.72), ('CG', 'GLU', 'CG', 'ARG', 16.5), ('CG', 'GLU', 'CD', 'ARG', 15.87), ('CG', 'GLU', 'NE', 'ARG', 14.95), ('CG', 'GLU', 'CZ', 'ARG', 13.63), ('CG', 'GLU', 'NH1', 'ARG', 13.04), ('CG', 'GLU', 'NH2', 'ARG', 12.98)], [('CD', 'GLU', 'CB', 'ARG', 14.42), ('CD', 'GLU', 'CG', 'ARG', 15.26), ('CD', 'GLU', 'CD', 'ARG', 14.73), ('CD', 'GLU', 'NE', 'ARG', 13.82), ('CD', 'GLU', 'CZ', 'ARG', 12.51), ('CD', 'GLU', 'NH1', 'ARG', 11.92), ('CD', 'GLU', 'NH2', 'ARG', 11.88)], [('OE1', 'GLU', 'CB', 'ARG', 13.46), ('OE1', 'GLU', 'CG', 'ARG', 14.23), ('OE1', 'GLU', 'CD', 'ARG', 13.62), ('OE1', 'GLU', 'NE', 'ARG', 12.7), ('OE1', 'GLU', 'CZ', 'ARG', 11.38), ('OE1', 'GLU', 'NH1', 'ARG', 10.8), ('OE1', 'GLU', 'NH2', 'ARG', 10.77)], [('OE2', 'GLU', 'CB', 'ARG', 14.42), ('OE2', 'GLU', 'CG', 'ARG', 15.36), ('OE2', 'GLU', 'CD', 'ARG', 14.96), ('OE2', 'GLU', 'NE', 'ARG', 14.09), ('OE2', 'GLU', 'CZ', 'ARG', 12.79), ('OE2', 'GLU', 'NH1', 'ARG', 12.2), ('OE2', 'GLU', 'NH2', 'ARG', 12.19)]]}
GLY_ARG = { 
	'distances':
		[[9.41, 9.73, 8.79, 9.14, 8.56, 7.39, 9.43], [10.35, 10.72, 9.76, 9.93, 9.21, 8.03, 9.91], [10.28, 10.79, 9.86, 9.79, 8.86, 7.66, 9.36], [8.98, 9.62, 8.83, 8.76, 7.79, 6.52, 8.34]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ARG', 9.41), ('O', 'GLY', 'CG', 'ARG', 9.73), ('O', 'GLY', 'CD', 'ARG', 8.79), ('O', 'GLY', 'NE', 'ARG', 9.14), ('O', 'GLY', 'CZ', 'ARG', 8.56), ('O', 'GLY', 'NH1', 'ARG', 7.39), ('O', 'GLY', 'NH2', 'ARG', 9.43)], [('C', 'GLY', 'CB', 'ARG', 10.35), ('C', 'GLY', 'CG', 'ARG', 10.72), ('C', 'GLY', 'CD', 'ARG', 9.76), ('C', 'GLY', 'NE', 'ARG', 9.93), ('C', 'GLY', 'CZ', 'ARG', 9.21), ('C', 'GLY', 'NH1', 'ARG', 8.03), ('C', 'GLY', 'NH2', 'ARG', 9.91)], [('CA', 'GLY', 'CB', 'ARG', 10.28), ('CA', 'GLY', 'CG', 'ARG', 10.79), ('CA', 'GLY', 'CD', 'ARG', 9.86), ('CA', 'GLY', 'NE', 'ARG', 9.79), ('CA', 'GLY', 'CZ', 'ARG', 8.86), ('CA', 'GLY', 'NH1', 'ARG', 7.66), ('CA', 'GLY', 'NH2', 'ARG', 9.36)], [('N', 'GLY', 'CB', 'ARG', 8.98), ('N', 'GLY', 'CG', 'ARG', 9.62), ('N', 'GLY', 'CD', 'ARG', 8.83), ('N', 'GLY', 'NE', 'ARG', 8.76), ('N', 'GLY', 'CZ', 'ARG', 7.79), ('N', 'GLY', 'NH1', 'ARG', 6.52), ('N', 'GLY', 'NH2', 'ARG', 8.34)]]}
SER_ARG = { 
	'distances':
		[[14.78, 15.15, 14.26, 13.12, 11.88, 11.65, 11.0], [14.0, 14.48, 13.63, 12.58, 11.3, 10.9, 10.55]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 14.78), ('CB', 'SER', 'CG', 'ARG', 15.15), ('CB', 'SER', 'CD', 'ARG', 14.26), ('CB', 'SER', 'NE', 'ARG', 13.12), ('CB', 'SER', 'CZ', 'ARG', 11.88), ('CB', 'SER', 'NH1', 'ARG', 11.65), ('CB', 'SER', 'NH2', 'ARG', 11.0)], [('OG', 'SER', 'CB', 'ARG', 14.0), ('OG', 'SER', 'CG', 'ARG', 14.48), ('OG', 'SER', 'CD', 'ARG', 13.63), ('OG', 'SER', 'NE', 'ARG', 12.58), ('OG', 'SER', 'CZ', 'ARG', 11.3), ('OG', 'SER', 'NH1', 'ARG', 10.9), ('OG', 'SER', 'NH2', 'ARG', 10.55)]]}
GLU_SER = { 
	'distances':
		[[7.04, 6.11], [6.19, 5.43], [6.41, 5.44], [5.75, 4.58], [7.48, 6.57]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 7.04), ('CB', 'GLU', 'OG', 'SER', 6.11)], [('CG', 'GLU', 'CB', 'SER', 6.19), ('CG', 'GLU', 'OG', 'SER', 5.43)], [('CD', 'GLU', 'CB', 'SER', 6.41), ('CD', 'GLU', 'OG', 'SER', 5.44)], [('OE1', 'GLU', 'CB', 'SER', 5.75), ('OE1', 'GLU', 'OG', 'SER', 4.58)], [('OE2', 'GLU', 'CB', 'SER', 7.48), ('OE2', 'GLU', 'OG', 'SER', 6.57)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'A_2dln_6_3_2_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLY, d, 'A_2dln_6_3_2_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_TYR, d, 'A_2dln_6_3_2_4')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_GLY, d, 'A_2dln_6_3_2_4')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_ARG, d, 'A_2dln_6_3_2_4')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_GLY, d, 'A_2dln_6_3_2_4')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLU_ARG, d, 'A_2dln_6_3_2_4')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLY_ARG, d, 'A_2dln_6_3_2_4')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_ARG, d, 'A_2dln_6_3_2_4')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(GLU_SER, d, 'A_2dln_6_3_2_4')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'GLU_GLY' :  match2,
		'GLU_TYR' :  match3,
		'SER_GLY' :  match4,
		'TYR_ARG' :  match5,
		'TYR_GLY' :  match6,
		'GLU_ARG' :  match7,
		'GLY_ARG' :  match8,
		'SER_ARG' :  match9,
		'GLU_SER' :  match10}