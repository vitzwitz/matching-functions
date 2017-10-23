'''
FUNC:P_1d5l_1_11_1_7
PDB:1d5l
EC:1.11.1.7
RESI:gln,his,arg
LOCI:a-91,95;c-239;
'''
import motifFunctions as cmd
GLN_HIS = { 
	'distances':
		[[7.51, 6.65, 6.49, 6.38, 6.13, 6.05], [6.84, 5.72, 5.37, 5.37, 4.78, 4.77], [7.76, 6.55, 5.84, 6.29, 5.08, 5.38], [8.51, 7.41, 6.62, 7.33, 6.01, 6.48], [8.0, 6.63, 5.82, 6.23, 4.79, 5.08]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 7.51), ('CB', 'GLN', 'CG', 'HIS', 6.65), ('CB', 'GLN', 'ND1', 'HIS', 6.49), ('CB', 'GLN', 'CD2', 'HIS', 6.38), ('CB', 'GLN', 'CE1', 'HIS', 6.13), ('CB', 'GLN', 'NE2', 'HIS', 6.05)], [('CG', 'GLN', 'CB', 'HIS', 6.84), ('CG', 'GLN', 'CG', 'HIS', 5.72), ('CG', 'GLN', 'ND1', 'HIS', 5.37), ('CG', 'GLN', 'CD2', 'HIS', 5.37), ('CG', 'GLN', 'CE1', 'HIS', 4.78), ('CG', 'GLN', 'NE2', 'HIS', 4.77)], [('CD', 'GLN', 'CB', 'HIS', 7.76), ('CD', 'GLN', 'CG', 'HIS', 6.55), ('CD', 'GLN', 'ND1', 'HIS', 5.84), ('CD', 'GLN', 'CD2', 'HIS', 6.29), ('CD', 'GLN', 'CE1', 'HIS', 5.08), ('CD', 'GLN', 'NE2', 'HIS', 5.38)], [('OE1', 'GLN', 'CB', 'HIS', 8.51), ('OE1', 'GLN', 'CG', 'HIS', 7.41), ('OE1', 'GLN', 'ND1', 'HIS', 6.62), ('OE1', 'GLN', 'CD2', 'HIS', 7.33), ('OE1', 'GLN', 'CE1', 'HIS', 6.01), ('OE1', 'GLN', 'NE2', 'HIS', 6.48)], [('NE2', 'GLN', 'CB', 'HIS', 8.0), ('NE2', 'GLN', 'CG', 'HIS', 6.63), ('NE2', 'GLN', 'ND1', 'HIS', 5.82), ('NE2', 'GLN', 'CD2', 'HIS', 6.23), ('NE2', 'GLN', 'CE1', 'HIS', 4.79), ('NE2', 'GLN', 'NE2', 'HIS', 5.08)]]}
HIS_ARG = { 
	'distances':
		[[6.73, 7.26, 6.58, 5.48, 5.26, 6.05, 4.74], [5.75, 6.29, 5.53, 4.71, 4.63, 5.24, 4.6], [4.85, 5.7, 5.26, 4.79, 5.16, 5.81, 5.43], [5.97, 6.21, 5.15, 4.51, 4.18, 4.37, 4.42], [4.53, 5.25, 4.7, 4.66, 5.1, 5.45, 5.72], [5.27, 5.58, 4.61, 4.48, 4.52, 4.55, 5.19]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 6.73), ('CB', 'HIS', 'CG', 'ARG', 7.26), ('CB', 'HIS', 'CD', 'ARG', 6.58), ('CB', 'HIS', 'NE', 'ARG', 5.48), ('CB', 'HIS', 'CZ', 'ARG', 5.26), ('CB', 'HIS', 'NH1', 'ARG', 6.05), ('CB', 'HIS', 'NH2', 'ARG', 4.74)], [('CG', 'HIS', 'CB', 'ARG', 5.75), ('CG', 'HIS', 'CG', 'ARG', 6.29), ('CG', 'HIS', 'CD', 'ARG', 5.53), ('CG', 'HIS', 'NE', 'ARG', 4.71), ('CG', 'HIS', 'CZ', 'ARG', 4.63), ('CG', 'HIS', 'NH1', 'ARG', 5.24), ('CG', 'HIS', 'NH2', 'ARG', 4.6)], [('ND1', 'HIS', 'CB', 'ARG', 4.85), ('ND1', 'HIS', 'CG', 'ARG', 5.7), ('ND1', 'HIS', 'CD', 'ARG', 5.26), ('ND1', 'HIS', 'NE', 'ARG', 4.79), ('ND1', 'HIS', 'CZ', 'ARG', 5.16), ('ND1', 'HIS', 'NH1', 'ARG', 5.81), ('ND1', 'HIS', 'NH2', 'ARG', 5.43)], [('CD2', 'HIS', 'CB', 'ARG', 5.97), ('CD2', 'HIS', 'CG', 'ARG', 6.21), ('CD2', 'HIS', 'CD', 'ARG', 5.15), ('CD2', 'HIS', 'NE', 'ARG', 4.51), ('CD2', 'HIS', 'CZ', 'ARG', 4.18), ('CD2', 'HIS', 'NH1', 'ARG', 4.37), ('CD2', 'HIS', 'NH2', 'ARG', 4.42)], [('CE1', 'HIS', 'CB', 'ARG', 4.53), ('CE1', 'HIS', 'CG', 'ARG', 5.25), ('CE1', 'HIS', 'CD', 'ARG', 4.7), ('CE1', 'HIS', 'NE', 'ARG', 4.66), ('CE1', 'HIS', 'CZ', 'ARG', 5.1), ('CE1', 'HIS', 'NH1', 'ARG', 5.45), ('CE1', 'HIS', 'NH2', 'ARG', 5.72)], [('NE2', 'HIS', 'CB', 'ARG', 5.27), ('NE2', 'HIS', 'CG', 'ARG', 5.58), ('NE2', 'HIS', 'CD', 'ARG', 4.61), ('NE2', 'HIS', 'NE', 'ARG', 4.48), ('NE2', 'HIS', 'CZ', 'ARG', 4.52), ('NE2', 'HIS', 'NH1', 'ARG', 4.55), ('NE2', 'HIS', 'NH2', 'ARG', 5.19)]]}
