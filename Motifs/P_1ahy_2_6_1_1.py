'''
FUNC:P_1ahy_2_6_1_1
PDB:1ahy
EC:2.6.1.1
RESI:trp,asp
LOCI:a-140,222;
'''
import motifFunctions as cmd
TRP_ASP = { 
	'distances':
		[[9.22, 8.61, 9.42, 7.37], [9.63, 8.75, 9.37, 7.5], [10.66, 9.7, 10.2, 8.51], [9.44, 8.4, 8.9, 7.14], [11.09, 9.97, 10.3, 8.81], [10.43, 9.25, 9.55, 8.07], [8.78, 7.75, 8.26, 6.5], [10.79, 9.5, 9.63, 8.42], [9.25, 8.09, 8.38, 6.97], [10.25, 8.96, 9.08, 7.92]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'ASP', 9.22), ('CB', 'TRP', 'CG', 'ASP', 8.61), ('CB', 'TRP', 'OD1', 'ASP', 9.42), ('CB', 'TRP', 'OD2', 'ASP', 7.37)], [('CG', 'TRP', 'CB', 'ASP', 9.63), ('CG', 'TRP', 'CG', 'ASP', 8.75), ('CG', 'TRP', 'OD1', 'ASP', 9.37), ('CG', 'TRP', 'OD2', 'ASP', 7.5)], [('CD1', 'TRP', 'CB', 'ASP', 10.66), ('CD1', 'TRP', 'CG', 'ASP', 9.7), ('CD1', 'TRP', 'OD1', 'ASP', 10.2), ('CD1', 'TRP', 'OD2', 'ASP', 8.51)], [('CD2', 'TRP', 'CB', 'ASP', 9.44), ('CD2', 'TRP', 'CG', 'ASP', 8.4), ('CD2', 'TRP', 'OD1', 'ASP', 8.9), ('CD2', 'TRP', 'OD2', 'ASP', 7.14)], [('NE1', 'TRP', 'CB', 'ASP', 11.09), ('NE1', 'TRP', 'CG', 'ASP', 9.97), ('NE1', 'TRP', 'OD1', 'ASP', 10.3), ('NE1', 'TRP', 'OD2', 'ASP', 8.81)], [('CE2', 'TRP', 'CB', 'ASP', 10.43), ('CE2', 'TRP', 'CG', 'ASP', 9.25), ('CE2', 'TRP', 'OD1', 'ASP', 9.55), ('CE2', 'TRP', 'OD2', 'ASP', 8.07)], [('CE3', 'TRP', 'CB', 'ASP', 8.78), ('CE3', 'TRP', 'CG', 'ASP', 7.75), ('CE3', 'TRP', 'OD1', 'ASP', 8.26), ('CE3', 'TRP', 'OD2', 'ASP', 6.5)], [('CZ2', 'TRP', 'CB', 'ASP', 10.79), ('CZ2', 'TRP', 'CG', 'ASP', 9.5), ('CZ2', 'TRP', 'OD1', 'ASP', 9.63), ('CZ2', 'TRP', 'OD2', 'ASP', 8.42)], [('CZ3', 'TRP', 'CB', 'ASP', 9.25), ('CZ3', 'TRP', 'CG', 'ASP', 8.09), ('CZ3', 'TRP', 'OD1', 'ASP', 8.38), ('CZ3', 'TRP', 'OD2', 'ASP', 6.97)], [('CH2', 'TRP', 'CB', 'ASP', 10.25), ('CH2', 'TRP', 'CG', 'ASP', 8.96), ('CH2', 'TRP', 'OD1', 'ASP', 9.08), ('CH2', 'TRP', 'OD2', 'ASP', 7.92)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_ASP, d, 'P_1ahy_2_6_1_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_ASP' :  match1}