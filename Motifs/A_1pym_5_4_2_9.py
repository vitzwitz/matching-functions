'''
FUNC:A_1pym_5_4_2_9
PDB:1pym
EC:5.4.2.9
RESI:gly,leu,asp,lys
LOCI:a-47,48,58,120;
'''
import motifFunctions as cmd
ASP_GLY = { 
	'distances':
		[[6.72, 7.0, 8.14, 9.13], [6.19, 6.17, 7.08, 8.02], [5.48, 5.53, 6.24, 7.37], [6.92, 6.62, 7.39, 8.09]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLY', 6.72), ('CB', 'ASP', 'C', 'GLY', 7.0), ('CB', 'ASP', 'CA', 'GLY', 8.14), ('CB', 'ASP', 'N', 'GLY', 9.13)], [('CG', 'ASP', 'O', 'GLY', 6.19), ('CG', 'ASP', 'C', 'GLY', 6.17), ('CG', 'ASP', 'CA', 'GLY', 7.08), ('CG', 'ASP', 'N', 'GLY', 8.02)], [('OD1', 'ASP', 'O', 'GLY', 5.48), ('OD1', 'ASP', 'C', 'GLY', 5.53), ('OD1', 'ASP', 'CA', 'GLY', 6.24), ('OD1', 'ASP', 'N', 'GLY', 7.37)], [('OD2', 'ASP', 'O', 'GLY', 6.92), ('OD2', 'ASP', 'C', 'GLY', 6.62), ('OD2', 'ASP', 'CA', 'GLY', 7.39), ('OD2', 'ASP', 'N', 'GLY', 8.09)]]}
GLY_LYS = { 
	'distances':
		[[11.86, 10.47, 9.26, 9.02, 9.24], [11.7, 10.34, 9.2, 8.76, 8.77], [11.54, 10.12, 9.21, 8.84, 8.58], [12.44, 11.08, 10.25, 9.71, 9.24]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'LYS', 11.86), ('O', 'GLY', 'CG', 'LYS', 10.47), ('O', 'GLY', 'CD', 'LYS', 9.26), ('O', 'GLY', 'CE', 'LYS', 9.02), ('O', 'GLY', 'NZ', 'LYS', 9.24)], [('C', 'GLY', 'CB', 'LYS', 11.7), ('C', 'GLY', 'CG', 'LYS', 10.34), ('C', 'GLY', 'CD', 'LYS', 9.2), ('C', 'GLY', 'CE', 'LYS', 8.76), ('C', 'GLY', 'NZ', 'LYS', 8.77)], [('CA', 'GLY', 'CB', 'LYS', 11.54), ('CA', 'GLY', 'CG', 'LYS', 10.12), ('CA', 'GLY', 'CD', 'LYS', 9.21), ('CA', 'GLY', 'CE', 'LYS', 8.84), ('CA', 'GLY', 'NZ', 'LYS', 8.58)], [('N', 'GLY', 'CB', 'LYS', 12.44), ('N', 'GLY', 'CG', 'LYS', 11.08), ('N', 'GLY', 'CD', 'LYS', 10.25), ('N', 'GLY', 'CE', 'LYS', 9.71), ('N', 'GLY', 'NZ', 'LYS', 9.24)]]}
