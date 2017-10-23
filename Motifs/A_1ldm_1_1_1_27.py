'''
FUNC:A_1ldm_1_1_1_27
PDB:1ldm
EC:1.1.1.27
RESI:asp,arg,his
LOCI:a-166,169,193;
'''
import motifFunctions as cmd
ARG_ASP = { 
	'distances':
		[[7.61, 8.28, 8.13, 9.17], [7.87, 8.22, 8.04, 8.93], [7.78, 7.82, 7.38, 8.54], [8.81, 8.6, 8.1, 9.14], [8.84, 8.37, 7.9, 8.7], [10.08, 9.5, 9.03, 9.7], [7.87, 7.21, 6.74, 7.47]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 7.61), ('CB', 'ARG', 'CG', 'ASP', 8.28), ('CB', 'ARG', 'OD1', 'ASP', 8.13), ('CB', 'ARG', 'OD2', 'ASP', 9.17)], [('CG', 'ARG', 'CB', 'ASP', 7.87), ('CG', 'ARG', 'CG', 'ASP', 8.22), ('CG', 'ARG', 'OD1', 'ASP', 8.04), ('CG', 'ARG', 'OD2', 'ASP', 8.93)], [('CD', 'ARG', 'CB', 'ASP', 7.78), ('CD', 'ARG', 'CG', 'ASP', 7.82), ('CD', 'ARG', 'OD1', 'ASP', 7.38), ('CD', 'ARG', 'OD2', 'ASP', 8.54)], [('NE', 'ARG', 'CB', 'ASP', 8.81), ('NE', 'ARG', 'CG', 'ASP', 8.6), ('NE', 'ARG', 'OD1', 'ASP', 8.1), ('NE', 'ARG', 'OD2', 'ASP', 9.14)], [('CZ', 'ARG', 'CB', 'ASP', 8.84), ('CZ', 'ARG', 'CG', 'ASP', 8.37), ('CZ', 'ARG', 'OD1', 'ASP', 7.9), ('CZ', 'ARG', 'OD2', 'ASP', 8.7)], [('NH1', 'ARG', 'CB', 'ASP', 10.08), ('NH1', 'ARG', 'CG', 'ASP', 9.5), ('NH1', 'ARG', 'OD1', 'ASP', 9.03), ('NH1', 'ARG', 'OD2', 'ASP', 9.7)], [('NH2', 'ARG', 'CB', 'ASP', 7.87), ('NH2', 'ARG', 'CG', 'ASP', 7.21), ('NH2', 'ARG', 'OD1', 'ASP', 6.74), ('NH2', 'ARG', 'OD2', 'ASP', 7.47)]]}
ASP_HIS = { 
	'distances':
		[[8.52, 8.0, 6.73, 8.89, 7.06, 8.35], [7.21, 6.58, 5.31, 7.44, 5.68, 6.94], [7.43, 6.68, 5.49, 7.38, 5.68, 6.82], [6.25, 5.64, 4.38, 6.57, 4.95, 6.21]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.52), ('CB', 'ASP', 'CG', 'HIS', 8.0), ('CB', 'ASP', 'ND1', 'HIS', 6.73), ('CB', 'ASP', 'CD2', 'HIS', 8.89), ('CB', 'ASP', 'CE1', 'HIS', 7.06), ('CB', 'ASP', 'NE2', 'HIS', 8.35)], [('CG', 'ASP', 'CB', 'HIS', 7.21), ('CG', 'ASP', 'CG', 'HIS', 6.58), ('CG', 'ASP', 'ND1', 'HIS', 5.31), ('CG', 'ASP', 'CD2', 'HIS', 7.44), ('CG', 'ASP', 'CE1', 'HIS', 5.68), ('CG', 'ASP', 'NE2', 'HIS', 6.94)], [('OD1', 'ASP', 'CB', 'HIS', 7.43), ('OD1', 'ASP', 'CG', 'HIS', 6.68), ('OD1', 'ASP', 'ND1', 'HIS', 5.49), ('OD1', 'ASP', 'CD2', 'HIS', 7.38), ('OD1', 'ASP', 'CE1', 'HIS', 5.68), ('OD1', 'ASP', 'NE2', 'HIS', 6.82)], [('OD2', 'ASP', 'CB', 'HIS', 6.25), ('OD2', 'ASP', 'CG', 'HIS', 5.64), ('OD2', 'ASP', 'ND1', 'HIS', 4.38), ('OD2', 'ASP', 'CD2', 'HIS', 6.57), ('OD2', 'ASP', 'CE1', 'HIS', 4.95), ('OD2', 'ASP', 'NE2', 'HIS', 6.21)]]}
