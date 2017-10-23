'''
FUNC:P_1ajo_3_2_1_73
PDB:1ajo
EC:3.2.1.73
RESI:glu,asp,glu
LOCI:a-193,195,197;
'''
import motifFunctions as cmd
GLU_GLU = { 
	'distances':
		[[12.88, 11.57, 11.03, 10.95, 11.01], [11.43, 10.1, 9.61, 9.61, 9.6], [11.06, 9.65, 9.01, 9.1, 8.77], [12.05, 10.63, 9.88, 9.96, 9.49], [9.91, 8.48, 7.83, 8.03, 7.53], [12.88, 11.43, 11.06, 12.05, 9.91], [11.57, 10.1, 9.65, 10.63, 8.48], [11.03, 9.61, 9.01, 9.88, 7.83], [10.95, 9.61, 9.1, 9.96, 8.03], [11.01, 9.6, 8.77, 9.49, 7.53]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.88), ('CB', 'GLU', 'CG', 'GLU', 11.57), ('CB', 'GLU', 'CD', 'GLU', 11.03), ('CB', 'GLU', 'OE1', 'GLU', 10.95), ('CB', 'GLU', 'OE2', 'GLU', 11.01)], [('CG', 'GLU', 'CB', 'GLU', 11.43), ('CG', 'GLU', 'CG', 'GLU', 10.1), ('CG', 'GLU', 'CD', 'GLU', 9.61), ('CG', 'GLU', 'OE1', 'GLU', 9.61), ('CG', 'GLU', 'OE2', 'GLU', 9.6)], [('CD', 'GLU', 'CB', 'GLU', 11.06), ('CD', 'GLU', 'CG', 'GLU', 9.65), ('CD', 'GLU', 'CD', 'GLU', 9.01), ('CD', 'GLU', 'OE1', 'GLU', 9.1), ('CD', 'GLU', 'OE2', 'GLU', 8.77)], [('OE1', 'GLU', 'CB', 'GLU', 12.05), ('OE1', 'GLU', 'CG', 'GLU', 10.63), ('OE1', 'GLU', 'CD', 'GLU', 9.88), ('OE1', 'GLU', 'OE1', 'GLU', 9.96), ('OE1', 'GLU', 'OE2', 'GLU', 9.49)], [('OE2', 'GLU', 'CB', 'GLU', 9.91), ('OE2', 'GLU', 'CG', 'GLU', 8.48), ('OE2', 'GLU', 'CD', 'GLU', 7.83), ('OE2', 'GLU', 'OE1', 'GLU', 8.03), ('OE2', 'GLU', 'OE2', 'GLU', 7.53)], [('CB', 'GLU', 'CB', 'GLU', 12.88), ('CB', 'GLU', 'CG', 'GLU', 11.43), ('CB', 'GLU', 'CD', 'GLU', 11.06), ('CB', 'GLU', 'OE1', 'GLU', 12.05), ('CB', 'GLU', 'OE2', 'GLU', 9.91)], [('CG', 'GLU', 'CB', 'GLU', 11.57), ('CG', 'GLU', 'CG', 'GLU', 10.1), ('CG', 'GLU', 'CD', 'GLU', 9.65), ('CG', 'GLU', 'OE1', 'GLU', 10.63), ('CG', 'GLU', 'OE2', 'GLU', 8.48)], [('CD', 'GLU', 'CB', 'GLU', 11.03), ('CD', 'GLU', 'CG', 'GLU', 9.61), ('CD', 'GLU', 'CD', 'GLU', 9.01), ('CD', 'GLU', 'OE1', 'GLU', 9.88), ('CD', 'GLU', 'OE2', 'GLU', 7.83)], [('OE1', 'GLU', 'CB', 'GLU', 10.95), ('OE1', 'GLU', 'CG', 'GLU', 9.61), ('OE1', 'GLU', 'CD', 'GLU', 9.1), ('OE1', 'GLU', 'OE1', 'GLU', 9.96), ('OE1', 'GLU', 'OE2', 'GLU', 8.03)], [('OE2', 'GLU', 'CB', 'GLU', 11.01), ('OE2', 'GLU', 'CG', 'GLU', 9.6), ('OE2', 'GLU', 'CD', 'GLU', 8.77), ('OE2', 'GLU', 'OE1', 'GLU', 9.49), ('OE2', 'GLU', 'OE2', 'GLU', 7.53)]]}
