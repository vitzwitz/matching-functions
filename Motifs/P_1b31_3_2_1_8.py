'''
FUNC:P_1b31_3_2_1_8
PDB:1b31
EC:3.2.1.8
RESI:glu,his,glu,asp
LOCI:a-132,210,238,240;
'''
import motifFunctions as cmd
ASP_GLUI = { 
	'distances':
		[[9.04, 10.49, 11.16, 10.6, 12.4], [8.27, 9.7, 10.17, 9.48, 11.41], [8.37, 9.83, 10.22, 9.49, 11.44], [7.93, 9.25, 9.59, 8.83, 10.82]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLUI', 9.04), ('CB', 'ASP', 'CG', 'GLUI', 10.49), ('CB', 'ASP', 'CD', 'GLUI', 11.16), ('CB', 'ASP', 'OE1', 'GLUI', 10.6), ('CB', 'ASP', 'OE2', 'GLUI', 12.4)], [('CG', 'ASP', 'CB', 'GLUI', 8.27), ('CG', 'ASP', 'CG', 'GLUI', 9.7), ('CG', 'ASP', 'CD', 'GLUI', 10.17), ('CG', 'ASP', 'OE1', 'GLUI', 9.48), ('CG', 'ASP', 'OE2', 'GLUI', 11.41)], [('OD1', 'ASP', 'CB', 'GLUI', 8.37), ('OD1', 'ASP', 'CG', 'GLUI', 9.83), ('OD1', 'ASP', 'CD', 'GLUI', 10.22), ('OD1', 'ASP', 'OE1', 'GLUI', 9.49), ('OD1', 'ASP', 'OE2', 'GLUI', 11.44)], [('OD2', 'ASP', 'CB', 'GLUI', 7.93), ('OD2', 'ASP', 'CG', 'GLUI', 9.25), ('OD2', 'ASP', 'CD', 'GLUI', 9.59), ('OD2', 'ASP', 'OE1', 'GLUI', 8.83), ('OD2', 'ASP', 'OE2', 'GLUI', 10.82)]]}
GLU_GLU = { 
	'distances':
		[[12.76, 12.0, 10.75, 10.63, 10.07], [11.25, 10.52, 9.25, 9.11, 8.63], [11.01, 10.38, 9.01, 8.62, 8.52], [12.07, 11.47, 10.05, 9.58, 9.58], [9.9, 9.34, 7.95, 7.46, 7.61], [12.76, 11.25, 11.01, 12.07, 9.9], [12.0, 10.52, 10.38, 11.47, 9.34], [10.75, 9.25, 9.01, 10.05, 7.95], [10.63, 9.11, 8.62, 9.58, 7.46], [10.07, 8.63, 8.52, 9.58, 7.61]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.76), ('CB', 'GLU', 'CG', 'GLU', 12.0), ('CB', 'GLU', 'CD', 'GLU', 10.75), ('CB', 'GLU', 'OE1', 'GLU', 10.63), ('CB', 'GLU', 'OE2', 'GLU', 10.07)], [('CG', 'GLU', 'CB', 'GLU', 11.25), ('CG', 'GLU', 'CG', 'GLU', 10.52), ('CG', 'GLU', 'CD', 'GLU', 9.25), ('CG', 'GLU', 'OE1', 'GLU', 9.11), ('CG', 'GLU', 'OE2', 'GLU', 8.63)], [('CD', 'GLU', 'CB', 'GLU', 11.01), ('CD', 'GLU', 'CG', 'GLU', 10.38), ('CD', 'GLU', 'CD', 'GLU', 9.01), ('CD', 'GLU', 'OE1', 'GLU', 8.62), ('CD', 'GLU', 'OE2', 'GLU', 8.52)], [('OE1', 'GLU', 'CB', 'GLU', 12.07), ('OE1', 'GLU', 'CG', 'GLU', 11.47), ('OE1', 'GLU', 'CD', 'GLU', 10.05), ('OE1', 'GLU', 'OE1', 'GLU', 9.58), ('OE1', 'GLU', 'OE2', 'GLU', 9.58)], [('OE2', 'GLU', 'CB', 'GLU', 9.9), ('OE2', 'GLU', 'CG', 'GLU', 9.34), ('OE2', 'GLU', 'CD', 'GLU', 7.95), ('OE2', 'GLU', 'OE1', 'GLU', 7.46), ('OE2', 'GLU', 'OE2', 'GLU', 7.61)], [('CB', 'GLU', 'CB', 'GLU', 12.76), ('CB', 'GLU', 'CG', 'GLU', 11.25), ('CB', 'GLU', 'CD', 'GLU', 11.01), ('CB', 'GLU', 'OE1', 'GLU', 12.07), ('CB', 'GLU', 'OE2', 'GLU', 9.9)], [('CG', 'GLU', 'CB', 'GLU', 12.0), ('CG', 'GLU', 'CG', 'GLU', 10.52), ('CG', 'GLU', 'CD', 'GLU', 10.38), ('CG', 'GLU', 'OE1', 'GLU', 11.47), ('CG', 'GLU', 'OE2', 'GLU', 9.34)], [('CD', 'GLU', 'CB', 'GLU', 10.75), ('CD', 'GLU', 'CG', 'GLU', 9.25), ('CD', 'GLU', 'CD', 'GLU', 9.01), ('CD', 'GLU', 'OE1', 'GLU', 10.05), ('CD', 'GLU', 'OE2', 'GLU', 7.95)], [('OE1', 'GLU', 'CB', 'GLU', 10.63), ('OE1', 'GLU', 'CG', 'GLU', 9.11), ('OE1', 'GLU', 'CD', 'GLU', 8.62), ('OE1', 'GLU', 'OE1', 'GLU', 9.58), ('OE1', 'GLU', 'OE2', 'GLU', 7.46)], [('OE2', 'GLU', 'CB', 'GLU', 10.07), ('OE2', 'GLU', 'CG', 'GLU', 8.63), ('OE2', 'GLU', 'CD', 'GLU', 8.52), ('OE2', 'GLU', 'OE1', 'GLU', 9.58), ('OE2', 'GLU', 'OE2', 'GLU', 7.61)]]}
