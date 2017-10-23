'''
FUNC:P_1f6d_5_1_3_14
PDB:1f6d
EC:5.1.3.14
RESI:asp,glu,glu,his
LOCI:a-95,117,131,213;
'''
import motifFunctions as cmd
GLU_HIS = { 
	'distances':
		[[20.46, 19.21, 19.17, 18.02, 18.02, 17.26], [19.4, 18.11, 18.06, 16.91, 16.87, 16.11], [18.01, 16.75, 16.76, 15.54, 15.6, 14.79], [17.43, 16.19, 16.18, 15.02, 15.04, 14.27], [17.56, 16.33, 16.41, 15.07, 15.27, 14.38], [15.66, 14.7, 14.3, 14.21, 13.58, 13.5], [14.84, 13.96, 13.69, 13.46, 13.04, 12.87], [14.36, 13.6, 13.34, 13.24, 12.83, 12.75], [14.34, 13.58, 13.21, 13.32, 12.73, 12.79], [14.17, 13.52, 13.38, 13.16, 12.95, 12.81]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 20.46), ('CB', 'GLU', 'CG', 'HIS', 19.21), ('CB', 'GLU', 'ND1', 'HIS', 19.17), ('CB', 'GLU', 'CD2', 'HIS', 18.02), ('CB', 'GLU', 'CE1', 'HIS', 18.02), ('CB', 'GLU', 'NE2', 'HIS', 17.26)], [('CG', 'GLU', 'CB', 'HIS', 19.4), ('CG', 'GLU', 'CG', 'HIS', 18.11), ('CG', 'GLU', 'ND1', 'HIS', 18.06), ('CG', 'GLU', 'CD2', 'HIS', 16.91), ('CG', 'GLU', 'CE1', 'HIS', 16.87), ('CG', 'GLU', 'NE2', 'HIS', 16.11)], [('CD', 'GLU', 'CB', 'HIS', 18.01), ('CD', 'GLU', 'CG', 'HIS', 16.75), ('CD', 'GLU', 'ND1', 'HIS', 16.76), ('CD', 'GLU', 'CD2', 'HIS', 15.54), ('CD', 'GLU', 'CE1', 'HIS', 15.6), ('CD', 'GLU', 'NE2', 'HIS', 14.79)], [('OE1', 'GLU', 'CB', 'HIS', 17.43), ('OE1', 'GLU', 'CG', 'HIS', 16.19), ('OE1', 'GLU', 'ND1', 'HIS', 16.18), ('OE1', 'GLU', 'CD2', 'HIS', 15.02), ('OE1', 'GLU', 'CE1', 'HIS', 15.04), ('OE1', 'GLU', 'NE2', 'HIS', 14.27)], [('OE2', 'GLU', 'CB', 'HIS', 17.56), ('OE2', 'GLU', 'CG', 'HIS', 16.33), ('OE2', 'GLU', 'ND1', 'HIS', 16.41), ('OE2', 'GLU', 'CD2', 'HIS', 15.07), ('OE2', 'GLU', 'CE1', 'HIS', 15.27), ('OE2', 'GLU', 'NE2', 'HIS', 14.38)], [('CB', 'GLU', 'CB', 'HIS', 15.66), ('CB', 'GLU', 'CG', 'HIS', 14.7), ('CB', 'GLU', 'ND1', 'HIS', 14.3), ('CB', 'GLU', 'CD2', 'HIS', 14.21), ('CB', 'GLU', 'CE1', 'HIS', 13.58), ('CB', 'GLU', 'NE2', 'HIS', 13.5)], [('CG', 'GLU', 'CB', 'HIS', 14.84), ('CG', 'GLU', 'CG', 'HIS', 13.96), ('CG', 'GLU', 'ND1', 'HIS', 13.69), ('CG', 'GLU', 'CD2', 'HIS', 13.46), ('CG', 'GLU', 'CE1', 'HIS', 13.04), ('CG', 'GLU', 'NE2', 'HIS', 12.87)], [('CD', 'GLU', 'CB', 'HIS', 14.36), ('CD', 'GLU', 'CG', 'HIS', 13.6), ('CD', 'GLU', 'ND1', 'HIS', 13.34), ('CD', 'GLU', 'CD2', 'HIS', 13.24), ('CD', 'GLU', 'CE1', 'HIS', 12.83), ('CD', 'GLU', 'NE2', 'HIS', 12.75)], [('OE1', 'GLU', 'CB', 'HIS', 14.34), ('OE1', 'GLU', 'CG', 'HIS', 13.58), ('OE1', 'GLU', 'ND1', 'HIS', 13.21), ('OE1', 'GLU', 'CD2', 'HIS', 13.32), ('OE1', 'GLU', 'CE1', 'HIS', 12.73), ('OE1', 'GLU', 'NE2', 'HIS', 12.79)], [('OE2', 'GLU', 'CB', 'HIS', 14.17), ('OE2', 'GLU', 'CG', 'HIS', 13.52), ('OE2', 'GLU', 'ND1', 'HIS', 13.38), ('OE2', 'GLU', 'CD2', 'HIS', 13.16), ('OE2', 'GLU', 'CE1', 'HIS', 12.95), ('OE2', 'GLU', 'NE2', 'HIS', 12.81)]]}
