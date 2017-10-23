'''
FUNC:A_1boo_2_1_1_113
PDB:1boo
EC:2.1.1.113
RESI:ser,pro,asp
LOCI:a-53,54,96;
'''
import motifFunctions as cmd
ASP_PRO = { 
	'distances':
		[[9.71, 9.11, 7.65, 9.25, 9.82, 9.29, 7.9], [10.25, 9.9, 8.43, 9.22, 9.99, 9.75, 8.47], [10.89, 10.57, 9.15, 9.85, 10.7, 10.52, 9.31], [10.32, 10.12, 8.64, 8.87, 9.69, 9.61, 8.4]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'PRO', 9.71), ('CB', 'ASP', 'CG', 'PRO', 9.11), ('CB', 'ASP', 'CD', 'PRO', 7.65), ('CB', 'ASP', 'O', 'PRO', 9.25), ('CB', 'ASP', 'C', 'PRO', 9.82), ('CB', 'ASP', 'CA', 'PRO', 9.29), ('CB', 'ASP', 'N', 'PRO', 7.9)], [('CG', 'ASP', 'CB', 'PRO', 10.25), ('CG', 'ASP', 'CG', 'PRO', 9.9), ('CG', 'ASP', 'CD', 'PRO', 8.43), ('CG', 'ASP', 'O', 'PRO', 9.22), ('CG', 'ASP', 'C', 'PRO', 9.99), ('CG', 'ASP', 'CA', 'PRO', 9.75), ('CG', 'ASP', 'N', 'PRO', 8.47)], [('OD1', 'ASP', 'CB', 'PRO', 10.89), ('OD1', 'ASP', 'CG', 'PRO', 10.57), ('OD1', 'ASP', 'CD', 'PRO', 9.15), ('OD1', 'ASP', 'O', 'PRO', 9.85), ('OD1', 'ASP', 'C', 'PRO', 10.7), ('OD1', 'ASP', 'CA', 'PRO', 10.52), ('OD1', 'ASP', 'N', 'PRO', 9.31)], [('OD2', 'ASP', 'CB', 'PRO', 10.32), ('OD2', 'ASP', 'CG', 'PRO', 10.12), ('OD2', 'ASP', 'CD', 'PRO', 8.64), ('OD2', 'ASP', 'O', 'PRO', 8.87), ('OD2', 'ASP', 'C', 'PRO', 9.69), ('OD2', 'ASP', 'CA', 'PRO', 9.61), ('OD2', 'ASP', 'N', 'PRO', 8.4)]]}
SER_PRO = { 
	'distances':
		[[7.89, 7.65, 6.23, 6.85, 7.29, 6.94, 5.67], [8.45, 8.4, 7.1, 6.95, 7.36, 7.24, 6.19]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'PRO', 7.89), ('CB', 'SER', 'CG', 'PRO', 7.65), ('CB', 'SER', 'CD', 'PRO', 6.23), ('CB', 'SER', 'O', 'PRO', 6.85), ('CB', 'SER', 'C', 'PRO', 7.29), ('CB', 'SER', 'CA', 'PRO', 6.94), ('CB', 'SER', 'N', 'PRO', 5.67)], [('OG', 'SER', 'CB', 'PRO', 8.45), ('OG', 'SER', 'CG', 'PRO', 8.4), ('OG', 'SER', 'CD', 'PRO', 7.1), ('OG', 'SER', 'O', 'PRO', 6.95), ('OG', 'SER', 'C', 'PRO', 7.36), ('OG', 'SER', 'CA', 'PRO', 7.24), ('OG', 'SER', 'N', 'PRO', 6.19)]]}
SER_ASP = { 
	'distances':
		[[5.27, 5.59, 6.73, 5.16], [6.45, 6.53, 7.68, 5.77]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 5.27), ('CB', 'SER', 'CG', 'ASP', 5.59), ('CB', 'SER', 'OD1', 'ASP', 6.73), ('CB', 'SER', 'OD2', 'ASP', 5.16)], [('OG', 'SER', 'CB', 'ASP', 6.45), ('OG', 'SER', 'CG', 'ASP', 6.53), ('OG', 'SER', 'OD1', 'ASP', 7.68), ('OG', 'SER', 'OD2', 'ASP', 5.77)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_PRO, d, 'A_1boo_2_1_1_113')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_PRO, d, 'A_1boo_2_1_1_113')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_ASP, d, 'A_1boo_2_1_1_113')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_PRO' :  match1,
		'SER_PRO' :  match2,
		'SER_ASP' :  match3}