'''
FUNC:P_1pow_1_2_3_3
PDB:1pow
EC:1.2.3.3
RESI:arg,phe,glu
LOCI:a-264,479,483;
'''
import motifFunctions as cmd
ARG_PHE = { 
	'distances':
		[[11.11, 9.7, 8.92, 9.41, 7.69, 8.28, 7.31], [9.97, 8.63, 7.77, 8.56, 6.66, 7.6, 6.56], [9.16, 7.9, 7.27, 7.73, 6.36, 6.89, 6.13], [8.18, 7.08, 6.39, 7.2, 5.76, 6.67, 5.93], [7.15, 6.18, 5.79, 6.29, 5.5, 6.03, 5.63], [7.14, 6.12, 6.11, 5.82, 5.81, 5.48, 5.48], [6.51, 5.87, 5.49, 6.35, 5.66, 6.48, 6.17]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'PHE', 11.11), ('CB', 'ARG', 'CG', 'PHE', 9.7), ('CB', 'ARG', 'CD1', 'PHE', 8.92), ('CB', 'ARG', 'CD2', 'PHE', 9.41), ('CB', 'ARG', 'CE1', 'PHE', 7.69), ('CB', 'ARG', 'CE2', 'PHE', 8.28), ('CB', 'ARG', 'CZ', 'PHE', 7.31)], [('CG', 'ARG', 'CB', 'PHE', 9.97), ('CG', 'ARG', 'CG', 'PHE', 8.63), ('CG', 'ARG', 'CD1', 'PHE', 7.77), ('CG', 'ARG', 'CD2', 'PHE', 8.56), ('CG', 'ARG', 'CE1', 'PHE', 6.66), ('CG', 'ARG', 'CE2', 'PHE', 7.6), ('CG', 'ARG', 'CZ', 'PHE', 6.56)], [('CD', 'ARG', 'CB', 'PHE', 9.16), ('CD', 'ARG', 'CG', 'PHE', 7.9), ('CD', 'ARG', 'CD1', 'PHE', 7.27), ('CD', 'ARG', 'CD2', 'PHE', 7.73), ('CD', 'ARG', 'CE1', 'PHE', 6.36), ('CD', 'ARG', 'CE2', 'PHE', 6.89), ('CD', 'ARG', 'CZ', 'PHE', 6.13)], [('NE', 'ARG', 'CB', 'PHE', 8.18), ('NE', 'ARG', 'CG', 'PHE', 7.08), ('NE', 'ARG', 'CD1', 'PHE', 6.39), ('NE', 'ARG', 'CD2', 'PHE', 7.2), ('NE', 'ARG', 'CE1', 'PHE', 5.76), ('NE', 'ARG', 'CE2', 'PHE', 6.67), ('NE', 'ARG', 'CZ', 'PHE', 5.93)], [('CZ', 'ARG', 'CB', 'PHE', 7.15), ('CZ', 'ARG', 'CG', 'PHE', 6.18), ('CZ', 'ARG', 'CD1', 'PHE', 5.79), ('CZ', 'ARG', 'CD2', 'PHE', 6.29), ('CZ', 'ARG', 'CE1', 'PHE', 5.5), ('CZ', 'ARG', 'CE2', 'PHE', 6.03), ('CZ', 'ARG', 'CZ', 'PHE', 5.63)], [('NH1', 'ARG', 'CB', 'PHE', 7.14), ('NH1', 'ARG', 'CG', 'PHE', 6.12), ('NH1', 'ARG', 'CD1', 'PHE', 6.11), ('NH1', 'ARG', 'CD2', 'PHE', 5.82), ('NH1', 'ARG', 'CE1', 'PHE', 5.81), ('NH1', 'ARG', 'CE2', 'PHE', 5.48), ('NH1', 'ARG', 'CZ', 'PHE', 5.48)], [('NH2', 'ARG', 'CB', 'PHE', 6.51), ('NH2', 'ARG', 'CG', 'PHE', 5.87), ('NH2', 'ARG', 'CD1', 'PHE', 5.49), ('NH2', 'ARG', 'CD2', 'PHE', 6.35), ('NH2', 'ARG', 'CE1', 'PHE', 5.66), ('NH2', 'ARG', 'CE2', 'PHE', 6.48), ('NH2', 'ARG', 'CZ', 'PHE', 6.17)]]}
