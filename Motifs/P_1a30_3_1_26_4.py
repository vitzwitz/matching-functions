'''
FUNC:P_1a30_3_1_26_4
PDB:1a30
EC:3.1.26.4
RESI:asp,thr
LOCI:a-25,26;
'''
import motifFunctions as cmd
ASP_THR = { 
	'distances':
		[[7.11, 7.27, 7.51, 7.19, 6.12, 5.85, 4.65], [7.27, 7.18, 7.96, 6.94, 5.9, 6.04, 5.0], [6.45, 6.2, 7.31, 6.09, 5.03, 5.34, 4.45], [8.47, 8.35, 9.2, 7.9, 6.94, 7.22, 6.23], [5.23, 5.88, 5.81, 4.88, 4.03, 3.74, 3.24], [4.73, 5.18, 5.15, 5.17, 4.09, 3.42, 2.33], [5.92, 6.13, 6.12, 6.62, 5.48, 4.82, 3.45], [6.65, 7.01, 6.47, 7.69, 6.61, 5.68, 4.36]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 7.11), ('CB', 'ASP', 'OG1', 'THR', 7.27), ('CB', 'ASP', 'CG2', 'THR', 7.51), ('CB', 'ASP', 'O', 'THR', 7.19), ('CB', 'ASP', 'C', 'THR', 6.12), ('CB', 'ASP', 'CA', 'THR', 5.85), ('CB', 'ASP', 'N', 'THR', 4.65)], [('CG', 'ASP', 'CB', 'THR', 7.27), ('CG', 'ASP', 'OG1', 'THR', 7.18), ('CG', 'ASP', 'CG2', 'THR', 7.96), ('CG', 'ASP', 'O', 'THR', 6.94), ('CG', 'ASP', 'C', 'THR', 5.9), ('CG', 'ASP', 'CA', 'THR', 6.04), ('CG', 'ASP', 'N', 'THR', 5.0)], [('OD1', 'ASP', 'CB', 'THR', 6.45), ('OD1', 'ASP', 'OG1', 'THR', 6.2), ('OD1', 'ASP', 'CG2', 'THR', 7.31), ('OD1', 'ASP', 'O', 'THR', 6.09), ('OD1', 'ASP', 'C', 'THR', 5.03), ('OD1', 'ASP', 'CA', 'THR', 5.34), ('OD1', 'ASP', 'N', 'THR', 4.45)], [('OD2', 'ASP', 'CB', 'THR', 8.47), ('OD2', 'ASP', 'OG1', 'THR', 8.35), ('OD2', 'ASP', 'CG2', 'THR', 9.2), ('OD2', 'ASP', 'O', 'THR', 7.9), ('OD2', 'ASP', 'C', 'THR', 6.94), ('OD2', 'ASP', 'CA', 'THR', 7.22), ('OD2', 'ASP', 'N', 'THR', 6.23)], [('O', 'ASP', 'CB', 'THR', 5.23), ('O', 'ASP', 'OG1', 'THR', 5.88), ('O', 'ASP', 'CG2', 'THR', 5.81), ('O', 'ASP', 'O', 'THR', 4.88), ('O', 'ASP', 'C', 'THR', 4.03), ('O', 'ASP', 'CA', 'THR', 3.74), ('O', 'ASP', 'N', 'THR', 3.24)], [('C', 'ASP', 'CB', 'THR', 4.73), ('C', 'ASP', 'OG1', 'THR', 5.18), ('C', 'ASP', 'CG2', 'THR', 5.15), ('C', 'ASP', 'O', 'THR', 5.17), ('C', 'ASP', 'C', 'THR', 4.09), ('C', 'ASP', 'CA', 'THR', 3.42), ('C', 'ASP', 'N', 'THR', 2.33)], [('CA', 'ASP', 'CB', 'THR', 5.92), ('CA', 'ASP', 'OG1', 'THR', 6.13), ('CA', 'ASP', 'CG2', 'THR', 6.12), ('CA', 'ASP', 'O', 'THR', 6.62), ('CA', 'ASP', 'C', 'THR', 5.48), ('CA', 'ASP', 'CA', 'THR', 4.82), ('CA', 'ASP', 'N', 'THR', 3.45)], [('N', 'ASP', 'CB', 'THR', 6.65), ('N', 'ASP', 'OG1', 'THR', 7.01), ('N', 'ASP', 'CG2', 'THR', 6.47), ('N', 'ASP', 'O', 'THR', 7.69), ('N', 'ASP', 'C', 'THR', 6.61), ('N', 'ASP', 'CA', 'THR', 5.68), ('N', 'ASP', 'N', 'THR', 4.36)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_THR, d, 'P_1a30_3_1_26_4')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_THR' :  match1}