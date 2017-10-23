'''
FUNC:A_1d1q_3_1_3_2
PDB:1d1q
EC:3.1.3.2
RESI:ala,arg,ser,asp
LOCI:a-13,19,20,132;
'''
import motifFunctions as cmd
ALA_SER = { 
	'distances':
		[5.8, 5.75],
	'comparisons':
		[('CB', 'ALA', 'CB', 'SER', 5.8), ('CB', 'ALA', 'OG', 'SER', 5.75)]}
ALA_ARG = { 
	'distances':
		[6.36, 7.35, 7.1, 6.18, 6.21, 7.06, 5.95],
	'comparisons':
		[('CB', 'ALA', 'CB', 'ARG', 6.36), ('CB', 'ALA', 'CG', 'ARG', 7.35), ('CB', 'ALA', 'CD', 'ARG', 7.1), ('CB', 'ALA', 'NE', 'ARG', 6.18), ('CB', 'ALA', 'CZ', 'ARG', 6.21), ('CB', 'ALA', 'NH1', 'ARG', 7.06), ('CB', 'ALA', 'NH2', 'ARG', 5.95)]}
ALA_ASP = { 
	'distances':
		[9.72, 9.62, 9.68, 9.79],
	'comparisons':
		[('CB', 'ALA', 'CB', 'ASP', 9.72), ('CB', 'ALA', 'CG', 'ASP', 9.62), ('CB', 'ALA', 'OD1', 'ASP', 9.68), ('CB', 'ALA', 'OD2', 'ASP', 9.79)]}
ARG_ASP = { 
	'distances':
		[[9.0, 9.13, 8.72, 9.93], [7.92, 8.16, 7.71, 9.12], [6.8, 7.3, 7.13, 8.22], [6.23, 6.48, 6.43, 7.21], [5.76, 6.18, 6.5, 6.72], [5.82, 6.68, 7.18, 7.25], [5.89, 5.97, 6.42, 6.17]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 9.0), ('CB', 'ARG', 'CG', 'ASP', 9.13), ('CB', 'ARG', 'OD1', 'ASP', 8.72), ('CB', 'ARG', 'OD2', 'ASP', 9.93)], [('CG', 'ARG', 'CB', 'ASP', 7.92), ('CG', 'ARG', 'CG', 'ASP', 8.16), ('CG', 'ARG', 'OD1', 'ASP', 7.71), ('CG', 'ARG', 'OD2', 'ASP', 9.12)], [('CD', 'ARG', 'CB', 'ASP', 6.8), ('CD', 'ARG', 'CG', 'ASP', 7.3), ('CD', 'ARG', 'OD1', 'ASP', 7.13), ('CD', 'ARG', 'OD2', 'ASP', 8.22)], [('NE', 'ARG', 'CB', 'ASP', 6.23), ('NE', 'ARG', 'CG', 'ASP', 6.48), ('NE', 'ARG', 'OD1', 'ASP', 6.43), ('NE', 'ARG', 'OD2', 'ASP', 7.21)], [('CZ', 'ARG', 'CB', 'ASP', 5.76), ('CZ', 'ARG', 'CG', 'ASP', 6.18), ('CZ', 'ARG', 'OD1', 'ASP', 6.5), ('CZ', 'ARG', 'OD2', 'ASP', 6.72)], [('NH1', 'ARG', 'CB', 'ASP', 5.82), ('NH1', 'ARG', 'CG', 'ASP', 6.68), ('NH1', 'ARG', 'OD1', 'ASP', 7.18), ('NH1', 'ARG', 'OD2', 'ASP', 7.25)], [('NH2', 'ARG', 'CB', 'ASP', 5.89), ('NH2', 'ARG', 'CG', 'ASP', 5.97), ('NH2', 'ARG', 'OD1', 'ASP', 6.42), ('NH2', 'ARG', 'OD2', 'ASP', 6.17)]]}
SER_ARG = { 
	'distances':
		[[7.24, 8.75, 9.25, 8.93, 9.47, 10.25, 9.53], [7.75, 9.18, 9.66, 9.11, 9.61, 10.54, 9.45]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 7.24), ('CB', 'SER', 'CG', 'ARG', 8.75), ('CB', 'SER', 'CD', 'ARG', 9.25), ('CB', 'SER', 'NE', 'ARG', 8.93), ('CB', 'SER', 'CZ', 'ARG', 9.47), ('CB', 'SER', 'NH1', 'ARG', 10.25), ('CB', 'SER', 'NH2', 'ARG', 9.53)], [('OG', 'SER', 'CB', 'ARG', 7.75), ('OG', 'SER', 'CG', 'ARG', 9.18), ('OG', 'SER', 'CD', 'ARG', 9.66), ('OG', 'SER', 'NE', 'ARG', 9.11), ('OG', 'SER', 'CZ', 'ARG', 9.61), ('OG', 'SER', 'NH1', 'ARG', 10.54), ('OG', 'SER', 'NH2', 'ARG', 9.45)]]}
SER_ASP = { 
	'distances':
		[[12.98, 12.82, 12.59, 13.15], [12.94, 12.59, 12.34, 12.8]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 12.98), ('CB', 'SER', 'CG', 'ASP', 12.82), ('CB', 'SER', 'OD1', 'ASP', 12.59), ('CB', 'SER', 'OD2', 'ASP', 13.15)], [('OG', 'SER', 'CB', 'ASP', 12.94), ('OG', 'SER', 'CG', 'ASP', 12.59), ('OG', 'SER', 'OD1', 'ASP', 12.34), ('OG', 'SER', 'OD2', 'ASP', 12.8)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ALA_SER, d, 'A_1d1q_3_1_3_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ALA_ARG, d, 'A_1d1q_3_1_3_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ALA_ASP, d, 'A_1d1q_3_1_3_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_ASP, d, 'A_1d1q_3_1_3_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_ARG, d, 'A_1d1q_3_1_3_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_ASP, d, 'A_1d1q_3_1_3_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ALA_SER' :  match1,
		'ALA_ARG' :  match2,
		'ALA_ASP' :  match3,
		'ARG_ASP' :  match4,
		'SER_ARG' :  match5,
		'SER_ASP' :  match6}