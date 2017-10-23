'''
FUNC:M_1d8c_2_3_3_9
PDB:1d8c
EC:2.3.3.9
RESI:asp,glu,arg,asp,mg
LOCI:a-270,272,338,631,3001;
'''
import motifFunctions as cmd
ASP_MG = { 
	'distances':
		[[9.66], [8.3], [7.89], [7.86], [11.87], [10.6], [10.39], [9.9]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 9.66)], [('CG', 'ASP', 'MG', 'MG', 8.3)], [('OD1', 'ASP', 'MG', 'MG', 7.89)], [('OD2', 'ASP', 'MG', 'MG', 7.86)], [('CB', 'ASP', 'MG', 'MG', 11.87)], [('CG', 'ASP', 'MG', 'MG', 10.6)], [('OD1', 'ASP', 'MG', 'MG', 10.39)], [('OD2', 'ASP', 'MG', 'MG', 9.9)]]}
ASP_ASP = { 
	'distances':
		[[10.38, 9.58, 10.21, 8.31], [10.33, 9.43, 9.98, 8.15], [11.38, 10.43, 10.9, 9.18], [9.18, 8.29, 8.86, 7.02], [10.38, 10.33, 11.38, 9.18], [9.58, 9.43, 10.43, 8.29], [10.21, 9.98, 10.9, 8.86], [8.31, 8.15, 9.18, 7.02]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 10.38), ('CB', 'ASP', 'CG', 'ASP', 9.58), ('CB', 'ASP', 'OD1', 'ASP', 10.21), ('CB', 'ASP', 'OD2', 'ASP', 8.31)], [('CG', 'ASP', 'CB', 'ASP', 10.33), ('CG', 'ASP', 'CG', 'ASP', 9.43), ('CG', 'ASP', 'OD1', 'ASP', 9.98), ('CG', 'ASP', 'OD2', 'ASP', 8.15)], [('OD1', 'ASP', 'CB', 'ASP', 11.38), ('OD1', 'ASP', 'CG', 'ASP', 10.43), ('OD1', 'ASP', 'OD1', 'ASP', 10.9), ('OD1', 'ASP', 'OD2', 'ASP', 9.18)], [('OD2', 'ASP', 'CB', 'ASP', 9.18), ('OD2', 'ASP', 'CG', 'ASP', 8.29), ('OD2', 'ASP', 'OD1', 'ASP', 8.86), ('OD2', 'ASP', 'OD2', 'ASP', 7.02)], [('CB', 'ASP', 'CB', 'ASP', 10.38), ('CB', 'ASP', 'CG', 'ASP', 10.33), ('CB', 'ASP', 'OD1', 'ASP', 11.38), ('CB', 'ASP', 'OD2', 'ASP', 9.18)], [('CG', 'ASP', 'CB', 'ASP', 9.58), ('CG', 'ASP', 'CG', 'ASP', 9.43), ('CG', 'ASP', 'OD1', 'ASP', 10.43), ('CG', 'ASP', 'OD2', 'ASP', 8.29)], [('OD1', 'ASP', 'CB', 'ASP', 10.21), ('OD1', 'ASP', 'CG', 'ASP', 9.98), ('OD1', 'ASP', 'OD1', 'ASP', 10.9), ('OD1', 'ASP', 'OD2', 'ASP', 8.86)], [('OD2', 'ASP', 'CB', 'ASP', 8.31), ('OD2', 'ASP', 'CG', 'ASP', 8.15), ('OD2', 'ASP', 'OD1', 'ASP', 9.18), ('OD2', 'ASP', 'OD2', 'ASP', 7.02)]]}
