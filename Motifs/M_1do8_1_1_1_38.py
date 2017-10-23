'''
FUNC:M_1do8_1_1_1_38
PDB:1do8
EC:1.1.1.38
RESI:tyr,lys,asp,mn
LOCI:a-112,183,278,604;
'''
import motifFunctions as cmd
ASP_MN = { 
	'distances':
		[[7.69], [7.71], [8.56], [7.23], [7.69], [7.71], [8.56], [7.23]],
	'comparisons':
		[[('CB', 'ASP', 'MN', 'MN', 7.69)], [('CG', 'ASP', 'MN', 'MN', 7.71)], [('OD1', 'ASP', 'MN', 'MN', 8.56)], [('OD2', 'ASP', 'MN', 'MN', 7.23)], [('CB', 'ASP', 'MN', 'MN', 7.69)], [('CG', 'ASP', 'MN', 'MN', 7.71)], [('OD1', 'ASP', 'MN', 'MN', 8.56)], [('OD2', 'ASP', 'MN', 'MN', 7.23)]]}
ASP_TYR = { 
	'distances':
		[[15.08, 13.63, 12.6, 13.42, 11.26, 12.19, 11.03, 9.81], [13.94, 12.47, 11.53, 12.17, 10.16, 10.91, 9.81, 8.55], [14.29, 12.79, 11.97, 12.34, 10.59, 11.04, 10.07, 8.75], [12.79, 11.34, 10.35, 11.12, 8.99, 9.91, 8.75, 7.56], [15.08, 13.63, 12.6, 13.42, 11.26, 12.19, 11.03, 9.81], [13.94, 12.47, 11.53, 12.17, 10.16, 10.91, 9.81, 8.55], [14.29, 12.79, 11.97, 12.34, 10.59, 11.04, 10.07, 8.75], [12.79, 11.34, 10.35, 11.12, 8.99, 9.91, 8.75, 7.56]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 15.08), ('CB', 'ASP', 'CG', 'TYR', 13.63), ('CB', 'ASP', 'CD1', 'TYR', 12.6), ('CB', 'ASP', 'CD2', 'TYR', 13.42), ('CB', 'ASP', 'CE1', 'TYR', 11.26), ('CB', 'ASP', 'CE2', 'TYR', 12.19), ('CB', 'ASP', 'CZ', 'TYR', 11.03), ('CB', 'ASP', 'OH', 'TYR', 9.81)], [('CG', 'ASP', 'CB', 'TYR', 13.94), ('CG', 'ASP', 'CG', 'TYR', 12.47), ('CG', 'ASP', 'CD1', 'TYR', 11.53), ('CG', 'ASP', 'CD2', 'TYR', 12.17), ('CG', 'ASP', 'CE1', 'TYR', 10.16), ('CG', 'ASP', 'CE2', 'TYR', 10.91), ('CG', 'ASP', 'CZ', 'TYR', 9.81), ('CG', 'ASP', 'OH', 'TYR', 8.55)], [('OD1', 'ASP', 'CB', 'TYR', 14.29), ('OD1', 'ASP', 'CG', 'TYR', 12.79), ('OD1', 'ASP', 'CD1', 'TYR', 11.97), ('OD1', 'ASP', 'CD2', 'TYR', 12.34), ('OD1', 'ASP', 'CE1', 'TYR', 10.59), ('OD1', 'ASP', 'CE2', 'TYR', 11.04), ('OD1', 'ASP', 'CZ', 'TYR', 10.07), ('OD1', 'ASP', 'OH', 'TYR', 8.75)], [('OD2', 'ASP', 'CB', 'TYR', 12.79), ('OD2', 'ASP', 'CG', 'TYR', 11.34), ('OD2', 'ASP', 'CD1', 'TYR', 10.35), ('OD2', 'ASP', 'CD2', 'TYR', 11.12), ('OD2', 'ASP', 'CE1', 'TYR', 8.99), ('OD2', 'ASP', 'CE2', 'TYR', 9.91), ('OD2', 'ASP', 'CZ', 'TYR', 8.75), ('OD2', 'ASP', 'OH', 'TYR', 7.56)], [('CB', 'ASP', 'CB', 'TYR', 15.08), ('CB', 'ASP', 'CG', 'TYR', 13.63), ('CB', 'ASP', 'CD1', 'TYR', 12.6), ('CB', 'ASP', 'CD2', 'TYR', 13.42), ('CB', 'ASP', 'CE1', 'TYR', 11.26), ('CB', 'ASP', 'CE2', 'TYR', 12.19), ('CB', 'ASP', 'CZ', 'TYR', 11.03), ('CB', 'ASP', 'OH', 'TYR', 9.81)], [('CG', 'ASP', 'CB', 'TYR', 13.94), ('CG', 'ASP', 'CG', 'TYR', 12.47), ('CG', 'ASP', 'CD1', 'TYR', 11.53), ('CG', 'ASP', 'CD2', 'TYR', 12.17), ('CG', 'ASP', 'CE1', 'TYR', 10.16), ('CG', 'ASP', 'CE2', 'TYR', 10.91), ('CG', 'ASP', 'CZ', 'TYR', 9.81), ('CG', 'ASP', 'OH', 'TYR', 8.55)], [('OD1', 'ASP', 'CB', 'TYR', 14.29), ('OD1', 'ASP', 'CG', 'TYR', 12.79), ('OD1', 'ASP', 'CD1', 'TYR', 11.97), ('OD1', 'ASP', 'CD2', 'TYR', 12.34), ('OD1', 'ASP', 'CE1', 'TYR', 10.59), ('OD1', 'ASP', 'CE2', 'TYR', 11.04), ('OD1', 'ASP', 'CZ', 'TYR', 10.07), ('OD1', 'ASP', 'OH', 'TYR', 8.75)], [('OD2', 'ASP', 'CB', 'TYR', 12.79), ('OD2', 'ASP', 'CG', 'TYR', 11.34), ('OD2', 'ASP', 'CD1', 'TYR', 10.35), ('OD2', 'ASP', 'CD2', 'TYR', 11.12), ('OD2', 'ASP', 'CE1', 'TYR', 8.99), ('OD2', 'ASP', 'CE2', 'TYR', 9.91), ('OD2', 'ASP', 'CZ', 'TYR', 8.75), ('OD2', 'ASP', 'OH', 'TYR', 7.56)]]}
