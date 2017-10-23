'''
FUNC:M_1vzx_2_4_1_87
PDB:1vzx
EC:2.4.1.87
RESI:tyr,glu,arg,mn
LOCI:a-314,317,365,1371;
'''
import motifFunctions as cmd
GLU_TYR = { 
	'distances':
		[[6.23, 7.42, 8.41, 7.9, 9.62, 9.2, 9.96, 11.26], [6.89, 7.78, 8.67, 8.17, 9.74, 9.31, 10.02, 11.23], [6.95, 7.55, 8.54, 7.6, 9.43, 8.61, 9.45, 10.57], [6.24, 6.57, 7.52, 6.52, 8.3, 7.44, 8.26, 9.35], [8.03, 8.6, 9.65, 8.47, 10.47, 9.42, 10.36, 11.42]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 6.23), ('CB', 'GLU', 'CG', 'TYR', 7.42), ('CB', 'GLU', 'CD1', 'TYR', 8.41), ('CB', 'GLU', 'CD2', 'TYR', 7.9), ('CB', 'GLU', 'CE1', 'TYR', 9.62), ('CB', 'GLU', 'CE2', 'TYR', 9.2), ('CB', 'GLU', 'CZ', 'TYR', 9.96), ('CB', 'GLU', 'OH', 'TYR', 11.26)], [('CG', 'GLU', 'CB', 'TYR', 6.89), ('CG', 'GLU', 'CG', 'TYR', 7.78), ('CG', 'GLU', 'CD1', 'TYR', 8.67), ('CG', 'GLU', 'CD2', 'TYR', 8.17), ('CG', 'GLU', 'CE1', 'TYR', 9.74), ('CG', 'GLU', 'CE2', 'TYR', 9.31), ('CG', 'GLU', 'CZ', 'TYR', 10.02), ('CG', 'GLU', 'OH', 'TYR', 11.23)], [('CD', 'GLU', 'CB', 'TYR', 6.95), ('CD', 'GLU', 'CG', 'TYR', 7.55), ('CD', 'GLU', 'CD1', 'TYR', 8.54), ('CD', 'GLU', 'CD2', 'TYR', 7.6), ('CD', 'GLU', 'CE1', 'TYR', 9.43), ('CD', 'GLU', 'CE2', 'TYR', 8.61), ('CD', 'GLU', 'CZ', 'TYR', 9.45), ('CD', 'GLU', 'OH', 'TYR', 10.57)], [('OE1', 'GLU', 'CB', 'TYR', 6.24), ('OE1', 'GLU', 'CG', 'TYR', 6.57), ('OE1', 'GLU', 'CD1', 'TYR', 7.52), ('OE1', 'GLU', 'CD2', 'TYR', 6.52), ('OE1', 'GLU', 'CE1', 'TYR', 8.3), ('OE1', 'GLU', 'CE2', 'TYR', 7.44), ('OE1', 'GLU', 'CZ', 'TYR', 8.26), ('OE1', 'GLU', 'OH', 'TYR', 9.35)], [('OE2', 'GLU', 'CB', 'TYR', 8.03), ('OE2', 'GLU', 'CG', 'TYR', 8.6), ('OE2', 'GLU', 'CD1', 'TYR', 9.65), ('OE2', 'GLU', 'CD2', 'TYR', 8.47), ('OE2', 'GLU', 'CE1', 'TYR', 10.47), ('OE2', 'GLU', 'CE2', 'TYR', 9.42), ('OE2', 'GLU', 'CZ', 'TYR', 10.36), ('OE2', 'GLU', 'OH', 'TYR', 11.42)]]}
ARG_MN = { 
	'distances':
		[[13.4], [11.9], [11.48], [10.1], [9.69], [10.64], [8.51]],
	'comparisons':
		[[('CB', 'ARG', 'MN', 'MN', 13.4)], [('CG', 'ARG', 'MN', 'MN', 11.9)], [('CD', 'ARG', 'MN', 'MN', 11.48)], [('NE', 'ARG', 'MN', 'MN', 10.1)], [('CZ', 'ARG', 'MN', 'MN', 9.69)], [('NH1', 'ARG', 'MN', 'MN', 10.64)], [('NH2', 'ARG', 'MN', 'MN', 8.51)]]}
