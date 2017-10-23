'''
FUNC:A_1rk2_2_7_1_15
PDB:1rk2
EC:2.7.1.15
RESI:ala,ala,gly,asp
LOCI:a-252,253,254,255;
'''
import motifFunctions as cmd
ASP_ALAI = { 
	'distances':
		[[6.38, 5.75, 6.18, 6.08, 7.34], [6.65, 6.56, 6.6, 6.13, 7.09], [7.85, 7.53, 7.56, 7.19, 8.03], [5.98, 6.61, 6.41, 5.55, 6.31]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ALAI', 6.38), ('CB', 'ASP', 'O', 'ALAI', 5.75), ('CB', 'ASP', 'C', 'ALAI', 6.18), ('CB', 'ASP', 'CA', 'ALAI', 6.08), ('CB', 'ASP', 'N', 'ALAI', 7.34)], [('CG', 'ASP', 'CB', 'ALAI', 6.65), ('CG', 'ASP', 'O', 'ALAI', 6.56), ('CG', 'ASP', 'C', 'ALAI', 6.6), ('CG', 'ASP', 'CA', 'ALAI', 6.13), ('CG', 'ASP', 'N', 'ALAI', 7.09)], [('OD1', 'ASP', 'CB', 'ALAI', 7.85), ('OD1', 'ASP', 'O', 'ALAI', 7.53), ('OD1', 'ASP', 'C', 'ALAI', 7.56), ('OD1', 'ASP', 'CA', 'ALAI', 7.19), ('OD1', 'ASP', 'N', 'ALAI', 8.03)], [('OD2', 'ASP', 'CB', 'ALAI', 5.98), ('OD2', 'ASP', 'O', 'ALAI', 6.61), ('OD2', 'ASP', 'C', 'ALAI', 6.41), ('OD2', 'ASP', 'CA', 'ALAI', 5.55), ('OD2', 'ASP', 'N', 'ALAI', 6.31)]]}
ALA_ASP = { 
	'distances':
		[[9.24, 9.57, 10.15, 9.57], [7.3, 8.13, 8.61, 8.64], [7.22, 7.79, 8.29, 8.13], [7.9, 8.4, 9.09, 8.45], [7.25, 7.54, 8.34, 7.36], [6.38, 6.65, 7.85, 5.98], [5.75, 6.56, 7.53, 6.61], [6.18, 6.6, 7.56, 6.41], [6.08, 6.13, 7.19, 5.55], [7.34, 7.09, 8.03, 6.31]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'ASP', 9.24), ('CB', 'ALA', 'CG', 'ASP', 9.57), ('CB', 'ALA', 'OD1', 'ASP', 10.15), ('CB', 'ALA', 'OD2', 'ASP', 9.57)], [('O', 'ALA', 'CB', 'ASP', 7.3), ('O', 'ALA', 'CG', 'ASP', 8.13), ('O', 'ALA', 'OD1', 'ASP', 8.61), ('O', 'ALA', 'OD2', 'ASP', 8.64)], [('C', 'ALA', 'CB', 'ASP', 7.22), ('C', 'ALA', 'CG', 'ASP', 7.79), ('C', 'ALA', 'OD1', 'ASP', 8.29), ('C', 'ALA', 'OD2', 'ASP', 8.13)], [('CA', 'ALA', 'CB', 'ASP', 7.9), ('CA', 'ALA', 'CG', 'ASP', 8.4), ('CA', 'ALA', 'OD1', 'ASP', 9.09), ('CA', 'ALA', 'OD2', 'ASP', 8.45)], [('N', 'ALA', 'CB', 'ASP', 7.25), ('N', 'ALA', 'CG', 'ASP', 7.54), ('N', 'ALA', 'OD1', 'ASP', 8.34), ('N', 'ALA', 'OD2', 'ASP', 7.36)], [('CB', 'ALA', 'CB', 'ASP', 6.38), ('CB', 'ALA', 'CG', 'ASP', 6.65), ('CB', 'ALA', 'OD1', 'ASP', 7.85), ('CB', 'ALA', 'OD2', 'ASP', 5.98)], [('O', 'ALA', 'CB', 'ASP', 5.75), ('O', 'ALA', 'CG', 'ASP', 6.56), ('O', 'ALA', 'OD1', 'ASP', 7.53), ('O', 'ALA', 'OD2', 'ASP', 6.61)], [('C', 'ALA', 'CB', 'ASP', 6.18), ('C', 'ALA', 'CG', 'ASP', 6.6), ('C', 'ALA', 'OD1', 'ASP', 7.56), ('C', 'ALA', 'OD2', 'ASP', 6.41)], [('CA', 'ALA', 'CB', 'ASP', 6.08), ('CA', 'ALA', 'CG', 'ASP', 6.13), ('CA', 'ALA', 'OD1', 'ASP', 7.19), ('CA', 'ALA', 'OD2', 'ASP', 5.55)], [('N', 'ALA', 'CB', 'ASP', 7.34), ('N', 'ALA', 'CG', 'ASP', 7.09), ('N', 'ALA', 'OD1', 'ASP', 8.03), ('N', 'ALA', 'OD2', 'ASP', 6.31)]]}