TYR_MN = { 
	'distances':
		[[12.78], [11.46], [10.48], [11.42], [9.36], [10.44], [9.35], [8.49], [12.78], [11.46], [10.48], [11.42], [9.36], [10.44], [9.35], [8.49]],
	'comparisons':
		[[('CB', 'TYR', 'MN', 'MN', 12.78)], [('CG', 'TYR', 'MN', 'MN', 11.46)], [('CD1', 'TYR', 'MN', 'MN', 10.48)], [('CD2', 'TYR', 'MN', 'MN', 11.42)], [('CE1', 'TYR', 'MN', 'MN', 9.36)], [('CE2', 'TYR', 'MN', 'MN', 10.44)], [('CZ', 'TYR', 'MN', 'MN', 9.35)], [('OH', 'TYR', 'MN', 'MN', 8.49)], [('CB', 'TYR', 'MN', 'MN', 12.78)], [('CG', 'TYR', 'MN', 'MN', 11.46)], [('CD1', 'TYR', 'MN', 'MN', 10.48)], [('CD2', 'TYR', 'MN', 'MN', 11.42)], [('CE1', 'TYR', 'MN', 'MN', 9.36)], [('CE2', 'TYR', 'MN', 'MN', 10.44)], [('CZ', 'TYR', 'MN', 'MN', 9.35)], [('OH', 'TYR', 'MN', 'MN', 8.49)]]}
