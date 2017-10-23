'''
FUNC:M_1r1j_3_4_24_11
PDB:1r1j
EC:3.4.24.11
RESI:glu,asp,his,arg,zn
LOCI:a-584,650,711,717,1001;
'''
import motifFunctions as cmd
HIS_ZN = { 
	'distances':
		[[8.92], [7.72], [8.03], [6.45], [7.11], [5.98]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 8.92)], [('CG', 'HIS', 'ZN', 'ZN', 7.72)], [('ND1', 'HIS', 'ZN', 'ZN', 8.03)], [('CD2', 'HIS', 'ZN', 'ZN', 6.45)], [('CE1', 'HIS', 'ZN', 'ZN', 7.11)], [('NE2', 'HIS', 'ZN', 'ZN', 5.98)]]}
HIS_ASP = { 
	'distances':
		[[10.62, 9.3, 8.38, 9.27], [10.73, 9.36, 8.64, 9.09], [12.01, 10.62, 9.96, 10.26], [9.94, 8.56, 8.03, 8.15], [12.07, 10.69, 10.21, 10.17], [10.89, 9.53, 9.15, 8.96]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 10.62), ('CB', 'HIS', 'CG', 'ASP', 9.3), ('CB', 'HIS', 'OD1', 'ASP', 8.38), ('CB', 'HIS', 'OD2', 'ASP', 9.27)], [('CG', 'HIS', 'CB', 'ASP', 10.73), ('CG', 'HIS', 'CG', 'ASP', 9.36), ('CG', 'HIS', 'OD1', 'ASP', 8.64), ('CG', 'HIS', 'OD2', 'ASP', 9.09)], [('ND1', 'HIS', 'CB', 'ASP', 12.01), ('ND1', 'HIS', 'CG', 'ASP', 10.62), ('ND1', 'HIS', 'OD1', 'ASP', 9.96), ('ND1', 'HIS', 'OD2', 'ASP', 10.26)], [('CD2', 'HIS', 'CB', 'ASP', 9.94), ('CD2', 'HIS', 'CG', 'ASP', 8.56), ('CD2', 'HIS', 'OD1', 'ASP', 8.03), ('CD2', 'HIS', 'OD2', 'ASP', 8.15)], [('CE1', 'HIS', 'CB', 'ASP', 12.07), ('CE1', 'HIS', 'CG', 'ASP', 10.69), ('CE1', 'HIS', 'OD1', 'ASP', 10.21), ('CE1', 'HIS', 'OD2', 'ASP', 10.17)], [('NE2', 'HIS', 'CB', 'ASP', 10.89), ('NE2', 'HIS', 'CG', 'ASP', 9.53), ('NE2', 'HIS', 'OD1', 'ASP', 9.15), ('NE2', 'HIS', 'OD2', 'ASP', 8.96)]]}
ARG_HIS = { 
	'distances':
		[[9.12, 9.92, 11.19, 9.86, 11.81, 11.11], [7.68, 8.6, 9.86, 8.7, 10.59, 9.99], [6.84, 7.58, 8.77, 7.64, 9.43, 8.85], [6.9, 7.29, 8.52, 7.01, 8.95, 8.16], [6.36, 6.41, 7.55, 5.95, 7.83, 6.98], [5.56, 5.57, 6.58, 5.37, 6.96, 6.34], [7.06, 6.78, 7.86, 5.96, 7.85, 6.79]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 9.12), ('CB', 'ARG', 'CG', 'HIS', 9.92), ('CB', 'ARG', 'ND1', 'HIS', 11.19), ('CB', 'ARG', 'CD2', 'HIS', 9.86), ('CB', 'ARG', 'CE1', 'HIS', 11.81), ('CB', 'ARG', 'NE2', 'HIS', 11.11)], [('CG', 'ARG', 'CB', 'HIS', 7.68), ('CG', 'ARG', 'CG', 'HIS', 8.6), ('CG', 'ARG', 'ND1', 'HIS', 9.86), ('CG', 'ARG', 'CD2', 'HIS', 8.7), ('CG', 'ARG', 'CE1', 'HIS', 10.59), ('CG', 'ARG', 'NE2', 'HIS', 9.99)], [('CD', 'ARG', 'CB', 'HIS', 6.84), ('CD', 'ARG', 'CG', 'HIS', 7.58), ('CD', 'ARG', 'ND1', 'HIS', 8.77), ('CD', 'ARG', 'CD2', 'HIS', 7.64), ('CD', 'ARG', 'CE1', 'HIS', 9.43), ('CD', 'ARG', 'NE2', 'HIS', 8.85)], [('NE', 'ARG', 'CB', 'HIS', 6.9), ('NE', 'ARG', 'CG', 'HIS', 7.29), ('NE', 'ARG', 'ND1', 'HIS', 8.52), ('NE', 'ARG', 'CD2', 'HIS', 7.01), ('NE', 'ARG', 'CE1', 'HIS', 8.95), ('NE', 'ARG', 'NE2', 'HIS', 8.16)], [('CZ', 'ARG', 'CB', 'HIS', 6.36), ('CZ', 'ARG', 'CG', 'HIS', 6.41), ('CZ', 'ARG', 'ND1', 'HIS', 7.55), ('CZ', 'ARG', 'CD2', 'HIS', 5.95), ('CZ', 'ARG', 'CE1', 'HIS', 7.83), ('CZ', 'ARG', 'NE2', 'HIS', 6.98)], [('NH1', 'ARG', 'CB', 'HIS', 5.56), ('NH1', 'ARG', 'CG', 'HIS', 5.57), ('NH1', 'ARG', 'ND1', 'HIS', 6.58), ('NH1', 'ARG', 'CD2', 'HIS', 5.37), ('NH1', 'ARG', 'CE1', 'HIS', 6.96), ('NH1', 'ARG', 'NE2', 'HIS', 6.34)], [('NH2', 'ARG', 'CB', 'HIS', 7.06), ('NH2', 'ARG', 'CG', 'HIS', 6.78), ('NH2', 'ARG', 'ND1', 'HIS', 7.86), ('NH2', 'ARG', 'CD2', 'HIS', 5.96), ('NH2', 'ARG', 'CE1', 'HIS', 7.85), ('NH2', 'ARG', 'NE2', 'HIS', 6.79)]]}
