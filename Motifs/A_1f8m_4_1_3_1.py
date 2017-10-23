'''
FUNC:A_1f8m_4_1_3_1
PDB:1f8m
EC:4.1.3.1
RESI:his,cys,arg
LOCI:a-180,191,228;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[15.68, 15.7], [14.5, 14.52], [13.29, 13.42], [14.39, 14.3], [12.4, 12.47], [13.1, 13.04]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 15.68), ('CB', 'HIS', 'SG', 'CYS', 15.7)], [('CG', 'HIS', 'CB', 'CYS', 14.5), ('CG', 'HIS', 'SG', 'CYS', 14.52)], [('ND1', 'HIS', 'CB', 'CYS', 13.29), ('ND1', 'HIS', 'SG', 'CYS', 13.42)], [('CD2', 'HIS', 'CB', 'CYS', 14.39), ('CD2', 'HIS', 'SG', 'CYS', 14.3)], [('CE1', 'HIS', 'CB', 'CYS', 12.4), ('CE1', 'HIS', 'SG', 'CYS', 12.47)], [('NE2', 'HIS', 'CB', 'CYS', 13.1), ('NE2', 'HIS', 'SG', 'CYS', 13.04)]]}
HIS_ARG = { 
	'distances':
		[[7.26, 8.35, 8.11, 9.4, 9.87, 9.25, 11.16], [7.59, 8.39, 7.79, 8.94, 9.16, 8.36, 10.42], [7.13, 7.7, 6.89, 7.88, 8.0, 7.19, 9.21], [8.58, 9.21, 8.46, 9.54, 9.59, 8.61, 10.82], [7.9, 8.19, 7.11, 7.91, 7.75, 6.73, 8.89], [8.71, 9.07, 8.06, 8.95, 8.78, 7.68, 9.93]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 7.26), ('CB', 'HIS', 'CG', 'ARG', 8.35), ('CB', 'HIS', 'CD', 'ARG', 8.11), ('CB', 'HIS', 'NE', 'ARG', 9.4), ('CB', 'HIS', 'CZ', 'ARG', 9.87), ('CB', 'HIS', 'NH1', 'ARG', 9.25), ('CB', 'HIS', 'NH2', 'ARG', 11.16)], [('CG', 'HIS', 'CB', 'ARG', 7.59), ('CG', 'HIS', 'CG', 'ARG', 8.39), ('CG', 'HIS', 'CD', 'ARG', 7.79), ('CG', 'HIS', 'NE', 'ARG', 8.94), ('CG', 'HIS', 'CZ', 'ARG', 9.16), ('CG', 'HIS', 'NH1', 'ARG', 8.36), ('CG', 'HIS', 'NH2', 'ARG', 10.42)], [('ND1', 'HIS', 'CB', 'ARG', 7.13), ('ND1', 'HIS', 'CG', 'ARG', 7.7), ('ND1', 'HIS', 'CD', 'ARG', 6.89), ('ND1', 'HIS', 'NE', 'ARG', 7.88), ('ND1', 'HIS', 'CZ', 'ARG', 8.0), ('ND1', 'HIS', 'NH1', 'ARG', 7.19), ('ND1', 'HIS', 'NH2', 'ARG', 9.21)], [('CD2', 'HIS', 'CB', 'ARG', 8.58), ('CD2', 'HIS', 'CG', 'ARG', 9.21), ('CD2', 'HIS', 'CD', 'ARG', 8.46), ('CD2', 'HIS', 'NE', 'ARG', 9.54), ('CD2', 'HIS', 'CZ', 'ARG', 9.59), ('CD2', 'HIS', 'NH1', 'ARG', 8.61), ('CD2', 'HIS', 'NH2', 'ARG', 10.82)], [('CE1', 'HIS', 'CB', 'ARG', 7.9), ('CE1', 'HIS', 'CG', 'ARG', 8.19), ('CE1', 'HIS', 'CD', 'ARG', 7.11), ('CE1', 'HIS', 'NE', 'ARG', 7.91), ('CE1', 'HIS', 'CZ', 'ARG', 7.75), ('CE1', 'HIS', 'NH1', 'ARG', 6.73), ('CE1', 'HIS', 'NH2', 'ARG', 8.89)], [('NE2', 'HIS', 'CB', 'ARG', 8.71), ('NE2', 'HIS', 'CG', 'ARG', 9.07), ('NE2', 'HIS', 'CD', 'ARG', 8.06), ('NE2', 'HIS', 'NE', 'ARG', 8.95), ('NE2', 'HIS', 'CZ', 'ARG', 8.78), ('NE2', 'HIS', 'NH1', 'ARG', 7.68), ('NE2', 'HIS', 'NH2', 'ARG', 9.93)]]}
ARG_CYS = { 
	'distances':
		[[13.89, 13.85], [12.68, 12.58], [11.37, 11.3], [10.2, 10.23], [8.94, 9.01], [8.81, 8.82], [7.99, 8.19]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYS', 13.89), ('CB', 'ARG', 'SG', 'CYS', 13.85)], [('CG', 'ARG', 'CB', 'CYS', 12.68), ('CG', 'ARG', 'SG', 'CYS', 12.58)], [('CD', 'ARG', 'CB', 'CYS', 11.37), ('CD', 'ARG', 'SG', 'CYS', 11.3)], [('NE', 'ARG', 'CB', 'CYS', 10.2), ('NE', 'ARG', 'SG', 'CYS', 10.23)], [('CZ', 'ARG', 'CB', 'CYS', 8.94), ('CZ', 'ARG', 'SG', 'CYS', 9.01)], [('NH1', 'ARG', 'CB', 'CYS', 8.81), ('NH1', 'ARG', 'SG', 'CYS', 8.82)], [('NH2', 'ARG', 'CB', 'CYS', 7.99), ('NH2', 'ARG', 'SG', 'CYS', 8.19)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_1f8m_4_1_3_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ARG, d, 'A_1f8m_4_1_3_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_CYS, d, 'A_1f8m_4_1_3_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'HIS_ARG' :  match2,
		'ARG_CYS' :  match3}