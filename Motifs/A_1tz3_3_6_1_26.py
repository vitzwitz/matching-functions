'''
FUNC:A_1tz3_3_6_1_26
PDB:1tz3
EC:3.6.1.26
RESI:gly,ala,gly,asp
LOCI:a-249,250,251,252;
'''
import motifFunctions as cmd
ALA_ASP = { 
	'distances':
		[[9.41, 9.74, 9.71, 10.32, 10.08, 8.96, 8.88, 7.64], [7.34, 8.13, 8.12, 9.06, 6.97, 6.01, 6.34, 5.41], [7.31, 7.85, 7.8, 8.66, 7.66, 6.56, 6.53, 5.35], [8.1, 8.6, 8.72, 9.2, 8.73, 7.6, 7.62, 6.52], [7.61, 7.95, 8.22, 8.34, 8.87, 7.69, 7.5, 6.48]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'ASP', 9.41), ('CB', 'ALA', 'CG', 'ASP', 9.74), ('CB', 'ALA', 'OD1', 'ASP', 9.71), ('CB', 'ALA', 'OD2', 'ASP', 10.32), ('CB', 'ALA', 'O', 'ASP', 10.08), ('CB', 'ALA', 'C', 'ASP', 8.96), ('CB', 'ALA', 'CA', 'ASP', 8.88), ('CB', 'ALA', 'N', 'ASP', 7.64)], [('O', 'ALA', 'CB', 'ASP', 7.34), ('O', 'ALA', 'CG', 'ASP', 8.13), ('O', 'ALA', 'OD1', 'ASP', 8.12), ('O', 'ALA', 'OD2', 'ASP', 9.06), ('O', 'ALA', 'O', 'ASP', 6.97), ('O', 'ALA', 'C', 'ASP', 6.01), ('O', 'ALA', 'CA', 'ASP', 6.34), ('O', 'ALA', 'N', 'ASP', 5.41)], [('C', 'ALA', 'CB', 'ASP', 7.31), ('C', 'ALA', 'CG', 'ASP', 7.85), ('C', 'ALA', 'OD1', 'ASP', 7.8), ('C', 'ALA', 'OD2', 'ASP', 8.66), ('C', 'ALA', 'O', 'ASP', 7.66), ('C', 'ALA', 'C', 'ASP', 6.56), ('C', 'ALA', 'CA', 'ASP', 6.53), ('C', 'ALA', 'N', 'ASP', 5.35)], [('CA', 'ALA', 'CB', 'ASP', 8.1), ('CA', 'ALA', 'CG', 'ASP', 8.6), ('CA', 'ALA', 'OD1', 'ASP', 8.72), ('CA', 'ALA', 'OD2', 'ASP', 9.2), ('CA', 'ALA', 'O', 'ASP', 8.73), ('CA', 'ALA', 'C', 'ASP', 7.6), ('CA', 'ALA', 'CA', 'ASP', 7.62), ('CA', 'ALA', 'N', 'ASP', 6.52)], [('N', 'ALA', 'CB', 'ASP', 7.61), ('N', 'ALA', 'CG', 'ASP', 7.95), ('N', 'ALA', 'OD1', 'ASP', 8.22), ('N', 'ALA', 'OD2', 'ASP', 8.34), ('N', 'ALA', 'O', 'ASP', 8.87), ('N', 'ALA', 'C', 'ASP', 7.69), ('N', 'ALA', 'CA', 'ASP', 7.5), ('N', 'ALA', 'N', 'ASP', 6.48)]]}
