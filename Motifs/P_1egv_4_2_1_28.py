'''
FUNC:P_1egv_4_2_1_28
PDB:1egv
EC:4.2.1.28
RESI:his,glu,gln,asp
LOCI:a-143,170,296,335;
'''
import motifFunctions as cmd
GLU_GLN = { 
	'distances':
		[[11.7, 11.24, 9.9, 9.07, 9.83], [11.45, 10.99, 9.56, 8.84, 9.27], [10.14, 9.6, 8.14, 7.45, 7.83], [9.59, 8.92, 7.49, 6.63, 7.45], [9.83, 9.37, 7.9, 7.42, 7.34]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLN', 11.7), ('CB', 'GLU', 'CG', 'GLN', 11.24), ('CB', 'GLU', 'CD', 'GLN', 9.9), ('CB', 'GLU', 'OE1', 'GLN', 9.07), ('CB', 'GLU', 'NE2', 'GLN', 9.83)], [('CG', 'GLU', 'CB', 'GLN', 11.45), ('CG', 'GLU', 'CG', 'GLN', 10.99), ('CG', 'GLU', 'CD', 'GLN', 9.56), ('CG', 'GLU', 'OE1', 'GLN', 8.84), ('CG', 'GLU', 'NE2', 'GLN', 9.27)], [('CD', 'GLU', 'CB', 'GLN', 10.14), ('CD', 'GLU', 'CG', 'GLN', 9.6), ('CD', 'GLU', 'CD', 'GLN', 8.14), ('CD', 'GLU', 'OE1', 'GLN', 7.45), ('CD', 'GLU', 'NE2', 'GLN', 7.83)], [('OE1', 'GLU', 'CB', 'GLN', 9.59), ('OE1', 'GLU', 'CG', 'GLN', 8.92), ('OE1', 'GLU', 'CD', 'GLN', 7.49), ('OE1', 'GLU', 'OE1', 'GLN', 6.63), ('OE1', 'GLU', 'NE2', 'GLN', 7.45)], [('OE2', 'GLU', 'CB', 'GLN', 9.83), ('OE2', 'GLU', 'CG', 'GLN', 9.37), ('OE2', 'GLU', 'CD', 'GLN', 7.9), ('OE2', 'GLU', 'OE1', 'GLN', 7.42), ('OE2', 'GLU', 'NE2', 'GLN', 7.34)]]}
HIS_ASP = { 
	'distances':
		[[8.92, 10.02, 11.1, 9.98], [7.61, 8.61, 9.71, 8.52], [6.91, 7.91, 8.9, 7.98], [7.18, 8.0, 9.19, 7.71], [5.91, 6.72, 7.74, 6.7], [6.08, 6.76, 7.92, 6.46]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 8.92), ('CB', 'HIS', 'CG', 'ASP', 10.02), ('CB', 'HIS', 'OD1', 'ASP', 11.1), ('CB', 'HIS', 'OD2', 'ASP', 9.98)], [('CG', 'HIS', 'CB', 'ASP', 7.61), ('CG', 'HIS', 'CG', 'ASP', 8.61), ('CG', 'HIS', 'OD1', 'ASP', 9.71), ('CG', 'HIS', 'OD2', 'ASP', 8.52)], [('ND1', 'HIS', 'CB', 'ASP', 6.91), ('ND1', 'HIS', 'CG', 'ASP', 7.91), ('ND1', 'HIS', 'OD1', 'ASP', 8.9), ('ND1', 'HIS', 'OD2', 'ASP', 7.98)], [('CD2', 'HIS', 'CB', 'ASP', 7.18), ('CD2', 'HIS', 'CG', 'ASP', 8.0), ('CD2', 'HIS', 'OD1', 'ASP', 9.19), ('CD2', 'HIS', 'OD2', 'ASP', 7.71)], [('CE1', 'HIS', 'CB', 'ASP', 5.91), ('CE1', 'HIS', 'CG', 'ASP', 6.72), ('CE1', 'HIS', 'OD1', 'ASP', 7.74), ('CE1', 'HIS', 'OD2', 'ASP', 6.7)], [('NE2', 'HIS', 'CB', 'ASP', 6.08), ('NE2', 'HIS', 'CG', 'ASP', 6.76), ('NE2', 'HIS', 'OD1', 'ASP', 7.92), ('NE2', 'HIS', 'OD2', 'ASP', 6.46)]]}
