'''
FUNC:P_1n7n_4_2_2_5
PDB:1n7n
EC:4.2.2.5
RESI:his,tyr,arg
LOCI:a-399,408,462;
'''
import motifFunctions as cmd
HIS_ARG = { 
	'distances':
		[[10.96, 10.49, 9.93, 10.25, 9.57, 8.34, 10.32], [10.42, 9.73, 9.1, 9.21, 8.4, 7.17, 9.02], [9.12, 8.39, 7.73, 7.85, 7.08, 5.86, 7.8], [11.19, 10.34, 9.67, 9.54, 8.56, 7.38, 8.96], [9.22, 8.26, 7.53, 7.35, 6.38, 5.2, 6.87], [10.51, 9.5, 8.79, 8.47, 7.4, 6.28, 7.68]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 10.96), ('CB', 'HIS', 'CG', 'ARG', 10.49), ('CB', 'HIS', 'CD', 'ARG', 9.93), ('CB', 'HIS', 'NE', 'ARG', 10.25), ('CB', 'HIS', 'CZ', 'ARG', 9.57), ('CB', 'HIS', 'NH1', 'ARG', 8.34), ('CB', 'HIS', 'NH2', 'ARG', 10.32)], [('CG', 'HIS', 'CB', 'ARG', 10.42), ('CG', 'HIS', 'CG', 'ARG', 9.73), ('CG', 'HIS', 'CD', 'ARG', 9.1), ('CG', 'HIS', 'NE', 'ARG', 9.21), ('CG', 'HIS', 'CZ', 'ARG', 8.4), ('CG', 'HIS', 'NH1', 'ARG', 7.17), ('CG', 'HIS', 'NH2', 'ARG', 9.02)], [('ND1', 'HIS', 'CB', 'ARG', 9.12), ('ND1', 'HIS', 'CG', 'ARG', 8.39), ('ND1', 'HIS', 'CD', 'ARG', 7.73), ('ND1', 'HIS', 'NE', 'ARG', 7.85), ('ND1', 'HIS', 'CZ', 'ARG', 7.08), ('ND1', 'HIS', 'NH1', 'ARG', 5.86), ('ND1', 'HIS', 'NH2', 'ARG', 7.8)], [('CD2', 'HIS', 'CB', 'ARG', 11.19), ('CD2', 'HIS', 'CG', 'ARG', 10.34), ('CD2', 'HIS', 'CD', 'ARG', 9.67), ('CD2', 'HIS', 'NE', 'ARG', 9.54), ('CD2', 'HIS', 'CZ', 'ARG', 8.56), ('CD2', 'HIS', 'NH1', 'ARG', 7.38), ('CD2', 'HIS', 'NH2', 'ARG', 8.96)], [('CE1', 'HIS', 'CB', 'ARG', 9.22), ('CE1', 'HIS', 'CG', 'ARG', 8.26), ('CE1', 'HIS', 'CD', 'ARG', 7.53), ('CE1', 'HIS', 'NE', 'ARG', 7.35), ('CE1', 'HIS', 'CZ', 'ARG', 6.38), ('CE1', 'HIS', 'NH1', 'ARG', 5.2), ('CE1', 'HIS', 'NH2', 'ARG', 6.87)], [('NE2', 'HIS', 'CB', 'ARG', 10.51), ('NE2', 'HIS', 'CG', 'ARG', 9.5), ('NE2', 'HIS', 'CD', 'ARG', 8.79), ('NE2', 'HIS', 'NE', 'ARG', 8.47), ('NE2', 'HIS', 'CZ', 'ARG', 7.4), ('NE2', 'HIS', 'NH1', 'ARG', 6.28), ('NE2', 'HIS', 'NH2', 'ARG', 7.68)]]}
