'''
FUNC:P_6enl_4_2_1_11
PDB:6enl
EC:4.2.1.11
RESI:glu,glu,his,lys
LOCI:a-168,211,373,396;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[10.66, 9.36, 9.0, 7.72, 7.73], [10.52, 9.09, 8.65, 7.21, 7.18], [9.36, 7.9, 7.34, 5.85, 5.83], [8.2, 6.78, 6.27, 4.86, 5.06], [9.69, 8.2, 7.53, 5.99, 5.81], [11.26, 10.13, 10.81, 9.97, 11.03], [10.9, 9.7, 10.22, 9.34, 10.32], [9.96, 8.65, 8.98, 7.98, 8.87], [9.19, 7.83, 8.19, 7.16, 8.12], [10.29, 8.95, 9.09, 8.05, 8.76]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 10.66), ('CB', 'GLU', 'CG', 'LYS', 9.36), ('CB', 'GLU', 'CD', 'LYS', 9.0), ('CB', 'GLU', 'CE', 'LYS', 7.72), ('CB', 'GLU', 'NZ', 'LYS', 7.73)], [('CG', 'GLU', 'CB', 'LYS', 10.52), ('CG', 'GLU', 'CG', 'LYS', 9.09), ('CG', 'GLU', 'CD', 'LYS', 8.65), ('CG', 'GLU', 'CE', 'LYS', 7.21), ('CG', 'GLU', 'NZ', 'LYS', 7.18)], [('CD', 'GLU', 'CB', 'LYS', 9.36), ('CD', 'GLU', 'CG', 'LYS', 7.9), ('CD', 'GLU', 'CD', 'LYS', 7.34), ('CD', 'GLU', 'CE', 'LYS', 5.85), ('CD', 'GLU', 'NZ', 'LYS', 5.83)], [('OE1', 'GLU', 'CB', 'LYS', 8.2), ('OE1', 'GLU', 'CG', 'LYS', 6.78), ('OE1', 'GLU', 'CD', 'LYS', 6.27), ('OE1', 'GLU', 'CE', 'LYS', 4.86), ('OE1', 'GLU', 'NZ', 'LYS', 5.06)], [('OE2', 'GLU', 'CB', 'LYS', 9.69), ('OE2', 'GLU', 'CG', 'LYS', 8.2), ('OE2', 'GLU', 'CD', 'LYS', 7.53), ('OE2', 'GLU', 'CE', 'LYS', 5.99), ('OE2', 'GLU', 'NZ', 'LYS', 5.81)], [('CB', 'GLU', 'CB', 'LYS', 11.26), ('CB', 'GLU', 'CG', 'LYS', 10.13), ('CB', 'GLU', 'CD', 'LYS', 10.81), ('CB', 'GLU', 'CE', 'LYS', 9.97), ('CB', 'GLU', 'NZ', 'LYS', 11.03)], [('CG', 'GLU', 'CB', 'LYS', 10.9), ('CG', 'GLU', 'CG', 'LYS', 9.7), ('CG', 'GLU', 'CD', 'LYS', 10.22), ('CG', 'GLU', 'CE', 'LYS', 9.34), ('CG', 'GLU', 'NZ', 'LYS', 10.32)], [('CD', 'GLU', 'CB', 'LYS', 9.96), ('CD', 'GLU', 'CG', 'LYS', 8.65), ('CD', 'GLU', 'CD', 'LYS', 8.98), ('CD', 'GLU', 'CE', 'LYS', 7.98), ('CD', 'GLU', 'NZ', 'LYS', 8.87)], [('OE1', 'GLU', 'CB', 'LYS', 9.19), ('OE1', 'GLU', 'CG', 'LYS', 7.83), ('OE1', 'GLU', 'CD', 'LYS', 8.19), ('OE1', 'GLU', 'CE', 'LYS', 7.16), ('OE1', 'GLU', 'NZ', 'LYS', 8.12)], [('OE2', 'GLU', 'CB', 'LYS', 10.29), ('OE2', 'GLU', 'CG', 'LYS', 8.95), ('OE2', 'GLU', 'CD', 'LYS', 9.09), ('OE2', 'GLU', 'CE', 'LYS', 8.05), ('OE2', 'GLU', 'NZ', 'LYS', 8.76)]]}
GLU_GLU = { 
	'distances':
		[[9.83, 9.88, 8.76, 7.75, 9.23], [9.11, 8.92, 7.71, 6.84, 8.0], [8.91, 8.49, 7.11, 6.24, 7.26], [9.08, 8.71, 7.34, 6.32, 7.61], [8.95, 8.27, 6.83, 6.22, 6.68], [9.83, 9.11, 8.91, 9.08, 8.95], [9.88, 8.92, 8.49, 8.71, 8.27], [8.76, 7.71, 7.11, 7.34, 6.83], [7.75, 6.84, 6.24, 6.32, 6.22], [9.23, 8.0, 7.26, 7.61, 6.68]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 9.83), ('CB', 'GLU', 'CG', 'GLU', 9.88), ('CB', 'GLU', 'CD', 'GLU', 8.76), ('CB', 'GLU', 'OE1', 'GLU', 7.75), ('CB', 'GLU', 'OE2', 'GLU', 9.23)], [('CG', 'GLU', 'CB', 'GLU', 9.11), ('CG', 'GLU', 'CG', 'GLU', 8.92), ('CG', 'GLU', 'CD', 'GLU', 7.71), ('CG', 'GLU', 'OE1', 'GLU', 6.84), ('CG', 'GLU', 'OE2', 'GLU', 8.0)], [('CD', 'GLU', 'CB', 'GLU', 8.91), ('CD', 'GLU', 'CG', 'GLU', 8.49), ('CD', 'GLU', 'CD', 'GLU', 7.11), ('CD', 'GLU', 'OE1', 'GLU', 6.24), ('CD', 'GLU', 'OE2', 'GLU', 7.26)], [('OE1', 'GLU', 'CB', 'GLU', 9.08), ('OE1', 'GLU', 'CG', 'GLU', 8.71), ('OE1', 'GLU', 'CD', 'GLU', 7.34), ('OE1', 'GLU', 'OE1', 'GLU', 6.32), ('OE1', 'GLU', 'OE2', 'GLU', 7.61)], [('OE2', 'GLU', 'CB', 'GLU', 8.95), ('OE2', 'GLU', 'CG', 'GLU', 8.27), ('OE2', 'GLU', 'CD', 'GLU', 6.83), ('OE2', 'GLU', 'OE1', 'GLU', 6.22), ('OE2', 'GLU', 'OE2', 'GLU', 6.68)], [('CB', 'GLU', 'CB', 'GLU', 9.83), ('CB', 'GLU', 'CG', 'GLU', 9.11), ('CB', 'GLU', 'CD', 'GLU', 8.91), ('CB', 'GLU', 'OE1', 'GLU', 9.08), ('CB', 'GLU', 'OE2', 'GLU', 8.95)], [('CG', 'GLU', 'CB', 'GLU', 9.88), ('CG', 'GLU', 'CG', 'GLU', 8.92), ('CG', 'GLU', 'CD', 'GLU', 8.49), ('CG', 'GLU', 'OE1', 'GLU', 8.71), ('CG', 'GLU', 'OE2', 'GLU', 8.27)], [('CD', 'GLU', 'CB', 'GLU', 8.76), ('CD', 'GLU', 'CG', 'GLU', 7.71), ('CD', 'GLU', 'CD', 'GLU', 7.11), ('CD', 'GLU', 'OE1', 'GLU', 7.34), ('CD', 'GLU', 'OE2', 'GLU', 6.83)], [('OE1', 'GLU', 'CB', 'GLU', 7.75), ('OE1', 'GLU', 'CG', 'GLU', 6.84), ('OE1', 'GLU', 'CD', 'GLU', 6.24), ('OE1', 'GLU', 'OE1', 'GLU', 6.32), ('OE1', 'GLU', 'OE2', 'GLU', 6.22)], [('OE2', 'GLU', 'CB', 'GLU', 9.23), ('OE2', 'GLU', 'CG', 'GLU', 8.0), ('OE2', 'GLU', 'CD', 'GLU', 7.26), ('OE2', 'GLU', 'OE1', 'GLU', 7.61), ('OE2', 'GLU', 'OE2', 'GLU', 6.68)]]}
HIS_GLUI = { 
	'distances':
		[[9.42, 8.52, 8.32, 8.62, 8.2], [8.16, 7.27, 6.96, 7.16, 6.94], [6.97, 6.26, 6.24, 6.49, 6.49], [8.09, 7.12, 6.43, 6.45, 6.34], [6.08, 5.4, 5.14, 5.21, 5.59], [6.87, 6.01, 5.25, 5.13, 5.43]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLUI', 9.42), ('CB', 'HIS', 'CG', 'GLUI', 8.52), ('CB', 'HIS', 'CD', 'GLUI', 8.32), ('CB', 'HIS', 'OE1', 'GLUI', 8.62), ('CB', 'HIS', 'OE2', 'GLUI', 8.2)], [('CG', 'HIS', 'CB', 'GLUI', 8.16), ('CG', 'HIS', 'CG', 'GLUI', 7.27), ('CG', 'HIS', 'CD', 'GLUI', 6.96), ('CG', 'HIS', 'OE1', 'GLUI', 7.16), ('CG', 'HIS', 'OE2', 'GLUI', 6.94)], [('ND1', 'HIS', 'CB', 'GLUI', 6.97), ('ND1', 'HIS', 'CG', 'GLUI', 6.26), ('ND1', 'HIS', 'CD', 'GLUI', 6.24), ('ND1', 'HIS', 'OE1', 'GLUI', 6.49), ('ND1', 'HIS', 'OE2', 'GLUI', 6.49)], [('CD2', 'HIS', 'CB', 'GLUI', 8.09), ('CD2', 'HIS', 'CG', 'GLUI', 7.12), ('CD2', 'HIS', 'CD', 'GLUI', 6.43), ('CD2', 'HIS', 'OE1', 'GLUI', 6.45), ('CD2', 'HIS', 'OE2', 'GLUI', 6.34)], [('CE1', 'HIS', 'CB', 'GLUI', 6.08), ('CE1', 'HIS', 'CG', 'GLUI', 5.4), ('CE1', 'HIS', 'CD', 'GLUI', 5.14), ('CE1', 'HIS', 'OE1', 'GLUI', 5.21), ('CE1', 'HIS', 'OE2', 'GLUI', 5.59)], [('NE2', 'HIS', 'CB', 'GLUI', 6.87), ('NE2', 'HIS', 'CG', 'GLUI', 6.01), ('NE2', 'HIS', 'CD', 'GLUI', 5.25), ('NE2', 'HIS', 'OE1', 'GLUI', 5.13), ('NE2', 'HIS', 'OE2', 'GLUI', 5.43)]]}
GLU_HIS = { 
	'distances':
		[[13.48, 12.05, 11.73, 10.94, 10.44, 9.86], [12.62, 11.2, 10.93, 10.06, 9.65, 9.01], [11.41, 10.03, 9.92, 8.82, 8.71, 7.89], [10.92, 9.56, 9.52, 8.34, 8.34, 7.47], [11.05, 9.73, 9.72, 8.5, 8.59, 7.69], [9.42, 8.16, 6.97, 8.09, 6.08, 6.87], [8.52, 7.27, 6.26, 7.12, 5.4, 6.01], [8.32, 6.96, 6.24, 6.43, 5.14, 5.25], [8.62, 7.16, 6.49, 6.45, 5.21, 5.13], [8.2, 6.94, 6.49, 6.34, 5.59, 5.43]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 13.48), ('CB', 'GLU', 'CG', 'HIS', 12.05), ('CB', 'GLU', 'ND1', 'HIS', 11.73), ('CB', 'GLU', 'CD2', 'HIS', 10.94), ('CB', 'GLU', 'CE1', 'HIS', 10.44), ('CB', 'GLU', 'NE2', 'HIS', 9.86)], [('CG', 'GLU', 'CB', 'HIS', 12.62), ('CG', 'GLU', 'CG', 'HIS', 11.2), ('CG', 'GLU', 'ND1', 'HIS', 10.93), ('CG', 'GLU', 'CD2', 'HIS', 10.06), ('CG', 'GLU', 'CE1', 'HIS', 9.65), ('CG', 'GLU', 'NE2', 'HIS', 9.01)], [('CD', 'GLU', 'CB', 'HIS', 11.41), ('CD', 'GLU', 'CG', 'HIS', 10.03), ('CD', 'GLU', 'ND1', 'HIS', 9.92), ('CD', 'GLU', 'CD2', 'HIS', 8.82), ('CD', 'GLU', 'CE1', 'HIS', 8.71), ('CD', 'GLU', 'NE2', 'HIS', 7.89)], [('OE1', 'GLU', 'CB', 'HIS', 10.92), ('OE1', 'GLU', 'CG', 'HIS', 9.56), ('OE1', 'GLU', 'ND1', 'HIS', 9.52), ('OE1', 'GLU', 'CD2', 'HIS', 8.34), ('OE1', 'GLU', 'CE1', 'HIS', 8.34), ('OE1', 'GLU', 'NE2', 'HIS', 7.47)], [('OE2', 'GLU', 'CB', 'HIS', 11.05), ('OE2', 'GLU', 'CG', 'HIS', 9.73), ('OE2', 'GLU', 'ND1', 'HIS', 9.72), ('OE2', 'GLU', 'CD2', 'HIS', 8.5), ('OE2', 'GLU', 'CE1', 'HIS', 8.59), ('OE2', 'GLU', 'NE2', 'HIS', 7.69)], [('CB', 'GLU', 'CB', 'HIS', 9.42), ('CB', 'GLU', 'CG', 'HIS', 8.16), ('CB', 'GLU', 'ND1', 'HIS', 6.97), ('CB', 'GLU', 'CD2', 'HIS', 8.09), ('CB', 'GLU', 'CE1', 'HIS', 6.08), ('CB', 'GLU', 'NE2', 'HIS', 6.87)], [('CG', 'GLU', 'CB', 'HIS', 8.52), ('CG', 'GLU', 'CG', 'HIS', 7.27), ('CG', 'GLU', 'ND1', 'HIS', 6.26), ('CG', 'GLU', 'CD2', 'HIS', 7.12), ('CG', 'GLU', 'CE1', 'HIS', 5.4), ('CG', 'GLU', 'NE2', 'HIS', 6.01)], [('CD', 'GLU', 'CB', 'HIS', 8.32), ('CD', 'GLU', 'CG', 'HIS', 6.96), ('CD', 'GLU', 'ND1', 'HIS', 6.24), ('CD', 'GLU', 'CD2', 'HIS', 6.43), ('CD', 'GLU', 'CE1', 'HIS', 5.14), ('CD', 'GLU', 'NE2', 'HIS', 5.25)], [('OE1', 'GLU', 'CB', 'HIS', 8.62), ('OE1', 'GLU', 'CG', 'HIS', 7.16), ('OE1', 'GLU', 'ND1', 'HIS', 6.49), ('OE1', 'GLU', 'CD2', 'HIS', 6.45), ('OE1', 'GLU', 'CE1', 'HIS', 5.21), ('OE1', 'GLU', 'NE2', 'HIS', 5.13)], [('OE2', 'GLU', 'CB', 'HIS', 8.2), ('OE2', 'GLU', 'CG', 'HIS', 6.94), ('OE2', 'GLU', 'ND1', 'HIS', 6.49), ('OE2', 'GLU', 'CD2', 'HIS', 6.34), ('OE2', 'GLU', 'CE1', 'HIS', 5.59), ('OE2', 'GLU', 'NE2', 'HIS', 5.43)]]}
HIS_LYS = { 
	'distances':
		[[8.43, 8.13, 8.86, 9.16, 10.25], [7.78, 7.21, 7.95, 8.05, 9.21], [8.32, 7.65, 8.54, 8.46, 9.72], [7.08, 6.26, 6.81, 6.76, 7.88], [8.02, 7.1, 7.93, 7.63, 8.89], [7.26, 6.2, 6.81, 6.46, 7.67]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 8.43), ('CB', 'HIS', 'CG', 'LYS', 8.13), ('CB', 'HIS', 'CD', 'LYS', 8.86), ('CB', 'HIS', 'CE', 'LYS', 9.16), ('CB', 'HIS', 'NZ', 'LYS', 10.25)], [('CG', 'HIS', 'CB', 'LYS', 7.78), ('CG', 'HIS', 'CG', 'LYS', 7.21), ('CG', 'HIS', 'CD', 'LYS', 7.95), ('CG', 'HIS', 'CE', 'LYS', 8.05), ('CG', 'HIS', 'NZ', 'LYS', 9.21)], [('ND1', 'HIS', 'CB', 'LYS', 8.32), ('ND1', 'HIS', 'CG', 'LYS', 7.65), ('ND1', 'HIS', 'CD', 'LYS', 8.54), ('ND1', 'HIS', 'CE', 'LYS', 8.46), ('ND1', 'HIS', 'NZ', 'LYS', 9.72)], [('CD2', 'HIS', 'CB', 'LYS', 7.08), ('CD2', 'HIS', 'CG', 'LYS', 6.26), ('CD2', 'HIS', 'CD', 'LYS', 6.81), ('CD2', 'HIS', 'CE', 'LYS', 6.76), ('CD2', 'HIS', 'NZ', 'LYS', 7.88)], [('CE1', 'HIS', 'CB', 'LYS', 8.02), ('CE1', 'HIS', 'CG', 'LYS', 7.1), ('CE1', 'HIS', 'CD', 'LYS', 7.93), ('CE1', 'HIS', 'CE', 'LYS', 7.63), ('CE1', 'HIS', 'NZ', 'LYS', 8.89)], [('NE2', 'HIS', 'CB', 'LYS', 7.26), ('NE2', 'HIS', 'CG', 'LYS', 6.2), ('NE2', 'HIS', 'CD', 'LYS', 6.81), ('NE2', 'HIS', 'CE', 'LYS', 6.46), ('NE2', 'HIS', 'NZ', 'LYS', 7.67)]]}
LYS_GLUI = { 
	'distances':
		[[11.26, 10.9, 9.96, 9.19, 10.29], [10.13, 9.7, 8.65, 7.83, 8.95], [10.81, 10.22, 8.98, 8.19, 9.09], [9.97, 9.34, 7.98, 7.16, 8.05], [11.03, 10.32, 8.87, 8.12, 8.76]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLUI', 11.26), ('CB', 'LYS', 'CG', 'GLUI', 10.9), ('CB', 'LYS', 'CD', 'GLUI', 9.96), ('CB', 'LYS', 'OE1', 'GLUI', 9.19), ('CB', 'LYS', 'OE2', 'GLUI', 10.29)], [('CG', 'LYS', 'CB', 'GLUI', 10.13), ('CG', 'LYS', 'CG', 'GLUI', 9.7), ('CG', 'LYS', 'CD', 'GLUI', 8.65), ('CG', 'LYS', 'OE1', 'GLUI', 7.83), ('CG', 'LYS', 'OE2', 'GLUI', 8.95)], [('CD', 'LYS', 'CB', 'GLUI', 10.81), ('CD', 'LYS', 'CG', 'GLUI', 10.22), ('CD', 'LYS', 'CD', 'GLUI', 8.98), ('CD', 'LYS', 'OE1', 'GLUI', 8.19), ('CD', 'LYS', 'OE2', 'GLUI', 9.09)], [('CE', 'LYS', 'CB', 'GLUI', 9.97), ('CE', 'LYS', 'CG', 'GLUI', 9.34), ('CE', 'LYS', 'CD', 'GLUI', 7.98), ('CE', 'LYS', 'OE1', 'GLUI', 7.16), ('CE', 'LYS', 'OE2', 'GLUI', 8.05)], [('NZ', 'LYS', 'CB', 'GLUI', 11.03), ('NZ', 'LYS', 'CG', 'GLUI', 10.32), ('NZ', 'LYS', 'CD', 'GLUI', 8.87), ('NZ', 'LYS', 'OE1', 'GLUI', 8.12), ('NZ', 'LYS', 'OE2', 'GLUI', 8.76)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'P_6enl_4_2_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'P_6enl_4_2_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_GLUI, d, 'P_6enl_4_2_1_11')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_HIS, d, 'P_6enl_4_2_1_11')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_LYS, d, 'P_6enl_4_2_1_11')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_GLUI, d, 'P_6enl_4_2_1_11')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'GLU_GLU' :  match2,
		'HIS_GLUI' :  match3,
		'GLU_HIS' :  match4,
		'HIS_LYS' :  match5,
		'LYS_GLUI' :  match6}