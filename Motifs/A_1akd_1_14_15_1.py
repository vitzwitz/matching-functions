'''
FUNC:A_1akd_1_14_15_1
PDB:1akd
EC:1.14.15.1
RESI:asp,thr
LOCI:a-251,252;
'''
import motifFunctions as cmd
ASP_THR = { 
	'distances':
		[[7.7, 8.15, 7.28, 8.43, 7.99, 6.88, 5.69], [8.4, 9.08, 8.04, 8.5, 8.34, 7.37, 6.4], [8.95, 9.59, 8.84, 8.45, 8.44, 7.73, 6.75], [8.67, 9.52, 8.12, 8.92, 8.83, 7.76, 7.02], [5.78, 6.71, 5.65, 6.08, 5.83, 4.71, 4.23], [5.47, 6.06, 5.53, 6.03, 5.5, 4.41, 3.33], [6.75, 7.03, 6.7, 7.28, 6.75, 5.81, 4.45], [6.95, 6.82, 6.9, 7.99, 7.22, 6.33, 4.89]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 7.7), ('CB', 'ASP', 'OG1', 'THR', 8.15), ('CB', 'ASP', 'CG2', 'THR', 7.28), ('CB', 'ASP', 'O', 'THR', 8.43), ('CB', 'ASP', 'C', 'THR', 7.99), ('CB', 'ASP', 'CA', 'THR', 6.88), ('CB', 'ASP', 'N', 'THR', 5.69)], [('CG', 'ASP', 'CB', 'THR', 8.4), ('CG', 'ASP', 'OG1', 'THR', 9.08), ('CG', 'ASP', 'CG2', 'THR', 8.04), ('CG', 'ASP', 'O', 'THR', 8.5), ('CG', 'ASP', 'C', 'THR', 8.34), ('CG', 'ASP', 'CA', 'THR', 7.37), ('CG', 'ASP', 'N', 'THR', 6.4)], [('OD1', 'ASP', 'CB', 'THR', 8.95), ('OD1', 'ASP', 'OG1', 'THR', 9.59), ('OD1', 'ASP', 'CG2', 'THR', 8.84), ('OD1', 'ASP', 'O', 'THR', 8.45), ('OD1', 'ASP', 'C', 'THR', 8.44), ('OD1', 'ASP', 'CA', 'THR', 7.73), ('OD1', 'ASP', 'N', 'THR', 6.75)], [('OD2', 'ASP', 'CB', 'THR', 8.67), ('OD2', 'ASP', 'OG1', 'THR', 9.52), ('OD2', 'ASP', 'CG2', 'THR', 8.12), ('OD2', 'ASP', 'O', 'THR', 8.92), ('OD2', 'ASP', 'C', 'THR', 8.83), ('OD2', 'ASP', 'CA', 'THR', 7.76), ('OD2', 'ASP', 'N', 'THR', 7.02)], [('O', 'ASP', 'CB', 'THR', 5.78), ('O', 'ASP', 'OG1', 'THR', 6.71), ('O', 'ASP', 'CG2', 'THR', 5.65), ('O', 'ASP', 'O', 'THR', 6.08), ('O', 'ASP', 'C', 'THR', 5.83), ('O', 'ASP', 'CA', 'THR', 4.71), ('O', 'ASP', 'N', 'THR', 4.23)], [('C', 'ASP', 'CB', 'THR', 5.47), ('C', 'ASP', 'OG1', 'THR', 6.06), ('C', 'ASP', 'CG2', 'THR', 5.53), ('C', 'ASP', 'O', 'THR', 6.03), ('C', 'ASP', 'C', 'THR', 5.5), ('C', 'ASP', 'CA', 'THR', 4.41), ('C', 'ASP', 'N', 'THR', 3.33)], [('CA', 'ASP', 'CB', 'THR', 6.75), ('CA', 'ASP', 'OG1', 'THR', 7.03), ('CA', 'ASP', 'CG2', 'THR', 6.7), ('CA', 'ASP', 'O', 'THR', 7.28), ('CA', 'ASP', 'C', 'THR', 6.75), ('CA', 'ASP', 'CA', 'THR', 5.81), ('CA', 'ASP', 'N', 'THR', 4.45)], [('N', 'ASP', 'CB', 'THR', 6.95), ('N', 'ASP', 'OG1', 'THR', 6.82), ('N', 'ASP', 'CG2', 'THR', 6.9), ('N', 'ASP', 'O', 'THR', 7.99), ('N', 'ASP', 'C', 'THR', 7.22), ('N', 'ASP', 'CA', 'THR', 6.33), ('N', 'ASP', 'N', 'THR', 4.89)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_THR, d, 'A_1akd_1_14_15_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_THR' :  match1}