TYR_ARG = { 
	'distances':
		[[12.04, 11.14, 11.47, 11.28, 10.27, 9.23, 10.49], [11.04, 10.03, 10.22, 9.93, 8.86, 7.83, 9.05], [11.57, 10.42, 10.44, 9.93, 8.74, 7.8, 8.7], [9.72, 8.77, 8.99, 8.83, 7.86, 6.76, 8.23], [10.93, 9.68, 9.52, 8.88, 7.62, 6.75, 7.48], [8.91, 7.84, 7.87, 7.6, 6.56, 5.45, 6.93], [9.61, 8.38, 8.19, 7.64, 6.42, 5.45, 6.47], [9.17, 7.85, 7.41, 6.69, 5.39, 4.54, 5.32]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 12.04), ('CB', 'TYR', 'CG', 'ARG', 11.14), ('CB', 'TYR', 'CD', 'ARG', 11.47), ('CB', 'TYR', 'NE', 'ARG', 11.28), ('CB', 'TYR', 'CZ', 'ARG', 10.27), ('CB', 'TYR', 'NH1', 'ARG', 9.23), ('CB', 'TYR', 'NH2', 'ARG', 10.49)], [('CG', 'TYR', 'CB', 'ARG', 11.04), ('CG', 'TYR', 'CG', 'ARG', 10.03), ('CG', 'TYR', 'CD', 'ARG', 10.22), ('CG', 'TYR', 'NE', 'ARG', 9.93), ('CG', 'TYR', 'CZ', 'ARG', 8.86), ('CG', 'TYR', 'NH1', 'ARG', 7.83), ('CG', 'TYR', 'NH2', 'ARG', 9.05)], [('CD1', 'TYR', 'CB', 'ARG', 11.57), ('CD1', 'TYR', 'CG', 'ARG', 10.42), ('CD1', 'TYR', 'CD', 'ARG', 10.44), ('CD1', 'TYR', 'NE', 'ARG', 9.93), ('CD1', 'TYR', 'CZ', 'ARG', 8.74), ('CD1', 'TYR', 'NH1', 'ARG', 7.8), ('CD1', 'TYR', 'NH2', 'ARG', 8.7)], [('CD2', 'TYR', 'CB', 'ARG', 9.72), ('CD2', 'TYR', 'CG', 'ARG', 8.77), ('CD2', 'TYR', 'CD', 'ARG', 8.99), ('CD2', 'TYR', 'NE', 'ARG', 8.83), ('CD2', 'TYR', 'CZ', 'ARG', 7.86), ('CD2', 'TYR', 'NH1', 'ARG', 6.76), ('CD2', 'TYR', 'NH2', 'ARG', 8.23)], [('CE1', 'TYR', 'CB', 'ARG', 10.93), ('CE1', 'TYR', 'CG', 'ARG', 9.68), ('CE1', 'TYR', 'CD', 'ARG', 9.52), ('CE1', 'TYR', 'NE', 'ARG', 8.88), ('CE1', 'TYR', 'CZ', 'ARG', 7.62), ('CE1', 'TYR', 'NH1', 'ARG', 6.75), ('CE1', 'TYR', 'NH2', 'ARG', 7.48)], [('CE2', 'TYR', 'CB', 'ARG', 8.91), ('CE2', 'TYR', 'CG', 'ARG', 7.84), ('CE2', 'TYR', 'CD', 'ARG', 7.87), ('CE2', 'TYR', 'NE', 'ARG', 7.6), ('CE2', 'TYR', 'CZ', 'ARG', 6.56), ('CE2', 'TYR', 'NH1', 'ARG', 5.45), ('CE2', 'TYR', 'NH2', 'ARG', 6.93)], [('CZ', 'TYR', 'CB', 'ARG', 9.61), ('CZ', 'TYR', 'CG', 'ARG', 8.38), ('CZ', 'TYR', 'CD', 'ARG', 8.19), ('CZ', 'TYR', 'NE', 'ARG', 7.64), ('CZ', 'TYR', 'CZ', 'ARG', 6.42), ('CZ', 'TYR', 'NH1', 'ARG', 5.45), ('CZ', 'TYR', 'NH2', 'ARG', 6.47)], [('OH', 'TYR', 'CB', 'ARG', 9.17), ('OH', 'TYR', 'CG', 'ARG', 7.85), ('OH', 'TYR', 'CD', 'ARG', 7.41), ('OH', 'TYR', 'NE', 'ARG', 6.69), ('OH', 'TYR', 'CZ', 'ARG', 5.39), ('OH', 'TYR', 'NH1', 'ARG', 4.54), ('OH', 'TYR', 'NH2', 'ARG', 5.32)]]}