GLU_ASP = { 
	'distances':
		[[18.22, 16.85, 16.33, 16.42], [16.74, 15.39, 14.9, 14.94], [16.08, 14.68, 14.22, 14.15], [16.86, 15.42, 14.97, 14.85], [14.86, 13.46, 13.04, 12.91], [9.04, 8.27, 8.37, 7.93], [10.49, 9.7, 9.83, 9.25], [11.16, 10.17, 10.22, 9.59], [10.6, 9.48, 9.49, 8.83], [12.4, 11.41, 11.44, 10.82]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 18.22), ('CB', 'GLU', 'CG', 'ASP', 16.85), ('CB', 'GLU', 'OD1', 'ASP', 16.33), ('CB', 'GLU', 'OD2', 'ASP', 16.42)], [('CG', 'GLU', 'CB', 'ASP', 16.74), ('CG', 'GLU', 'CG', 'ASP', 15.39), ('CG', 'GLU', 'OD1', 'ASP', 14.9), ('CG', 'GLU', 'OD2', 'ASP', 14.94)], [('CD', 'GLU', 'CB', 'ASP', 16.08), ('CD', 'GLU', 'CG', 'ASP', 14.68), ('CD', 'GLU', 'OD1', 'ASP', 14.22), ('CD', 'GLU', 'OD2', 'ASP', 14.15)], [('OE1', 'GLU', 'CB', 'ASP', 16.86), ('OE1', 'GLU', 'CG', 'ASP', 15.42), ('OE1', 'GLU', 'OD1', 'ASP', 14.97), ('OE1', 'GLU', 'OD2', 'ASP', 14.85)], [('OE2', 'GLU', 'CB', 'ASP', 14.86), ('OE2', 'GLU', 'CG', 'ASP', 13.46), ('OE2', 'GLU', 'OD1', 'ASP', 13.04), ('OE2', 'GLU', 'OD2', 'ASP', 12.91)], [('CB', 'GLU', 'CB', 'ASP', 9.04), ('CB', 'GLU', 'CG', 'ASP', 8.27), ('CB', 'GLU', 'OD1', 'ASP', 8.37), ('CB', 'GLU', 'OD2', 'ASP', 7.93)], [('CG', 'GLU', 'CB', 'ASP', 10.49), ('CG', 'GLU', 'CG', 'ASP', 9.7), ('CG', 'GLU', 'OD1', 'ASP', 9.83), ('CG', 'GLU', 'OD2', 'ASP', 9.25)], [('CD', 'GLU', 'CB', 'ASP', 11.16), ('CD', 'GLU', 'CG', 'ASP', 10.17), ('CD', 'GLU', 'OD1', 'ASP', 10.22), ('CD', 'GLU', 'OD2', 'ASP', 9.59)], [('OE1', 'GLU', 'CB', 'ASP', 10.6), ('OE1', 'GLU', 'CG', 'ASP', 9.48), ('OE1', 'GLU', 'OD1', 'ASP', 9.49), ('OE1', 'GLU', 'OD2', 'ASP', 8.83)], [('OE2', 'GLU', 'CB', 'ASP', 12.4), ('OE2', 'GLU', 'CG', 'ASP', 11.41), ('OE2', 'GLU', 'OD1', 'ASP', 11.44), ('OE2', 'GLU', 'OD2', 'ASP', 10.82)]]}