ASP_ARG = { 
	'distances':
		[[13.05, 12.75, 11.84, 10.43, 9.44, 9.81, 8.24], [12.48, 12.07, 11.0, 9.65, 8.53, 8.7, 7.44], [13.19, 12.66, 11.49, 10.23, 9.03, 8.98, 8.09], [11.27, 10.93, 9.85, 8.47, 7.35, 7.59, 6.21], [6.7, 7.59, 7.74, 6.73, 7.16, 8.42, 6.6], [6.24, 6.76, 6.76, 5.61, 6.01, 7.33, 5.44], [5.41, 5.79, 6.01, 5.06, 5.79, 7.11, 5.57], [7.21, 7.48, 7.15, 5.77, 5.73, 6.98, 4.78]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 13.05), ('CB', 'ASP', 'CG', 'ARG', 12.75), ('CB', 'ASP', 'CD', 'ARG', 11.84), ('CB', 'ASP', 'NE', 'ARG', 10.43), ('CB', 'ASP', 'CZ', 'ARG', 9.44), ('CB', 'ASP', 'NH1', 'ARG', 9.81), ('CB', 'ASP', 'NH2', 'ARG', 8.24)], [('CG', 'ASP', 'CB', 'ARG', 12.48), ('CG', 'ASP', 'CG', 'ARG', 12.07), ('CG', 'ASP', 'CD', 'ARG', 11.0), ('CG', 'ASP', 'NE', 'ARG', 9.65), ('CG', 'ASP', 'CZ', 'ARG', 8.53), ('CG', 'ASP', 'NH1', 'ARG', 8.7), ('CG', 'ASP', 'NH2', 'ARG', 7.44)], [('OD1', 'ASP', 'CB', 'ARG', 13.19), ('OD1', 'ASP', 'CG', 'ARG', 12.66), ('OD1', 'ASP', 'CD', 'ARG', 11.49), ('OD1', 'ASP', 'NE', 'ARG', 10.23), ('OD1', 'ASP', 'CZ', 'ARG', 9.03), ('OD1', 'ASP', 'NH1', 'ARG', 8.98), ('OD1', 'ASP', 'NH2', 'ARG', 8.09)], [('OD2', 'ASP', 'CB', 'ARG', 11.27), ('OD2', 'ASP', 'CG', 'ARG', 10.93), ('OD2', 'ASP', 'CD', 'ARG', 9.85), ('OD2', 'ASP', 'NE', 'ARG', 8.47), ('OD2', 'ASP', 'CZ', 'ARG', 7.35), ('OD2', 'ASP', 'NH1', 'ARG', 7.59), ('OD2', 'ASP', 'NH2', 'ARG', 6.21)], [('CB', 'ASP', 'CB', 'ARG', 6.7), ('CB', 'ASP', 'CG', 'ARG', 7.59), ('CB', 'ASP', 'CD', 'ARG', 7.74), ('CB', 'ASP', 'NE', 'ARG', 6.73), ('CB', 'ASP', 'CZ', 'ARG', 7.16), ('CB', 'ASP', 'NH1', 'ARG', 8.42), ('CB', 'ASP', 'NH2', 'ARG', 6.6)], [('CG', 'ASP', 'CB', 'ARG', 6.24), ('CG', 'ASP', 'CG', 'ARG', 6.76), ('CG', 'ASP', 'CD', 'ARG', 6.76), ('CG', 'ASP', 'NE', 'ARG', 5.61), ('CG', 'ASP', 'CZ', 'ARG', 6.01), ('CG', 'ASP', 'NH1', 'ARG', 7.33), ('CG', 'ASP', 'NH2', 'ARG', 5.44)], [('OD1', 'ASP', 'CB', 'ARG', 5.41), ('OD1', 'ASP', 'CG', 'ARG', 5.79), ('OD1', 'ASP', 'CD', 'ARG', 6.01), ('OD1', 'ASP', 'NE', 'ARG', 5.06), ('OD1', 'ASP', 'CZ', 'ARG', 5.79), ('OD1', 'ASP', 'NH1', 'ARG', 7.11), ('OD1', 'ASP', 'NH2', 'ARG', 5.57)], [('OD2', 'ASP', 'CB', 'ARG', 7.21), ('OD2', 'ASP', 'CG', 'ARG', 7.48), ('OD2', 'ASP', 'CD', 'ARG', 7.15), ('OD2', 'ASP', 'NE', 'ARG', 5.77), ('OD2', 'ASP', 'CZ', 'ARG', 5.73), ('OD2', 'ASP', 'NH1', 'ARG', 6.98), ('OD2', 'ASP', 'NH2', 'ARG', 4.78)]]}