HIS_TYR = { 
	'distances':
		[[9.1, 8.32, 8.68, 7.65, 8.41, 7.32, 7.74, 7.89], [8.42, 7.42, 7.58, 6.76, 7.13, 6.22, 6.43, 6.47], [8.44, 7.27, 7.45, 6.38, 6.81, 5.58, 5.84, 5.66], [8.07, 7.01, 6.9, 6.62, 6.39, 6.08, 5.95, 6.01], [8.14, 6.81, 6.72, 6.03, 5.85, 5.0, 4.89, 4.49], [7.9, 6.62, 6.32, 6.17, 5.51, 5.34, 4.94, 4.74]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 9.1), ('CB', 'HIS', 'CG', 'TYR', 8.32), ('CB', 'HIS', 'CD1', 'TYR', 8.68), ('CB', 'HIS', 'CD2', 'TYR', 7.65), ('CB', 'HIS', 'CE1', 'TYR', 8.41), ('CB', 'HIS', 'CE2', 'TYR', 7.32), ('CB', 'HIS', 'CZ', 'TYR', 7.74), ('CB', 'HIS', 'OH', 'TYR', 7.89)], [('CG', 'HIS', 'CB', 'TYR', 8.42), ('CG', 'HIS', 'CG', 'TYR', 7.42), ('CG', 'HIS', 'CD1', 'TYR', 7.58), ('CG', 'HIS', 'CD2', 'TYR', 6.76), ('CG', 'HIS', 'CE1', 'TYR', 7.13), ('CG', 'HIS', 'CE2', 'TYR', 6.22), ('CG', 'HIS', 'CZ', 'TYR', 6.43), ('CG', 'HIS', 'OH', 'TYR', 6.47)], [('ND1', 'HIS', 'CB', 'TYR', 8.44), ('ND1', 'HIS', 'CG', 'TYR', 7.27), ('ND1', 'HIS', 'CD1', 'TYR', 7.45), ('ND1', 'HIS', 'CD2', 'TYR', 6.38), ('ND1', 'HIS', 'CE1', 'TYR', 6.81), ('ND1', 'HIS', 'CE2', 'TYR', 5.58), ('ND1', 'HIS', 'CZ', 'TYR', 5.84), ('ND1', 'HIS', 'OH', 'TYR', 5.66)], [('CD2', 'HIS', 'CB', 'TYR', 8.07), ('CD2', 'HIS', 'CG', 'TYR', 7.01), ('CD2', 'HIS', 'CD1', 'TYR', 6.9), ('CD2', 'HIS', 'CD2', 'TYR', 6.62), ('CD2', 'HIS', 'CE1', 'TYR', 6.39), ('CD2', 'HIS', 'CE2', 'TYR', 6.08), ('CD2', 'HIS', 'CZ', 'TYR', 5.95), ('CD2', 'HIS', 'OH', 'TYR', 6.01)], [('CE1', 'HIS', 'CB', 'TYR', 8.14), ('CE1', 'HIS', 'CG', 'TYR', 6.81), ('CE1', 'HIS', 'CD1', 'TYR', 6.72), ('CE1', 'HIS', 'CD2', 'TYR', 6.03), ('CE1', 'HIS', 'CE1', 'TYR', 5.85), ('CE1', 'HIS', 'CE2', 'TYR', 5.0), ('CE1', 'HIS', 'CZ', 'TYR', 4.89), ('CE1', 'HIS', 'OH', 'TYR', 4.49)], [('NE2', 'HIS', 'CB', 'TYR', 7.9), ('NE2', 'HIS', 'CG', 'TYR', 6.62), ('NE2', 'HIS', 'CD1', 'TYR', 6.32), ('NE2', 'HIS', 'CD2', 'TYR', 6.17), ('NE2', 'HIS', 'CE1', 'TYR', 5.51), ('NE2', 'HIS', 'CE2', 'TYR', 5.34), ('NE2', 'HIS', 'CZ', 'TYR', 4.94), ('NE2', 'HIS', 'OH', 'TYR', 4.74)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ARG, d, 'P_1n7n_4_2_2_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ARG, d, 'P_1n7n_4_2_2_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_TYR, d, 'P_1n7n_4_2_2_5')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ARG' :  match1,
		'TYR_ARG' :  match2,
		'HIS_TYR' :  match3}