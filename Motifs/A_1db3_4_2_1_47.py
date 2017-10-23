'''
FUNC:A_1db3_4_2_1_47
PDB:1db3
EC:4.2.1.47
RESI:thr,glu,tyr,lys
LOCI:a-132,134,156,160;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[8.88, 8.68, 9.88, 9.9, 11.25], [9.89, 9.46, 10.5, 10.44, 11.68], [10.05, 9.39, 10.4, 10.53, 11.73], [9.21, 8.4, 9.35, 9.59, 10.76], [11.2, 10.51, 11.52, 11.71, 12.88]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 8.88), ('CB', 'GLU', 'CG', 'LYS', 8.68), ('CB', 'GLU', 'CD', 'LYS', 9.88), ('CB', 'GLU', 'CE', 'LYS', 9.9), ('CB', 'GLU', 'NZ', 'LYS', 11.25)], [('CG', 'GLU', 'CB', 'LYS', 9.89), ('CG', 'GLU', 'CG', 'LYS', 9.46), ('CG', 'GLU', 'CD', 'LYS', 10.5), ('CG', 'GLU', 'CE', 'LYS', 10.44), ('CG', 'GLU', 'NZ', 'LYS', 11.68)], [('CD', 'GLU', 'CB', 'LYS', 10.05), ('CD', 'GLU', 'CG', 'LYS', 9.39), ('CD', 'GLU', 'CD', 'LYS', 10.4), ('CD', 'GLU', 'CE', 'LYS', 10.53), ('CD', 'GLU', 'NZ', 'LYS', 11.73)], [('OE1', 'GLU', 'CB', 'LYS', 9.21), ('OE1', 'GLU', 'CG', 'LYS', 8.4), ('OE1', 'GLU', 'CD', 'LYS', 9.35), ('OE1', 'GLU', 'CE', 'LYS', 9.59), ('OE1', 'GLU', 'NZ', 'LYS', 10.76)], [('OE2', 'GLU', 'CB', 'LYS', 11.2), ('OE2', 'GLU', 'CG', 'LYS', 10.51), ('OE2', 'GLU', 'CD', 'LYS', 11.52), ('OE2', 'GLU', 'CE', 'LYS', 11.71), ('OE2', 'GLU', 'NZ', 'LYS', 12.88)]]}
GLU_TYR = { 
	'distances':
		[[9.31, 8.58, 9.47, 7.21, 9.24, 6.86, 8.02, 8.16], [9.62, 8.81, 9.64, 7.44, 9.33, 6.99, 8.08, 8.15], [8.58, 7.85, 8.74, 6.55, 8.58, 6.31, 7.46, 7.76], [7.53, 6.68, 7.51, 5.39, 7.34, 5.1, 6.26, 6.68], [9.01, 8.47, 9.42, 7.29, 9.39, 7.24, 8.38, 8.77]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 9.31), ('CB', 'GLU', 'CG', 'TYR', 8.58), ('CB', 'GLU', 'CD1', 'TYR', 9.47), ('CB', 'GLU', 'CD2', 'TYR', 7.21), ('CB', 'GLU', 'CE1', 'TYR', 9.24), ('CB', 'GLU', 'CE2', 'TYR', 6.86), ('CB', 'GLU', 'CZ', 'TYR', 8.02), ('CB', 'GLU', 'OH', 'TYR', 8.16)], [('CG', 'GLU', 'CB', 'TYR', 9.62), ('CG', 'GLU', 'CG', 'TYR', 8.81), ('CG', 'GLU', 'CD1', 'TYR', 9.64), ('CG', 'GLU', 'CD2', 'TYR', 7.44), ('CG', 'GLU', 'CE1', 'TYR', 9.33), ('CG', 'GLU', 'CE2', 'TYR', 6.99), ('CG', 'GLU', 'CZ', 'TYR', 8.08), ('CG', 'GLU', 'OH', 'TYR', 8.15)], [('CD', 'GLU', 'CB', 'TYR', 8.58), ('CD', 'GLU', 'CG', 'TYR', 7.85), ('CD', 'GLU', 'CD1', 'TYR', 8.74), ('CD', 'GLU', 'CD2', 'TYR', 6.55), ('CD', 'GLU', 'CE1', 'TYR', 8.58), ('CD', 'GLU', 'CE2', 'TYR', 6.31), ('CD', 'GLU', 'CZ', 'TYR', 7.46), ('CD', 'GLU', 'OH', 'TYR', 7.76)], [('OE1', 'GLU', 'CB', 'TYR', 7.53), ('OE1', 'GLU', 'CG', 'TYR', 6.68), ('OE1', 'GLU', 'CD1', 'TYR', 7.51), ('OE1', 'GLU', 'CD2', 'TYR', 5.39), ('OE1', 'GLU', 'CE1', 'TYR', 7.34), ('OE1', 'GLU', 'CE2', 'TYR', 5.1), ('OE1', 'GLU', 'CZ', 'TYR', 6.26), ('OE1', 'GLU', 'OH', 'TYR', 6.68)], [('OE2', 'GLU', 'CB', 'TYR', 9.01), ('OE2', 'GLU', 'CG', 'TYR', 8.47), ('OE2', 'GLU', 'CD1', 'TYR', 9.42), ('OE2', 'GLU', 'CD2', 'TYR', 7.29), ('OE2', 'GLU', 'CE1', 'TYR', 9.39), ('OE2', 'GLU', 'CE2', 'TYR', 7.24), ('OE2', 'GLU', 'CZ', 'TYR', 8.38), ('OE2', 'GLU', 'OH', 'TYR', 8.77)]]}
LYS_TYR = { 
	'distances':
		[[8.6, 7.76, 7.73, 7.41, 7.36, 7.02, 6.99, 7.09], [7.61, 6.56, 6.33, 6.31, 5.83, 5.81, 5.54, 5.72], [8.44, 7.29, 6.65, 7.24, 5.87, 6.57, 5.83, 5.68], [9.65, 8.37, 7.74, 8.08, 6.7, 7.12, 6.35, 5.7], [10.65, 9.35, 8.51, 9.21, 7.38, 8.24, 7.24, 6.46]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 8.6), ('CB', 'LYS', 'CG', 'TYR', 7.76), ('CB', 'LYS', 'CD1', 'TYR', 7.73), ('CB', 'LYS', 'CD2', 'TYR', 7.41), ('CB', 'LYS', 'CE1', 'TYR', 7.36), ('CB', 'LYS', 'CE2', 'TYR', 7.02), ('CB', 'LYS', 'CZ', 'TYR', 6.99), ('CB', 'LYS', 'OH', 'TYR', 7.09)], [('CG', 'LYS', 'CB', 'TYR', 7.61), ('CG', 'LYS', 'CG', 'TYR', 6.56), ('CG', 'LYS', 'CD1', 'TYR', 6.33), ('CG', 'LYS', 'CD2', 'TYR', 6.31), ('CG', 'LYS', 'CE1', 'TYR', 5.83), ('CG', 'LYS', 'CE2', 'TYR', 5.81), ('CG', 'LYS', 'CZ', 'TYR', 5.54), ('CG', 'LYS', 'OH', 'TYR', 5.72)], [('CD', 'LYS', 'CB', 'TYR', 8.44), ('CD', 'LYS', 'CG', 'TYR', 7.29), ('CD', 'LYS', 'CD1', 'TYR', 6.65), ('CD', 'LYS', 'CD2', 'TYR', 7.24), ('CD', 'LYS', 'CE1', 'TYR', 5.87), ('CD', 'LYS', 'CE2', 'TYR', 6.57), ('CD', 'LYS', 'CZ', 'TYR', 5.83), ('CD', 'LYS', 'OH', 'TYR', 5.68)], [('CE', 'LYS', 'CB', 'TYR', 9.65), ('CE', 'LYS', 'CG', 'TYR', 8.37), ('CE', 'LYS', 'CD1', 'TYR', 7.74), ('CE', 'LYS', 'CD2', 'TYR', 8.08), ('CE', 'LYS', 'CE1', 'TYR', 6.7), ('CE', 'LYS', 'CE2', 'TYR', 7.12), ('CE', 'LYS', 'CZ', 'TYR', 6.35), ('CE', 'LYS', 'OH', 'TYR', 5.7)], [('NZ', 'LYS', 'CB', 'TYR', 10.65), ('NZ', 'LYS', 'CG', 'TYR', 9.35), ('NZ', 'LYS', 'CD1', 'TYR', 8.51), ('NZ', 'LYS', 'CD2', 'TYR', 9.21), ('NZ', 'LYS', 'CE1', 'TYR', 7.38), ('NZ', 'LYS', 'CE2', 'TYR', 8.24), ('NZ', 'LYS', 'CZ', 'TYR', 7.24), ('NZ', 'LYS', 'OH', 'TYR', 6.46)]]}
THR_LYS = { 
	'distances':
		[[7.53, 7.27, 7.71, 6.89, 7.9], [8.43, 8.06, 8.67, 8.04, 9.08], [6.12, 6.01, 6.72, 6.16, 7.43]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'LYS', 7.53), ('CB', 'THR', 'CG', 'LYS', 7.27), ('CB', 'THR', 'CD', 'LYS', 7.71), ('CB', 'THR', 'CE', 'LYS', 6.89), ('CB', 'THR', 'NZ', 'LYS', 7.9)], [('OG1', 'THR', 'CB', 'LYS', 8.43), ('OG1', 'THR', 'CG', 'LYS', 8.06), ('OG1', 'THR', 'CD', 'LYS', 8.67), ('OG1', 'THR', 'CE', 'LYS', 8.04), ('OG1', 'THR', 'NZ', 'LYS', 9.08)], [('CG2', 'THR', 'CB', 'LYS', 6.12), ('CG2', 'THR', 'CG', 'LYS', 6.01), ('CG2', 'THR', 'CD', 'LYS', 6.72), ('CG2', 'THR', 'CE', 'LYS', 6.16), ('CG2', 'THR', 'NZ', 'LYS', 7.43)]]}
GLU_THR = { 
	'distances':
		[[6.52, 5.58, 6.23], [6.79, 5.55, 6.89], [7.57, 6.42, 7.54], [7.26, 6.33, 7.07], [8.76, 7.54, 8.78]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'THR', 6.52), ('CB', 'GLU', 'OG1', 'THR', 5.58), ('CB', 'GLU', 'CG2', 'THR', 6.23)], [('CG', 'GLU', 'CB', 'THR', 6.79), ('CG', 'GLU', 'OG1', 'THR', 5.55), ('CG', 'GLU', 'CG2', 'THR', 6.89)], [('CD', 'GLU', 'CB', 'THR', 7.57), ('CD', 'GLU', 'OG1', 'THR', 6.42), ('CD', 'GLU', 'CG2', 'THR', 7.54)], [('OE1', 'GLU', 'CB', 'THR', 7.26), ('OE1', 'GLU', 'OG1', 'THR', 6.33), ('OE1', 'GLU', 'CG2', 'THR', 7.07)], [('OE2', 'GLU', 'CB', 'THR', 8.76), ('OE2', 'GLU', 'OG1', 'THR', 7.54), ('OE2', 'GLU', 'CG2', 'THR', 8.78)]]}
THR_TYR = { 
	'distances':
		[[10.73, 9.42, 9.53, 8.28, 8.55, 7.07, 7.25, 6.39], [10.6, 9.36, 9.64, 8.09, 8.76, 6.96, 7.39, 6.7], [9.76, 8.54, 8.72, 7.45, 7.89, 6.4, 6.68, 6.1]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'TYR', 10.73), ('CB', 'THR', 'CG', 'TYR', 9.42), ('CB', 'THR', 'CD1', 'TYR', 9.53), ('CB', 'THR', 'CD2', 'TYR', 8.28), ('CB', 'THR', 'CE1', 'TYR', 8.55), ('CB', 'THR', 'CE2', 'TYR', 7.07), ('CB', 'THR', 'CZ', 'TYR', 7.25), ('CB', 'THR', 'OH', 'TYR', 6.39)], [('OG1', 'THR', 'CB', 'TYR', 10.6), ('OG1', 'THR', 'CG', 'TYR', 9.36), ('OG1', 'THR', 'CD1', 'TYR', 9.64), ('OG1', 'THR', 'CD2', 'TYR', 8.09), ('OG1', 'THR', 'CE1', 'TYR', 8.76), ('OG1', 'THR', 'CE2', 'TYR', 6.96), ('OG1', 'THR', 'CZ', 'TYR', 7.39), ('OG1', 'THR', 'OH', 'TYR', 6.7)], [('CG2', 'THR', 'CB', 'TYR', 9.76), ('CG2', 'THR', 'CG', 'TYR', 8.54), ('CG2', 'THR', 'CD1', 'TYR', 8.72), ('CG2', 'THR', 'CD2', 'TYR', 7.45), ('CG2', 'THR', 'CE1', 'TYR', 7.89), ('CG2', 'THR', 'CE2', 'TYR', 6.4), ('CG2', 'THR', 'CZ', 'TYR', 6.68), ('CG2', 'THR', 'OH', 'TYR', 6.1)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'A_1db3_4_2_1_47')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_TYR, d, 'A_1db3_4_2_1_47')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_TYR, d, 'A_1db3_4_2_1_47')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_LYS, d, 'A_1db3_4_2_1_47')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_THR, d, 'A_1db3_4_2_1_47')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_TYR, d, 'A_1db3_4_2_1_47')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'GLU_TYR' :  match2,
		'LYS_TYR' :  match3,
		'THR_LYS' :  match4,
		'GLU_THR' :  match5,
		'THR_TYR' :  match6}