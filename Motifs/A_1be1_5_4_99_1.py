'''
FUNC:A_1be1_5_4_99_1
PDB:1be1
EC:5.4.99.1
RESI:asp,his
LOCI:a-14,16;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[8.09, 8.59, 8.04, 9.95, 9.17, 10.24], [9.14, 9.59, 8.93, 10.95, 10.0, 11.15], [10.22, 10.75, 10.13, 12.12, 11.22, 12.36], [9.06, 9.36, 8.6, 10.68, 9.59, 10.78]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.09), ('CB', 'ASP', 'CG', 'HIS', 8.59), ('CB', 'ASP', 'ND1', 'HIS', 8.04), ('CB', 'ASP', 'CD2', 'HIS', 9.95), ('CB', 'ASP', 'CE1', 'HIS', 9.17), ('CB', 'ASP', 'NE2', 'HIS', 10.24)], [('CG', 'ASP', 'CB', 'HIS', 9.14), ('CG', 'ASP', 'CG', 'HIS', 9.59), ('CG', 'ASP', 'ND1', 'HIS', 8.93), ('CG', 'ASP', 'CD2', 'HIS', 10.95), ('CG', 'ASP', 'CE1', 'HIS', 10.0), ('CG', 'ASP', 'NE2', 'HIS', 11.15)], [('OD1', 'ASP', 'CB', 'HIS', 10.22), ('OD1', 'ASP', 'CG', 'HIS', 10.75), ('OD1', 'ASP', 'ND1', 'HIS', 10.13), ('OD1', 'ASP', 'CD2', 'HIS', 12.12), ('OD1', 'ASP', 'CE1', 'HIS', 11.22), ('OD1', 'ASP', 'NE2', 'HIS', 12.36)], [('OD2', 'ASP', 'CB', 'HIS', 9.06), ('OD2', 'ASP', 'CG', 'HIS', 9.36), ('OD2', 'ASP', 'ND1', 'HIS', 8.6), ('OD2', 'ASP', 'CD2', 'HIS', 10.68), ('OD2', 'ASP', 'CE1', 'HIS', 9.59), ('OD2', 'ASP', 'NE2', 'HIS', 10.78)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1be1_5_4_99_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1}