ARG_GLU = { 
	'distances':
		[[11.52, 10.27, 10.54, 11.73, 9.7], [10.63, 9.39, 9.8, 11.01, 9.06], [9.16, 7.91, 8.35, 9.57, 7.67], [8.53, 7.33, 7.94, 9.14, 7.44], [7.43, 6.16, 6.74, 7.92, 6.32], [6.85, 5.43, 5.71, 6.91, 5.11], [7.24, 6.13, 6.87, 7.93, 6.71]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 11.52), ('CB', 'ARG', 'CG', 'GLU', 10.27), ('CB', 'ARG', 'CD', 'GLU', 10.54), ('CB', 'ARG', 'OE1', 'GLU', 11.73), ('CB', 'ARG', 'OE2', 'GLU', 9.7)], [('CG', 'ARG', 'CB', 'GLU', 10.63), ('CG', 'ARG', 'CG', 'GLU', 9.39), ('CG', 'ARG', 'CD', 'GLU', 9.8), ('CG', 'ARG', 'OE1', 'GLU', 11.01), ('CG', 'ARG', 'OE2', 'GLU', 9.06)], [('CD', 'ARG', 'CB', 'GLU', 9.16), ('CD', 'ARG', 'CG', 'GLU', 7.91), ('CD', 'ARG', 'CD', 'GLU', 8.35), ('CD', 'ARG', 'OE1', 'GLU', 9.57), ('CD', 'ARG', 'OE2', 'GLU', 7.67)], [('NE', 'ARG', 'CB', 'GLU', 8.53), ('NE', 'ARG', 'CG', 'GLU', 7.33), ('NE', 'ARG', 'CD', 'GLU', 7.94), ('NE', 'ARG', 'OE1', 'GLU', 9.14), ('NE', 'ARG', 'OE2', 'GLU', 7.44)], [('CZ', 'ARG', 'CB', 'GLU', 7.43), ('CZ', 'ARG', 'CG', 'GLU', 6.16), ('CZ', 'ARG', 'CD', 'GLU', 6.74), ('CZ', 'ARG', 'OE1', 'GLU', 7.92), ('CZ', 'ARG', 'OE2', 'GLU', 6.32)], [('NH1', 'ARG', 'CB', 'GLU', 6.85), ('NH1', 'ARG', 'CG', 'GLU', 5.43), ('NH1', 'ARG', 'CD', 'GLU', 5.71), ('NH1', 'ARG', 'OE1', 'GLU', 6.91), ('NH1', 'ARG', 'OE2', 'GLU', 5.11)], [('NH2', 'ARG', 'CB', 'GLU', 7.24), ('NH2', 'ARG', 'CG', 'GLU', 6.13), ('NH2', 'ARG', 'CD', 'GLU', 6.87), ('NH2', 'ARG', 'OE1', 'GLU', 7.93), ('NH2', 'ARG', 'OE2', 'GLU', 6.71)]]}
PHE_GLU = { 
	'distances':
		[[8.93, 7.87, 7.59, 7.99, 7.38], [8.96, 7.68, 7.37, 8.0, 6.86], [9.59, 8.29, 8.22, 9.01, 7.67], [8.77, 7.39, 6.78, 7.4, 6.05], [10.01, 8.61, 8.53, 9.45, 7.79], [9.24, 7.76, 7.17, 7.95, 6.2], [9.85, 8.37, 8.05, 8.97, 7.12]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'GLU', 8.93), ('CB', 'PHE', 'CG', 'GLU', 7.87), ('CB', 'PHE', 'CD', 'GLU', 7.59), ('CB', 'PHE', 'OE1', 'GLU', 7.99), ('CB', 'PHE', 'OE2', 'GLU', 7.38)], [('CG', 'PHE', 'CB', 'GLU', 8.96), ('CG', 'PHE', 'CG', 'GLU', 7.68), ('CG', 'PHE', 'CD', 'GLU', 7.37), ('CG', 'PHE', 'OE1', 'GLU', 8.0), ('CG', 'PHE', 'OE2', 'GLU', 6.86)], [('CD1', 'PHE', 'CB', 'GLU', 9.59), ('CD1', 'PHE', 'CG', 'GLU', 8.29), ('CD1', 'PHE', 'CD', 'GLU', 8.22), ('CD1', 'PHE', 'OE1', 'GLU', 9.01), ('CD1', 'PHE', 'OE2', 'GLU', 7.67)], [('CD2', 'PHE', 'CB', 'GLU', 8.77), ('CD2', 'PHE', 'CG', 'GLU', 7.39), ('CD2', 'PHE', 'CD', 'GLU', 6.78), ('CD2', 'PHE', 'OE1', 'GLU', 7.4), ('CD2', 'PHE', 'OE2', 'GLU', 6.05)], [('CE1', 'PHE', 'CB', 'GLU', 10.01), ('CE1', 'PHE', 'CG', 'GLU', 8.61), ('CE1', 'PHE', 'CD', 'GLU', 8.53), ('CE1', 'PHE', 'OE1', 'GLU', 9.45), ('CE1', 'PHE', 'OE2', 'GLU', 7.79)], [('CE2', 'PHE', 'CB', 'GLU', 9.24), ('CE2', 'PHE', 'CG', 'GLU', 7.76), ('CE2', 'PHE', 'CD', 'GLU', 7.17), ('CE2', 'PHE', 'OE1', 'GLU', 7.95), ('CE2', 'PHE', 'OE2', 'GLU', 6.2)], [('CZ', 'PHE', 'CB', 'GLU', 9.85), ('CZ', 'PHE', 'CG', 'GLU', 8.37), ('CZ', 'PHE', 'CD', 'GLU', 8.05), ('CZ', 'PHE', 'OE1', 'GLU', 8.97), ('CZ', 'PHE', 'OE2', 'GLU', 7.12)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_PHE, d, 'P_1pow_1_2_3_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_GLU, d, 'P_1pow_1_2_3_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_GLU, d, 'P_1pow_1_2_3_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_PHE' :  match1,
		'ARG_GLU' :  match2,
		'PHE_GLU' :  match3}