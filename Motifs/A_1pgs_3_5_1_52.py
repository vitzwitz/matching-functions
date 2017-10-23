'''
FUNC:A_1pgs_3_5_1_52
PDB:1pgs
EC:3.5.1.52
RESI:asp,glu
LOCI:a-60,206;
'''
import motifFunctions as cmd
ASP_GLU = { 
	'distances':
		[[11.79, 10.78, 9.54, 9.56, 8.79], [10.7, 9.74, 8.39, 8.3, 7.67], [11.27, 10.4, 8.97, 8.71, 8.3], [9.52, 8.53, 7.21, 7.19, 6.5]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 11.79), ('CB', 'ASP', 'CG', 'GLU', 10.78), ('CB', 'ASP', 'CD', 'GLU', 9.54), ('CB', 'ASP', 'OE1', 'GLU', 9.56), ('CB', 'ASP', 'OE2', 'GLU', 8.79)], [('CG', 'ASP', 'CB', 'GLU', 10.7), ('CG', 'ASP', 'CG', 'GLU', 9.74), ('CG', 'ASP', 'CD', 'GLU', 8.39), ('CG', 'ASP', 'OE1', 'GLU', 8.3), ('CG', 'ASP', 'OE2', 'GLU', 7.67)], [('OD1', 'ASP', 'CB', 'GLU', 11.27), ('OD1', 'ASP', 'CG', 'GLU', 10.4), ('OD1', 'ASP', 'CD', 'GLU', 8.97), ('OD1', 'ASP', 'OE1', 'GLU', 8.71), ('OD1', 'ASP', 'OE2', 'GLU', 8.3)], [('OD2', 'ASP', 'CB', 'GLU', 9.52), ('OD2', 'ASP', 'CG', 'GLU', 8.53), ('OD2', 'ASP', 'CD', 'GLU', 7.21), ('OD2', 'ASP', 'OE1', 'GLU', 7.19), ('OD2', 'ASP', 'OE2', 'GLU', 6.5)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLU, d, 'A_1pgs_3_5_1_52')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLU' :  match1}