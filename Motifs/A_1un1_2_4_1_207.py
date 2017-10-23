'''
FUNC:A_1un1_2_4_1_207
PDB:1un1
EC:2.4.1.207
RESI:glu,asp,glu
LOCI:a-85,87,89;
'''
import motifFunctions as cmd
GLU_GLU = { 
	'distances':
		[[13.21, 11.85, 11.45, 12.43, 10.27], [11.87, 10.49, 10.01, 10.97, 8.81], [11.55, 10.24, 9.56, 10.38, 8.34], [11.15, 9.94, 9.32, 10.14, 8.16], [11.95, 10.63, 9.77, 10.45, 8.53], [13.21, 11.87, 11.55, 11.15, 11.95], [11.85, 10.49, 10.24, 9.94, 10.63], [11.45, 10.01, 9.56, 9.32, 9.77], [12.43, 10.97, 10.38, 10.14, 10.45], [10.27, 8.81, 8.34, 8.16, 8.53]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 13.21), ('CB', 'GLU', 'CG', 'GLU', 11.85), ('CB', 'GLU', 'CD', 'GLU', 11.45), ('CB', 'GLU', 'OE1', 'GLU', 12.43), ('CB', 'GLU', 'OE2', 'GLU', 10.27)], [('CG', 'GLU', 'CB', 'GLU', 11.87), ('CG', 'GLU', 'CG', 'GLU', 10.49), ('CG', 'GLU', 'CD', 'GLU', 10.01), ('CG', 'GLU', 'OE1', 'GLU', 10.97), ('CG', 'GLU', 'OE2', 'GLU', 8.81)], [('CD', 'GLU', 'CB', 'GLU', 11.55), ('CD', 'GLU', 'CG', 'GLU', 10.24), ('CD', 'GLU', 'CD', 'GLU', 9.56), ('CD', 'GLU', 'OE1', 'GLU', 10.38), ('CD', 'GLU', 'OE2', 'GLU', 8.34)], [('OE1', 'GLU', 'CB', 'GLU', 11.15), ('OE1', 'GLU', 'CG', 'GLU', 9.94), ('OE1', 'GLU', 'CD', 'GLU', 9.32), ('OE1', 'GLU', 'OE1', 'GLU', 10.14), ('OE1', 'GLU', 'OE2', 'GLU', 8.16)], [('OE2', 'GLU', 'CB', 'GLU', 11.95), ('OE2', 'GLU', 'CG', 'GLU', 10.63), ('OE2', 'GLU', 'CD', 'GLU', 9.77), ('OE2', 'GLU', 'OE1', 'GLU', 10.45), ('OE2', 'GLU', 'OE2', 'GLU', 8.53)], [('CB', 'GLU', 'CB', 'GLU', 13.21), ('CB', 'GLU', 'CG', 'GLU', 11.87), ('CB', 'GLU', 'CD', 'GLU', 11.55), ('CB', 'GLU', 'OE1', 'GLU', 11.15), ('CB', 'GLU', 'OE2', 'GLU', 11.95)], [('CG', 'GLU', 'CB', 'GLU', 11.85), ('CG', 'GLU', 'CG', 'GLU', 10.49), ('CG', 'GLU', 'CD', 'GLU', 10.24), ('CG', 'GLU', 'OE1', 'GLU', 9.94), ('CG', 'GLU', 'OE2', 'GLU', 10.63)], [('CD', 'GLU', 'CB', 'GLU', 11.45), ('CD', 'GLU', 'CG', 'GLU', 10.01), ('CD', 'GLU', 'CD', 'GLU', 9.56), ('CD', 'GLU', 'OE1', 'GLU', 9.32), ('CD', 'GLU', 'OE2', 'GLU', 9.77)], [('OE1', 'GLU', 'CB', 'GLU', 12.43), ('OE1', 'GLU', 'CG', 'GLU', 10.97), ('OE1', 'GLU', 'CD', 'GLU', 10.38), ('OE1', 'GLU', 'OE1', 'GLU', 10.14), ('OE1', 'GLU', 'OE2', 'GLU', 10.45)], [('OE2', 'GLU', 'CB', 'GLU', 10.27), ('OE2', 'GLU', 'CG', 'GLU', 8.81), ('OE2', 'GLU', 'CD', 'GLU', 8.34), ('OE2', 'GLU', 'OE1', 'GLU', 8.16), ('OE2', 'GLU', 'OE2', 'GLU', 8.53)]]}