GLU_HIS = { 
	'distances':
		[[15.18, 13.96, 14.15, 12.63, 13.03, 12.02], [14.34, 13.09, 13.24, 11.79, 12.12, 11.14], [13.07, 11.77, 11.85, 10.49, 10.69, 9.75], [13.09, 11.76, 11.76, 10.5, 10.56, 9.68], [12.19, 10.9, 10.98, 9.64, 9.85, 8.91]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 15.18), ('CB', 'GLU', 'CG', 'HIS', 13.96), ('CB', 'GLU', 'ND1', 'HIS', 14.15), ('CB', 'GLU', 'CD2', 'HIS', 12.63), ('CB', 'GLU', 'CE1', 'HIS', 13.03), ('CB', 'GLU', 'NE2', 'HIS', 12.02)], [('CG', 'GLU', 'CB', 'HIS', 14.34), ('CG', 'GLU', 'CG', 'HIS', 13.09), ('CG', 'GLU', 'ND1', 'HIS', 13.24), ('CG', 'GLU', 'CD2', 'HIS', 11.79), ('CG', 'GLU', 'CE1', 'HIS', 12.12), ('CG', 'GLU', 'NE2', 'HIS', 11.14)], [('CD', 'GLU', 'CB', 'HIS', 13.07), ('CD', 'GLU', 'CG', 'HIS', 11.77), ('CD', 'GLU', 'ND1', 'HIS', 11.85), ('CD', 'GLU', 'CD2', 'HIS', 10.49), ('CD', 'GLU', 'CE1', 'HIS', 10.69), ('CD', 'GLU', 'NE2', 'HIS', 9.75)], [('OE1', 'GLU', 'CB', 'HIS', 13.09), ('OE1', 'GLU', 'CG', 'HIS', 11.76), ('OE1', 'GLU', 'ND1', 'HIS', 11.76), ('OE1', 'GLU', 'CD2', 'HIS', 10.5), ('OE1', 'GLU', 'CE1', 'HIS', 10.56), ('OE1', 'GLU', 'NE2', 'HIS', 9.68)], [('OE2', 'GLU', 'CB', 'HIS', 12.19), ('OE2', 'GLU', 'CG', 'HIS', 10.9), ('OE2', 'GLU', 'ND1', 'HIS', 10.98), ('OE2', 'GLU', 'CD2', 'HIS', 9.64), ('OE2', 'GLU', 'CE1', 'HIS', 9.85), ('OE2', 'GLU', 'NE2', 'HIS', 8.91)]]}
ASP_ZN = { 
	'distances':
		[[9.84], [8.87], [9.12], [8.09]],
	'comparisons':
		[[('CB', 'ASP', 'ZN', 'ZN', 9.84)], [('CG', 'ASP', 'ZN', 'ZN', 8.87)], [('OD1', 'ASP', 'ZN', 'ZN', 9.12)], [('OD2', 'ASP', 'ZN', 'ZN', 8.09)]]}
