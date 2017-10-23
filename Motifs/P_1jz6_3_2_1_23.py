'''
FUNC:P_1jz6_3_2_1_23
PDB:1jz6
EC:3.2.1.23
RESI:glu,tyr,glu
LOCI:a-461,503,537;
'''
import motifFunctions as cmd
GLU_TYR = { 
	'distances':
		[[8.3, 7.18, 6.63, 6.99, 5.8, 6.28, 5.62, 5.44], [9.65, 8.5, 7.72, 8.4, 6.74, 7.58, 6.68, 6.19], [9.87, 8.64, 7.63, 8.71, 6.52, 7.84, 6.67, 6.07], [10.88, 9.7, 8.59, 9.86, 7.52, 9.03, 7.81, 7.19], [9.11, 7.81, 6.76, 7.88, 5.53, 6.98, 5.69, 5.08], [14.3, 13.55, 12.15, 14.38, 11.65, 14.0, 12.66, 12.5], [12.8, 12.03, 10.63, 12.85, 10.13, 12.48, 11.15, 11.04], [12.27, 11.4, 10.0, 12.16, 9.41, 11.72, 10.37, 10.2], [13.0, 12.02, 10.64, 12.66, 9.89, 12.08, 10.7, 10.35], [11.08, 10.27, 8.88, 11.11, 8.41, 10.78, 9.47, 9.47]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 8.3), ('CB', 'GLU', 'CG', 'TYR', 7.18), ('CB', 'GLU', 'CD1', 'TYR', 6.63), ('CB', 'GLU', 'CD2', 'TYR', 6.99), ('CB', 'GLU', 'CE1', 'TYR', 5.8), ('CB', 'GLU', 'CE2', 'TYR', 6.28), ('CB', 'GLU', 'CZ', 'TYR', 5.62), ('CB', 'GLU', 'OH', 'TYR', 5.44)], [('CG', 'GLU', 'CB', 'TYR', 9.65), ('CG', 'GLU', 'CG', 'TYR', 8.5), ('CG', 'GLU', 'CD1', 'TYR', 7.72), ('CG', 'GLU', 'CD2', 'TYR', 8.4), ('CG', 'GLU', 'CE1', 'TYR', 6.74), ('CG', 'GLU', 'CE2', 'TYR', 7.58), ('CG', 'GLU', 'CZ', 'TYR', 6.68), ('CG', 'GLU', 'OH', 'TYR', 6.19)], [('CD', 'GLU', 'CB', 'TYR', 9.87), ('CD', 'GLU', 'CG', 'TYR', 8.64), ('CD', 'GLU', 'CD1', 'TYR', 7.63), ('CD', 'GLU', 'CD2', 'TYR', 8.71), ('CD', 'GLU', 'CE1', 'TYR', 6.52), ('CD', 'GLU', 'CE2', 'TYR', 7.84), ('CD', 'GLU', 'CZ', 'TYR', 6.67), ('CD', 'GLU', 'OH', 'TYR', 6.07)], [('OE1', 'GLU', 'CB', 'TYR', 10.88), ('OE1', 'GLU', 'CG', 'TYR', 9.7), ('OE1', 'GLU', 'CD1', 'TYR', 8.59), ('OE1', 'GLU', 'CD2', 'TYR', 9.86), ('OE1', 'GLU', 'CE1', 'TYR', 7.52), ('OE1', 'GLU', 'CE2', 'TYR', 9.03), ('OE1', 'GLU', 'CZ', 'TYR', 7.81), ('OE1', 'GLU', 'OH', 'TYR', 7.19)], [('OE2', 'GLU', 'CB', 'TYR', 9.11), ('OE2', 'GLU', 'CG', 'TYR', 7.81), ('OE2', 'GLU', 'CD1', 'TYR', 6.76), ('OE2', 'GLU', 'CD2', 'TYR', 7.88), ('OE2', 'GLU', 'CE1', 'TYR', 5.53), ('OE2', 'GLU', 'CE2', 'TYR', 6.98), ('OE2', 'GLU', 'CZ', 'TYR', 5.69), ('OE2', 'GLU', 'OH', 'TYR', 5.08)], [('CB', 'GLU', 'CB', 'TYR', 14.3), ('CB', 'GLU', 'CG', 'TYR', 13.55), ('CB', 'GLU', 'CD1', 'TYR', 12.15), ('CB', 'GLU', 'CD2', 'TYR', 14.38), ('CB', 'GLU', 'CE1', 'TYR', 11.65), ('CB', 'GLU', 'CE2', 'TYR', 14.0), ('CB', 'GLU', 'CZ', 'TYR', 12.66), ('CB', 'GLU', 'OH', 'TYR', 12.5)], [('CG', 'GLU', 'CB', 'TYR', 12.8), ('CG', 'GLU', 'CG', 'TYR', 12.03), ('CG', 'GLU', 'CD1', 'TYR', 10.63), ('CG', 'GLU', 'CD2', 'TYR', 12.85), ('CG', 'GLU', 'CE1', 'TYR', 10.13), ('CG', 'GLU', 'CE2', 'TYR', 12.48), ('CG', 'GLU', 'CZ', 'TYR', 11.15), ('CG', 'GLU', 'OH', 'TYR', 11.04)], [('CD', 'GLU', 'CB', 'TYR', 12.27), ('CD', 'GLU', 'CG', 'TYR', 11.4), ('CD', 'GLU', 'CD1', 'TYR', 10.0), ('CD', 'GLU', 'CD2', 'TYR', 12.16), ('CD', 'GLU', 'CE1', 'TYR', 9.41), ('CD', 'GLU', 'CE2', 'TYR', 11.72), ('CD', 'GLU', 'CZ', 'TYR', 10.37), ('CD', 'GLU', 'OH', 'TYR', 10.2)], [('OE1', 'GLU', 'CB', 'TYR', 13.0), ('OE1', 'GLU', 'CG', 'TYR', 12.02), ('OE1', 'GLU', 'CD1', 'TYR', 10.64), ('OE1', 'GLU', 'CD2', 'TYR', 12.66), ('OE1', 'GLU', 'CE1', 'TYR', 9.89), ('OE1', 'GLU', 'CE2', 'TYR', 12.08), ('OE1', 'GLU', 'CZ', 'TYR', 10.7), ('OE1', 'GLU', 'OH', 'TYR', 10.35)], [('OE2', 'GLU', 'CB', 'TYR', 11.08), ('OE2', 'GLU', 'CG', 'TYR', 10.27), ('OE2', 'GLU', 'CD1', 'TYR', 8.88), ('OE2', 'GLU', 'CD2', 'TYR', 11.11), ('OE2', 'GLU', 'CE1', 'TYR', 8.41), ('OE2', 'GLU', 'CE2', 'TYR', 10.78), ('OE2', 'GLU', 'CZ', 'TYR', 9.47), ('OE2', 'GLU', 'OH', 'TYR', 9.47)]]}
