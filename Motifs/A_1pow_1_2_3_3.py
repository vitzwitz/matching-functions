'''
FUNC:A_1pow_1_2_3_3
PDB:1pow
EC:1.2.3.3
RESI:arg,phe,glu
LOCI:a-264,479,483;
'''
import motifFunctions as cmd
GLU_PHE = { 
	'distances':
		[[8.93, 8.96, 9.59, 8.77, 10.01, 9.24, 9.85], [7.87, 7.68, 8.29, 7.39, 8.61, 7.76, 8.37], [7.59, 7.37, 8.22, 6.78, 8.53, 7.17, 8.05], [7.99, 8.0, 9.01, 7.4, 9.45, 7.95, 8.97], [7.38, 6.86, 7.67, 6.05, 7.79, 6.2, 7.12]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'PHE', 8.93), ('CB', 'GLU', 'CG', 'PHE', 8.96), ('CB', 'GLU', 'CD1', 'PHE', 9.59), ('CB', 'GLU', 'CD2', 'PHE', 8.77), ('CB', 'GLU', 'CE1', 'PHE', 10.01), ('CB', 'GLU', 'CE2', 'PHE', 9.24), ('CB', 'GLU', 'CZ', 'PHE', 9.85)], [('CG', 'GLU', 'CB', 'PHE', 7.87), ('CG', 'GLU', 'CG', 'PHE', 7.68), ('CG', 'GLU', 'CD1', 'PHE', 8.29), ('CG', 'GLU', 'CD2', 'PHE', 7.39), ('CG', 'GLU', 'CE1', 'PHE', 8.61), ('CG', 'GLU', 'CE2', 'PHE', 7.76), ('CG', 'GLU', 'CZ', 'PHE', 8.37)], [('CD', 'GLU', 'CB', 'PHE', 7.59), ('CD', 'GLU', 'CG', 'PHE', 7.37), ('CD', 'GLU', 'CD1', 'PHE', 8.22), ('CD', 'GLU', 'CD2', 'PHE', 6.78), ('CD', 'GLU', 'CE1', 'PHE', 8.53), ('CD', 'GLU', 'CE2', 'PHE', 7.17), ('CD', 'GLU', 'CZ', 'PHE', 8.05)], [('OE1', 'GLU', 'CB', 'PHE', 7.99), ('OE1', 'GLU', 'CG', 'PHE', 8.0), ('OE1', 'GLU', 'CD1', 'PHE', 9.01), ('OE1', 'GLU', 'CD2', 'PHE', 7.4), ('OE1', 'GLU', 'CE1', 'PHE', 9.45), ('OE1', 'GLU', 'CE2', 'PHE', 7.95), ('OE1', 'GLU', 'CZ', 'PHE', 8.97)], [('OE2', 'GLU', 'CB', 'PHE', 7.38), ('OE2', 'GLU', 'CG', 'PHE', 6.86), ('OE2', 'GLU', 'CD1', 'PHE', 7.67), ('OE2', 'GLU', 'CD2', 'PHE', 6.05), ('OE2', 'GLU', 'CE1', 'PHE', 7.79), ('OE2', 'GLU', 'CE2', 'PHE', 6.2), ('OE2', 'GLU', 'CZ', 'PHE', 7.12)]]}
GLU_ARG = { 
	'distances':
		[[11.52, 10.63, 9.16, 8.53, 7.43, 6.85, 7.24], [10.27, 9.39, 7.91, 7.33, 6.16, 5.43, 6.13], [10.54, 9.8, 8.35, 7.94, 6.74, 5.71, 6.87], [11.73, 11.01, 9.57, 9.14, 7.92, 6.91, 7.93], [9.7, 9.06, 7.67, 7.44, 6.32, 5.11, 6.71]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 11.52), ('CB', 'GLU', 'CG', 'ARG', 10.63), ('CB', 'GLU', 'CD', 'ARG', 9.16), ('CB', 'GLU', 'NE', 'ARG', 8.53), ('CB', 'GLU', 'CZ', 'ARG', 7.43), ('CB', 'GLU', 'NH1', 'ARG', 6.85), ('CB', 'GLU', 'NH2', 'ARG', 7.24)], [('CG', 'GLU', 'CB', 'ARG', 10.27), ('CG', 'GLU', 'CG', 'ARG', 9.39), ('CG', 'GLU', 'CD', 'ARG', 7.91), ('CG', 'GLU', 'NE', 'ARG', 7.33), ('CG', 'GLU', 'CZ', 'ARG', 6.16), ('CG', 'GLU', 'NH1', 'ARG', 5.43), ('CG', 'GLU', 'NH2', 'ARG', 6.13)], [('CD', 'GLU', 'CB', 'ARG', 10.54), ('CD', 'GLU', 'CG', 'ARG', 9.8), ('CD', 'GLU', 'CD', 'ARG', 8.35), ('CD', 'GLU', 'NE', 'ARG', 7.94), ('CD', 'GLU', 'CZ', 'ARG', 6.74), ('CD', 'GLU', 'NH1', 'ARG', 5.71), ('CD', 'GLU', 'NH2', 'ARG', 6.87)], [('OE1', 'GLU', 'CB', 'ARG', 11.73), ('OE1', 'GLU', 'CG', 'ARG', 11.01), ('OE1', 'GLU', 'CD', 'ARG', 9.57), ('OE1', 'GLU', 'NE', 'ARG', 9.14), ('OE1', 'GLU', 'CZ', 'ARG', 7.92), ('OE1', 'GLU', 'NH1', 'ARG', 6.91), ('OE1', 'GLU', 'NH2', 'ARG', 7.93)], [('OE2', 'GLU', 'CB', 'ARG', 9.7), ('OE2', 'GLU', 'CG', 'ARG', 9.06), ('OE2', 'GLU', 'CD', 'ARG', 7.67), ('OE2', 'GLU', 'NE', 'ARG', 7.44), ('OE2', 'GLU', 'CZ', 'ARG', 6.32), ('OE2', 'GLU', 'NH1', 'ARG', 5.11), ('OE2', 'GLU', 'NH2', 'ARG', 6.71)]]}