ARG_ZN = { 
	'distances':
		[[12.33], [11.61], [10.73], [9.52], [8.46], [8.61], [7.48]],
	'comparisons':
		[[('CB', 'ARG', 'ZN', 'ZN', 12.33)], [('CG', 'ARG', 'ZN', 'ZN', 11.61)], [('CD', 'ARG', 'ZN', 'ZN', 10.73)], [('NE', 'ARG', 'ZN', 'ZN', 9.52)], [('CZ', 'ARG', 'ZN', 'ZN', 8.46)], [('NH1', 'ARG', 'ZN', 'ZN', 8.61)], [('NH2', 'ARG', 'ZN', 'ZN', 7.48)]]}
ARG_ASP = { 
	'distances':
		[[7.39, 6.73, 5.85, 7.39], [7.79, 6.88, 5.77, 7.47], [8.09, 6.9, 5.88, 7.14], [7.07, 5.72, 4.87, 5.78], [7.53, 6.05, 5.42, 5.74], [8.83, 7.34, 6.66, 7.0], [6.99, 5.48, 5.24, 4.84]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 7.39), ('CB', 'ARG', 'CG', 'ASP', 6.73), ('CB', 'ARG', 'OD1', 'ASP', 5.85), ('CB', 'ARG', 'OD2', 'ASP', 7.39)], [('CG', 'ARG', 'CB', 'ASP', 7.79), ('CG', 'ARG', 'CG', 'ASP', 6.88), ('CG', 'ARG', 'OD1', 'ASP', 5.77), ('CG', 'ARG', 'OD2', 'ASP', 7.47)], [('CD', 'ARG', 'CB', 'ASP', 8.09), ('CD', 'ARG', 'CG', 'ASP', 6.9), ('CD', 'ARG', 'OD1', 'ASP', 5.88), ('CD', 'ARG', 'OD2', 'ASP', 7.14)], [('NE', 'ARG', 'CB', 'ASP', 7.07), ('NE', 'ARG', 'CG', 'ASP', 5.72), ('NE', 'ARG', 'OD1', 'ASP', 4.87), ('NE', 'ARG', 'OD2', 'ASP', 5.78)], [('CZ', 'ARG', 'CB', 'ASP', 7.53), ('CZ', 'ARG', 'CG', 'ASP', 6.05), ('CZ', 'ARG', 'OD1', 'ASP', 5.42), ('CZ', 'ARG', 'OD2', 'ASP', 5.74)], [('NH1', 'ARG', 'CB', 'ASP', 8.83), ('NH1', 'ARG', 'CG', 'ASP', 7.34), ('NH1', 'ARG', 'OD1', 'ASP', 6.66), ('NH1', 'ARG', 'OD2', 'ASP', 7.0)], [('NH2', 'ARG', 'CB', 'ASP', 6.99), ('NH2', 'ARG', 'CG', 'ASP', 5.48), ('NH2', 'ARG', 'OD1', 'ASP', 5.24), ('NH2', 'ARG', 'OD2', 'ASP', 4.84)]]}