GLN_ARG = { 
	'distances':
		[[9.48, 10.24, 9.53, 9.51, 9.44, 9.29, 9.8], [8.03, 8.76, 8.1, 8.2, 8.26, 8.12, 8.77], [7.8, 8.64, 8.21, 8.57, 8.87, 8.77, 9.54], [8.55, 9.52, 9.24, 9.59, 9.95, 9.93, 10.58], [7.04, 7.76, 7.39, 7.98, 8.38, 8.21, 9.22]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ARG', 9.48), ('CB', 'GLN', 'CG', 'ARG', 10.24), ('CB', 'GLN', 'CD', 'ARG', 9.53), ('CB', 'GLN', 'NE', 'ARG', 9.51), ('CB', 'GLN', 'CZ', 'ARG', 9.44), ('CB', 'GLN', 'NH1', 'ARG', 9.29), ('CB', 'GLN', 'NH2', 'ARG', 9.8)], [('CG', 'GLN', 'CB', 'ARG', 8.03), ('CG', 'GLN', 'CG', 'ARG', 8.76), ('CG', 'GLN', 'CD', 'ARG', 8.1), ('CG', 'GLN', 'NE', 'ARG', 8.2), ('CG', 'GLN', 'CZ', 'ARG', 8.26), ('CG', 'GLN', 'NH1', 'ARG', 8.12), ('CG', 'GLN', 'NH2', 'ARG', 8.77)], [('CD', 'GLN', 'CB', 'ARG', 7.8), ('CD', 'GLN', 'CG', 'ARG', 8.64), ('CD', 'GLN', 'CD', 'ARG', 8.21), ('CD', 'GLN', 'NE', 'ARG', 8.57), ('CD', 'GLN', 'CZ', 'ARG', 8.87), ('CD', 'GLN', 'NH1', 'ARG', 8.77), ('CD', 'GLN', 'NH2', 'ARG', 9.54)], [('OE1', 'GLN', 'CB', 'ARG', 8.55), ('OE1', 'GLN', 'CG', 'ARG', 9.52), ('OE1', 'GLN', 'CD', 'ARG', 9.24), ('OE1', 'GLN', 'NE', 'ARG', 9.59), ('OE1', 'GLN', 'CZ', 'ARG', 9.95), ('OE1', 'GLN', 'NH1', 'ARG', 9.93), ('OE1', 'GLN', 'NH2', 'ARG', 10.58)], [('NE2', 'GLN', 'CB', 'ARG', 7.04), ('NE2', 'GLN', 'CG', 'ARG', 7.76), ('NE2', 'GLN', 'CD', 'ARG', 7.39), ('NE2', 'GLN', 'NE', 'ARG', 7.98), ('NE2', 'GLN', 'CZ', 'ARG', 8.38), ('NE2', 'GLN', 'NH1', 'ARG', 8.21), ('NE2', 'GLN', 'NH2', 'ARG', 9.22)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_HIS, d, 'P_1d5l_1_11_1_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ARG, d, 'P_1d5l_1_11_1_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLN_ARG, d, 'P_1d5l_1_11_1_7')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_HIS' :  match1,
		'HIS_ARG' :  match2,
		'GLN_ARG' :  match3}