ASP_GLU = { 
	'distances':
		[[7.59, 6.61, 6.82, 6.4, 7.79], [8.39, 7.17, 7.07, 6.68, 7.8], [8.89, 7.56, 7.59, 7.45, 8.17], [8.85, 7.62, 7.18, 6.59, 7.82], [8.13, 6.95, 7.18, 8.38, 6.43], [6.9, 5.66, 5.72, 6.91, 4.97], [6.49, 5.07, 5.18, 6.41, 4.48], [6.66, 5.6, 5.4, 6.43, 4.69]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 7.59), ('CB', 'ASP', 'CG', 'GLU', 6.61), ('CB', 'ASP', 'CD', 'GLU', 6.82), ('CB', 'ASP', 'OE1', 'GLU', 6.4), ('CB', 'ASP', 'OE2', 'GLU', 7.79)], [('CG', 'ASP', 'CB', 'GLU', 8.39), ('CG', 'ASP', 'CG', 'GLU', 7.17), ('CG', 'ASP', 'CD', 'GLU', 7.07), ('CG', 'ASP', 'OE1', 'GLU', 6.68), ('CG', 'ASP', 'OE2', 'GLU', 7.8)], [('OD1', 'ASP', 'CB', 'GLU', 8.89), ('OD1', 'ASP', 'CG', 'GLU', 7.56), ('OD1', 'ASP', 'CD', 'GLU', 7.59), ('OD1', 'ASP', 'OE1', 'GLU', 7.45), ('OD1', 'ASP', 'OE2', 'GLU', 8.17)], [('OD2', 'ASP', 'CB', 'GLU', 8.85), ('OD2', 'ASP', 'CG', 'GLU', 7.62), ('OD2', 'ASP', 'CD', 'GLU', 7.18), ('OD2', 'ASP', 'OE1', 'GLU', 6.59), ('OD2', 'ASP', 'OE2', 'GLU', 7.82)], [('CB', 'ASP', 'CB', 'GLU', 8.13), ('CB', 'ASP', 'CG', 'GLU', 6.95), ('CB', 'ASP', 'CD', 'GLU', 7.18), ('CB', 'ASP', 'OE1', 'GLU', 8.38), ('CB', 'ASP', 'OE2', 'GLU', 6.43)], [('CG', 'ASP', 'CB', 'GLU', 6.9), ('CG', 'ASP', 'CG', 'GLU', 5.66), ('CG', 'ASP', 'CD', 'GLU', 5.72), ('CG', 'ASP', 'OE1', 'GLU', 6.91), ('CG', 'ASP', 'OE2', 'GLU', 4.97)], [('OD1', 'ASP', 'CB', 'GLU', 6.49), ('OD1', 'ASP', 'CG', 'GLU', 5.07), ('OD1', 'ASP', 'CD', 'GLU', 5.18), ('OD1', 'ASP', 'OE1', 'GLU', 6.41), ('OD1', 'ASP', 'OE2', 'GLU', 4.48)], [('OD2', 'ASP', 'CB', 'GLU', 6.66), ('OD2', 'ASP', 'CG', 'GLU', 5.6), ('OD2', 'ASP', 'CD', 'GLU', 5.4), ('OD2', 'ASP', 'OE1', 'GLU', 6.43), ('OD2', 'ASP', 'OE2', 'GLU', 4.69)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLU, d, 'A_1un1_2_4_1_207')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_GLU, d, 'A_1un1_2_4_1_207')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLU' :  match1,
		'ASP_GLU' :  match2}