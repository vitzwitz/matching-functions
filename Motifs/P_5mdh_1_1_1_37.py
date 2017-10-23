'''
FUNC:P_5mdh_1_1_1_37
PDB:5mdh
EC:1.1.1.37
RESI:asp,arg,his
LOCI:a-158,161,186;
'''
import motifFunctions as cmd
ASP_ARG = { 
	'distances':
		[[7.37, 7.75, 7.17, 8.23, 8.35, 7.48, 9.59], [8.23, 8.31, 7.41, 8.19, 7.99, 6.91, 9.13], [7.92, 7.81, 6.69, 7.31, 6.96, 5.78, 8.07], [9.43, 9.5, 8.59, 9.28, 8.97, 7.82, 10.02]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 7.37), ('CB', 'ASP', 'CG', 'ARG', 7.75), ('CB', 'ASP', 'CD', 'ARG', 7.17), ('CB', 'ASP', 'NE', 'ARG', 8.23), ('CB', 'ASP', 'CZ', 'ARG', 8.35), ('CB', 'ASP', 'NH1', 'ARG', 7.48), ('CB', 'ASP', 'NH2', 'ARG', 9.59)], [('CG', 'ASP', 'CB', 'ARG', 8.23), ('CG', 'ASP', 'CG', 'ARG', 8.31), ('CG', 'ASP', 'CD', 'ARG', 7.41), ('CG', 'ASP', 'NE', 'ARG', 8.19), ('CG', 'ASP', 'CZ', 'ARG', 7.99), ('CG', 'ASP', 'NH1', 'ARG', 6.91), ('CG', 'ASP', 'NH2', 'ARG', 9.13)], [('OD1', 'ASP', 'CB', 'ARG', 7.92), ('OD1', 'ASP', 'CG', 'ARG', 7.81), ('OD1', 'ASP', 'CD', 'ARG', 6.69), ('OD1', 'ASP', 'NE', 'ARG', 7.31), ('OD1', 'ASP', 'CZ', 'ARG', 6.96), ('OD1', 'ASP', 'NH1', 'ARG', 5.78), ('OD1', 'ASP', 'NH2', 'ARG', 8.07)], [('OD2', 'ASP', 'CB', 'ARG', 9.43), ('OD2', 'ASP', 'CG', 'ARG', 9.5), ('OD2', 'ASP', 'CD', 'ARG', 8.59), ('OD2', 'ASP', 'NE', 'ARG', 9.28), ('OD2', 'ASP', 'CZ', 'ARG', 8.97), ('OD2', 'ASP', 'NH1', 'ARG', 7.82), ('OD2', 'ASP', 'NH2', 'ARG', 10.02)]]}
ASP_HIS = { 
	'distances':
		[[8.61, 8.06, 6.74, 8.87, 6.91, 8.23], [7.28, 6.63, 5.28, 7.41, 5.46, 6.79], [7.52, 6.62, 5.24, 7.15, 5.03, 6.31], [6.22, 5.78, 4.57, 6.77, 5.2, 6.44]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.61), ('CB', 'ASP', 'CG', 'HIS', 8.06), ('CB', 'ASP', 'ND1', 'HIS', 6.74), ('CB', 'ASP', 'CD2', 'HIS', 8.87), ('CB', 'ASP', 'CE1', 'HIS', 6.91), ('CB', 'ASP', 'NE2', 'HIS', 8.23)], [('CG', 'ASP', 'CB', 'HIS', 7.28), ('CG', 'ASP', 'CG', 'HIS', 6.63), ('CG', 'ASP', 'ND1', 'HIS', 5.28), ('CG', 'ASP', 'CD2', 'HIS', 7.41), ('CG', 'ASP', 'CE1', 'HIS', 5.46), ('CG', 'ASP', 'NE2', 'HIS', 6.79)], [('OD1', 'ASP', 'CB', 'HIS', 7.52), ('OD1', 'ASP', 'CG', 'HIS', 6.62), ('OD1', 'ASP', 'ND1', 'HIS', 5.24), ('OD1', 'ASP', 'CD2', 'HIS', 7.15), ('OD1', 'ASP', 'CE1', 'HIS', 5.03), ('OD1', 'ASP', 'NE2', 'HIS', 6.31)], [('OD2', 'ASP', 'CB', 'HIS', 6.22), ('OD2', 'ASP', 'CG', 'HIS', 5.78), ('OD2', 'ASP', 'ND1', 'HIS', 4.57), ('OD2', 'ASP', 'CD2', 'HIS', 6.77), ('OD2', 'ASP', 'CE1', 'HIS', 5.2), ('OD2', 'ASP', 'NE2', 'HIS', 6.44)]]}