TYR_ARG = { 
	'distances':
		[[17.3, 16.22, 14.9, 13.88, 12.64, 12.34, 11.86], [17.49, 16.47, 15.08, 14.13, 12.84, 12.39, 12.14], [18.58, 17.62, 16.2, 15.31, 14.03, 13.49, 13.4], [16.69, 15.66, 14.24, 13.3, 11.99, 11.5, 11.31], [18.9, 17.99, 16.53, 15.72, 14.41, 13.77, 13.86], [17.04, 16.07, 14.62, 13.76, 12.43, 11.82, 11.86], [18.16, 17.25, 15.78, 14.98, 13.66, 12.98, 13.15], [18.65, 17.81, 16.32, 15.6, 14.29, 13.51, 13.86]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 17.3), ('CB', 'TYR', 'CG', 'ARG', 16.22), ('CB', 'TYR', 'CD', 'ARG', 14.9), ('CB', 'TYR', 'NE', 'ARG', 13.88), ('CB', 'TYR', 'CZ', 'ARG', 12.64), ('CB', 'TYR', 'NH1', 'ARG', 12.34), ('CB', 'TYR', 'NH2', 'ARG', 11.86)], [('CG', 'TYR', 'CB', 'ARG', 17.49), ('CG', 'TYR', 'CG', 'ARG', 16.47), ('CG', 'TYR', 'CD', 'ARG', 15.08), ('CG', 'TYR', 'NE', 'ARG', 14.13), ('CG', 'TYR', 'CZ', 'ARG', 12.84), ('CG', 'TYR', 'NH1', 'ARG', 12.39), ('CG', 'TYR', 'NH2', 'ARG', 12.14)], [('CD1', 'TYR', 'CB', 'ARG', 18.58), ('CD1', 'TYR', 'CG', 'ARG', 17.62), ('CD1', 'TYR', 'CD', 'ARG', 16.2), ('CD1', 'TYR', 'NE', 'ARG', 15.31), ('CD1', 'TYR', 'CZ', 'ARG', 14.03), ('CD1', 'TYR', 'NH1', 'ARG', 13.49), ('CD1', 'TYR', 'NH2', 'ARG', 13.4)], [('CD2', 'TYR', 'CB', 'ARG', 16.69), ('CD2', 'TYR', 'CG', 'ARG', 15.66), ('CD2', 'TYR', 'CD', 'ARG', 14.24), ('CD2', 'TYR', 'NE', 'ARG', 13.3), ('CD2', 'TYR', 'CZ', 'ARG', 11.99), ('CD2', 'TYR', 'NH1', 'ARG', 11.5), ('CD2', 'TYR', 'NH2', 'ARG', 11.31)], [('CE1', 'TYR', 'CB', 'ARG', 18.9), ('CE1', 'TYR', 'CG', 'ARG', 17.99), ('CE1', 'TYR', 'CD', 'ARG', 16.53), ('CE1', 'TYR', 'NE', 'ARG', 15.72), ('CE1', 'TYR', 'CZ', 'ARG', 14.41), ('CE1', 'TYR', 'NH1', 'ARG', 13.77), ('CE1', 'TYR', 'NH2', 'ARG', 13.86)], [('CE2', 'TYR', 'CB', 'ARG', 17.04), ('CE2', 'TYR', 'CG', 'ARG', 16.07), ('CE2', 'TYR', 'CD', 'ARG', 14.62), ('CE2', 'TYR', 'NE', 'ARG', 13.76), ('CE2', 'TYR', 'CZ', 'ARG', 12.43), ('CE2', 'TYR', 'NH1', 'ARG', 11.82), ('CE2', 'TYR', 'NH2', 'ARG', 11.86)], [('CZ', 'TYR', 'CB', 'ARG', 18.16), ('CZ', 'TYR', 'CG', 'ARG', 17.25), ('CZ', 'TYR', 'CD', 'ARG', 15.78), ('CZ', 'TYR', 'NE', 'ARG', 14.98), ('CZ', 'TYR', 'CZ', 'ARG', 13.66), ('CZ', 'TYR', 'NH1', 'ARG', 12.98), ('CZ', 'TYR', 'NH2', 'ARG', 13.15)], [('OH', 'TYR', 'CB', 'ARG', 18.65), ('OH', 'TYR', 'CG', 'ARG', 17.81), ('OH', 'TYR', 'CD', 'ARG', 16.32), ('OH', 'TYR', 'NE', 'ARG', 15.6), ('OH', 'TYR', 'CZ', 'ARG', 14.29), ('OH', 'TYR', 'NH1', 'ARG', 13.51), ('OH', 'TYR', 'NH2', 'ARG', 13.86)]]}