ASP_LEU = { 
	'distances':
		[[6.6, 6.94, 5.97, 8.1, 7.0, 7.1, 6.12, 6.7], [6.18, 6.97, 6.4, 8.06, 7.22, 6.98, 5.71, 5.87], [6.67, 7.66, 7.28, 8.86, 7.36, 7.05, 5.85, 5.61], [5.94, 6.79, 6.35, 7.61, 7.73, 7.33, 5.91, 6.02]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LEU', 6.6), ('CB', 'ASP', 'CG', 'LEU', 6.94), ('CB', 'ASP', 'CD1', 'LEU', 5.97), ('CB', 'ASP', 'CD2', 'LEU', 8.1), ('CB', 'ASP', 'O', 'LEU', 7.0), ('CB', 'ASP', 'C', 'LEU', 7.1), ('CB', 'ASP', 'CA', 'LEU', 6.12), ('CB', 'ASP', 'N', 'LEU', 6.7)], [('CG', 'ASP', 'CB', 'LEU', 6.18), ('CG', 'ASP', 'CG', 'LEU', 6.97), ('CG', 'ASP', 'CD1', 'LEU', 6.4), ('CG', 'ASP', 'CD2', 'LEU', 8.06), ('CG', 'ASP', 'O', 'LEU', 7.22), ('CG', 'ASP', 'C', 'LEU', 6.98), ('CG', 'ASP', 'CA', 'LEU', 5.71), ('CG', 'ASP', 'N', 'LEU', 5.87)], [('OD1', 'ASP', 'CB', 'LEU', 6.67), ('OD1', 'ASP', 'CG', 'LEU', 7.66), ('OD1', 'ASP', 'CD1', 'LEU', 7.28), ('OD1', 'ASP', 'CD2', 'LEU', 8.86), ('OD1', 'ASP', 'O', 'LEU', 7.36), ('OD1', 'ASP', 'C', 'LEU', 7.05), ('OD1', 'ASP', 'CA', 'LEU', 5.85), ('OD1', 'ASP', 'N', 'LEU', 5.61)], [('OD2', 'ASP', 'CB', 'LEU', 5.94), ('OD2', 'ASP', 'CG', 'LEU', 6.79), ('OD2', 'ASP', 'CD1', 'LEU', 6.35), ('OD2', 'ASP', 'CD2', 'LEU', 7.61), ('OD2', 'ASP', 'O', 'LEU', 7.73), ('OD2', 'ASP', 'C', 'LEU', 7.33), ('OD2', 'ASP', 'CA', 'LEU', 5.91), ('OD2', 'ASP', 'N', 'LEU', 6.02)]]}
LEU_GLY = { 
	'distances':
		[[6.33, 5.8, 6.93, 6.95], [7.37, 7.08, 8.35, 8.4], [7.6, 7.56, 8.93, 9.27], [8.79, 8.34, 9.46, 9.29], [5.53, 5.89, 7.34, 7.77], [5.09, 5.08, 6.45, 6.7], [4.81, 4.48, 5.84, 6.19], [4.25, 3.35, 4.44, 4.78]],
	'comparisons':
		[[('CB', 'LEU', 'O', 'GLY', 6.33), ('CB', 'LEU', 'C', 'GLY', 5.8), ('CB', 'LEU', 'CA', 'GLY', 6.93), ('CB', 'LEU', 'N', 'GLY', 6.95)], [('CG', 'LEU', 'O', 'GLY', 7.37), ('CG', 'LEU', 'C', 'GLY', 7.08), ('CG', 'LEU', 'CA', 'GLY', 8.35), ('CG', 'LEU', 'N', 'GLY', 8.4)], [('CD1', 'LEU', 'O', 'GLY', 7.6), ('CD1', 'LEU', 'C', 'GLY', 7.56), ('CD1', 'LEU', 'CA', 'GLY', 8.93), ('CD1', 'LEU', 'N', 'GLY', 9.27)], [('CD2', 'LEU', 'O', 'GLY', 8.79), ('CD2', 'LEU', 'C', 'GLY', 8.34), ('CD2', 'LEU', 'CA', 'GLY', 9.46), ('CD2', 'LEU', 'N', 'GLY', 9.29)], [('O', 'LEU', 'O', 'GLY', 5.53), ('O', 'LEU', 'C', 'GLY', 5.89), ('O', 'LEU', 'CA', 'GLY', 7.34), ('O', 'LEU', 'N', 'GLY', 7.77)], [('C', 'LEU', 'O', 'GLY', 5.09), ('C', 'LEU', 'C', 'GLY', 5.08), ('C', 'LEU', 'CA', 'GLY', 6.45), ('C', 'LEU', 'N', 'GLY', 6.7)], [('CA', 'LEU', 'O', 'GLY', 4.81), ('CA', 'LEU', 'C', 'GLY', 4.48), ('CA', 'LEU', 'CA', 'GLY', 5.84), ('CA', 'LEU', 'N', 'GLY', 6.19)], [('N', 'LEU', 'O', 'GLY', 4.25), ('N', 'LEU', 'C', 'GLY', 3.35), ('N', 'LEU', 'CA', 'GLY', 4.44), ('N', 'LEU', 'N', 'GLY', 4.78)]]}
ASP_LYS = { 
	'distances':
		[[9.82, 8.97, 7.41, 6.92, 7.89], [9.05, 8.08, 6.59, 5.91, 6.64], [8.8, 7.62, 6.19, 5.79, 6.41], [8.96, 8.14, 6.75, 5.71, 6.22]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 9.82), ('CB', 'ASP', 'CG', 'LYS', 8.97), ('CB', 'ASP', 'CD', 'LYS', 7.41), ('CB', 'ASP', 'CE', 'LYS', 6.92), ('CB', 'ASP', 'NZ', 'LYS', 7.89)], [('CG', 'ASP', 'CB', 'LYS', 9.05), ('CG', 'ASP', 'CG', 'LYS', 8.08), ('CG', 'ASP', 'CD', 'LYS', 6.59), ('CG', 'ASP', 'CE', 'LYS', 5.91), ('CG', 'ASP', 'NZ', 'LYS', 6.64)], [('OD1', 'ASP', 'CB', 'LYS', 8.8), ('OD1', 'ASP', 'CG', 'LYS', 7.62), ('OD1', 'ASP', 'CD', 'LYS', 6.19), ('OD1', 'ASP', 'CE', 'LYS', 5.79), ('OD1', 'ASP', 'NZ', 'LYS', 6.41)], [('OD2', 'ASP', 'CB', 'LYS', 8.96), ('OD2', 'ASP', 'CG', 'LYS', 8.14), ('OD2', 'ASP', 'CD', 'LYS', 6.75), ('OD2', 'ASP', 'CE', 'LYS', 5.71), ('OD2', 'ASP', 'NZ', 'LYS', 6.22)]]}