ARG_HIS = { 
	'distances':
		[[13.15, 12.08, 10.74, 12.35, 10.19, 11.21], [12.68, 11.48, 10.17, 11.57, 9.43, 10.33], [11.98, 10.72, 9.49, 10.72, 8.67, 9.48], [12.15, 10.79, 9.66, 10.56, 8.66, 9.24], [11.32, 9.89, 8.86, 9.52, 7.74, 8.17], [11.89, 10.4, 9.53, 9.83, 8.3, 8.47], [9.97, 8.56, 7.52, 8.25, 6.42, 6.92]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 13.15), ('CB', 'ARG', 'CG', 'HIS', 12.08), ('CB', 'ARG', 'ND1', 'HIS', 10.74), ('CB', 'ARG', 'CD2', 'HIS', 12.35), ('CB', 'ARG', 'CE1', 'HIS', 10.19), ('CB', 'ARG', 'NE2', 'HIS', 11.21)], [('CG', 'ARG', 'CB', 'HIS', 12.68), ('CG', 'ARG', 'CG', 'HIS', 11.48), ('CG', 'ARG', 'ND1', 'HIS', 10.17), ('CG', 'ARG', 'CD2', 'HIS', 11.57), ('CG', 'ARG', 'CE1', 'HIS', 9.43), ('CG', 'ARG', 'NE2', 'HIS', 10.33)], [('CD', 'ARG', 'CB', 'HIS', 11.98), ('CD', 'ARG', 'CG', 'HIS', 10.72), ('CD', 'ARG', 'ND1', 'HIS', 9.49), ('CD', 'ARG', 'CD2', 'HIS', 10.72), ('CD', 'ARG', 'CE1', 'HIS', 8.67), ('CD', 'ARG', 'NE2', 'HIS', 9.48)], [('NE', 'ARG', 'CB', 'HIS', 12.15), ('NE', 'ARG', 'CG', 'HIS', 10.79), ('NE', 'ARG', 'ND1', 'HIS', 9.66), ('NE', 'ARG', 'CD2', 'HIS', 10.56), ('NE', 'ARG', 'CE1', 'HIS', 8.66), ('NE', 'ARG', 'NE2', 'HIS', 9.24)], [('CZ', 'ARG', 'CB', 'HIS', 11.32), ('CZ', 'ARG', 'CG', 'HIS', 9.89), ('CZ', 'ARG', 'ND1', 'HIS', 8.86), ('CZ', 'ARG', 'CD2', 'HIS', 9.52), ('CZ', 'ARG', 'CE1', 'HIS', 7.74), ('CZ', 'ARG', 'NE2', 'HIS', 8.17)], [('NH1', 'ARG', 'CB', 'HIS', 11.89), ('NH1', 'ARG', 'CG', 'HIS', 10.4), ('NH1', 'ARG', 'ND1', 'HIS', 9.53), ('NH1', 'ARG', 'CD2', 'HIS', 9.83), ('NH1', 'ARG', 'CE1', 'HIS', 8.3), ('NH1', 'ARG', 'NE2', 'HIS', 8.47)], [('NH2', 'ARG', 'CB', 'HIS', 9.97), ('NH2', 'ARG', 'CG', 'HIS', 8.56), ('NH2', 'ARG', 'ND1', 'HIS', 7.52), ('NH2', 'ARG', 'CD2', 'HIS', 8.25), ('NH2', 'ARG', 'CE1', 'HIS', 6.42), ('NH2', 'ARG', 'NE2', 'HIS', 6.92)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_ASP, d, 'A_1ldm_1_1_1_27')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1ldm_1_1_1_27')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_HIS, d, 'A_1ldm_1_1_1_27')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_ASP' :  match1,
		'ASP_HIS' :  match2,
		'ARG_HIS' :  match3}