HIS_ASP = { 
	'distances':
		[[7.96, 6.68, 5.61, 7.02], [7.75, 6.38, 5.62, 6.4], [6.66, 5.26, 4.81, 5.11], [8.79, 7.43, 6.83, 7.25], [7.28, 5.97, 5.86, 5.47], [8.53, 7.2, 6.92, 6.77]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.96), ('CB', 'HIS', 'CG', 'ASP', 6.68), ('CB', 'HIS', 'OD1', 'ASP', 5.61), ('CB', 'HIS', 'OD2', 'ASP', 7.02)], [('CG', 'HIS', 'CB', 'ASP', 7.75), ('CG', 'HIS', 'CG', 'ASP', 6.38), ('CG', 'HIS', 'OD1', 'ASP', 5.62), ('CG', 'HIS', 'OD2', 'ASP', 6.4)], [('ND1', 'HIS', 'CB', 'ASP', 6.66), ('ND1', 'HIS', 'CG', 'ASP', 5.26), ('ND1', 'HIS', 'OD1', 'ASP', 4.81), ('ND1', 'HIS', 'OD2', 'ASP', 5.11)], [('CD2', 'HIS', 'CB', 'ASP', 8.79), ('CD2', 'HIS', 'CG', 'ASP', 7.43), ('CD2', 'HIS', 'OD1', 'ASP', 6.83), ('CD2', 'HIS', 'OD2', 'ASP', 7.25)], [('CE1', 'HIS', 'CB', 'ASP', 7.28), ('CE1', 'HIS', 'CG', 'ASP', 5.97), ('CE1', 'HIS', 'OD1', 'ASP', 5.86), ('CE1', 'HIS', 'OD2', 'ASP', 5.47)], [('NE2', 'HIS', 'CB', 'ASP', 8.53), ('NE2', 'HIS', 'CG', 'ASP', 7.2), ('NE2', 'HIS', 'OD1', 'ASP', 6.92), ('NE2', 'HIS', 'OD2', 'ASP', 6.77)]]}