LYS_TYR = { 
	'distances':
		[[10.85, 9.94, 8.63, 10.58, 8.0, 10.11, 8.86, 8.73], [10.43, 9.39, 8.03, 9.97, 7.25, 9.41, 8.08, 7.85], [9.93, 8.71, 7.43, 9.06, 6.4, 8.31, 6.96, 6.53], [9.71, 8.41, 7.16, 8.66, 6.01, 7.83, 6.46, 5.91], [9.73, 8.29, 7.25, 8.23, 5.9, 7.16, 5.86, 4.92], [10.85, 9.94, 8.63, 10.58, 8.0, 10.11, 8.86, 8.73], [10.43, 9.39, 8.03, 9.97, 7.25, 9.41, 8.08, 7.85], [9.93, 8.71, 7.43, 9.06, 6.4, 8.31, 6.96, 6.53], [9.71, 8.41, 7.16, 8.66, 6.01, 7.83, 6.46, 5.91], [9.73, 8.29, 7.25, 8.23, 5.9, 7.16, 5.86, 4.92]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 10.85), ('CB', 'LYS', 'CG', 'TYR', 9.94), ('CB', 'LYS', 'CD1', 'TYR', 8.63), ('CB', 'LYS', 'CD2', 'TYR', 10.58), ('CB', 'LYS', 'CE1', 'TYR', 8.0), ('CB', 'LYS', 'CE2', 'TYR', 10.11), ('CB', 'LYS', 'CZ', 'TYR', 8.86), ('CB', 'LYS', 'OH', 'TYR', 8.73)], [('CG', 'LYS', 'CB', 'TYR', 10.43), ('CG', 'LYS', 'CG', 'TYR', 9.39), ('CG', 'LYS', 'CD1', 'TYR', 8.03), ('CG', 'LYS', 'CD2', 'TYR', 9.97), ('CG', 'LYS', 'CE1', 'TYR', 7.25), ('CG', 'LYS', 'CE2', 'TYR', 9.41), ('CG', 'LYS', 'CZ', 'TYR', 8.08), ('CG', 'LYS', 'OH', 'TYR', 7.85)], [('CD', 'LYS', 'CB', 'TYR', 9.93), ('CD', 'LYS', 'CG', 'TYR', 8.71), ('CD', 'LYS', 'CD1', 'TYR', 7.43), ('CD', 'LYS', 'CD2', 'TYR', 9.06), ('CD', 'LYS', 'CE1', 'TYR', 6.4), ('CD', 'LYS', 'CE2', 'TYR', 8.31), ('CD', 'LYS', 'CZ', 'TYR', 6.96), ('CD', 'LYS', 'OH', 'TYR', 6.53)], [('CE', 'LYS', 'CB', 'TYR', 9.71), ('CE', 'LYS', 'CG', 'TYR', 8.41), ('CE', 'LYS', 'CD1', 'TYR', 7.16), ('CE', 'LYS', 'CD2', 'TYR', 8.66), ('CE', 'LYS', 'CE1', 'TYR', 6.01), ('CE', 'LYS', 'CE2', 'TYR', 7.83), ('CE', 'LYS', 'CZ', 'TYR', 6.46), ('CE', 'LYS', 'OH', 'TYR', 5.91)], [('NZ', 'LYS', 'CB', 'TYR', 9.73), ('NZ', 'LYS', 'CG', 'TYR', 8.29), ('NZ', 'LYS', 'CD1', 'TYR', 7.25), ('NZ', 'LYS', 'CD2', 'TYR', 8.23), ('NZ', 'LYS', 'CE1', 'TYR', 5.9), ('NZ', 'LYS', 'CE2', 'TYR', 7.16), ('NZ', 'LYS', 'CZ', 'TYR', 5.86), ('NZ', 'LYS', 'OH', 'TYR', 4.92)], [('CB', 'LYS', 'CB', 'TYR', 10.85), ('CB', 'LYS', 'CG', 'TYR', 9.94), ('CB', 'LYS', 'CD1', 'TYR', 8.63), ('CB', 'LYS', 'CD2', 'TYR', 10.58), ('CB', 'LYS', 'CE1', 'TYR', 8.0), ('CB', 'LYS', 'CE2', 'TYR', 10.11), ('CB', 'LYS', 'CZ', 'TYR', 8.86), ('CB', 'LYS', 'OH', 'TYR', 8.73)], [('CG', 'LYS', 'CB', 'TYR', 10.43), ('CG', 'LYS', 'CG', 'TYR', 9.39), ('CG', 'LYS', 'CD1', 'TYR', 8.03), ('CG', 'LYS', 'CD2', 'TYR', 9.97), ('CG', 'LYS', 'CE1', 'TYR', 7.25), ('CG', 'LYS', 'CE2', 'TYR', 9.41), ('CG', 'LYS', 'CZ', 'TYR', 8.08), ('CG', 'LYS', 'OH', 'TYR', 7.85)], [('CD', 'LYS', 'CB', 'TYR', 9.93), ('CD', 'LYS', 'CG', 'TYR', 8.71), ('CD', 'LYS', 'CD1', 'TYR', 7.43), ('CD', 'LYS', 'CD2', 'TYR', 9.06), ('CD', 'LYS', 'CE1', 'TYR', 6.4), ('CD', 'LYS', 'CE2', 'TYR', 8.31), ('CD', 'LYS', 'CZ', 'TYR', 6.96), ('CD', 'LYS', 'OH', 'TYR', 6.53)], [('CE', 'LYS', 'CB', 'TYR', 9.71), ('CE', 'LYS', 'CG', 'TYR', 8.41), ('CE', 'LYS', 'CD1', 'TYR', 7.16), ('CE', 'LYS', 'CD2', 'TYR', 8.66), ('CE', 'LYS', 'CE1', 'TYR', 6.01), ('CE', 'LYS', 'CE2', 'TYR', 7.83), ('CE', 'LYS', 'CZ', 'TYR', 6.46), ('CE', 'LYS', 'OH', 'TYR', 5.91)], [('NZ', 'LYS', 'CB', 'TYR', 9.73), ('NZ', 'LYS', 'CG', 'TYR', 8.29), ('NZ', 'LYS', 'CD1', 'TYR', 7.25), ('NZ', 'LYS', 'CD2', 'TYR', 8.23), ('NZ', 'LYS', 'CE1', 'TYR', 5.9), ('NZ', 'LYS', 'CE2', 'TYR', 7.16), ('NZ', 'LYS', 'CZ', 'TYR', 5.86), ('NZ', 'LYS', 'OH', 'TYR', 4.92)]]}