HIS_GLUI = { 
	'distances':
		[[15.66, 14.84, 14.36, 14.34, 14.17], [14.7, 13.96, 13.6, 13.58, 13.52], [14.3, 13.69, 13.34, 13.21, 13.38], [14.21, 13.46, 13.24, 13.32, 13.16], [13.58, 13.04, 12.83, 12.73, 12.95], [13.5, 12.87, 12.75, 12.79, 12.81]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLUI', 15.66), ('CB', 'HIS', 'CG', 'GLUI', 14.84), ('CB', 'HIS', 'CD', 'GLUI', 14.36), ('CB', 'HIS', 'OE1', 'GLUI', 14.34), ('CB', 'HIS', 'OE2', 'GLUI', 14.17)], [('CG', 'HIS', 'CB', 'GLUI', 14.7), ('CG', 'HIS', 'CG', 'GLUI', 13.96), ('CG', 'HIS', 'CD', 'GLUI', 13.6), ('CG', 'HIS', 'OE1', 'GLUI', 13.58), ('CG', 'HIS', 'OE2', 'GLUI', 13.52)], [('ND1', 'HIS', 'CB', 'GLUI', 14.3), ('ND1', 'HIS', 'CG', 'GLUI', 13.69), ('ND1', 'HIS', 'CD', 'GLUI', 13.34), ('ND1', 'HIS', 'OE1', 'GLUI', 13.21), ('ND1', 'HIS', 'OE2', 'GLUI', 13.38)], [('CD2', 'HIS', 'CB', 'GLUI', 14.21), ('CD2', 'HIS', 'CG', 'GLUI', 13.46), ('CD2', 'HIS', 'CD', 'GLUI', 13.24), ('CD2', 'HIS', 'OE1', 'GLUI', 13.32), ('CD2', 'HIS', 'OE2', 'GLUI', 13.16)], [('CE1', 'HIS', 'CB', 'GLUI', 13.58), ('CE1', 'HIS', 'CG', 'GLUI', 13.04), ('CE1', 'HIS', 'CD', 'GLUI', 12.83), ('CE1', 'HIS', 'OE1', 'GLUI', 12.73), ('CE1', 'HIS', 'OE2', 'GLUI', 12.95)], [('NE2', 'HIS', 'CB', 'GLUI', 13.5), ('NE2', 'HIS', 'CG', 'GLUI', 12.87), ('NE2', 'HIS', 'CD', 'GLUI', 12.75), ('NE2', 'HIS', 'OE1', 'GLUI', 12.79), ('NE2', 'HIS', 'OE2', 'GLUI', 12.81)]]}
GLU_GLU = { 
	'distances':
		[[12.59, 12.69, 14.15, 14.96, 14.58], [12.56, 12.64, 14.06, 14.82, 14.52], [11.8, 11.73, 13.1, 13.89, 13.48], [10.57, 10.48, 11.86, 12.67, 12.25], [12.55, 12.36, 13.66, 14.48, 13.98], [12.59, 12.56, 11.8, 10.57, 12.55], [12.69, 12.64, 11.73, 10.48, 12.36], [14.15, 14.06, 13.1, 11.86, 13.66], [14.96, 14.82, 13.89, 12.67, 14.48], [14.58, 14.52, 13.48, 12.25, 13.98]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.59), ('CB', 'GLU', 'CG', 'GLU', 12.69), ('CB', 'GLU', 'CD', 'GLU', 14.15), ('CB', 'GLU', 'OE1', 'GLU', 14.96), ('CB', 'GLU', 'OE2', 'GLU', 14.58)], [('CG', 'GLU', 'CB', 'GLU', 12.56), ('CG', 'GLU', 'CG', 'GLU', 12.64), ('CG', 'GLU', 'CD', 'GLU', 14.06), ('CG', 'GLU', 'OE1', 'GLU', 14.82), ('CG', 'GLU', 'OE2', 'GLU', 14.52)], [('CD', 'GLU', 'CB', 'GLU', 11.8), ('CD', 'GLU', 'CG', 'GLU', 11.73), ('CD', 'GLU', 'CD', 'GLU', 13.1), ('CD', 'GLU', 'OE1', 'GLU', 13.89), ('CD', 'GLU', 'OE2', 'GLU', 13.48)], [('OE1', 'GLU', 'CB', 'GLU', 10.57), ('OE1', 'GLU', 'CG', 'GLU', 10.48), ('OE1', 'GLU', 'CD', 'GLU', 11.86), ('OE1', 'GLU', 'OE1', 'GLU', 12.67), ('OE1', 'GLU', 'OE2', 'GLU', 12.25)], [('OE2', 'GLU', 'CB', 'GLU', 12.55), ('OE2', 'GLU', 'CG', 'GLU', 12.36), ('OE2', 'GLU', 'CD', 'GLU', 13.66), ('OE2', 'GLU', 'OE1', 'GLU', 14.48), ('OE2', 'GLU', 'OE2', 'GLU', 13.98)], [('CB', 'GLU', 'CB', 'GLU', 12.59), ('CB', 'GLU', 'CG', 'GLU', 12.56), ('CB', 'GLU', 'CD', 'GLU', 11.8), ('CB', 'GLU', 'OE1', 'GLU', 10.57), ('CB', 'GLU', 'OE2', 'GLU', 12.55)], [('CG', 'GLU', 'CB', 'GLU', 12.69), ('CG', 'GLU', 'CG', 'GLU', 12.64), ('CG', 'GLU', 'CD', 'GLU', 11.73), ('CG', 'GLU', 'OE1', 'GLU', 10.48), ('CG', 'GLU', 'OE2', 'GLU', 12.36)], [('CD', 'GLU', 'CB', 'GLU', 14.15), ('CD', 'GLU', 'CG', 'GLU', 14.06), ('CD', 'GLU', 'CD', 'GLU', 13.1), ('CD', 'GLU', 'OE1', 'GLU', 11.86), ('CD', 'GLU', 'OE2', 'GLU', 13.66)], [('OE1', 'GLU', 'CB', 'GLU', 14.96), ('OE1', 'GLU', 'CG', 'GLU', 14.82), ('OE1', 'GLU', 'CD', 'GLU', 13.89), ('OE1', 'GLU', 'OE1', 'GLU', 12.67), ('OE1', 'GLU', 'OE2', 'GLU', 14.48)], [('OE2', 'GLU', 'CB', 'GLU', 14.58), ('OE2', 'GLU', 'CG', 'GLU', 14.52), ('OE2', 'GLU', 'CD', 'GLU', 13.48), ('OE2', 'GLU', 'OE1', 'GLU', 12.25), ('OE2', 'GLU', 'OE2', 'GLU', 13.98)]]}