HIS_GLU = { 
	'distances':
		[[7.25, 7.61, 7.91, 7.46, 8.9], [7.05, 7.22, 7.14, 6.53, 8.04], [8.27, 8.27, 7.95, 7.29, 8.68], [6.17, 6.27, 5.96, 5.23, 6.88], [8.28, 8.14, 7.51, 6.75, 8.11], [7.13, 7.0, 6.29, 5.45, 6.97]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 7.25), ('CB', 'HIS', 'CG', 'GLU', 7.61), ('CB', 'HIS', 'CD', 'GLU', 7.91), ('CB', 'HIS', 'OE1', 'GLU', 7.46), ('CB', 'HIS', 'OE2', 'GLU', 8.9)], [('CG', 'HIS', 'CB', 'GLU', 7.05), ('CG', 'HIS', 'CG', 'GLU', 7.22), ('CG', 'HIS', 'CD', 'GLU', 7.14), ('CG', 'HIS', 'OE1', 'GLU', 6.53), ('CG', 'HIS', 'OE2', 'GLU', 8.04)], [('ND1', 'HIS', 'CB', 'GLU', 8.27), ('ND1', 'HIS', 'CG', 'GLU', 8.27), ('ND1', 'HIS', 'CD', 'GLU', 7.95), ('ND1', 'HIS', 'OE1', 'GLU', 7.29), ('ND1', 'HIS', 'OE2', 'GLU', 8.68)], [('CD2', 'HIS', 'CB', 'GLU', 6.17), ('CD2', 'HIS', 'CG', 'GLU', 6.27), ('CD2', 'HIS', 'CD', 'GLU', 5.96), ('CD2', 'HIS', 'OE1', 'GLU', 5.23), ('CD2', 'HIS', 'OE2', 'GLU', 6.88)], [('CE1', 'HIS', 'CB', 'GLU', 8.28), ('CE1', 'HIS', 'CG', 'GLU', 8.14), ('CE1', 'HIS', 'CD', 'GLU', 7.51), ('CE1', 'HIS', 'OE1', 'GLU', 6.75), ('CE1', 'HIS', 'OE2', 'GLU', 8.11)], [('NE2', 'HIS', 'CB', 'GLU', 7.13), ('NE2', 'HIS', 'CG', 'GLU', 7.0), ('NE2', 'HIS', 'CD', 'GLU', 6.29), ('NE2', 'HIS', 'OE1', 'GLU', 5.45), ('NE2', 'HIS', 'OE2', 'GLU', 6.97)]]}
