'''
FUNC:A_1qba_3_2_1_52
PDB:1qba
EC:3.2.1.52
RESI:asp,glu
LOCI:a-539,540;
'''
import motifFunctions as cmd
GLU_ASP = { 
	'distances':
		[[6.4, 6.72, 7.4, 6.81, 5.25, 5.08, 6.32, 7.51], [6.16, 6.61, 7.57, 6.49, 6.16, 5.66, 6.47, 7.83], [6.76, 6.86, 7.86, 6.34, 7.06, 6.74, 7.43, 8.72], [6.9, 6.61, 7.48, 5.93, 6.99, 6.93, 7.64, 8.79], [7.64, 7.83, 8.91, 7.21, 8.26, 7.83, 8.4, 9.74], [8.27, 8.5, 8.73, 8.86, 5.68, 6.07, 7.59, 8.36], [7.42, 7.88, 8.17, 8.41, 5.0, 5.12, 6.6, 7.41], [6.38, 7.03, 7.58, 7.47, 4.86, 4.47, 5.8, 6.93], [5.14, 6.03, 6.59, 6.69, 4.26, 3.33, 4.41, 5.61]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 6.4), ('CB', 'GLU', 'CG', 'ASP', 6.72), ('CB', 'GLU', 'OD1', 'ASP', 7.4), ('CB', 'GLU', 'OD2', 'ASP', 6.81), ('CB', 'GLU', 'O', 'ASP', 5.25), ('CB', 'GLU', 'C', 'ASP', 5.08), ('CB', 'GLU', 'CA', 'ASP', 6.32), ('CB', 'GLU', 'N', 'ASP', 7.51)], [('CG', 'GLU', 'CB', 'ASP', 6.16), ('CG', 'GLU', 'CG', 'ASP', 6.61), ('CG', 'GLU', 'OD1', 'ASP', 7.57), ('CG', 'GLU', 'OD2', 'ASP', 6.49), ('CG', 'GLU', 'O', 'ASP', 6.16), ('CG', 'GLU', 'C', 'ASP', 5.66), ('CG', 'GLU', 'CA', 'ASP', 6.47), ('CG', 'GLU', 'N', 'ASP', 7.83)], [('CD', 'GLU', 'CB', 'ASP', 6.76), ('CD', 'GLU', 'CG', 'ASP', 6.86), ('CD', 'GLU', 'OD1', 'ASP', 7.86), ('CD', 'GLU', 'OD2', 'ASP', 6.34), ('CD', 'GLU', 'O', 'ASP', 7.06), ('CD', 'GLU', 'C', 'ASP', 6.74), ('CD', 'GLU', 'CA', 'ASP', 7.43), ('CD', 'GLU', 'N', 'ASP', 8.72)], [('OE1', 'GLU', 'CB', 'ASP', 6.9), ('OE1', 'GLU', 'CG', 'ASP', 6.61), ('OE1', 'GLU', 'OD1', 'ASP', 7.48), ('OE1', 'GLU', 'OD2', 'ASP', 5.93), ('OE1', 'GLU', 'O', 'ASP', 6.99), ('OE1', 'GLU', 'C', 'ASP', 6.93), ('OE1', 'GLU', 'CA', 'ASP', 7.64), ('OE1', 'GLU', 'N', 'ASP', 8.79)], [('OE2', 'GLU', 'CB', 'ASP', 7.64), ('OE2', 'GLU', 'CG', 'ASP', 7.83), ('OE2', 'GLU', 'OD1', 'ASP', 8.91), ('OE2', 'GLU', 'OD2', 'ASP', 7.21), ('OE2', 'GLU', 'O', 'ASP', 8.26), ('OE2', 'GLU', 'C', 'ASP', 7.83), ('OE2', 'GLU', 'CA', 'ASP', 8.4), ('OE2', 'GLU', 'N', 'ASP', 9.74)], [('O', 'GLU', 'CB', 'ASP', 8.27), ('O', 'GLU', 'CG', 'ASP', 8.5), ('O', 'GLU', 'OD1', 'ASP', 8.73), ('O', 'GLU', 'OD2', 'ASP', 8.86), ('O', 'GLU', 'O', 'ASP', 5.68), ('O', 'GLU', 'C', 'ASP', 6.07), ('O', 'GLU', 'CA', 'ASP', 7.59), ('O', 'GLU', 'N', 'ASP', 8.36)], [('C', 'GLU', 'CB', 'ASP', 7.42), ('C', 'GLU', 'CG', 'ASP', 7.88), ('C', 'GLU', 'OD1', 'ASP', 8.17), ('C', 'GLU', 'OD2', 'ASP', 8.41), ('C', 'GLU', 'O', 'ASP', 5.0), ('C', 'GLU', 'C', 'ASP', 5.12), ('C', 'GLU', 'CA', 'ASP', 6.6), ('C', 'GLU', 'N', 'ASP', 7.41)], [('CA', 'GLU', 'CB', 'ASP', 6.38), ('CA', 'GLU', 'CG', 'ASP', 7.03), ('CA', 'GLU', 'OD1', 'ASP', 7.58), ('CA', 'GLU', 'OD2', 'ASP', 7.47), ('CA', 'GLU', 'O', 'ASP', 4.86), ('CA', 'GLU', 'C', 'ASP', 4.47), ('CA', 'GLU', 'CA', 'ASP', 5.8), ('CA', 'GLU', 'N', 'ASP', 6.93)], [('N', 'GLU', 'CB', 'ASP', 5.14), ('N', 'GLU', 'CG', 'ASP', 6.03), ('N', 'GLU', 'OD1', 'ASP', 6.59), ('N', 'GLU', 'OD2', 'ASP', 6.69), ('N', 'GLU', 'O', 'ASP', 4.26), ('N', 'GLU', 'C', 'ASP', 3.33), ('N', 'GLU', 'CA', 'ASP', 4.41), ('N', 'GLU', 'N', 'ASP', 5.61)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ASP, d, 'A_1qba_3_2_1_52')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ASP' :  match1}