HIS_GLU = { 
	'distances':
		[[13.39, 12.08, 11.51, 12.26, 10.46], [12.75, 11.36, 10.73, 11.53, 9.6], [13.61, 12.16, 11.48, 12.27, 10.28], [11.51, 10.08, 9.49, 10.33, 8.34], [13.03, 11.54, 10.85, 11.66, 9.62], [11.73, 10.24, 9.59, 10.45, 8.38], [8.12, 9.29, 9.27, 8.47, 10.29], [6.84, 7.97, 7.88, 7.04, 8.94], [6.4, 7.66, 7.73, 6.88, 8.9], [6.26, 7.12, 6.81, 5.94, 7.78], [5.47, 6.59, 6.57, 5.68, 7.75], [5.33, 6.17, 5.84, 4.89, 6.92]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 13.39), ('CB', 'HIS', 'CG', 'GLU', 12.08), ('CB', 'HIS', 'CD', 'GLU', 11.51), ('CB', 'HIS', 'OE1', 'GLU', 12.26), ('CB', 'HIS', 'OE2', 'GLU', 10.46)], [('CG', 'HIS', 'CB', 'GLU', 12.75), ('CG', 'HIS', 'CG', 'GLU', 11.36), ('CG', 'HIS', 'CD', 'GLU', 10.73), ('CG', 'HIS', 'OE1', 'GLU', 11.53), ('CG', 'HIS', 'OE2', 'GLU', 9.6)], [('ND1', 'HIS', 'CB', 'GLU', 13.61), ('ND1', 'HIS', 'CG', 'GLU', 12.16), ('ND1', 'HIS', 'CD', 'GLU', 11.48), ('ND1', 'HIS', 'OE1', 'GLU', 12.27), ('ND1', 'HIS', 'OE2', 'GLU', 10.28)], [('CD2', 'HIS', 'CB', 'GLU', 11.51), ('CD2', 'HIS', 'CG', 'GLU', 10.08), ('CD2', 'HIS', 'CD', 'GLU', 9.49), ('CD2', 'HIS', 'OE1', 'GLU', 10.33), ('CD2', 'HIS', 'OE2', 'GLU', 8.34)], [('CE1', 'HIS', 'CB', 'GLU', 13.03), ('CE1', 'HIS', 'CG', 'GLU', 11.54), ('CE1', 'HIS', 'CD', 'GLU', 10.85), ('CE1', 'HIS', 'OE1', 'GLU', 11.66), ('CE1', 'HIS', 'OE2', 'GLU', 9.62)], [('NE2', 'HIS', 'CB', 'GLU', 11.73), ('NE2', 'HIS', 'CG', 'GLU', 10.24), ('NE2', 'HIS', 'CD', 'GLU', 9.59), ('NE2', 'HIS', 'OE1', 'GLU', 10.45), ('NE2', 'HIS', 'OE2', 'GLU', 8.38)], [('CB', 'HIS', 'CB', 'GLU', 8.12), ('CB', 'HIS', 'CG', 'GLU', 9.29), ('CB', 'HIS', 'CD', 'GLU', 9.27), ('CB', 'HIS', 'OE1', 'GLU', 8.47), ('CB', 'HIS', 'OE2', 'GLU', 10.29)], [('CG', 'HIS', 'CB', 'GLU', 6.84), ('CG', 'HIS', 'CG', 'GLU', 7.97), ('CG', 'HIS', 'CD', 'GLU', 7.88), ('CG', 'HIS', 'OE1', 'GLU', 7.04), ('CG', 'HIS', 'OE2', 'GLU', 8.94)], [('ND1', 'HIS', 'CB', 'GLU', 6.4), ('ND1', 'HIS', 'CG', 'GLU', 7.66), ('ND1', 'HIS', 'CD', 'GLU', 7.73), ('ND1', 'HIS', 'OE1', 'GLU', 6.88), ('ND1', 'HIS', 'OE2', 'GLU', 8.9)], [('CD2', 'HIS', 'CB', 'GLU', 6.26), ('CD2', 'HIS', 'CG', 'GLU', 7.12), ('CD2', 'HIS', 'CD', 'GLU', 6.81), ('CD2', 'HIS', 'OE1', 'GLU', 5.94), ('CD2', 'HIS', 'OE2', 'GLU', 7.78)], [('CE1', 'HIS', 'CB', 'GLU', 5.47), ('CE1', 'HIS', 'CG', 'GLU', 6.59), ('CE1', 'HIS', 'CD', 'GLU', 6.57), ('CE1', 'HIS', 'OE1', 'GLU', 5.68), ('CE1', 'HIS', 'OE2', 'GLU', 7.75)], [('NE2', 'HIS', 'CB', 'GLU', 5.33), ('NE2', 'HIS', 'CG', 'GLU', 6.17), ('NE2', 'HIS', 'CD', 'GLU', 5.84), ('NE2', 'HIS', 'OE1', 'GLU', 4.89), ('NE2', 'HIS', 'OE2', 'GLU', 6.92)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLUI, d, 'P_1b31_3_2_1_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'P_1b31_3_2_1_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ASP, d, 'P_1b31_3_2_1_8')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_ASP, d, 'P_1b31_3_2_1_8')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_GLU, d, 'P_1b31_3_2_1_8')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLUI' :  match1,
		'GLU_GLU' :  match2,
		'GLU_ASP' :  match3,
		'HIS_ASP' :  match4,
		'HIS_GLU' :  match5}