GLY_ASP = { 
	'distances':
		[[6.23, 6.81, 6.36, 8.04, 5.55, 4.96, 4.75, 4.24], [5.69, 6.11, 5.7, 7.27, 5.91, 4.99, 4.42, 3.32], [6.81, 6.97, 6.44, 8.0, 7.35, 6.36, 5.77, 4.41], [7.04, 7.26, 6.99, 8.09, 7.86, 6.73, 6.28, 4.88], [5.96, 6.76, 7.33, 7.22, 6.96, 5.85, 5.95, 5.44], [6.61, 7.07, 7.56, 7.37, 8.07, 6.9, 6.73, 5.99], [6.79, 6.96, 7.6, 6.91, 8.85, 7.73, 7.34, 6.76], [7.88, 7.75, 8.22, 7.59, 10.13, 8.97, 8.41, 7.64]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASP', 6.23), ('O', 'GLY', 'CG', 'ASP', 6.81), ('O', 'GLY', 'OD1', 'ASP', 6.36), ('O', 'GLY', 'OD2', 'ASP', 8.04), ('O', 'GLY', 'O', 'ASP', 5.55), ('O', 'GLY', 'C', 'ASP', 4.96), ('O', 'GLY', 'CA', 'ASP', 4.75), ('O', 'GLY', 'N', 'ASP', 4.24)], [('C', 'GLY', 'CB', 'ASP', 5.69), ('C', 'GLY', 'CG', 'ASP', 6.11), ('C', 'GLY', 'OD1', 'ASP', 5.7), ('C', 'GLY', 'OD2', 'ASP', 7.27), ('C', 'GLY', 'O', 'ASP', 5.91), ('C', 'GLY', 'C', 'ASP', 4.99), ('C', 'GLY', 'CA', 'ASP', 4.42), ('C', 'GLY', 'N', 'ASP', 3.32)], [('CA', 'GLY', 'CB', 'ASP', 6.81), ('CA', 'GLY', 'CG', 'ASP', 6.97), ('CA', 'GLY', 'OD1', 'ASP', 6.44), ('CA', 'GLY', 'OD2', 'ASP', 8.0), ('CA', 'GLY', 'O', 'ASP', 7.35), ('CA', 'GLY', 'C', 'ASP', 6.36), ('CA', 'GLY', 'CA', 'ASP', 5.77), ('CA', 'GLY', 'N', 'ASP', 4.41)], [('N', 'GLY', 'CB', 'ASP', 7.04), ('N', 'GLY', 'CG', 'ASP', 7.26), ('N', 'GLY', 'OD1', 'ASP', 6.99), ('N', 'GLY', 'OD2', 'ASP', 8.09), ('N', 'GLY', 'O', 'ASP', 7.86), ('N', 'GLY', 'C', 'ASP', 6.73), ('N', 'GLY', 'CA', 'ASP', 6.28), ('N', 'GLY', 'N', 'ASP', 4.88)], [('O', 'GLY', 'CB', 'ASP', 5.96), ('O', 'GLY', 'CG', 'ASP', 6.76), ('O', 'GLY', 'OD1', 'ASP', 7.33), ('O', 'GLY', 'OD2', 'ASP', 7.22), ('O', 'GLY', 'O', 'ASP', 6.96), ('O', 'GLY', 'C', 'ASP', 5.85), ('O', 'GLY', 'CA', 'ASP', 5.95), ('O', 'GLY', 'N', 'ASP', 5.44)], [('C', 'GLY', 'CB', 'ASP', 6.61), ('C', 'GLY', 'CG', 'ASP', 7.07), ('C', 'GLY', 'OD1', 'ASP', 7.56), ('C', 'GLY', 'OD2', 'ASP', 7.37), ('C', 'GLY', 'O', 'ASP', 8.07), ('C', 'GLY', 'C', 'ASP', 6.9), ('C', 'GLY', 'CA', 'ASP', 6.73), ('C', 'GLY', 'N', 'ASP', 5.99)], [('CA', 'GLY', 'CB', 'ASP', 6.79), ('CA', 'GLY', 'CG', 'ASP', 6.96), ('CA', 'GLY', 'OD1', 'ASP', 7.6), ('CA', 'GLY', 'OD2', 'ASP', 6.91), ('CA', 'GLY', 'O', 'ASP', 8.85), ('CA', 'GLY', 'C', 'ASP', 7.73), ('CA', 'GLY', 'CA', 'ASP', 7.34), ('CA', 'GLY', 'N', 'ASP', 6.76)], [('N', 'GLY', 'CB', 'ASP', 7.88), ('N', 'GLY', 'CG', 'ASP', 7.75), ('N', 'GLY', 'OD1', 'ASP', 8.22), ('N', 'GLY', 'OD2', 'ASP', 7.59), ('N', 'GLY', 'O', 'ASP', 10.13), ('N', 'GLY', 'C', 'ASP', 8.97), ('N', 'GLY', 'CA', 'ASP', 8.41), ('N', 'GLY', 'N', 'ASP', 7.64)]]}
ASP_GLYI = { 
	'distances':
		[[5.96, 6.61, 6.79, 7.88], [6.76, 7.07, 6.96, 7.75], [7.33, 7.56, 7.6, 8.22], [7.22, 7.37, 6.91, 7.59], [6.96, 8.07, 8.85, 10.13], [5.85, 6.9, 7.73, 8.97], [5.95, 6.73, 7.34, 8.41], [5.44, 5.99, 6.76, 7.64]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLYI', 5.96), ('CB', 'ASP', 'C', 'GLYI', 6.61), ('CB', 'ASP', 'CA', 'GLYI', 6.79), ('CB', 'ASP', 'N', 'GLYI', 7.88)], [('CG', 'ASP', 'O', 'GLYI', 6.76), ('CG', 'ASP', 'C', 'GLYI', 7.07), ('CG', 'ASP', 'CA', 'GLYI', 6.96), ('CG', 'ASP', 'N', 'GLYI', 7.75)], [('OD1', 'ASP', 'O', 'GLYI', 7.33), ('OD1', 'ASP', 'C', 'GLYI', 7.56), ('OD1', 'ASP', 'CA', 'GLYI', 7.6), ('OD1', 'ASP', 'N', 'GLYI', 8.22)], [('OD2', 'ASP', 'O', 'GLYI', 7.22), ('OD2', 'ASP', 'C', 'GLYI', 7.37), ('OD2', 'ASP', 'CA', 'GLYI', 6.91), ('OD2', 'ASP', 'N', 'GLYI', 7.59)], [('O', 'ASP', 'O', 'GLYI', 6.96), ('O', 'ASP', 'C', 'GLYI', 8.07), ('O', 'ASP', 'CA', 'GLYI', 8.85), ('O', 'ASP', 'N', 'GLYI', 10.13)], [('C', 'ASP', 'O', 'GLYI', 5.85), ('C', 'ASP', 'C', 'GLYI', 6.9), ('C', 'ASP', 'CA', 'GLYI', 7.73), ('C', 'ASP', 'N', 'GLYI', 8.97)], [('CA', 'ASP', 'O', 'GLYI', 5.95), ('CA', 'ASP', 'C', 'GLYI', 6.73), ('CA', 'ASP', 'CA', 'GLYI', 7.34), ('CA', 'ASP', 'N', 'GLYI', 8.41)], [('N', 'ASP', 'O', 'GLYI', 5.44), ('N', 'ASP', 'C', 'GLYI', 5.99), ('N', 'ASP', 'CA', 'GLYI', 6.76), ('N', 'ASP', 'N', 'GLYI', 7.64)]]}
GLY_GLY = { 
	'distances':
		[[7.02, 7.69, 8.75, 9.59], [6.14, 6.64, 7.65, 8.41], [6.36, 6.52, 7.57, 8.03], [5.46, 5.36, 6.5, 6.87], [7.02, 6.14, 6.36, 5.46], [7.69, 6.64, 6.52, 5.36], [8.75, 7.65, 7.57, 6.5], [9.59, 8.41, 8.03, 6.87]],
	'comparisons':
		[[('O', 'GLY', 'O', 'GLY', 7.02), ('O', 'GLY', 'C', 'GLY', 7.69), ('O', 'GLY', 'CA', 'GLY', 8.75), ('O', 'GLY', 'N', 'GLY', 9.59)], [('C', 'GLY', 'O', 'GLY', 6.14), ('C', 'GLY', 'C', 'GLY', 6.64), ('C', 'GLY', 'CA', 'GLY', 7.65), ('C', 'GLY', 'N', 'GLY', 8.41)], [('CA', 'GLY', 'O', 'GLY', 6.36), ('CA', 'GLY', 'C', 'GLY', 6.52), ('CA', 'GLY', 'CA', 'GLY', 7.57), ('CA', 'GLY', 'N', 'GLY', 8.03)], [('N', 'GLY', 'O', 'GLY', 5.46), ('N', 'GLY', 'C', 'GLY', 5.36), ('N', 'GLY', 'CA', 'GLY', 6.5), ('N', 'GLY', 'N', 'GLY', 6.87)], [('O', 'GLY', 'O', 'GLY', 7.02), ('O', 'GLY', 'C', 'GLY', 6.14), ('O', 'GLY', 'CA', 'GLY', 6.36), ('O', 'GLY', 'N', 'GLY', 5.46)], [('C', 'GLY', 'O', 'GLY', 7.69), ('C', 'GLY', 'C', 'GLY', 6.64), ('C', 'GLY', 'CA', 'GLY', 6.52), ('C', 'GLY', 'N', 'GLY', 5.36)], [('CA', 'GLY', 'O', 'GLY', 8.75), ('CA', 'GLY', 'C', 'GLY', 7.65), ('CA', 'GLY', 'CA', 'GLY', 7.57), ('CA', 'GLY', 'N', 'GLY', 6.5)], [('N', 'GLY', 'O', 'GLY', 9.59), ('N', 'GLY', 'C', 'GLY', 8.41), ('N', 'GLY', 'CA', 'GLY', 8.03), ('N', 'GLY', 'N', 'GLY', 6.87)]]}
GLY_ALA = { 
	'distances':
		[[8.25, 5.39, 5.86, 7.35, 7.87], [7.38, 4.93, 5.04, 6.47, 6.81], [6.35, 4.75, 4.42, 5.8, 6.28], [5.02, 4.25, 3.33, 4.43, 4.89], [6.23, 5.18, 4.87, 4.76, 4.25], [5.67, 5.68, 4.97, 4.42, 3.33], [6.79, 7.15, 6.37, 5.78, 4.41], [6.76, 7.93, 6.94, 6.16, 4.72]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ALA', 8.25), ('O', 'GLY', 'O', 'ALA', 5.39), ('O', 'GLY', 'C', 'ALA', 5.86), ('O', 'GLY', 'CA', 'ALA', 7.35), ('O', 'GLY', 'N', 'ALA', 7.87)], [('C', 'GLY', 'CB', 'ALA', 7.38), ('C', 'GLY', 'O', 'ALA', 4.93), ('C', 'GLY', 'C', 'ALA', 5.04), ('C', 'GLY', 'CA', 'ALA', 6.47), ('C', 'GLY', 'N', 'ALA', 6.81)], [('CA', 'GLY', 'CB', 'ALA', 6.35), ('CA', 'GLY', 'O', 'ALA', 4.75), ('CA', 'GLY', 'C', 'ALA', 4.42), ('CA', 'GLY', 'CA', 'ALA', 5.8), ('CA', 'GLY', 'N', 'ALA', 6.28)], [('N', 'GLY', 'CB', 'ALA', 5.02), ('N', 'GLY', 'O', 'ALA', 4.25), ('N', 'GLY', 'C', 'ALA', 3.33), ('N', 'GLY', 'CA', 'ALA', 4.43), ('N', 'GLY', 'N', 'ALA', 4.89)], [('O', 'GLY', 'CB', 'ALA', 6.23), ('O', 'GLY', 'O', 'ALA', 5.18), ('O', 'GLY', 'C', 'ALA', 4.87), ('O', 'GLY', 'CA', 'ALA', 4.76), ('O', 'GLY', 'N', 'ALA', 4.25)], [('C', 'GLY', 'CB', 'ALA', 5.67), ('C', 'GLY', 'O', 'ALA', 5.68), ('C', 'GLY', 'C', 'ALA', 4.97), ('C', 'GLY', 'CA', 'ALA', 4.42), ('C', 'GLY', 'N', 'ALA', 3.33)], [('CA', 'GLY', 'CB', 'ALA', 6.79), ('CA', 'GLY', 'O', 'ALA', 7.15), ('CA', 'GLY', 'C', 'ALA', 6.37), ('CA', 'GLY', 'CA', 'ALA', 5.78), ('CA', 'GLY', 'N', 'ALA', 4.41)], [('N', 'GLY', 'CB', 'ALA', 6.76), ('N', 'GLY', 'O', 'ALA', 7.93), ('N', 'GLY', 'C', 'ALA', 6.94), ('N', 'GLY', 'CA', 'ALA', 6.16), ('N', 'GLY', 'N', 'ALA', 4.72)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ALA_ASP, d, 'A_1tz3_3_6_1_26')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_ASP, d, 'A_1tz3_3_6_1_26')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLYI, d, 'A_1tz3_3_6_1_26')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLY_GLY, d, 'A_1tz3_3_6_1_26')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_ALA, d, 'A_1tz3_3_6_1_26')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ALA_ASP' :  match1,
		'GLY_ASP' :  match2,
		'ASP_GLYI' :  match3,
		'GLY_GLY' :  match4,
		'GLY_ALA' :  match5}