GLY_ASP = { 
	'distances':
		[[6.24, 6.88, 6.73, 7.9], [5.72, 6.21, 6.21, 7.07], [6.88, 7.13, 7.15, 7.77], [7.01, 7.28, 7.59, 7.64]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASP', 6.24), ('O', 'GLY', 'CG', 'ASP', 6.88), ('O', 'GLY', 'OD1', 'ASP', 6.73), ('O', 'GLY', 'OD2', 'ASP', 7.9)], [('C', 'GLY', 'CB', 'ASP', 5.72), ('C', 'GLY', 'CG', 'ASP', 6.21), ('C', 'GLY', 'OD1', 'ASP', 6.21), ('C', 'GLY', 'OD2', 'ASP', 7.07)], [('CA', 'GLY', 'CB', 'ASP', 6.88), ('CA', 'GLY', 'CG', 'ASP', 7.13), ('CA', 'GLY', 'OD1', 'ASP', 7.15), ('CA', 'GLY', 'OD2', 'ASP', 7.77)], [('N', 'GLY', 'CB', 'ASP', 7.01), ('N', 'GLY', 'CG', 'ASP', 7.28), ('N', 'GLY', 'OD1', 'ASP', 7.59), ('N', 'GLY', 'OD2', 'ASP', 7.64)]]}
ALA_ALA = { 
	'distances':
		[[7.99, 6.2, 5.69, 6.89, 6.9], [7.94, 5.12, 5.62, 7.08, 7.95], [7.39, 4.83, 4.91, 6.32, 6.99], [6.82, 4.71, 4.41, 5.82, 6.23], [5.61, 4.24, 3.33, 4.46, 4.78], [7.99, 7.94, 7.39, 6.82, 5.61], [6.2, 5.12, 4.83, 4.71, 4.24], [5.69, 5.62, 4.91, 4.41, 3.33], [6.89, 7.08, 6.32, 5.82, 4.46], [6.9, 7.95, 6.99, 6.23, 4.78]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'ALA', 7.99), ('CB', 'ALA', 'O', 'ALA', 6.2), ('CB', 'ALA', 'C', 'ALA', 5.69), ('CB', 'ALA', 'CA', 'ALA', 6.89), ('CB', 'ALA', 'N', 'ALA', 6.9)], [('O', 'ALA', 'CB', 'ALA', 7.94), ('O', 'ALA', 'O', 'ALA', 5.12), ('O', 'ALA', 'C', 'ALA', 5.62), ('O', 'ALA', 'CA', 'ALA', 7.08), ('O', 'ALA', 'N', 'ALA', 7.95)], [('C', 'ALA', 'CB', 'ALA', 7.39), ('C', 'ALA', 'O', 'ALA', 4.83), ('C', 'ALA', 'C', 'ALA', 4.91), ('C', 'ALA', 'CA', 'ALA', 6.32), ('C', 'ALA', 'N', 'ALA', 6.99)], [('CA', 'ALA', 'CB', 'ALA', 6.82), ('CA', 'ALA', 'O', 'ALA', 4.71), ('CA', 'ALA', 'C', 'ALA', 4.41), ('CA', 'ALA', 'CA', 'ALA', 5.82), ('CA', 'ALA', 'N', 'ALA', 6.23)], [('N', 'ALA', 'CB', 'ALA', 5.61), ('N', 'ALA', 'O', 'ALA', 4.24), ('N', 'ALA', 'C', 'ALA', 3.33), ('N', 'ALA', 'CA', 'ALA', 4.46), ('N', 'ALA', 'N', 'ALA', 4.78)], [('CB', 'ALA', 'CB', 'ALA', 7.99), ('CB', 'ALA', 'O', 'ALA', 7.94), ('CB', 'ALA', 'C', 'ALA', 7.39), ('CB', 'ALA', 'CA', 'ALA', 6.82), ('CB', 'ALA', 'N', 'ALA', 5.61)], [('O', 'ALA', 'CB', 'ALA', 6.2), ('O', 'ALA', 'O', 'ALA', 5.12), ('O', 'ALA', 'C', 'ALA', 4.83), ('O', 'ALA', 'CA', 'ALA', 4.71), ('O', 'ALA', 'N', 'ALA', 4.24)], [('C', 'ALA', 'CB', 'ALA', 5.69), ('C', 'ALA', 'O', 'ALA', 5.62), ('C', 'ALA', 'C', 'ALA', 4.91), ('C', 'ALA', 'CA', 'ALA', 4.41), ('C', 'ALA', 'N', 'ALA', 3.33)], [('CA', 'ALA', 'CB', 'ALA', 6.89), ('CA', 'ALA', 'O', 'ALA', 7.08), ('CA', 'ALA', 'C', 'ALA', 6.32), ('CA', 'ALA', 'CA', 'ALA', 5.82), ('CA', 'ALA', 'N', 'ALA', 4.46)], [('N', 'ALA', 'CB', 'ALA', 6.9), ('N', 'ALA', 'O', 'ALA', 7.95), ('N', 'ALA', 'C', 'ALA', 6.99), ('N', 'ALA', 'CA', 'ALA', 6.23), ('N', 'ALA', 'N', 'ALA', 4.78)]]}
