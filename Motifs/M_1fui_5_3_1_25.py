'''
FUNC:M_1fui_5_3_1_25
PDB:1fui
EC:5.3.1.25
RESI:glu,asp,mn
LOCI:a-337,361,592;
'''
import motifFunctions as cmd
GLU_MN = { 
	'distances':
		[[7.13], [6.58], [5.13], [4.47], [5.07]],
	'comparisons':
		[[('CB', 'GLU', 'MN', 'MN', 7.13)], [('CG', 'GLU', 'MN', 'MN', 6.58)], [('CD', 'GLU', 'MN', 'MN', 5.13)], [('OE1', 'GLU', 'MN', 'MN', 4.47)], [('OE2', 'GLU', 'MN', 'MN', 5.07)]]}
ASP_MN = { 
	'distances':
		[[6.59], [5.11], [4.73], [4.72]],
	'comparisons':
		[[('CB', 'ASP', 'MN', 'MN', 6.59)], [('CG', 'ASP', 'MN', 'MN', 5.11)], [('OD1', 'ASP', 'MN', 'MN', 4.73)], [('OD2', 'ASP', 'MN', 'MN', 4.72)]]}
ASP_GLU = { 
	'distances':
		[[11.61, 11.13, 9.69, 9.02, 9.38], [10.18, 9.65, 8.2, 7.56, 7.89], [9.58, 9.0, 7.63, 7.14, 7.28], [9.76, 9.25, 7.76, 7.02, 7.51]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 11.61), ('CB', 'ASP', 'CG', 'GLU', 11.13), ('CB', 'ASP', 'CD', 'GLU', 9.69), ('CB', 'ASP', 'OE1', 'GLU', 9.02), ('CB', 'ASP', 'OE2', 'GLU', 9.38)], [('CG', 'ASP', 'CB', 'GLU', 10.18), ('CG', 'ASP', 'CG', 'GLU', 9.65), ('CG', 'ASP', 'CD', 'GLU', 8.2), ('CG', 'ASP', 'OE1', 'GLU', 7.56), ('CG', 'ASP', 'OE2', 'GLU', 7.89)], [('OD1', 'ASP', 'CB', 'GLU', 9.58), ('OD1', 'ASP', 'CG', 'GLU', 9.0), ('OD1', 'ASP', 'CD', 'GLU', 7.63), ('OD1', 'ASP', 'OE1', 'GLU', 7.14), ('OD1', 'ASP', 'OE2', 'GLU', 7.28)], [('OD2', 'ASP', 'CB', 'GLU', 9.76), ('OD2', 'ASP', 'CG', 'GLU', 9.25), ('OD2', 'ASP', 'CD', 'GLU', 7.76), ('OD2', 'ASP', 'OE1', 'GLU', 7.02), ('OD2', 'ASP', 'OE2', 'GLU', 7.51)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_MN, d, 'M_1fui_5_3_1_25')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_MN, d, 'M_1fui_5_3_1_25')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLU, d, 'M_1fui_5_3_1_25')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_MN' :  match1,
		'ASP_MN' :  match2,
		'ASP_GLU' :  match3}