PHE_ARG = { 
	'distances':
		[[11.11, 9.97, 9.16, 8.18, 7.15, 7.14, 6.51], [9.7, 8.63, 7.9, 7.08, 6.18, 6.12, 5.87], [8.92, 7.77, 7.27, 6.39, 5.79, 6.11, 5.49], [9.41, 8.56, 7.73, 7.2, 6.29, 5.82, 6.35], [7.69, 6.66, 6.36, 5.76, 5.5, 5.81, 5.66], [8.28, 7.6, 6.89, 6.67, 6.03, 5.48, 6.48], [7.31, 6.56, 6.13, 5.93, 5.63, 5.48, 6.17]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'ARG', 11.11), ('CB', 'PHE', 'CG', 'ARG', 9.97), ('CB', 'PHE', 'CD', 'ARG', 9.16), ('CB', 'PHE', 'NE', 'ARG', 8.18), ('CB', 'PHE', 'CZ', 'ARG', 7.15), ('CB', 'PHE', 'NH1', 'ARG', 7.14), ('CB', 'PHE', 'NH2', 'ARG', 6.51)], [('CG', 'PHE', 'CB', 'ARG', 9.7), ('CG', 'PHE', 'CG', 'ARG', 8.63), ('CG', 'PHE', 'CD', 'ARG', 7.9), ('CG', 'PHE', 'NE', 'ARG', 7.08), ('CG', 'PHE', 'CZ', 'ARG', 6.18), ('CG', 'PHE', 'NH1', 'ARG', 6.12), ('CG', 'PHE', 'NH2', 'ARG', 5.87)], [('CD1', 'PHE', 'CB', 'ARG', 8.92), ('CD1', 'PHE', 'CG', 'ARG', 7.77), ('CD1', 'PHE', 'CD', 'ARG', 7.27), ('CD1', 'PHE', 'NE', 'ARG', 6.39), ('CD1', 'PHE', 'CZ', 'ARG', 5.79), ('CD1', 'PHE', 'NH1', 'ARG', 6.11), ('CD1', 'PHE', 'NH2', 'ARG', 5.49)], [('CD2', 'PHE', 'CB', 'ARG', 9.41), ('CD2', 'PHE', 'CG', 'ARG', 8.56), ('CD2', 'PHE', 'CD', 'ARG', 7.73), ('CD2', 'PHE', 'NE', 'ARG', 7.2), ('CD2', 'PHE', 'CZ', 'ARG', 6.29), ('CD2', 'PHE', 'NH1', 'ARG', 5.82), ('CD2', 'PHE', 'NH2', 'ARG', 6.35)], [('CE1', 'PHE', 'CB', 'ARG', 7.69), ('CE1', 'PHE', 'CG', 'ARG', 6.66), ('CE1', 'PHE', 'CD', 'ARG', 6.36), ('CE1', 'PHE', 'NE', 'ARG', 5.76), ('CE1', 'PHE', 'CZ', 'ARG', 5.5), ('CE1', 'PHE', 'NH1', 'ARG', 5.81), ('CE1', 'PHE', 'NH2', 'ARG', 5.66)], [('CE2', 'PHE', 'CB', 'ARG', 8.28), ('CE2', 'PHE', 'CG', 'ARG', 7.6), ('CE2', 'PHE', 'CD', 'ARG', 6.89), ('CE2', 'PHE', 'NE', 'ARG', 6.67), ('CE2', 'PHE', 'CZ', 'ARG', 6.03), ('CE2', 'PHE', 'NH1', 'ARG', 5.48), ('CE2', 'PHE', 'NH2', 'ARG', 6.48)], [('CZ', 'PHE', 'CB', 'ARG', 7.31), ('CZ', 'PHE', 'CG', 'ARG', 6.56), ('CZ', 'PHE', 'CD', 'ARG', 6.13), ('CZ', 'PHE', 'NE', 'ARG', 5.93), ('CZ', 'PHE', 'CZ', 'ARG', 5.63), ('CZ', 'PHE', 'NH1', 'ARG', 5.48), ('CZ', 'PHE', 'NH2', 'ARG', 6.17)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_PHE, d, 'A_1pow_1_2_3_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ARG, d, 'A_1pow_1_2_3_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_ARG, d, 'A_1pow_1_2_3_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_PHE' :  match1,
		'GLU_ARG' :  match2,
		'PHE_ARG' :  match3}