GLY_ALA = { 
	'distances':
		[[8.3, 5.5, 5.91, 7.39, 7.72], [7.37, 4.97, 5.03, 6.43, 6.61], [6.35, 4.75, 4.42, 5.79, 6.15], [5.01, 4.24, 3.33, 4.42, 4.78], [9.27, 6.96, 7.48, 8.37, 9.39], [8.3, 6.07, 6.42, 7.27, 8.21], [8.61, 6.37, 6.4, 7.36, 8.01], [7.68, 5.48, 5.29, 6.39, 6.91]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ALA', 8.3), ('O', 'GLY', 'O', 'ALA', 5.5), ('O', 'GLY', 'C', 'ALA', 5.91), ('O', 'GLY', 'CA', 'ALA', 7.39), ('O', 'GLY', 'N', 'ALA', 7.72)], [('C', 'GLY', 'CB', 'ALA', 7.37), ('C', 'GLY', 'O', 'ALA', 4.97), ('C', 'GLY', 'C', 'ALA', 5.03), ('C', 'GLY', 'CA', 'ALA', 6.43), ('C', 'GLY', 'N', 'ALA', 6.61)], [('CA', 'GLY', 'CB', 'ALA', 6.35), ('CA', 'GLY', 'O', 'ALA', 4.75), ('CA', 'GLY', 'C', 'ALA', 4.42), ('CA', 'GLY', 'CA', 'ALA', 5.79), ('CA', 'GLY', 'N', 'ALA', 6.15)], [('N', 'GLY', 'CB', 'ALA', 5.01), ('N', 'GLY', 'O', 'ALA', 4.24), ('N', 'GLY', 'C', 'ALA', 3.33), ('N', 'GLY', 'CA', 'ALA', 4.42), ('N', 'GLY', 'N', 'ALA', 4.78)], [('O', 'GLY', 'CB', 'ALA', 9.27), ('O', 'GLY', 'O', 'ALA', 6.96), ('O', 'GLY', 'C', 'ALA', 7.48), ('O', 'GLY', 'CA', 'ALA', 8.37), ('O', 'GLY', 'N', 'ALA', 9.39)], [('C', 'GLY', 'CB', 'ALA', 8.3), ('C', 'GLY', 'O', 'ALA', 6.07), ('C', 'GLY', 'C', 'ALA', 6.42), ('C', 'GLY', 'CA', 'ALA', 7.27), ('C', 'GLY', 'N', 'ALA', 8.21)], [('CA', 'GLY', 'CB', 'ALA', 8.61), ('CA', 'GLY', 'O', 'ALA', 6.37), ('CA', 'GLY', 'C', 'ALA', 6.4), ('CA', 'GLY', 'CA', 'ALA', 7.36), ('CA', 'GLY', 'N', 'ALA', 8.01)], [('N', 'GLY', 'CB', 'ALA', 7.68), ('N', 'GLY', 'O', 'ALA', 5.48), ('N', 'GLY', 'C', 'ALA', 5.29), ('N', 'GLY', 'CA', 'ALA', 6.39), ('N', 'GLY', 'N', 'ALA', 6.91)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ALAI, d, 'A_1rk2_2_7_1_15')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ALA_ASP, d, 'A_1rk2_2_7_1_15')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_ASP, d, 'A_1rk2_2_7_1_15')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ALA_ALA, d, 'A_1rk2_2_7_1_15')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_ALA, d, 'A_1rk2_2_7_1_15')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ALAI' :  match1,
		'ALA_ASP' :  match2,
		'GLY_ASP' :  match3,
		'ALA_ALA' :  match4,
		'GLY_ALA' :  match5}