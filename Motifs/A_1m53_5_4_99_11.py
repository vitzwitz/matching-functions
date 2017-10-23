'''
FUNC:A_1m53_5_4_99_11
PDB:1m53
EC:5.4.99.11
RESI:asp,glu
LOCI:a-241,295;
'''
import motifFunctions as cmd
ASP_GLU = { 
	'distances':
		[[7.66, 8.26, 7.54, 6.51, 8.29, 8.64, 9.27, 8.8, 8.68], [7.85, 8.08, 7.05, 5.94, 7.63, 8.79, 9.47, 9.14, 9.32], [8.63, 8.75, 7.69, 6.49, 8.27, 9.12, 9.96, 9.84, 10.05], [7.59, 7.62, 6.43, 5.47, 6.78, 8.93, 9.47, 9.02, 9.38], [7.77, 8.43, 8.11, 7.0, 9.17, 7.3, 8.29, 8.4, 8.15], [6.64, 7.29, 6.95, 5.87, 8.02, 6.58, 7.46, 7.42, 7.31], [6.48, 7.3, 6.91, 5.95, 7.88, 7.27, 7.89, 7.45, 7.23], [7.01, 8.12, 7.99, 7.18, 9.0, 7.76, 8.27, 7.69, 7.11]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 7.66), ('CB', 'ASP', 'CG', 'GLU', 8.26), ('CB', 'ASP', 'CD', 'GLU', 7.54), ('CB', 'ASP', 'OE1', 'GLU', 6.51), ('CB', 'ASP', 'OE2', 'GLU', 8.29), ('CB', 'ASP', 'O', 'GLU', 8.64), ('CB', 'ASP', 'C', 'GLU', 9.27), ('CB', 'ASP', 'CA', 'GLU', 8.8), ('CB', 'ASP', 'N', 'GLU', 8.68)], [('CG', 'ASP', 'CB', 'GLU', 7.85), ('CG', 'ASP', 'CG', 'GLU', 8.08), ('CG', 'ASP', 'CD', 'GLU', 7.05), ('CG', 'ASP', 'OE1', 'GLU', 5.94), ('CG', 'ASP', 'OE2', 'GLU', 7.63), ('CG', 'ASP', 'O', 'GLU', 8.79), ('CG', 'ASP', 'C', 'GLU', 9.47), ('CG', 'ASP', 'CA', 'GLU', 9.14), ('CG', 'ASP', 'N', 'GLU', 9.32)], [('OD1', 'ASP', 'CB', 'GLU', 8.63), ('OD1', 'ASP', 'CG', 'GLU', 8.75), ('OD1', 'ASP', 'CD', 'GLU', 7.69), ('OD1', 'ASP', 'OE1', 'GLU', 6.49), ('OD1', 'ASP', 'OE2', 'GLU', 8.27), ('OD1', 'ASP', 'O', 'GLU', 9.12), ('OD1', 'ASP', 'C', 'GLU', 9.96), ('OD1', 'ASP', 'CA', 'GLU', 9.84), ('OD1', 'ASP', 'N', 'GLU', 10.05)], [('OD2', 'ASP', 'CB', 'GLU', 7.59), ('OD2', 'ASP', 'CG', 'GLU', 7.62), ('OD2', 'ASP', 'CD', 'GLU', 6.43), ('OD2', 'ASP', 'OE1', 'GLU', 5.47), ('OD2', 'ASP', 'OE2', 'GLU', 6.78), ('OD2', 'ASP', 'O', 'GLU', 8.93), ('OD2', 'ASP', 'C', 'GLU', 9.47), ('OD2', 'ASP', 'CA', 'GLU', 9.02), ('OD2', 'ASP', 'N', 'GLU', 9.38)], [('O', 'ASP', 'CB', 'GLU', 7.77), ('O', 'ASP', 'CG', 'GLU', 8.43), ('O', 'ASP', 'CD', 'GLU', 8.11), ('O', 'ASP', 'OE1', 'GLU', 7.0), ('O', 'ASP', 'OE2', 'GLU', 9.17), ('O', 'ASP', 'O', 'GLU', 7.3), ('O', 'ASP', 'C', 'GLU', 8.29), ('O', 'ASP', 'CA', 'GLU', 8.4), ('O', 'ASP', 'N', 'GLU', 8.15)], [('C', 'ASP', 'CB', 'GLU', 6.64), ('C', 'ASP', 'CG', 'GLU', 7.29), ('C', 'ASP', 'CD', 'GLU', 6.95), ('C', 'ASP', 'OE1', 'GLU', 5.87), ('C', 'ASP', 'OE2', 'GLU', 8.02), ('C', 'ASP', 'O', 'GLU', 6.58), ('C', 'ASP', 'C', 'GLU', 7.46), ('C', 'ASP', 'CA', 'GLU', 7.42), ('C', 'ASP', 'N', 'GLU', 7.31)], [('CA', 'ASP', 'CB', 'GLU', 6.48), ('CA', 'ASP', 'CG', 'GLU', 7.3), ('CA', 'ASP', 'CD', 'GLU', 6.91), ('CA', 'ASP', 'OE1', 'GLU', 5.95), ('CA', 'ASP', 'OE2', 'GLU', 7.88), ('CA', 'ASP', 'O', 'GLU', 7.27), ('CA', 'ASP', 'C', 'GLU', 7.89), ('CA', 'ASP', 'CA', 'GLU', 7.45), ('CA', 'ASP', 'N', 'GLU', 7.23)], [('N', 'ASP', 'CB', 'GLU', 7.01), ('N', 'ASP', 'CG', 'GLU', 8.12), ('N', 'ASP', 'CD', 'GLU', 7.99), ('N', 'ASP', 'OE1', 'GLU', 7.18), ('N', 'ASP', 'OE2', 'GLU', 9.0), ('N', 'ASP', 'O', 'GLU', 7.76), ('N', 'ASP', 'C', 'GLU', 8.27), ('N', 'ASP', 'CA', 'GLU', 7.69), ('N', 'ASP', 'N', 'GLU', 7.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLU, d, 'A_1m53_5_4_99_11')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLU' :  match1}