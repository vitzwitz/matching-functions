'''
FUNC:A_2ayh_3_2_1_73
PDB:2ayh
EC:3.2.1.73
RESI:glu,asp,glu
LOCI:a-105,107,109;
'''
import motifFunctions as cmd
GLU_GLU = { 
	'distances':
		[[12.97, 11.49, 10.97, 11.94, 9.83], [11.56, 10.06, 9.49, 10.45, 8.34], [10.98, 9.54, 8.79, 9.64, 7.64], [10.97, 9.61, 8.91, 9.74, 7.85], [10.87, 9.43, 8.48, 9.18, 7.29], [12.97, 11.56, 10.98, 10.97, 10.87], [11.49, 10.06, 9.54, 9.61, 9.43], [10.97, 9.49, 8.79, 8.91, 8.48], [11.94, 10.45, 9.64, 9.74, 9.18], [9.83, 8.34, 7.64, 7.85, 7.29]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 12.97), ('CB', 'GLU', 'CG', 'GLU', 11.49), ('CB', 'GLU', 'CD', 'GLU', 10.97), ('CB', 'GLU', 'OE1', 'GLU', 11.94), ('CB', 'GLU', 'OE2', 'GLU', 9.83)], [('CG', 'GLU', 'CB', 'GLU', 11.56), ('CG', 'GLU', 'CG', 'GLU', 10.06), ('CG', 'GLU', 'CD', 'GLU', 9.49), ('CG', 'GLU', 'OE1', 'GLU', 10.45), ('CG', 'GLU', 'OE2', 'GLU', 8.34)], [('CD', 'GLU', 'CB', 'GLU', 10.98), ('CD', 'GLU', 'CG', 'GLU', 9.54), ('CD', 'GLU', 'CD', 'GLU', 8.79), ('CD', 'GLU', 'OE1', 'GLU', 9.64), ('CD', 'GLU', 'OE2', 'GLU', 7.64)], [('OE1', 'GLU', 'CB', 'GLU', 10.97), ('OE1', 'GLU', 'CG', 'GLU', 9.61), ('OE1', 'GLU', 'CD', 'GLU', 8.91), ('OE1', 'GLU', 'OE1', 'GLU', 9.74), ('OE1', 'GLU', 'OE2', 'GLU', 7.85)], [('OE2', 'GLU', 'CB', 'GLU', 10.87), ('OE2', 'GLU', 'CG', 'GLU', 9.43), ('OE2', 'GLU', 'CD', 'GLU', 8.48), ('OE2', 'GLU', 'OE1', 'GLU', 9.18), ('OE2', 'GLU', 'OE2', 'GLU', 7.29)], [('CB', 'GLU', 'CB', 'GLU', 12.97), ('CB', 'GLU', 'CG', 'GLU', 11.56), ('CB', 'GLU', 'CD', 'GLU', 10.98), ('CB', 'GLU', 'OE1', 'GLU', 10.97), ('CB', 'GLU', 'OE2', 'GLU', 10.87)], [('CG', 'GLU', 'CB', 'GLU', 11.49), ('CG', 'GLU', 'CG', 'GLU', 10.06), ('CG', 'GLU', 'CD', 'GLU', 9.54), ('CG', 'GLU', 'OE1', 'GLU', 9.61), ('CG', 'GLU', 'OE2', 'GLU', 9.43)], [('CD', 'GLU', 'CB', 'GLU', 10.97), ('CD', 'GLU', 'CG', 'GLU', 9.49), ('CD', 'GLU', 'CD', 'GLU', 8.79), ('CD', 'GLU', 'OE1', 'GLU', 8.91), ('CD', 'GLU', 'OE2', 'GLU', 8.48)], [('OE1', 'GLU', 'CB', 'GLU', 11.94), ('OE1', 'GLU', 'CG', 'GLU', 10.45), ('OE1', 'GLU', 'CD', 'GLU', 9.64), ('OE1', 'GLU', 'OE1', 'GLU', 9.74), ('OE1', 'GLU', 'OE2', 'GLU', 9.18)], [('OE2', 'GLU', 'CB', 'GLU', 9.83), ('OE2', 'GLU', 'CG', 'GLU', 8.34), ('OE2', 'GLU', 'CD', 'GLU', 7.64), ('OE2', 'GLU', 'OE1', 'GLU', 7.85), ('OE2', 'GLU', 'OE2', 'GLU', 7.29)]]}