ARG_GLU = { 
	'distances':
		[[6.81, 7.97, 8.26, 7.94, 9.29], [6.11, 6.98, 7.08, 6.83, 7.99], [6.35, 7.01, 6.67, 6.1, 7.56], [5.89, 6.69, 6.31, 5.49, 7.39], [6.55, 7.12, 6.42, 5.34, 7.43], [7.5, 7.79, 6.81, 5.69, 7.57], [6.68, 7.34, 6.72, 5.6, 7.81]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 6.81), ('CB', 'ARG', 'CG', 'GLU', 7.97), ('CB', 'ARG', 'CD', 'GLU', 8.26), ('CB', 'ARG', 'OE1', 'GLU', 7.94), ('CB', 'ARG', 'OE2', 'GLU', 9.29)], [('CG', 'ARG', 'CB', 'GLU', 6.11), ('CG', 'ARG', 'CG', 'GLU', 6.98), ('CG', 'ARG', 'CD', 'GLU', 7.08), ('CG', 'ARG', 'OE1', 'GLU', 6.83), ('CG', 'ARG', 'OE2', 'GLU', 7.99)], [('CD', 'ARG', 'CB', 'GLU', 6.35), ('CD', 'ARG', 'CG', 'GLU', 7.01), ('CD', 'ARG', 'CD', 'GLU', 6.67), ('CD', 'ARG', 'OE1', 'GLU', 6.1), ('CD', 'ARG', 'OE2', 'GLU', 7.56)], [('NE', 'ARG', 'CB', 'GLU', 5.89), ('NE', 'ARG', 'CG', 'GLU', 6.69), ('NE', 'ARG', 'CD', 'GLU', 6.31), ('NE', 'ARG', 'OE1', 'GLU', 5.49), ('NE', 'ARG', 'OE2', 'GLU', 7.39)], [('CZ', 'ARG', 'CB', 'GLU', 6.55), ('CZ', 'ARG', 'CG', 'GLU', 7.12), ('CZ', 'ARG', 'CD', 'GLU', 6.42), ('CZ', 'ARG', 'OE1', 'GLU', 5.34), ('CZ', 'ARG', 'OE2', 'GLU', 7.43)], [('NH1', 'ARG', 'CB', 'GLU', 7.5), ('NH1', 'ARG', 'CG', 'GLU', 7.79), ('NH1', 'ARG', 'CD', 'GLU', 6.81), ('NH1', 'ARG', 'OE1', 'GLU', 5.69), ('NH1', 'ARG', 'OE2', 'GLU', 7.57)], [('NH2', 'ARG', 'CB', 'GLU', 6.68), ('NH2', 'ARG', 'CG', 'GLU', 7.34), ('NH2', 'ARG', 'CD', 'GLU', 6.72), ('NH2', 'ARG', 'OE1', 'GLU', 5.6), ('NH2', 'ARG', 'OE2', 'GLU', 7.81)]]}
ARG_MG = { 
	'distances':
		[[10.92], [9.79], [8.4], [7.98], [6.97], [5.99], [7.3]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 10.92)], [('CG', 'ARG', 'MG', 'MG', 9.79)], [('CD', 'ARG', 'MG', 'MG', 8.4)], [('NE', 'ARG', 'MG', 'MG', 7.98)], [('CZ', 'ARG', 'MG', 'MG', 6.97)], [('NH1', 'ARG', 'MG', 'MG', 5.99)], [('NH2', 'ARG', 'MG', 'MG', 7.3)]]}
MG_ASPI = { 
	'distances':
		[11.87, 10.6, 10.39, 9.9],
	'comparisons':
		[('MG', 'MG', 'CB', 'ASPI', 11.87), ('MG', 'MG', 'CG', 'ASPI', 10.6), ('MG', 'MG', 'OD1', 'ASPI', 10.39), ('MG', 'MG', 'OD2', 'ASPI', 9.9)]}
GLU_MG = { 
	'distances':
		[[9.51], [8.98], [7.49], [6.62], [7.44]],
	'comparisons':
		[[('CB', 'GLU', 'MG', 'MG', 9.51)], [('CG', 'GLU', 'MG', 'MG', 8.98)], [('CD', 'GLU', 'MG', 'MG', 7.49)], [('OE1', 'GLU', 'MG', 'MG', 6.62)], [('OE2', 'GLU', 'MG', 'MG', 7.44)]]}
