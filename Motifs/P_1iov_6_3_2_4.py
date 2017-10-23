'''
FUNC:P_1iov_6_3_2_4
PDB:1iov
EC:6.3.2.4
RESI:glu,ser,tyr,arg,gly
LOCI:a-15,150,216,255,276;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[7.9, 6.58, 6.76, 5.39, 5.85, 4.16, 4.47, 3.78], [8.17, 6.77, 6.73, 5.74, 5.66, 4.42, 4.37, 3.43]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 7.9), ('CB', 'SER', 'CG', 'TYR', 6.58), ('CB', 'SER', 'CD1', 'TYR', 6.76), ('CB', 'SER', 'CD2', 'TYR', 5.39), ('CB', 'SER', 'CE1', 'TYR', 5.85), ('CB', 'SER', 'CE2', 'TYR', 4.16), ('CB', 'SER', 'CZ', 'TYR', 4.47), ('CB', 'SER', 'OH', 'TYR', 3.78)], [('OG', 'SER', 'CB', 'TYR', 8.17), ('OG', 'SER', 'CG', 'TYR', 6.77), ('OG', 'SER', 'CD1', 'TYR', 6.73), ('OG', 'SER', 'CD2', 'TYR', 5.74), ('OG', 'SER', 'CE1', 'TYR', 5.66), ('OG', 'SER', 'CE2', 'TYR', 4.42), ('OG', 'SER', 'CZ', 'TYR', 4.37), ('OG', 'SER', 'OH', 'TYR', 3.43)]]}
GLU_GLY = { 
	'distances':
		[[11.67, 10.7, 9.27, 9.42], [11.66, 10.78, 9.29, 9.29], [10.96, 10.2, 8.67, 8.45], [9.81, 9.07, 7.53, 7.32], [11.55, 10.87, 9.34, 8.94]],
	'comparisons':
		[[('CB', 'GLU', 'O', 'GLY', 11.67), ('CB', 'GLU', 'C', 'GLY', 10.7), ('CB', 'GLU', 'CA', 'GLY', 9.27), ('CB', 'GLU', 'N', 'GLY', 9.42)], [('CG', 'GLU', 'O', 'GLY', 11.66), ('CG', 'GLU', 'C', 'GLY', 10.78), ('CG', 'GLU', 'CA', 'GLY', 9.29), ('CG', 'GLU', 'N', 'GLY', 9.29)], [('CD', 'GLU', 'O', 'GLY', 10.96), ('CD', 'GLU', 'C', 'GLY', 10.2), ('CD', 'GLU', 'CA', 'GLY', 8.67), ('CD', 'GLU', 'N', 'GLY', 8.45)], [('OE1', 'GLU', 'O', 'GLY', 9.81), ('OE1', 'GLU', 'C', 'GLY', 9.07), ('OE1', 'GLU', 'CA', 'GLY', 7.53), ('OE1', 'GLU', 'N', 'GLY', 7.32)], [('OE2', 'GLU', 'O', 'GLY', 11.55), ('OE2', 'GLU', 'C', 'GLY', 10.87), ('OE2', 'GLU', 'CA', 'GLY', 9.34), ('OE2', 'GLU', 'N', 'GLY', 8.94)]]}
ARG_GLY = { 
	'distances':
		[[7.9, 8.79, 8.65, 7.38], [8.06, 9.04, 9.05, 7.94], [7.33, 8.25, 8.27, 7.32], [7.68, 8.43, 8.2, 7.24], [7.15, 7.75, 7.3, 6.31], [6.01, 6.58, 6.1, 5.03], [8.09, 8.53, 7.88, 6.96]],
	'comparisons':
		[[('CB', 'ARG', 'O', 'GLY', 7.9), ('CB', 'ARG', 'C', 'GLY', 8.79), ('CB', 'ARG', 'CA', 'GLY', 8.65), ('CB', 'ARG', 'N', 'GLY', 7.38)], [('CG', 'ARG', 'O', 'GLY', 8.06), ('CG', 'ARG', 'C', 'GLY', 9.04), ('CG', 'ARG', 'CA', 'GLY', 9.05), ('CG', 'ARG', 'N', 'GLY', 7.94)], [('CD', 'ARG', 'O', 'GLY', 7.33), ('CD', 'ARG', 'C', 'GLY', 8.25), ('CD', 'ARG', 'CA', 'GLY', 8.27), ('CD', 'ARG', 'N', 'GLY', 7.32)], [('NE', 'ARG', 'O', 'GLY', 7.68), ('NE', 'ARG', 'C', 'GLY', 8.43), ('NE', 'ARG', 'CA', 'GLY', 8.2), ('NE', 'ARG', 'N', 'GLY', 7.24)], [('CZ', 'ARG', 'O', 'GLY', 7.15), ('CZ', 'ARG', 'C', 'GLY', 7.75), ('CZ', 'ARG', 'CA', 'GLY', 7.3), ('CZ', 'ARG', 'N', 'GLY', 6.31)], [('NH1', 'ARG', 'O', 'GLY', 6.01), ('NH1', 'ARG', 'C', 'GLY', 6.58), ('NH1', 'ARG', 'CA', 'GLY', 6.1), ('NH1', 'ARG', 'N', 'GLY', 5.03)], [('NH2', 'ARG', 'O', 'GLY', 8.09), ('NH2', 'ARG', 'C', 'GLY', 8.53), ('NH2', 'ARG', 'CA', 'GLY', 7.88), ('NH2', 'ARG', 'N', 'GLY', 6.96)]]}
GLU_TYR = { 
	'distances':
		[[10.75, 9.55, 9.56, 8.62, 8.66, 7.61, 7.63, 6.91], [10.51, 9.24, 9.28, 8.2, 8.3, 7.06, 7.13, 6.28], [11.03, 9.65, 9.51, 8.66, 8.38, 7.39, 7.23, 6.15], [10.26, 8.83, 8.56, 7.94, 7.35, 6.62, 6.27, 5.09], [12.2, 10.81, 10.65, 9.81, 9.48, 8.51, 8.33, 7.18]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 10.75), ('CB', 'GLU', 'CG', 'TYR', 9.55), ('CB', 'GLU', 'CD1', 'TYR', 9.56), ('CB', 'GLU', 'CD2', 'TYR', 8.62), ('CB', 'GLU', 'CE1', 'TYR', 8.66), ('CB', 'GLU', 'CE2', 'TYR', 7.61), ('CB', 'GLU', 'CZ', 'TYR', 7.63), ('CB', 'GLU', 'OH', 'TYR', 6.91)], [('CG', 'GLU', 'CB', 'TYR', 10.51), ('CG', 'GLU', 'CG', 'TYR', 9.24), ('CG', 'GLU', 'CD1', 'TYR', 9.28), ('CG', 'GLU', 'CD2', 'TYR', 8.2), ('CG', 'GLU', 'CE1', 'TYR', 8.3), ('CG', 'GLU', 'CE2', 'TYR', 7.06), ('CG', 'GLU', 'CZ', 'TYR', 7.13), ('CG', 'GLU', 'OH', 'TYR', 6.28)], [('CD', 'GLU', 'CB', 'TYR', 11.03), ('CD', 'GLU', 'CG', 'TYR', 9.65), ('CD', 'GLU', 'CD1', 'TYR', 9.51), ('CD', 'GLU', 'CD2', 'TYR', 8.66), ('CD', 'GLU', 'CE1', 'TYR', 8.38), ('CD', 'GLU', 'CE2', 'TYR', 7.39), ('CD', 'GLU', 'CZ', 'TYR', 7.23), ('CD', 'GLU', 'OH', 'TYR', 6.15)], [('OE1', 'GLU', 'CB', 'TYR', 10.26), ('OE1', 'GLU', 'CG', 'TYR', 8.83), ('OE1', 'GLU', 'CD1', 'TYR', 8.56), ('OE1', 'GLU', 'CD2', 'TYR', 7.94), ('OE1', 'GLU', 'CE1', 'TYR', 7.35), ('OE1', 'GLU', 'CE2', 'TYR', 6.62), ('OE1', 'GLU', 'CZ', 'TYR', 6.27), ('OE1', 'GLU', 'OH', 'TYR', 5.09)], [('OE2', 'GLU', 'CB', 'TYR', 12.2), ('OE2', 'GLU', 'CG', 'TYR', 10.81), ('OE2', 'GLU', 'CD1', 'TYR', 10.65), ('OE2', 'GLU', 'CD2', 'TYR', 9.81), ('OE2', 'GLU', 'CE1', 'TYR', 9.48), ('OE2', 'GLU', 'CE2', 'TYR', 8.51), ('OE2', 'GLU', 'CZ', 'TYR', 8.33), ('OE2', 'GLU', 'OH', 'TYR', 7.18)]]}
SER_GLY = { 
	'distances':
		[[11.09, 10.37, 8.95, 9.03], [10.14, 9.36, 7.9, 7.98]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 11.09), ('CB', 'SER', 'C', 'GLY', 10.37), ('CB', 'SER', 'CA', 'GLY', 8.95), ('CB', 'SER', 'N', 'GLY', 9.03)], [('OG', 'SER', 'O', 'GLY', 10.14), ('OG', 'SER', 'C', 'GLY', 9.36), ('OG', 'SER', 'CA', 'GLY', 7.9), ('OG', 'SER', 'N', 'GLY', 7.98)]]}
TYR_ARG = { 
	'distances':
		[[15.93, 15.78, 14.45, 13.68, 12.79, 12.46, 12.4], [14.63, 14.56, 13.28, 12.47, 11.51, 11.14, 11.12], [13.51, 13.43, 12.14, 11.42, 10.49, 10.05, 10.22], [14.64, 14.68, 13.45, 12.54, 11.5, 11.15, 10.98], [12.34, 12.35, 11.12, 10.37, 9.36, 8.87, 9.09], [13.58, 13.71, 12.55, 11.61, 10.49, 10.1, 9.95], [12.38, 12.51, 11.35, 10.48, 9.37, 8.9, 8.94], [11.38, 11.64, 10.57, 9.67, 8.48, 7.95, 8.04]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 15.93), ('CB', 'TYR', 'CG', 'ARG', 15.78), ('CB', 'TYR', 'CD', 'ARG', 14.45), ('CB', 'TYR', 'NE', 'ARG', 13.68), ('CB', 'TYR', 'CZ', 'ARG', 12.79), ('CB', 'TYR', 'NH1', 'ARG', 12.46), ('CB', 'TYR', 'NH2', 'ARG', 12.4)], [('CG', 'TYR', 'CB', 'ARG', 14.63), ('CG', 'TYR', 'CG', 'ARG', 14.56), ('CG', 'TYR', 'CD', 'ARG', 13.28), ('CG', 'TYR', 'NE', 'ARG', 12.47), ('CG', 'TYR', 'CZ', 'ARG', 11.51), ('CG', 'TYR', 'NH1', 'ARG', 11.14), ('CG', 'TYR', 'NH2', 'ARG', 11.12)], [('CD1', 'TYR', 'CB', 'ARG', 13.51), ('CD1', 'TYR', 'CG', 'ARG', 13.43), ('CD1', 'TYR', 'CD', 'ARG', 12.14), ('CD1', 'TYR', 'NE', 'ARG', 11.42), ('CD1', 'TYR', 'CZ', 'ARG', 10.49), ('CD1', 'TYR', 'NH1', 'ARG', 10.05), ('CD1', 'TYR', 'NH2', 'ARG', 10.22)], [('CD2', 'TYR', 'CB', 'ARG', 14.64), ('CD2', 'TYR', 'CG', 'ARG', 14.68), ('CD2', 'TYR', 'CD', 'ARG', 13.45), ('CD2', 'TYR', 'NE', 'ARG', 12.54), ('CD2', 'TYR', 'CZ', 'ARG', 11.5), ('CD2', 'TYR', 'NH1', 'ARG', 11.15), ('CD2', 'TYR', 'NH2', 'ARG', 10.98)], [('CE1', 'TYR', 'CB', 'ARG', 12.34), ('CE1', 'TYR', 'CG', 'ARG', 12.35), ('CE1', 'TYR', 'CD', 'ARG', 11.12), ('CE1', 'TYR', 'NE', 'ARG', 10.37), ('CE1', 'TYR', 'CZ', 'ARG', 9.36), ('CE1', 'TYR', 'NH1', 'ARG', 8.87), ('CE1', 'TYR', 'NH2', 'ARG', 9.09)], [('CE2', 'TYR', 'CB', 'ARG', 13.58), ('CE2', 'TYR', 'CG', 'ARG', 13.71), ('CE2', 'TYR', 'CD', 'ARG', 12.55), ('CE2', 'TYR', 'NE', 'ARG', 11.61), ('CE2', 'TYR', 'CZ', 'ARG', 10.49), ('CE2', 'TYR', 'NH1', 'ARG', 10.1), ('CE2', 'TYR', 'NH2', 'ARG', 9.95)], [('CZ', 'TYR', 'CB', 'ARG', 12.38), ('CZ', 'TYR', 'CG', 'ARG', 12.51), ('CZ', 'TYR', 'CD', 'ARG', 11.35), ('CZ', 'TYR', 'NE', 'ARG', 10.48), ('CZ', 'TYR', 'CZ', 'ARG', 9.37), ('CZ', 'TYR', 'NH1', 'ARG', 8.9), ('CZ', 'TYR', 'NH2', 'ARG', 8.94)], [('OH', 'TYR', 'CB', 'ARG', 11.38), ('OH', 'TYR', 'CG', 'ARG', 11.64), ('OH', 'TYR', 'CD', 'ARG', 10.57), ('OH', 'TYR', 'NE', 'ARG', 9.67), ('OH', 'TYR', 'CZ', 'ARG', 8.48), ('OH', 'TYR', 'NH1', 'ARG', 7.95), ('OH', 'TYR', 'NH2', 'ARG', 8.04)]]}
TYR_GLY = { 
	'distances':
		[[11.56, 10.75, 10.16, 11.14], [10.46, 9.65, 8.92, 9.82], [9.11, 8.33, 7.69, 8.63], [10.94, 10.11, 9.18, 9.94], [8.21, 7.43, 6.61, 7.43], [10.2, 9.38, 8.31, 8.93], [8.83, 8.05, 6.99, 7.62], [8.31, 7.57, 6.34, 6.74]],
	'comparisons':
		[[('CB', 'TYR', 'O', 'GLY', 11.56), ('CB', 'TYR', 'C', 'GLY', 10.75), ('CB', 'TYR', 'CA', 'GLY', 10.16), ('CB', 'TYR', 'N', 'GLY', 11.14)], [('CG', 'TYR', 'O', 'GLY', 10.46), ('CG', 'TYR', 'C', 'GLY', 9.65), ('CG', 'TYR', 'CA', 'GLY', 8.92), ('CG', 'TYR', 'N', 'GLY', 9.82)], [('CD1', 'TYR', 'O', 'GLY', 9.11), ('CD1', 'TYR', 'C', 'GLY', 8.33), ('CD1', 'TYR', 'CA', 'GLY', 7.69), ('CD1', 'TYR', 'N', 'GLY', 8.63)], [('CD2', 'TYR', 'O', 'GLY', 10.94), ('CD2', 'TYR', 'C', 'GLY', 10.11), ('CD2', 'TYR', 'CA', 'GLY', 9.18), ('CD2', 'TYR', 'N', 'GLY', 9.94)], [('CE1', 'TYR', 'O', 'GLY', 8.21), ('CE1', 'TYR', 'C', 'GLY', 7.43), ('CE1', 'TYR', 'CA', 'GLY', 6.61), ('CE1', 'TYR', 'N', 'GLY', 7.43)], [('CE2', 'TYR', 'O', 'GLY', 10.2), ('CE2', 'TYR', 'C', 'GLY', 9.38), ('CE2', 'TYR', 'CA', 'GLY', 8.31), ('CE2', 'TYR', 'N', 'GLY', 8.93)], [('CZ', 'TYR', 'O', 'GLY', 8.83), ('CZ', 'TYR', 'C', 'GLY', 8.05), ('CZ', 'TYR', 'CA', 'GLY', 6.99), ('CZ', 'TYR', 'N', 'GLY', 7.62)], [('OH', 'TYR', 'O', 'GLY', 8.31), ('OH', 'TYR', 'C', 'GLY', 7.57), ('OH', 'TYR', 'CA', 'GLY', 6.34), ('OH', 'TYR', 'N', 'GLY', 6.74)]]}
GLU_ARG = { 
	'distances':
		[[14.59, 15.44, 14.85, 14.06, 12.73, 11.91, 12.37], [13.91, 14.73, 14.13, 13.23, 11.9, 11.2, 11.4], [12.62, 13.49, 12.98, 12.08, 10.75, 10.06, 10.26], [11.64, 12.45, 11.87, 10.99, 9.66, 8.94, 9.22], [12.56, 13.53, 13.14, 12.24, 10.93, 10.27, 10.42]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 14.59), ('CB', 'GLU', 'CG', 'ARG', 15.44), ('CB', 'GLU', 'CD', 'ARG', 14.85), ('CB', 'GLU', 'NE', 'ARG', 14.06), ('CB', 'GLU', 'CZ', 'ARG', 12.73), ('CB', 'GLU', 'NH1', 'ARG', 11.91), ('CB', 'GLU', 'NH2', 'ARG', 12.37)], [('CG', 'GLU', 'CB', 'ARG', 13.91), ('CG', 'GLU', 'CG', 'ARG', 14.73), ('CG', 'GLU', 'CD', 'ARG', 14.13), ('CG', 'GLU', 'NE', 'ARG', 13.23), ('CG', 'GLU', 'CZ', 'ARG', 11.9), ('CG', 'GLU', 'NH1', 'ARG', 11.2), ('CG', 'GLU', 'NH2', 'ARG', 11.4)], [('CD', 'GLU', 'CB', 'ARG', 12.62), ('CD', 'GLU', 'CG', 'ARG', 13.49), ('CD', 'GLU', 'CD', 'ARG', 12.98), ('CD', 'GLU', 'NE', 'ARG', 12.08), ('CD', 'GLU', 'CZ', 'ARG', 10.75), ('CD', 'GLU', 'NH1', 'ARG', 10.06), ('CD', 'GLU', 'NH2', 'ARG', 10.26)], [('OE1', 'GLU', 'CB', 'ARG', 11.64), ('OE1', 'GLU', 'CG', 'ARG', 12.45), ('OE1', 'GLU', 'CD', 'ARG', 11.87), ('OE1', 'GLU', 'NE', 'ARG', 10.99), ('OE1', 'GLU', 'CZ', 'ARG', 9.66), ('OE1', 'GLU', 'NH1', 'ARG', 8.94), ('OE1', 'GLU', 'NH2', 'ARG', 9.22)], [('OE2', 'GLU', 'CB', 'ARG', 12.56), ('OE2', 'GLU', 'CG', 'ARG', 13.53), ('OE2', 'GLU', 'CD', 'ARG', 13.14), ('OE2', 'GLU', 'NE', 'ARG', 12.24), ('OE2', 'GLU', 'CZ', 'ARG', 10.93), ('OE2', 'GLU', 'NH1', 'ARG', 10.27), ('OE2', 'GLU', 'NH2', 'ARG', 10.42)]]}
SER_ARG = { 
	'distances':
		[[12.9, 13.36, 12.48, 11.37, 10.1, 9.74, 9.34], [12.35, 12.91, 12.08, 11.08, 9.78, 9.24, 9.17]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 12.9), ('CB', 'SER', 'CG', 'ARG', 13.36), ('CB', 'SER', 'CD', 'ARG', 12.48), ('CB', 'SER', 'NE', 'ARG', 11.37), ('CB', 'SER', 'CZ', 'ARG', 10.1), ('CB', 'SER', 'NH1', 'ARG', 9.74), ('CB', 'SER', 'NH2', 'ARG', 9.34)], [('OG', 'SER', 'CB', 'ARG', 12.35), ('OG', 'SER', 'CG', 'ARG', 12.91), ('OG', 'SER', 'CD', 'ARG', 12.08), ('OG', 'SER', 'NE', 'ARG', 11.08), ('OG', 'SER', 'CZ', 'ARG', 9.78), ('OG', 'SER', 'NH1', 'ARG', 9.24), ('OG', 'SER', 'NH2', 'ARG', 9.17)]]}
GLU_SER = { 
	'distances':
		[[5.63, 4.63], [4.46, 3.6], [4.51, 3.56], [4.06, 2.89], [5.41, 4.61]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 5.63), ('CB', 'GLU', 'OG', 'SER', 4.63)], [('CG', 'GLU', 'CB', 'SER', 4.46), ('CG', 'GLU', 'OG', 'SER', 3.6)], [('CD', 'GLU', 'CB', 'SER', 4.51), ('CD', 'GLU', 'OG', 'SER', 3.56)], [('OE1', 'GLU', 'CB', 'SER', 4.06), ('OE1', 'GLU', 'OG', 'SER', 2.89)], [('OE2', 'GLU', 'CB', 'SER', 5.41), ('OE2', 'GLU', 'OG', 'SER', 4.61)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'P_1iov_6_3_2_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLY, d, 'P_1iov_6_3_2_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_GLY, d, 'P_1iov_6_3_2_4')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_TYR, d, 'P_1iov_6_3_2_4')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_GLY, d, 'P_1iov_6_3_2_4')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_ARG, d, 'P_1iov_6_3_2_4')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(TYR_GLY, d, 'P_1iov_6_3_2_4')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLU_ARG, d, 'P_1iov_6_3_2_4')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_ARG, d, 'P_1iov_6_3_2_4')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(GLU_SER, d, 'P_1iov_6_3_2_4')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'GLU_GLY' :  match2,
		'ARG_GLY' :  match3,
		'GLU_TYR' :  match4,
		'SER_GLY' :  match5,
		'TYR_ARG' :  match6,
		'TYR_GLY' :  match7,
		'GLU_ARG' :  match8,
		'SER_ARG' :  match9,
		'GLU_SER' :  match10}