GLN_ASP = { 
	'distances':
		[[10.22, 9.26, 9.66, 8.32], [8.75, 7.74, 8.13, 6.82], [8.13, 7.23, 7.87, 6.13], [7.11, 6.42, 7.24, 5.35], [9.07, 8.14, 8.8, 6.95]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASP', 10.22), ('CB', 'GLN', 'CG', 'ASP', 9.26), ('CB', 'GLN', 'OD1', 'ASP', 9.66), ('CB', 'GLN', 'OD2', 'ASP', 8.32)], [('CG', 'GLN', 'CB', 'ASP', 8.75), ('CG', 'GLN', 'CG', 'ASP', 7.74), ('CG', 'GLN', 'OD1', 'ASP', 8.13), ('CG', 'GLN', 'OD2', 'ASP', 6.82)], [('CD', 'GLN', 'CB', 'ASP', 8.13), ('CD', 'GLN', 'CG', 'ASP', 7.23), ('CD', 'GLN', 'OD1', 'ASP', 7.87), ('CD', 'GLN', 'OD2', 'ASP', 6.13)], [('OE1', 'GLN', 'CB', 'ASP', 7.11), ('OE1', 'GLN', 'CG', 'ASP', 6.42), ('OE1', 'GLN', 'OD1', 'ASP', 7.24), ('OE1', 'GLN', 'OD2', 'ASP', 5.35)], [('NE2', 'GLN', 'CB', 'ASP', 9.07), ('NE2', 'GLN', 'CG', 'ASP', 8.14), ('NE2', 'GLN', 'OD1', 'ASP', 8.8), ('NE2', 'GLN', 'OD2', 'ASP', 6.95)]]}
HIS_GLN = { 
	'distances':
		[[14.35, 13.31, 12.03, 10.89, 12.34], [13.08, 11.97, 10.7, 9.56, 11.03], [13.18, 11.95, 10.73, 9.61, 11.12], [11.81, 10.77, 9.46, 8.34, 9.76], [12.03, 10.75, 9.56, 8.47, 9.96], [11.11, 9.94, 8.66, 7.55, 9.01]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 14.35), ('CB', 'HIS', 'CG', 'GLN', 13.31), ('CB', 'HIS', 'CD', 'GLN', 12.03), ('CB', 'HIS', 'OE1', 'GLN', 10.89), ('CB', 'HIS', 'NE2', 'GLN', 12.34)], [('CG', 'HIS', 'CB', 'GLN', 13.08), ('CG', 'HIS', 'CG', 'GLN', 11.97), ('CG', 'HIS', 'CD', 'GLN', 10.7), ('CG', 'HIS', 'OE1', 'GLN', 9.56), ('CG', 'HIS', 'NE2', 'GLN', 11.03)], [('ND1', 'HIS', 'CB', 'GLN', 13.18), ('ND1', 'HIS', 'CG', 'GLN', 11.95), ('ND1', 'HIS', 'CD', 'GLN', 10.73), ('ND1', 'HIS', 'OE1', 'GLN', 9.61), ('ND1', 'HIS', 'NE2', 'GLN', 11.12)], [('CD2', 'HIS', 'CB', 'GLN', 11.81), ('CD2', 'HIS', 'CG', 'GLN', 10.77), ('CD2', 'HIS', 'CD', 'GLN', 9.46), ('CD2', 'HIS', 'OE1', 'GLN', 8.34), ('CD2', 'HIS', 'NE2', 'GLN', 9.76)], [('CE1', 'HIS', 'CB', 'GLN', 12.03), ('CE1', 'HIS', 'CG', 'GLN', 10.75), ('CE1', 'HIS', 'CD', 'GLN', 9.56), ('CE1', 'HIS', 'OE1', 'GLN', 8.47), ('CE1', 'HIS', 'NE2', 'GLN', 9.96)], [('NE2', 'HIS', 'CB', 'GLN', 11.11), ('NE2', 'HIS', 'CG', 'GLN', 9.94), ('NE2', 'HIS', 'CD', 'GLN', 8.66), ('NE2', 'HIS', 'OE1', 'GLN', 7.55), ('NE2', 'HIS', 'NE2', 'GLN', 9.01)]]}
GLU_ASP = { 
	'distances':
		[[10.47, 10.98, 12.23, 10.3], [10.54, 10.87, 12.08, 10.06], [9.5, 9.64, 10.83, 8.74], [8.39, 8.61, 9.83, 7.77], [9.96, 9.88, 11.0, 8.86]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 10.47), ('CB', 'GLU', 'CG', 'ASP', 10.98), ('CB', 'GLU', 'OD1', 'ASP', 12.23), ('CB', 'GLU', 'OD2', 'ASP', 10.3)], [('CG', 'GLU', 'CB', 'ASP', 10.54), ('CG', 'GLU', 'CG', 'ASP', 10.87), ('CG', 'GLU', 'OD1', 'ASP', 12.08), ('CG', 'GLU', 'OD2', 'ASP', 10.06)], [('CD', 'GLU', 'CB', 'ASP', 9.5), ('CD', 'GLU', 'CG', 'ASP', 9.64), ('CD', 'GLU', 'OD1', 'ASP', 10.83), ('CD', 'GLU', 'OD2', 'ASP', 8.74)], [('OE1', 'GLU', 'CB', 'ASP', 8.39), ('OE1', 'GLU', 'CG', 'ASP', 8.61), ('OE1', 'GLU', 'OD1', 'ASP', 9.83), ('OE1', 'GLU', 'OD2', 'ASP', 7.77)], [('OE2', 'GLU', 'CB', 'ASP', 9.96), ('OE2', 'GLU', 'CG', 'ASP', 9.88), ('OE2', 'GLU', 'OD1', 'ASP', 11.0), ('OE2', 'GLU', 'OD2', 'ASP', 8.86)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLN, d, 'P_1egv_4_2_1_28')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1egv_4_2_1_28')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_GLU, d, 'P_1egv_4_2_1_28')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLN_ASP, d, 'P_1egv_4_2_1_28')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_GLN, d, 'P_1egv_4_2_1_28')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_ASP, d, 'P_1egv_4_2_1_28')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLN' :  match1,
		'HIS_ASP' :  match2,
		'HIS_GLU' :  match3,
		'GLN_ASP' :  match4,
		'HIS_GLN' :  match5,
		'GLU_ASP' :  match6}