LYS_MN = { 
	'distances':
		[[9.91], [8.45], [7.89], [6.56], [6.39], [9.91], [8.45], [7.89], [6.56], [6.39]],
	'comparisons':
		[[('CB', 'LYS', 'MN', 'MN', 9.91)], [('CG', 'LYS', 'MN', 'MN', 8.45)], [('CD', 'LYS', 'MN', 'MN', 7.89)], [('CE', 'LYS', 'MN', 'MN', 6.56)], [('NZ', 'LYS', 'MN', 'MN', 6.39)], [('CB', 'LYS', 'MN', 'MN', 9.91)], [('CG', 'LYS', 'MN', 'MN', 8.45)], [('CD', 'LYS', 'MN', 'MN', 7.89)], [('CE', 'LYS', 'MN', 'MN', 6.56)], [('NZ', 'LYS', 'MN', 'MN', 6.39)]]}
ASP_LYS = { 
	'distances':
		[[9.37, 8.7, 7.96, 7.85, 7.43], [8.93, 8.27, 7.25, 7.17, 6.48], [9.84, 9.26, 8.12, 8.05, 7.14], [7.86, 7.12, 6.03, 5.96, 5.32], [9.37, 8.7, 7.96, 7.85, 7.43], [8.93, 8.27, 7.25, 7.17, 6.48], [9.84, 9.26, 8.12, 8.05, 7.14], [7.86, 7.12, 6.03, 5.96, 5.32]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 9.37), ('CB', 'ASP', 'CG', 'LYS', 8.7), ('CB', 'ASP', 'CD', 'LYS', 7.96), ('CB', 'ASP', 'CE', 'LYS', 7.85), ('CB', 'ASP', 'NZ', 'LYS', 7.43)], [('CG', 'ASP', 'CB', 'LYS', 8.93), ('CG', 'ASP', 'CG', 'LYS', 8.27), ('CG', 'ASP', 'CD', 'LYS', 7.25), ('CG', 'ASP', 'CE', 'LYS', 7.17), ('CG', 'ASP', 'NZ', 'LYS', 6.48)], [('OD1', 'ASP', 'CB', 'LYS', 9.84), ('OD1', 'ASP', 'CG', 'LYS', 9.26), ('OD1', 'ASP', 'CD', 'LYS', 8.12), ('OD1', 'ASP', 'CE', 'LYS', 8.05), ('OD1', 'ASP', 'NZ', 'LYS', 7.14)], [('OD2', 'ASP', 'CB', 'LYS', 7.86), ('OD2', 'ASP', 'CG', 'LYS', 7.12), ('OD2', 'ASP', 'CD', 'LYS', 6.03), ('OD2', 'ASP', 'CE', 'LYS', 5.96), ('OD2', 'ASP', 'NZ', 'LYS', 5.32)], [('CB', 'ASP', 'CB', 'LYS', 9.37), ('CB', 'ASP', 'CG', 'LYS', 8.7), ('CB', 'ASP', 'CD', 'LYS', 7.96), ('CB', 'ASP', 'CE', 'LYS', 7.85), ('CB', 'ASP', 'NZ', 'LYS', 7.43)], [('CG', 'ASP', 'CB', 'LYS', 8.93), ('CG', 'ASP', 'CG', 'LYS', 8.27), ('CG', 'ASP', 'CD', 'LYS', 7.25), ('CG', 'ASP', 'CE', 'LYS', 7.17), ('CG', 'ASP', 'NZ', 'LYS', 6.48)], [('OD1', 'ASP', 'CB', 'LYS', 9.84), ('OD1', 'ASP', 'CG', 'LYS', 9.26), ('OD1', 'ASP', 'CD', 'LYS', 8.12), ('OD1', 'ASP', 'CE', 'LYS', 8.05), ('OD1', 'ASP', 'NZ', 'LYS', 7.14)], [('OD2', 'ASP', 'CB', 'LYS', 7.86), ('OD2', 'ASP', 'CG', 'LYS', 7.12), ('OD2', 'ASP', 'CD', 'LYS', 6.03), ('OD2', 'ASP', 'CE', 'LYS', 5.96), ('OD2', 'ASP', 'NZ', 'LYS', 5.32)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_MN, d, 'M_1do8_1_1_1_38')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_TYR, d, 'M_1do8_1_1_1_38')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_MN, d, 'M_1do8_1_1_1_38')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_TYR, d, 'M_1do8_1_1_1_38')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(LYS_MN, d, 'M_1do8_1_1_1_38')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_LYS, d, 'M_1do8_1_1_1_38')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_MN' :  match1,
		'ASP_TYR' :  match2,
		'TYR_MN' :  match3,
		'LYS_TYR' :  match4,
		'LYS_MN' :  match5,
		'ASP_LYS' :  match6}