GLU_MN = { 
	'distances':
		[[11.39], [11.51], [10.64], [11.08], [9.7]],
	'comparisons':
		[[('CB', 'GLU', 'MN', 'MN', 11.39)], [('CG', 'GLU', 'MN', 'MN', 11.51)], [('CD', 'GLU', 'MN', 'MN', 10.64)], [('OE1', 'GLU', 'MN', 'MN', 11.08)], [('OE2', 'GLU', 'MN', 'MN', 9.7)]]}
TYR_MN = { 
	'distances':
		[[13.29], [13.76], [15.11], [12.99], [15.73], [13.71], [15.07], [15.88]],
	'comparisons':
		[[('CB', 'TYR', 'MN', 'MN', 13.29)], [('CG', 'TYR', 'MN', 'MN', 13.76)], [('CD1', 'TYR', 'MN', 'MN', 15.11)], [('CD2', 'TYR', 'MN', 'MN', 12.99)], [('CE1', 'TYR', 'MN', 'MN', 15.73)], [('CE2', 'TYR', 'MN', 'MN', 13.71)], [('CZ', 'TYR', 'MN', 'MN', 15.07)], [('OH', 'TYR', 'MN', 'MN', 15.88)]]}
GLU_ARG = { 
	'distances':
		[[18.09, 16.78, 15.72, 14.43, 13.36, 13.55, 12.24], [19.03, 17.69, 16.62, 15.3, 14.21, 14.39, 13.05], [18.42, 17.07, 15.97, 14.64, 13.52, 13.67, 12.35], [18.26, 16.96, 15.77, 14.51, 13.32, 13.34, 12.22], [18.22, 16.82, 15.79, 14.42, 13.35, 13.62, 12.13]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 18.09), ('CB', 'GLU', 'CG', 'ARG', 16.78), ('CB', 'GLU', 'CD', 'ARG', 15.72), ('CB', 'GLU', 'NE', 'ARG', 14.43), ('CB', 'GLU', 'CZ', 'ARG', 13.36), ('CB', 'GLU', 'NH1', 'ARG', 13.55), ('CB', 'GLU', 'NH2', 'ARG', 12.24)], [('CG', 'GLU', 'CB', 'ARG', 19.03), ('CG', 'GLU', 'CG', 'ARG', 17.69), ('CG', 'GLU', 'CD', 'ARG', 16.62), ('CG', 'GLU', 'NE', 'ARG', 15.3), ('CG', 'GLU', 'CZ', 'ARG', 14.21), ('CG', 'GLU', 'NH1', 'ARG', 14.39), ('CG', 'GLU', 'NH2', 'ARG', 13.05)], [('CD', 'GLU', 'CB', 'ARG', 18.42), ('CD', 'GLU', 'CG', 'ARG', 17.07), ('CD', 'GLU', 'CD', 'ARG', 15.97), ('CD', 'GLU', 'NE', 'ARG', 14.64), ('CD', 'GLU', 'CZ', 'ARG', 13.52), ('CD', 'GLU', 'NH1', 'ARG', 13.67), ('CD', 'GLU', 'NH2', 'ARG', 12.35)], [('OE1', 'GLU', 'CB', 'ARG', 18.26), ('OE1', 'GLU', 'CG', 'ARG', 16.96), ('OE1', 'GLU', 'CD', 'ARG', 15.77), ('OE1', 'GLU', 'NE', 'ARG', 14.51), ('OE1', 'GLU', 'CZ', 'ARG', 13.32), ('OE1', 'GLU', 'NH1', 'ARG', 13.34), ('OE1', 'GLU', 'NH2', 'ARG', 12.22)], [('OE2', 'GLU', 'CB', 'ARG', 18.22), ('OE2', 'GLU', 'CG', 'ARG', 16.82), ('OE2', 'GLU', 'CD', 'ARG', 15.79), ('OE2', 'GLU', 'NE', 'ARG', 14.42), ('OE2', 'GLU', 'CZ', 'ARG', 13.35), ('OE2', 'GLU', 'NH1', 'ARG', 13.62), ('OE2', 'GLU', 'NH2', 'ARG', 12.13)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_TYR, d, 'M_1vzx_2_4_1_87')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_MN, d, 'M_1vzx_2_4_1_87')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ARG, d, 'M_1vzx_2_4_1_87')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_MN, d, 'M_1vzx_2_4_1_87')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_MN, d, 'M_1vzx_2_4_1_87')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_ARG, d, 'M_1vzx_2_4_1_87')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_TYR' :  match1,
		'ARG_MN' :  match2,
		'TYR_ARG' :  match3,
		'GLU_MN' :  match4,
		'TYR_MN' :  match5,
		'GLU_ARG' :  match6}