ASP_HIS = { 
	'distances':
		[[17.76, 16.7, 16.45, 15.94, 15.56, 15.21], [16.33, 15.27, 15.07, 14.47, 14.18, 13.78], [16.15, 15.14, 15.06, 14.3, 14.21, 13.7], [15.45, 14.34, 14.07, 13.58, 13.15, 12.81]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 17.76), ('CB', 'ASP', 'CG', 'HIS', 16.7), ('CB', 'ASP', 'ND1', 'HIS', 16.45), ('CB', 'ASP', 'CD2', 'HIS', 15.94), ('CB', 'ASP', 'CE1', 'HIS', 15.56), ('CB', 'ASP', 'NE2', 'HIS', 15.21)], [('CG', 'ASP', 'CB', 'HIS', 16.33), ('CG', 'ASP', 'CG', 'HIS', 15.27), ('CG', 'ASP', 'ND1', 'HIS', 15.07), ('CG', 'ASP', 'CD2', 'HIS', 14.47), ('CG', 'ASP', 'CE1', 'HIS', 14.18), ('CG', 'ASP', 'NE2', 'HIS', 13.78)], [('OD1', 'ASP', 'CB', 'HIS', 16.15), ('OD1', 'ASP', 'CG', 'HIS', 15.14), ('OD1', 'ASP', 'ND1', 'HIS', 15.06), ('OD1', 'ASP', 'CD2', 'HIS', 14.3), ('OD1', 'ASP', 'CE1', 'HIS', 14.21), ('OD1', 'ASP', 'NE2', 'HIS', 13.7)], [('OD2', 'ASP', 'CB', 'HIS', 15.45), ('OD2', 'ASP', 'CG', 'HIS', 14.34), ('OD2', 'ASP', 'ND1', 'HIS', 14.07), ('OD2', 'ASP', 'CD2', 'HIS', 13.58), ('OD2', 'ASP', 'CE1', 'HIS', 13.15), ('OD2', 'ASP', 'NE2', 'HIS', 12.81)]]}
