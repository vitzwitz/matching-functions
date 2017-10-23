'''
FUNC:P_1gk2_4_3_1_3
PDB:1gk2
EC:4.3.1.3
RESI:ser,gly,tyr,glu
LOCI:a-143,144,280,414;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[10.05, 8.59, 8.34, 7.69, 7.16, 6.34, 5.99, 4.84], [10.85, 9.35, 8.86, 8.62, 7.55, 7.25, 6.59, 5.24]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 10.05), ('CB', 'SER', 'CG', 'TYR', 8.59), ('CB', 'SER', 'CD1', 'TYR', 8.34), ('CB', 'SER', 'CD2', 'TYR', 7.69), ('CB', 'SER', 'CE1', 'TYR', 7.16), ('CB', 'SER', 'CE2', 'TYR', 6.34), ('CB', 'SER', 'CZ', 'TYR', 5.99), ('CB', 'SER', 'OH', 'TYR', 4.84)], [('OG', 'SER', 'CB', 'TYR', 10.85), ('OG', 'SER', 'CG', 'TYR', 9.35), ('OG', 'SER', 'CD1', 'TYR', 8.86), ('OG', 'SER', 'CD2', 'TYR', 8.62), ('OG', 'SER', 'CE1', 'TYR', 7.55), ('OG', 'SER', 'CE2', 'TYR', 7.25), ('OG', 'SER', 'CZ', 'TYR', 6.59), ('OG', 'SER', 'OH', 'TYR', 5.24)]]}
SER_GLY = { 
	'distances':
		[[6.95, 7.23, 6.55, 5.16], [7.78, 7.91, 7.14, 5.9]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 6.95), ('CB', 'SER', 'C', 'GLY', 7.23), ('CB', 'SER', 'CA', 'GLY', 6.55), ('CB', 'SER', 'N', 'GLY', 5.16)], [('OG', 'SER', 'O', 'GLY', 7.78), ('OG', 'SER', 'C', 'GLY', 7.91), ('OG', 'SER', 'CA', 'GLY', 7.14), ('OG', 'SER', 'N', 'GLY', 5.9)]]}
GLY_TYR = { 
	'distances':
		[[13.35, 12.16, 12.39, 10.96, 11.51, 9.92, 10.24, 9.49], [13.82, 12.61, 12.74, 11.5, 11.82, 10.44, 10.62, 9.82], [13.15, 11.91, 11.89, 10.92, 10.94, 9.84, 9.85, 9.02], [11.89, 10.6, 10.55, 9.62, 9.55, 8.48, 8.45, 7.6]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'TYR', 13.35), ('O', 'GLY', 'CG', 'TYR', 12.16), ('O', 'GLY', 'CD1', 'TYR', 12.39), ('O', 'GLY', 'CD2', 'TYR', 10.96), ('O', 'GLY', 'CE1', 'TYR', 11.51), ('O', 'GLY', 'CE2', 'TYR', 9.92), ('O', 'GLY', 'CZ', 'TYR', 10.24), ('O', 'GLY', 'OH', 'TYR', 9.49)], [('C', 'GLY', 'CB', 'TYR', 13.82), ('C', 'GLY', 'CG', 'TYR', 12.61), ('C', 'GLY', 'CD1', 'TYR', 12.74), ('C', 'GLY', 'CD2', 'TYR', 11.5), ('C', 'GLY', 'CE1', 'TYR', 11.82), ('C', 'GLY', 'CE2', 'TYR', 10.44), ('C', 'GLY', 'CZ', 'TYR', 10.62), ('C', 'GLY', 'OH', 'TYR', 9.82)], [('CA', 'GLY', 'CB', 'TYR', 13.15), ('CA', 'GLY', 'CG', 'TYR', 11.91), ('CA', 'GLY', 'CD1', 'TYR', 11.89), ('CA', 'GLY', 'CD2', 'TYR', 10.92), ('CA', 'GLY', 'CE1', 'TYR', 10.94), ('CA', 'GLY', 'CE2', 'TYR', 9.84), ('CA', 'GLY', 'CZ', 'TYR', 9.85), ('CA', 'GLY', 'OH', 'TYR', 9.02)], [('N', 'GLY', 'CB', 'TYR', 11.89), ('N', 'GLY', 'CG', 'TYR', 10.6), ('N', 'GLY', 'CD1', 'TYR', 10.55), ('N', 'GLY', 'CD2', 'TYR', 9.62), ('N', 'GLY', 'CE1', 'TYR', 9.55), ('N', 'GLY', 'CE2', 'TYR', 8.48), ('N', 'GLY', 'CZ', 'TYR', 8.45), ('N', 'GLY', 'OH', 'TYR', 7.6)]]}
TYR_GLU = { 
	'distances':
		[[7.57, 8.15, 8.92, 8.99, 9.74], [6.7, 6.99, 7.66, 7.82, 8.37], [7.18, 7.1, 7.78, 8.21, 8.26], [5.86, 6.2, 6.63, 6.61, 7.44], [6.96, 6.49, 6.98, 7.56, 7.24], [5.55, 5.44, 5.58, 5.67, 6.22], [6.18, 5.62, 5.81, 6.28, 6.09], [6.57, 5.6, 5.4, 6.04, 5.27]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 7.57), ('CB', 'TYR', 'CG', 'GLU', 8.15), ('CB', 'TYR', 'CD', 'GLU', 8.92), ('CB', 'TYR', 'OE1', 'GLU', 8.99), ('CB', 'TYR', 'OE2', 'GLU', 9.74)], [('CG', 'TYR', 'CB', 'GLU', 6.7), ('CG', 'TYR', 'CG', 'GLU', 6.99), ('CG', 'TYR', 'CD', 'GLU', 7.66), ('CG', 'TYR', 'OE1', 'GLU', 7.82), ('CG', 'TYR', 'OE2', 'GLU', 8.37)], [('CD1', 'TYR', 'CB', 'GLU', 7.18), ('CD1', 'TYR', 'CG', 'GLU', 7.1), ('CD1', 'TYR', 'CD', 'GLU', 7.78), ('CD1', 'TYR', 'OE1', 'GLU', 8.21), ('CD1', 'TYR', 'OE2', 'GLU', 8.26)], [('CD2', 'TYR', 'CB', 'GLU', 5.86), ('CD2', 'TYR', 'CG', 'GLU', 6.2), ('CD2', 'TYR', 'CD', 'GLU', 6.63), ('CD2', 'TYR', 'OE1', 'GLU', 6.61), ('CD2', 'TYR', 'OE2', 'GLU', 7.44)], [('CE1', 'TYR', 'CB', 'GLU', 6.96), ('CE1', 'TYR', 'CG', 'GLU', 6.49), ('CE1', 'TYR', 'CD', 'GLU', 6.98), ('CE1', 'TYR', 'OE1', 'GLU', 7.56), ('CE1', 'TYR', 'OE2', 'GLU', 7.24)], [('CE2', 'TYR', 'CB', 'GLU', 5.55), ('CE2', 'TYR', 'CG', 'GLU', 5.44), ('CE2', 'TYR', 'CD', 'GLU', 5.58), ('CE2', 'TYR', 'OE1', 'GLU', 5.67), ('CE2', 'TYR', 'OE2', 'GLU', 6.22)], [('CZ', 'TYR', 'CB', 'GLU', 6.18), ('CZ', 'TYR', 'CG', 'GLU', 5.62), ('CZ', 'TYR', 'CD', 'GLU', 5.81), ('CZ', 'TYR', 'OE1', 'GLU', 6.28), ('CZ', 'TYR', 'OE2', 'GLU', 6.09)], [('OH', 'TYR', 'CB', 'GLU', 6.57), ('OH', 'TYR', 'CG', 'GLU', 5.6), ('OH', 'TYR', 'CD', 'GLU', 5.4), ('OH', 'TYR', 'OE1', 'GLU', 6.04), ('OH', 'TYR', 'OE2', 'GLU', 5.27)]]}
GLY_GLU = { 
	'distances':
		[[11.07, 10.53, 9.07, 8.43, 8.77], [11.93, 11.3, 9.86, 9.34, 9.46], [11.76, 11.03, 9.7, 9.33, 9.22], [10.45, 9.69, 8.4, 8.12, 7.93]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'GLU', 11.07), ('O', 'GLY', 'CG', 'GLU', 10.53), ('O', 'GLY', 'CD', 'GLU', 9.07), ('O', 'GLY', 'OE1', 'GLU', 8.43), ('O', 'GLY', 'OE2', 'GLU', 8.77)], [('C', 'GLY', 'CB', 'GLU', 11.93), ('C', 'GLY', 'CG', 'GLU', 11.3), ('C', 'GLY', 'CD', 'GLU', 9.86), ('C', 'GLY', 'OE1', 'GLU', 9.34), ('C', 'GLY', 'OE2', 'GLU', 9.46)], [('CA', 'GLY', 'CB', 'GLU', 11.76), ('CA', 'GLY', 'CG', 'GLU', 11.03), ('CA', 'GLY', 'CD', 'GLU', 9.7), ('CA', 'GLY', 'OE1', 'GLU', 9.33), ('CA', 'GLY', 'OE2', 'GLU', 9.22)], [('N', 'GLY', 'CB', 'GLU', 10.45), ('N', 'GLY', 'CG', 'GLU', 9.69), ('N', 'GLY', 'CD', 'GLU', 8.4), ('N', 'GLY', 'OE1', 'GLU', 8.12), ('N', 'GLY', 'OE2', 'GLU', 7.93)]]}
SER_GLU = { 
	'distances':
		[[7.92, 6.86, 5.73, 5.96, 5.07], [8.61, 7.33, 6.34, 6.88, 5.37]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 7.92), ('CB', 'SER', 'CG', 'GLU', 6.86), ('CB', 'SER', 'CD', 'GLU', 5.73), ('CB', 'SER', 'OE1', 'GLU', 5.96), ('CB', 'SER', 'OE2', 'GLU', 5.07)], [('OG', 'SER', 'CB', 'GLU', 8.61), ('OG', 'SER', 'CG', 'GLU', 7.33), ('OG', 'SER', 'CD', 'GLU', 6.34), ('OG', 'SER', 'OE1', 'GLU', 6.88), ('OG', 'SER', 'OE2', 'GLU', 5.37)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'P_1gk2_4_3_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_GLY, d, 'P_1gk2_4_3_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_TYR, d, 'P_1gk2_4_3_1_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_GLU, d, 'P_1gk2_4_3_1_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_GLU, d, 'P_1gk2_4_3_1_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_GLU, d, 'P_1gk2_4_3_1_3')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'SER_GLY' :  match2,
		'GLY_TYR' :  match3,
		'TYR_GLU' :  match4,
		'GLY_GLU' :  match5,
		'SER_GLU' :  match6}