GLU_ARG = { 
	'distances':
		[[16.67, 16.5, 15.62, 14.21, 13.26, 13.69, 11.98], [15.9, 15.7, 14.73, 13.34, 12.33, 12.68, 11.09], [15.26, 14.91, 13.89, 12.54, 11.45, 11.68, 10.25], [15.79, 15.34, 14.35, 13.02, 11.91, 12.09, 10.74], [14.37, 14.01, 12.91, 11.6, 10.46, 10.63, 9.31]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 16.67), ('CB', 'GLU', 'CG', 'ARG', 16.5), ('CB', 'GLU', 'CD', 'ARG', 15.62), ('CB', 'GLU', 'NE', 'ARG', 14.21), ('CB', 'GLU', 'CZ', 'ARG', 13.26), ('CB', 'GLU', 'NH1', 'ARG', 13.69), ('CB', 'GLU', 'NH2', 'ARG', 11.98)], [('CG', 'GLU', 'CB', 'ARG', 15.9), ('CG', 'GLU', 'CG', 'ARG', 15.7), ('CG', 'GLU', 'CD', 'ARG', 14.73), ('CG', 'GLU', 'NE', 'ARG', 13.34), ('CG', 'GLU', 'CZ', 'ARG', 12.33), ('CG', 'GLU', 'NH1', 'ARG', 12.68), ('CG', 'GLU', 'NH2', 'ARG', 11.09)], [('CD', 'GLU', 'CB', 'ARG', 15.26), ('CD', 'GLU', 'CG', 'ARG', 14.91), ('CD', 'GLU', 'CD', 'ARG', 13.89), ('CD', 'GLU', 'NE', 'ARG', 12.54), ('CD', 'GLU', 'CZ', 'ARG', 11.45), ('CD', 'GLU', 'NH1', 'ARG', 11.68), ('CD', 'GLU', 'NH2', 'ARG', 10.25)], [('OE1', 'GLU', 'CB', 'ARG', 15.79), ('OE1', 'GLU', 'CG', 'ARG', 15.34), ('OE1', 'GLU', 'CD', 'ARG', 14.35), ('OE1', 'GLU', 'NE', 'ARG', 13.02), ('OE1', 'GLU', 'CZ', 'ARG', 11.91), ('OE1', 'GLU', 'NH1', 'ARG', 12.09), ('OE1', 'GLU', 'NH2', 'ARG', 10.74)], [('OE2', 'GLU', 'CB', 'ARG', 14.37), ('OE2', 'GLU', 'CG', 'ARG', 14.01), ('OE2', 'GLU', 'CD', 'ARG', 12.91), ('OE2', 'GLU', 'NE', 'ARG', 11.6), ('OE2', 'GLU', 'CZ', 'ARG', 10.46), ('OE2', 'GLU', 'NH1', 'ARG', 10.63), ('OE2', 'GLU', 'NH2', 'ARG', 9.31)]]}
GLU_ZN = { 
	'distances':
		[[8.59], [8.1], [6.81], [6.52], [6.45]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 8.59)], [('CG', 'GLU', 'ZN', 'ZN', 8.1)], [('CD', 'GLU', 'ZN', 'ZN', 6.81)], [('OE1', 'GLU', 'ZN', 'ZN', 6.52)], [('OE2', 'GLU', 'ZN', 'ZN', 6.45)]]}
GLU_ASP = { 
	'distances':
		[[12.97, 12.54, 13.42, 11.48], [12.66, 12.06, 12.87, 10.92], [12.3, 11.54, 12.22, 10.42], [12.71, 11.98, 12.61, 10.93], [11.83, 10.94, 11.54, 9.77]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 12.97), ('CB', 'GLU', 'CG', 'ASP', 12.54), ('CB', 'GLU', 'OD1', 'ASP', 13.42), ('CB', 'GLU', 'OD2', 'ASP', 11.48)], [('CG', 'GLU', 'CB', 'ASP', 12.66), ('CG', 'GLU', 'CG', 'ASP', 12.06), ('CG', 'GLU', 'OD1', 'ASP', 12.87), ('CG', 'GLU', 'OD2', 'ASP', 10.92)], [('CD', 'GLU', 'CB', 'ASP', 12.3), ('CD', 'GLU', 'CG', 'ASP', 11.54), ('CD', 'GLU', 'OD1', 'ASP', 12.22), ('CD', 'GLU', 'OD2', 'ASP', 10.42)], [('OE1', 'GLU', 'CB', 'ASP', 12.71), ('OE1', 'GLU', 'CG', 'ASP', 11.98), ('OE1', 'GLU', 'OD1', 'ASP', 12.61), ('OE1', 'GLU', 'OD2', 'ASP', 10.93)], [('OE2', 'GLU', 'CB', 'ASP', 11.83), ('OE2', 'GLU', 'CG', 'ASP', 10.94), ('OE2', 'GLU', 'OD1', 'ASP', 11.54), ('OE2', 'GLU', 'OD2', 'ASP', 9.77)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ZN, d, 'M_1r1j_3_4_24_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'M_1r1j_3_4_24_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_HIS, d, 'M_1r1j_3_4_24_11')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_HIS, d, 'M_1r1j_3_4_24_11')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_ZN, d, 'M_1r1j_3_4_24_11')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_ZN, d, 'M_1r1j_3_4_24_11')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ARG_ASP, d, 'M_1r1j_3_4_24_11')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLU_ARG, d, 'M_1r1j_3_4_24_11')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLU_ZN, d, 'M_1r1j_3_4_24_11')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(GLU_ASP, d, 'M_1r1j_3_4_24_11')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ZN' :  match1,
		'HIS_ASP' :  match2,
		'ARG_HIS' :  match3,
		'GLU_HIS' :  match4,
		'ASP_ZN' :  match5,
		'ARG_ZN' :  match6,
		'ARG_ASP' :  match7,
		'GLU_ARG' :  match8,
		'GLU_ZN' :  match9,
		'GLU_ASP' :  match10}