GLU_GLU = { 
	'distances':
		[[12.02, 10.56, 10.27, 10.63, 9.78], [11.11, 9.73, 9.53, 9.77, 9.29], [9.82, 8.46, 8.13, 8.29, 7.95], [8.94, 7.68, 7.49, 7.58, 7.57], [9.89, 8.47, 7.88, 8.04, 7.5], [12.02, 11.11, 9.82, 8.94, 9.89], [10.56, 9.73, 8.46, 7.68, 8.47], [10.27, 9.53, 8.13, 7.49, 7.88], [10.63, 9.77, 8.29, 7.58, 8.04], [9.78, 9.29, 7.95, 7.57, 7.5]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.02), ('CB', 'GLU', 'CG', 'GLU', 10.56), ('CB', 'GLU', 'CD', 'GLU', 10.27), ('CB', 'GLU', 'OE1', 'GLU', 10.63), ('CB', 'GLU', 'OE2', 'GLU', 9.78)], [('CG', 'GLU', 'CB', 'GLU', 11.11), ('CG', 'GLU', 'CG', 'GLU', 9.73), ('CG', 'GLU', 'CD', 'GLU', 9.53), ('CG', 'GLU', 'OE1', 'GLU', 9.77), ('CG', 'GLU', 'OE2', 'GLU', 9.29)], [('CD', 'GLU', 'CB', 'GLU', 9.82), ('CD', 'GLU', 'CG', 'GLU', 8.46), ('CD', 'GLU', 'CD', 'GLU', 8.13), ('CD', 'GLU', 'OE1', 'GLU', 8.29), ('CD', 'GLU', 'OE2', 'GLU', 7.95)], [('OE1', 'GLU', 'CB', 'GLU', 8.94), ('OE1', 'GLU', 'CG', 'GLU', 7.68), ('OE1', 'GLU', 'CD', 'GLU', 7.49), ('OE1', 'GLU', 'OE1', 'GLU', 7.58), ('OE1', 'GLU', 'OE2', 'GLU', 7.57)], [('OE2', 'GLU', 'CB', 'GLU', 9.89), ('OE2', 'GLU', 'CG', 'GLU', 8.47), ('OE2', 'GLU', 'CD', 'GLU', 7.88), ('OE2', 'GLU', 'OE1', 'GLU', 8.04), ('OE2', 'GLU', 'OE2', 'GLU', 7.5)], [('CB', 'GLU', 'CB', 'GLU', 12.02), ('CB', 'GLU', 'CG', 'GLU', 11.11), ('CB', 'GLU', 'CD', 'GLU', 9.82), ('CB', 'GLU', 'OE1', 'GLU', 8.94), ('CB', 'GLU', 'OE2', 'GLU', 9.89)], [('CG', 'GLU', 'CB', 'GLU', 10.56), ('CG', 'GLU', 'CG', 'GLU', 9.73), ('CG', 'GLU', 'CD', 'GLU', 8.46), ('CG', 'GLU', 'OE1', 'GLU', 7.68), ('CG', 'GLU', 'OE2', 'GLU', 8.47)], [('CD', 'GLU', 'CB', 'GLU', 10.27), ('CD', 'GLU', 'CG', 'GLU', 9.53), ('CD', 'GLU', 'CD', 'GLU', 8.13), ('CD', 'GLU', 'OE1', 'GLU', 7.49), ('CD', 'GLU', 'OE2', 'GLU', 7.88)], [('OE1', 'GLU', 'CB', 'GLU', 10.63), ('OE1', 'GLU', 'CG', 'GLU', 9.77), ('OE1', 'GLU', 'CD', 'GLU', 8.29), ('OE1', 'GLU', 'OE1', 'GLU', 7.58), ('OE1', 'GLU', 'OE2', 'GLU', 8.04)], [('OE2', 'GLU', 'CB', 'GLU', 9.78), ('OE2', 'GLU', 'CG', 'GLU', 9.29), ('OE2', 'GLU', 'CD', 'GLU', 7.95), ('OE2', 'GLU', 'OE1', 'GLU', 7.57), ('OE2', 'GLU', 'OE2', 'GLU', 7.5)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_TYR, d, 'P_1jz6_3_2_1_23')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'P_1jz6_3_2_1_23')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_TYR' :  match1,
		'GLU_GLU' :  match2}