GLU_ASP = { 
	'distances':
		[[8.41, 7.16, 6.62, 6.99], [7.12, 5.81, 5.15, 5.82], [7.42, 5.94, 5.16, 5.87], [8.61, 7.11, 6.38, 6.9], [6.74, 5.28, 4.43, 5.37], [7.05, 7.83, 8.34, 8.32], [6.17, 6.68, 7.01, 7.27], [6.18, 6.33, 6.76, 6.6], [5.99, 6.2, 6.91, 6.19], [6.98, 6.79, 6.96, 7.02]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 8.41), ('CB', 'GLU', 'CG', 'ASP', 7.16), ('CB', 'GLU', 'OD1', 'ASP', 6.62), ('CB', 'GLU', 'OD2', 'ASP', 6.99)], [('CG', 'GLU', 'CB', 'ASP', 7.12), ('CG', 'GLU', 'CG', 'ASP', 5.81), ('CG', 'GLU', 'OD1', 'ASP', 5.15), ('CG', 'GLU', 'OD2', 'ASP', 5.82)], [('CD', 'GLU', 'CB', 'ASP', 7.42), ('CD', 'GLU', 'CG', 'ASP', 5.94), ('CD', 'GLU', 'OD1', 'ASP', 5.16), ('CD', 'GLU', 'OD2', 'ASP', 5.87)], [('OE1', 'GLU', 'CB', 'ASP', 8.61), ('OE1', 'GLU', 'CG', 'ASP', 7.11), ('OE1', 'GLU', 'OD1', 'ASP', 6.38), ('OE1', 'GLU', 'OD2', 'ASP', 6.9)], [('OE2', 'GLU', 'CB', 'ASP', 6.74), ('OE2', 'GLU', 'CG', 'ASP', 5.28), ('OE2', 'GLU', 'OD1', 'ASP', 4.43), ('OE2', 'GLU', 'OD2', 'ASP', 5.37)], [('CB', 'GLU', 'CB', 'ASP', 7.05), ('CB', 'GLU', 'CG', 'ASP', 7.83), ('CB', 'GLU', 'OD1', 'ASP', 8.34), ('CB', 'GLU', 'OD2', 'ASP', 8.32)], [('CG', 'GLU', 'CB', 'ASP', 6.17), ('CG', 'GLU', 'CG', 'ASP', 6.68), ('CG', 'GLU', 'OD1', 'ASP', 7.01), ('CG', 'GLU', 'OD2', 'ASP', 7.27)], [('CD', 'GLU', 'CB', 'ASP', 6.18), ('CD', 'GLU', 'CG', 'ASP', 6.33), ('CD', 'GLU', 'OD1', 'ASP', 6.76), ('CD', 'GLU', 'OD2', 'ASP', 6.6)], [('OE1', 'GLU', 'CB', 'ASP', 5.99), ('OE1', 'GLU', 'CG', 'ASP', 6.2), ('OE1', 'GLU', 'OD1', 'ASP', 6.91), ('OE1', 'GLU', 'OD2', 'ASP', 6.19)], [('OE2', 'GLU', 'CB', 'ASP', 6.98), ('OE2', 'GLU', 'CG', 'ASP', 6.79), ('OE2', 'GLU', 'OD1', 'ASP', 6.96), ('OE2', 'GLU', 'OD2', 'ASP', 7.02)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLU, d, 'P_1ajo_3_2_1_73')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ASP, d, 'P_1ajo_3_2_1_73')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLU' :  match1,
		'GLU_ASP' :  match2}