GLU_ASPI = { 
	'distances':
		[[7.64, 6.29, 5.34, 6.54], [9.08, 7.66, 6.79, 7.7], [9.47, 7.98, 7.23, 7.8], [8.89, 7.4, 6.8, 7.06], [10.76, 9.27, 8.52, 9.06]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASPI', 7.64), ('CB', 'GLU', 'CG', 'ASPI', 6.29), ('CB', 'GLU', 'OD1', 'ASPI', 5.34), ('CB', 'GLU', 'OD2', 'ASPI', 6.54)], [('CG', 'GLU', 'CB', 'ASPI', 9.08), ('CG', 'GLU', 'CG', 'ASPI', 7.66), ('CG', 'GLU', 'OD1', 'ASPI', 6.79), ('CG', 'GLU', 'OD2', 'ASPI', 7.7)], [('CD', 'GLU', 'CB', 'ASPI', 9.47), ('CD', 'GLU', 'CG', 'ASPI', 7.98), ('CD', 'GLU', 'OD1', 'ASPI', 7.23), ('CD', 'GLU', 'OD2', 'ASPI', 7.8)], [('OE1', 'GLU', 'CB', 'ASPI', 8.89), ('OE1', 'GLU', 'CG', 'ASPI', 7.4), ('OE1', 'GLU', 'OD1', 'ASPI', 6.8), ('OE1', 'GLU', 'OD2', 'ASPI', 7.06)], [('OE2', 'GLU', 'CB', 'ASPI', 10.76), ('OE2', 'GLU', 'CG', 'ASPI', 9.27), ('OE2', 'GLU', 'OD1', 'ASPI', 8.52), ('OE2', 'GLU', 'OD2', 'ASPI', 9.06)]]}
ASP_GLU = { 
	'distances':
		[[10.56, 10.68, 10.11, 9.34, 10.75], [10.29, 10.34, 9.54, 8.63, 10.14], [10.98, 10.86, 9.91, 9.0, 10.35], [9.46, 9.67, 8.9, 7.89, 9.64], [7.64, 9.08, 9.47, 8.89, 10.76], [6.29, 7.66, 7.98, 7.4, 9.27], [5.34, 6.79, 7.23, 6.8, 8.52], [6.54, 7.7, 7.8, 7.06, 9.06]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 10.56), ('CB', 'ASP', 'CG', 'GLU', 10.68), ('CB', 'ASP', 'CD', 'GLU', 10.11), ('CB', 'ASP', 'OE1', 'GLU', 9.34), ('CB', 'ASP', 'OE2', 'GLU', 10.75)], [('CG', 'ASP', 'CB', 'GLU', 10.29), ('CG', 'ASP', 'CG', 'GLU', 10.34), ('CG', 'ASP', 'CD', 'GLU', 9.54), ('CG', 'ASP', 'OE1', 'GLU', 8.63), ('CG', 'ASP', 'OE2', 'GLU', 10.14)], [('OD1', 'ASP', 'CB', 'GLU', 10.98), ('OD1', 'ASP', 'CG', 'GLU', 10.86), ('OD1', 'ASP', 'CD', 'GLU', 9.91), ('OD1', 'ASP', 'OE1', 'GLU', 9.0), ('OD1', 'ASP', 'OE2', 'GLU', 10.35)], [('OD2', 'ASP', 'CB', 'GLU', 9.46), ('OD2', 'ASP', 'CG', 'GLU', 9.67), ('OD2', 'ASP', 'CD', 'GLU', 8.9), ('OD2', 'ASP', 'OE1', 'GLU', 7.89), ('OD2', 'ASP', 'OE2', 'GLU', 9.64)], [('CB', 'ASP', 'CB', 'GLU', 7.64), ('CB', 'ASP', 'CG', 'GLU', 9.08), ('CB', 'ASP', 'CD', 'GLU', 9.47), ('CB', 'ASP', 'OE1', 'GLU', 8.89), ('CB', 'ASP', 'OE2', 'GLU', 10.76)], [('CG', 'ASP', 'CB', 'GLU', 6.29), ('CG', 'ASP', 'CG', 'GLU', 7.66), ('CG', 'ASP', 'CD', 'GLU', 7.98), ('CG', 'ASP', 'OE1', 'GLU', 7.4), ('CG', 'ASP', 'OE2', 'GLU', 9.27)], [('OD1', 'ASP', 'CB', 'GLU', 5.34), ('OD1', 'ASP', 'CG', 'GLU', 6.79), ('OD1', 'ASP', 'CD', 'GLU', 7.23), ('OD1', 'ASP', 'OE1', 'GLU', 6.8), ('OD1', 'ASP', 'OE2', 'GLU', 8.52)], [('OD2', 'ASP', 'CB', 'GLU', 6.54), ('OD2', 'ASP', 'CG', 'GLU', 7.7), ('OD2', 'ASP', 'CD', 'GLU', 7.8), ('OD2', 'ASP', 'OE1', 'GLU', 7.06), ('OD2', 'ASP', 'OE2', 'GLU', 9.06)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_MG, d, 'M_1d8c_2_3_3_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'M_1d8c_2_3_3_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ARG, d, 'M_1d8c_2_3_3_9')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_GLU, d, 'M_1d8c_2_3_3_9')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_MG, d, 'M_1d8c_2_3_3_9')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(MG_ASPI, d, 'M_1d8c_2_3_3_9')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLU_MG, d, 'M_1d8c_2_3_3_9')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLU_ASPI, d, 'M_1d8c_2_3_3_9')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ASP_GLU, d, 'M_1d8c_2_3_3_9')
	if match9 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_MG' :  match1,
		'ASP_ASP' :  match2,
		'ASP_ARG' :  match3,
		'ARG_GLU' :  match4,
		'ARG_MG' :  match5,
		'MG_ASPI' :  match6,
		'GLU_MG' :  match7,
		'GLU_ASPI' :  match8,
		'ASP_GLU' :  match9}