GLU_ASP = { 
	'distances':
		[[7.11, 7.89, 8.2, 8.53], [6.09, 6.65, 6.78, 7.37], [6.09, 6.23, 6.46, 6.66], [6.04, 6.16, 6.71, 6.32], [6.83, 6.64, 6.57, 7.05], [8.42, 7.22, 6.83, 6.94], [7.09, 5.85, 5.32, 5.76], [7.2, 5.78, 5.11, 5.63], [8.42, 6.97, 6.34, 6.67], [6.48, 5.09, 4.28, 5.13]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 7.11), ('CB', 'GLU', 'CG', 'ASP', 7.89), ('CB', 'GLU', 'OD1', 'ASP', 8.2), ('CB', 'GLU', 'OD2', 'ASP', 8.53)], [('CG', 'GLU', 'CB', 'ASP', 6.09), ('CG', 'GLU', 'CG', 'ASP', 6.65), ('CG', 'GLU', 'OD1', 'ASP', 6.78), ('CG', 'GLU', 'OD2', 'ASP', 7.37)], [('CD', 'GLU', 'CB', 'ASP', 6.09), ('CD', 'GLU', 'CG', 'ASP', 6.23), ('CD', 'GLU', 'OD1', 'ASP', 6.46), ('CD', 'GLU', 'OD2', 'ASP', 6.66)], [('OE1', 'GLU', 'CB', 'ASP', 6.04), ('OE1', 'GLU', 'CG', 'ASP', 6.16), ('OE1', 'GLU', 'OD1', 'ASP', 6.71), ('OE1', 'GLU', 'OD2', 'ASP', 6.32)], [('OE2', 'GLU', 'CB', 'ASP', 6.83), ('OE2', 'GLU', 'CG', 'ASP', 6.64), ('OE2', 'GLU', 'OD1', 'ASP', 6.57), ('OE2', 'GLU', 'OD2', 'ASP', 7.05)], [('CB', 'GLU', 'CB', 'ASP', 8.42), ('CB', 'GLU', 'CG', 'ASP', 7.22), ('CB', 'GLU', 'OD1', 'ASP', 6.83), ('CB', 'GLU', 'OD2', 'ASP', 6.94)], [('CG', 'GLU', 'CB', 'ASP', 7.09), ('CG', 'GLU', 'CG', 'ASP', 5.85), ('CG', 'GLU', 'OD1', 'ASP', 5.32), ('CG', 'GLU', 'OD2', 'ASP', 5.76)], [('CD', 'GLU', 'CB', 'ASP', 7.2), ('CD', 'GLU', 'CG', 'ASP', 5.78), ('CD', 'GLU', 'OD1', 'ASP', 5.11), ('CD', 'GLU', 'OD2', 'ASP', 5.63)], [('OE1', 'GLU', 'CB', 'ASP', 8.42), ('OE1', 'GLU', 'CG', 'ASP', 6.97), ('OE1', 'GLU', 'OD1', 'ASP', 6.34), ('OE1', 'GLU', 'OD2', 'ASP', 6.67)], [('OE2', 'GLU', 'CB', 'ASP', 6.48), ('OE2', 'GLU', 'CG', 'ASP', 5.09), ('OE2', 'GLU', 'OD1', 'ASP', 4.28), ('OE2', 'GLU', 'OD2', 'ASP', 5.13)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLU, d, 'A_2ayh_3_2_1_73')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ASP, d, 'A_2ayh_3_2_1_73')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLU' :  match1,
		'GLU_ASP' :  match2}