ARG_HIS = { 
	'distances':
		[[13.36, 12.38, 11.01, 12.67, 10.45, 11.53], [13.13, 12.01, 10.69, 12.12, 9.95, 10.89], [11.97, 10.79, 9.5, 10.84, 8.69, 9.58], [12.22, 10.92, 9.74, 10.75, 8.73, 9.42], [11.44, 10.07, 8.99, 9.76, 7.88, 8.41], [10.18, 8.84, 7.75, 8.6, 6.67, 7.28], [12.09, 10.66, 9.72, 10.15, 8.51, 8.79]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 13.36), ('CB', 'ARG', 'CG', 'HIS', 12.38), ('CB', 'ARG', 'ND1', 'HIS', 11.01), ('CB', 'ARG', 'CD2', 'HIS', 12.67), ('CB', 'ARG', 'CE1', 'HIS', 10.45), ('CB', 'ARG', 'NE2', 'HIS', 11.53)], [('CG', 'ARG', 'CB', 'HIS', 13.13), ('CG', 'ARG', 'CG', 'HIS', 12.01), ('CG', 'ARG', 'ND1', 'HIS', 10.69), ('CG', 'ARG', 'CD2', 'HIS', 12.12), ('CG', 'ARG', 'CE1', 'HIS', 9.95), ('CG', 'ARG', 'NE2', 'HIS', 10.89)], [('CD', 'ARG', 'CB', 'HIS', 11.97), ('CD', 'ARG', 'CG', 'HIS', 10.79), ('CD', 'ARG', 'ND1', 'HIS', 9.5), ('CD', 'ARG', 'CD2', 'HIS', 10.84), ('CD', 'ARG', 'CE1', 'HIS', 8.69), ('CD', 'ARG', 'NE2', 'HIS', 9.58)], [('NE', 'ARG', 'CB', 'HIS', 12.22), ('NE', 'ARG', 'CG', 'HIS', 10.92), ('NE', 'ARG', 'ND1', 'HIS', 9.74), ('NE', 'ARG', 'CD2', 'HIS', 10.75), ('NE', 'ARG', 'CE1', 'HIS', 8.73), ('NE', 'ARG', 'NE2', 'HIS', 9.42)], [('CZ', 'ARG', 'CB', 'HIS', 11.44), ('CZ', 'ARG', 'CG', 'HIS', 10.07), ('CZ', 'ARG', 'ND1', 'HIS', 8.99), ('CZ', 'ARG', 'CD2', 'HIS', 9.76), ('CZ', 'ARG', 'CE1', 'HIS', 7.88), ('CZ', 'ARG', 'NE2', 'HIS', 8.41)], [('NH1', 'ARG', 'CB', 'HIS', 10.18), ('NH1', 'ARG', 'CG', 'HIS', 8.84), ('NH1', 'ARG', 'ND1', 'HIS', 7.75), ('NH1', 'ARG', 'CD2', 'HIS', 8.6), ('NH1', 'ARG', 'CE1', 'HIS', 6.67), ('NH1', 'ARG', 'NE2', 'HIS', 7.28)], [('NH2', 'ARG', 'CB', 'HIS', 12.09), ('NH2', 'ARG', 'CG', 'HIS', 10.66), ('NH2', 'ARG', 'ND1', 'HIS', 9.72), ('NH2', 'ARG', 'CD2', 'HIS', 10.15), ('NH2', 'ARG', 'CE1', 'HIS', 8.51), ('NH2', 'ARG', 'NE2', 'HIS', 8.79)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ARG, d, 'P_5mdh_1_1_1_37')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'P_5mdh_1_1_1_37')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_HIS, d, 'P_5mdh_1_1_1_37')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ARG' :  match1,
		'ASP_HIS' :  match2,
		'ARG_HIS' :  match3}