ASP_GLU = { 
	'distances':
		[[9.37, 9.68, 9.16, 7.96, 10.11], [9.21, 9.31, 8.55, 7.3, 9.35], [9.02, 9.15, 8.26, 7.02, 8.97], [9.58, 9.46, 8.65, 7.41, 9.39], [4.79, 5.15, 6.61, 7.33, 7.25], [4.58, 4.54, 6.04, 6.86, 6.6], [5.41, 4.96, 6.33, 7.33, 6.63], [4.16, 4.27, 5.74, 6.41, 6.46]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 9.37), ('CB', 'ASP', 'CG', 'GLU', 9.68), ('CB', 'ASP', 'CD', 'GLU', 9.16), ('CB', 'ASP', 'OE1', 'GLU', 7.96), ('CB', 'ASP', 'OE2', 'GLU', 10.11)], [('CG', 'ASP', 'CB', 'GLU', 9.21), ('CG', 'ASP', 'CG', 'GLU', 9.31), ('CG', 'ASP', 'CD', 'GLU', 8.55), ('CG', 'ASP', 'OE1', 'GLU', 7.3), ('CG', 'ASP', 'OE2', 'GLU', 9.35)], [('OD1', 'ASP', 'CB', 'GLU', 9.02), ('OD1', 'ASP', 'CG', 'GLU', 9.15), ('OD1', 'ASP', 'CD', 'GLU', 8.26), ('OD1', 'ASP', 'OE1', 'GLU', 7.02), ('OD1', 'ASP', 'OE2', 'GLU', 8.97)], [('OD2', 'ASP', 'CB', 'GLU', 9.58), ('OD2', 'ASP', 'CG', 'GLU', 9.46), ('OD2', 'ASP', 'CD', 'GLU', 8.65), ('OD2', 'ASP', 'OE1', 'GLU', 7.41), ('OD2', 'ASP', 'OE2', 'GLU', 9.39)], [('CB', 'ASP', 'CB', 'GLU', 4.79), ('CB', 'ASP', 'CG', 'GLU', 5.15), ('CB', 'ASP', 'CD', 'GLU', 6.61), ('CB', 'ASP', 'OE1', 'GLU', 7.33), ('CB', 'ASP', 'OE2', 'GLU', 7.25)], [('CG', 'ASP', 'CB', 'GLU', 4.58), ('CG', 'ASP', 'CG', 'GLU', 4.54), ('CG', 'ASP', 'CD', 'GLU', 6.04), ('CG', 'ASP', 'OE1', 'GLU', 6.86), ('CG', 'ASP', 'OE2', 'GLU', 6.6)], [('OD1', 'ASP', 'CB', 'GLU', 5.41), ('OD1', 'ASP', 'CG', 'GLU', 4.96), ('OD1', 'ASP', 'CD', 'GLU', 6.33), ('OD1', 'ASP', 'OE1', 'GLU', 7.33), ('OD1', 'ASP', 'OE2', 'GLU', 6.63)], [('OD2', 'ASP', 'CB', 'GLU', 4.16), ('OD2', 'ASP', 'CG', 'GLU', 4.27), ('OD2', 'ASP', 'CD', 'GLU', 5.74), ('OD2', 'ASP', 'OE1', 'GLU', 6.41), ('OD2', 'ASP', 'OE2', 'GLU', 6.46)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_HIS, d, 'P_1f6d_5_1_3_14')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLUI, d, 'P_1f6d_5_1_3_14')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_GLU, d, 'P_1f6d_5_1_3_14')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_HIS, d, 'P_1f6d_5_1_3_14')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_GLU, d, 'P_1f6d_5_1_3_14')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_HIS' :  match1,
		'HIS_GLUI' :  match2,
		'GLU_GLU' :  match3,
		'ASP_HIS' :  match4,
		'ASP_GLU' :  match5}