LEU_LYS = { 
	'distances':
		[[12.74, 11.76, 10.43, 9.45, 9.56], [13.74, 12.85, 11.44, 10.47, 10.74], [13.22, 12.41, 10.93, 10.03, 10.54], [14.46, 13.69, 12.35, 11.22, 11.38], [14.14, 12.97, 11.54, 11.0, 11.42], [13.75, 12.57, 11.21, 10.57, 10.81], [12.39, 11.26, 9.91, 9.17, 9.37], [11.85, 10.62, 9.42, 8.72, 8.7]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'LYS', 12.74), ('CB', 'LEU', 'CG', 'LYS', 11.76), ('CB', 'LEU', 'CD', 'LYS', 10.43), ('CB', 'LEU', 'CE', 'LYS', 9.45), ('CB', 'LEU', 'NZ', 'LYS', 9.56)], [('CG', 'LEU', 'CB', 'LYS', 13.74), ('CG', 'LEU', 'CG', 'LYS', 12.85), ('CG', 'LEU', 'CD', 'LYS', 11.44), ('CG', 'LEU', 'CE', 'LYS', 10.47), ('CG', 'LEU', 'NZ', 'LYS', 10.74)], [('CD1', 'LEU', 'CB', 'LYS', 13.22), ('CD1', 'LEU', 'CG', 'LYS', 12.41), ('CD1', 'LEU', 'CD', 'LYS', 10.93), ('CD1', 'LEU', 'CE', 'LYS', 10.03), ('CD1', 'LEU', 'NZ', 'LYS', 10.54)], [('CD2', 'LEU', 'CB', 'LYS', 14.46), ('CD2', 'LEU', 'CG', 'LYS', 13.69), ('CD2', 'LEU', 'CD', 'LYS', 12.35), ('CD2', 'LEU', 'CE', 'LYS', 11.22), ('CD2', 'LEU', 'NZ', 'LYS', 11.38)], [('O', 'LEU', 'CB', 'LYS', 14.14), ('O', 'LEU', 'CG', 'LYS', 12.97), ('O', 'LEU', 'CD', 'LYS', 11.54), ('O', 'LEU', 'CE', 'LYS', 11.0), ('O', 'LEU', 'NZ', 'LYS', 11.42)], [('C', 'LEU', 'CB', 'LYS', 13.75), ('C', 'LEU', 'CG', 'LYS', 12.57), ('C', 'LEU', 'CD', 'LYS', 11.21), ('C', 'LEU', 'CE', 'LYS', 10.57), ('C', 'LEU', 'NZ', 'LYS', 10.81)], [('CA', 'LEU', 'CB', 'LYS', 12.39), ('CA', 'LEU', 'CG', 'LYS', 11.26), ('CA', 'LEU', 'CD', 'LYS', 9.91), ('CA', 'LEU', 'CE', 'LYS', 9.17), ('CA', 'LEU', 'NZ', 'LYS', 9.37)], [('N', 'LEU', 'CB', 'LYS', 11.85), ('N', 'LEU', 'CG', 'LYS', 10.62), ('N', 'LEU', 'CD', 'LYS', 9.42), ('N', 'LEU', 'CE', 'LYS', 8.72), ('N', 'LEU', 'NZ', 'LYS', 8.7)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_GLY, d, 'A_1pym_5_4_2_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_LYS, d, 'A_1pym_5_4_2_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_LEU, d, 'A_1pym_5_4_2_9')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LEU_GLY, d, 'A_1pym_5_4_2_9')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_LYS, d, 'A_1pym_5_4_2_9')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LEU_LYS, d, 'A_1pym_5_4_2_9')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_GLY' :  match1,
		'GLY_LYS' :  match2,
		'ASP_LEU' :  match3,
		'LEU_GLY' :  match4,
		'ASP_LYS' :  match5,
		'LEU_LYS' :  match6}