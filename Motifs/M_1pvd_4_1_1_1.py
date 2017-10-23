'''
FUNC:M_1pvd_4_1_1_1
PDB:1pvd
EC:4.1.1.1
RESI:asp,his,his,glu,mg
LOCI:a-28,114,115,477,558;
'''
import motifFunctions as cmd
HIS_MG = { 
	'distances':
		[[41.81], [40.96], [40.33], [40.73], [39.71], [39.95], [38.09], [38.11], [37.3], [38.93], [37.58], [38.6]],
	'comparisons':
		[[('CB', 'HIS', 'MG', 'MG', 41.81)], [('CG', 'HIS', 'MG', 'MG', 40.96)], [('ND1', 'HIS', 'MG', 'MG', 40.33)], [('CD2', 'HIS', 'MG', 'MG', 40.73)], [('CE1', 'HIS', 'MG', 'MG', 39.71)], [('NE2', 'HIS', 'MG', 'MG', 39.95)], [('CB', 'HIS', 'MG', 'MG', 38.09)], [('CG', 'HIS', 'MG', 'MG', 38.11)], [('ND1', 'HIS', 'MG', 'MG', 37.3)], [('CD2', 'HIS', 'MG', 'MG', 38.93)], [('CE1', 'HIS', 'MG', 'MG', 37.58)], [('NE2', 'HIS', 'MG', 'MG', 38.6)]]}
ASP_HIS = { 
	'distances':
		[[8.94, 8.76, 9.82, 7.84, 9.7, 8.56], [8.37, 7.9, 8.84, 6.79, 8.53, 7.32], [9.25, 8.59, 9.38, 7.35, 8.86, 7.6], [7.11, 6.64, 7.61, 5.58, 7.41, 6.24], [9.08, 7.99, 8.42, 6.67, 7.55, 6.33], [9.07, 7.77, 7.92, 6.51, 6.84, 5.76], [10.08, 8.71, 8.66, 7.53, 7.45, 6.59], [8.18, 6.85, 6.99, 5.59, 5.94, 4.81]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.94), ('CB', 'ASP', 'CG', 'HIS', 8.76), ('CB', 'ASP', 'ND1', 'HIS', 9.82), ('CB', 'ASP', 'CD2', 'HIS', 7.84), ('CB', 'ASP', 'CE1', 'HIS', 9.7), ('CB', 'ASP', 'NE2', 'HIS', 8.56)], [('CG', 'ASP', 'CB', 'HIS', 8.37), ('CG', 'ASP', 'CG', 'HIS', 7.9), ('CG', 'ASP', 'ND1', 'HIS', 8.84), ('CG', 'ASP', 'CD2', 'HIS', 6.79), ('CG', 'ASP', 'CE1', 'HIS', 8.53), ('CG', 'ASP', 'NE2', 'HIS', 7.32)], [('OD1', 'ASP', 'CB', 'HIS', 9.25), ('OD1', 'ASP', 'CG', 'HIS', 8.59), ('OD1', 'ASP', 'ND1', 'HIS', 9.38), ('OD1', 'ASP', 'CD2', 'HIS', 7.35), ('OD1', 'ASP', 'CE1', 'HIS', 8.86), ('OD1', 'ASP', 'NE2', 'HIS', 7.6)], [('OD2', 'ASP', 'CB', 'HIS', 7.11), ('OD2', 'ASP', 'CG', 'HIS', 6.64), ('OD2', 'ASP', 'ND1', 'HIS', 7.61), ('OD2', 'ASP', 'CD2', 'HIS', 5.58), ('OD2', 'ASP', 'CE1', 'HIS', 7.41), ('OD2', 'ASP', 'NE2', 'HIS', 6.24)], [('CB', 'ASP', 'CB', 'HIS', 9.08), ('CB', 'ASP', 'CG', 'HIS', 7.99), ('CB', 'ASP', 'ND1', 'HIS', 8.42), ('CB', 'ASP', 'CD2', 'HIS', 6.67), ('CB', 'ASP', 'CE1', 'HIS', 7.55), ('CB', 'ASP', 'NE2', 'HIS', 6.33)], [('CG', 'ASP', 'CB', 'HIS', 9.07), ('CG', 'ASP', 'CG', 'HIS', 7.77), ('CG', 'ASP', 'ND1', 'HIS', 7.92), ('CG', 'ASP', 'CD2', 'HIS', 6.51), ('CG', 'ASP', 'CE1', 'HIS', 6.84), ('CG', 'ASP', 'NE2', 'HIS', 5.76)], [('OD1', 'ASP', 'CB', 'HIS', 10.08), ('OD1', 'ASP', 'CG', 'HIS', 8.71), ('OD1', 'ASP', 'ND1', 'HIS', 8.66), ('OD1', 'ASP', 'CD2', 'HIS', 7.53), ('OD1', 'ASP', 'CE1', 'HIS', 7.45), ('OD1', 'ASP', 'NE2', 'HIS', 6.59)], [('OD2', 'ASP', 'CB', 'HIS', 8.18), ('OD2', 'ASP', 'CG', 'HIS', 6.85), ('OD2', 'ASP', 'ND1', 'HIS', 6.99), ('OD2', 'ASP', 'CD2', 'HIS', 5.59), ('OD2', 'ASP', 'CE1', 'HIS', 5.94), ('OD2', 'ASP', 'NE2', 'HIS', 4.81)]]}
ASP_GLU = { 
	'distances':
		[[41.49, 40.6, 39.24, 39.13, 38.45], [41.26, 40.4, 39.02, 38.87, 38.27], [41.32, 40.5, 39.12, 38.94, 38.4], [41.05, 40.18, 38.79, 38.61, 38.04]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 41.49), ('CB', 'ASP', 'CG', 'GLU', 40.6), ('CB', 'ASP', 'CD', 'GLU', 39.24), ('CB', 'ASP', 'OE1', 'GLU', 39.13), ('CB', 'ASP', 'OE2', 'GLU', 38.45)], [('CG', 'ASP', 'CB', 'GLU', 41.26), ('CG', 'ASP', 'CG', 'GLU', 40.4), ('CG', 'ASP', 'CD', 'GLU', 39.02), ('CG', 'ASP', 'OE1', 'GLU', 38.87), ('CG', 'ASP', 'OE2', 'GLU', 38.27)], [('OD1', 'ASP', 'CB', 'GLU', 41.32), ('OD1', 'ASP', 'CG', 'GLU', 40.5), ('OD1', 'ASP', 'CD', 'GLU', 39.12), ('OD1', 'ASP', 'OE1', 'GLU', 38.94), ('OD1', 'ASP', 'OE2', 'GLU', 38.4)], [('OD2', 'ASP', 'CB', 'GLU', 41.05), ('OD2', 'ASP', 'CG', 'GLU', 40.18), ('OD2', 'ASP', 'CD', 'GLU', 38.79), ('OD2', 'ASP', 'OE1', 'GLU', 38.61), ('OD2', 'ASP', 'OE2', 'GLU', 38.04)]]}
ASP_MG = { 
	'distances':
		[[40.69], [40.37], [40.14], [40.4]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 40.69)], [('CG', 'ASP', 'MG', 'MG', 40.37)], [('OD1', 'ASP', 'MG', 'MG', 40.14)], [('OD2', 'ASP', 'MG', 'MG', 40.4)]]}
MG_HISI = { 
	'distances':
		[38.09, 38.11, 37.3, 38.93, 37.58, 38.6],
	'comparisons':
		[('MG', 'MG', 'CB', 'HISI', 38.09), ('MG', 'MG', 'CG', 'HISI', 38.11), ('MG', 'MG', 'ND1', 'HISI', 37.3), ('MG', 'MG', 'CD2', 'HISI', 38.93), ('MG', 'MG', 'CE1', 'HISI', 37.58), ('MG', 'MG', 'NE2', 'HISI', 38.6)]}
GLU_MG = { 
	'distances':
		[[11.23], [12.18], [12.27], [12.06], [12.79]],
	'comparisons':
		[[('CB', 'GLU', 'MG', 'MG', 11.23)], [('CG', 'GLU', 'MG', 'MG', 12.18)], [('CD', 'GLU', 'MG', 'MG', 12.27)], [('OE1', 'GLU', 'MG', 'MG', 12.06)], [('OE2', 'GLU', 'MG', 'MG', 12.79)]]}
GLU_HISI = { 
	'distances':
		[[37.41, 37.78, 37.11, 38.83, 37.72, 38.79], [36.4, 36.81, 36.19, 37.88, 36.83, 37.88], [35.0, 35.41, 34.76, 36.48, 35.41, 36.48], [34.88, 35.26, 34.57, 36.34, 35.2, 36.3], [34.18, 34.62, 34.02, 35.69, 34.68, 35.72]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HISI', 37.41), ('CB', 'GLU', 'CG', 'HISI', 37.78), ('CB', 'GLU', 'ND1', 'HISI', 37.11), ('CB', 'GLU', 'CD2', 'HISI', 38.83), ('CB', 'GLU', 'CE1', 'HISI', 37.72), ('CB', 'GLU', 'NE2', 'HISI', 38.79)], [('CG', 'GLU', 'CB', 'HISI', 36.4), ('CG', 'GLU', 'CG', 'HISI', 36.81), ('CG', 'GLU', 'ND1', 'HISI', 36.19), ('CG', 'GLU', 'CD2', 'HISI', 37.88), ('CG', 'GLU', 'CE1', 'HISI', 36.83), ('CG', 'GLU', 'NE2', 'HISI', 37.88)], [('CD', 'GLU', 'CB', 'HISI', 35.0), ('CD', 'GLU', 'CG', 'HISI', 35.41), ('CD', 'GLU', 'ND1', 'HISI', 34.76), ('CD', 'GLU', 'CD2', 'HISI', 36.48), ('CD', 'GLU', 'CE1', 'HISI', 35.41), ('CD', 'GLU', 'NE2', 'HISI', 36.48)], [('OE1', 'GLU', 'CB', 'HISI', 34.88), ('OE1', 'GLU', 'CG', 'HISI', 35.26), ('OE1', 'GLU', 'ND1', 'HISI', 34.57), ('OE1', 'GLU', 'CD2', 'HISI', 36.34), ('OE1', 'GLU', 'CE1', 'HISI', 35.2), ('OE1', 'GLU', 'NE2', 'HISI', 36.3)], [('OE2', 'GLU', 'CB', 'HISI', 34.18), ('OE2', 'GLU', 'CG', 'HISI', 34.62), ('OE2', 'GLU', 'ND1', 'HISI', 34.02), ('OE2', 'GLU', 'CD2', 'HISI', 35.69), ('OE2', 'GLU', 'CE1', 'HISI', 34.68), ('OE2', 'GLU', 'NE2', 'HISI', 35.72)]]}
HIS_GLU = { 
	'distances':
		[[41.44, 40.5, 39.06, 38.84, 38.33], [40.83, 39.93, 38.48, 38.23, 37.79], [40.16, 39.29, 37.82, 37.53, 37.16], [40.92, 40.06, 38.61, 38.35, 37.92], [39.83, 39.0, 37.53, 37.21, 36.89], [40.3, 39.47, 38.02, 37.72, 37.37], [37.41, 36.4, 35.0, 34.88, 34.18], [37.78, 36.81, 35.41, 35.26, 34.62], [37.11, 36.19, 34.76, 34.57, 34.02], [38.83, 37.88, 36.48, 36.34, 35.69], [37.72, 36.83, 35.41, 35.2, 34.68], [38.79, 37.88, 36.48, 36.3, 35.72]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 41.44), ('CB', 'HIS', 'CG', 'GLU', 40.5), ('CB', 'HIS', 'CD', 'GLU', 39.06), ('CB', 'HIS', 'OE1', 'GLU', 38.84), ('CB', 'HIS', 'OE2', 'GLU', 38.33)], [('CG', 'HIS', 'CB', 'GLU', 40.83), ('CG', 'HIS', 'CG', 'GLU', 39.93), ('CG', 'HIS', 'CD', 'GLU', 38.48), ('CG', 'HIS', 'OE1', 'GLU', 38.23), ('CG', 'HIS', 'OE2', 'GLU', 37.79)], [('ND1', 'HIS', 'CB', 'GLU', 40.16), ('ND1', 'HIS', 'CG', 'GLU', 39.29), ('ND1', 'HIS', 'CD', 'GLU', 37.82), ('ND1', 'HIS', 'OE1', 'GLU', 37.53), ('ND1', 'HIS', 'OE2', 'GLU', 37.16)], [('CD2', 'HIS', 'CB', 'GLU', 40.92), ('CD2', 'HIS', 'CG', 'GLU', 40.06), ('CD2', 'HIS', 'CD', 'GLU', 38.61), ('CD2', 'HIS', 'OE1', 'GLU', 38.35), ('CD2', 'HIS', 'OE2', 'GLU', 37.92)], [('CE1', 'HIS', 'CB', 'GLU', 39.83), ('CE1', 'HIS', 'CG', 'GLU', 39.0), ('CE1', 'HIS', 'CD', 'GLU', 37.53), ('CE1', 'HIS', 'OE1', 'GLU', 37.21), ('CE1', 'HIS', 'OE2', 'GLU', 36.89)], [('NE2', 'HIS', 'CB', 'GLU', 40.3), ('NE2', 'HIS', 'CG', 'GLU', 39.47), ('NE2', 'HIS', 'CD', 'GLU', 38.02), ('NE2', 'HIS', 'OE1', 'GLU', 37.72), ('NE2', 'HIS', 'OE2', 'GLU', 37.37)], [('CB', 'HIS', 'CB', 'GLU', 37.41), ('CB', 'HIS', 'CG', 'GLU', 36.4), ('CB', 'HIS', 'CD', 'GLU', 35.0), ('CB', 'HIS', 'OE1', 'GLU', 34.88), ('CB', 'HIS', 'OE2', 'GLU', 34.18)], [('CG', 'HIS', 'CB', 'GLU', 37.78), ('CG', 'HIS', 'CG', 'GLU', 36.81), ('CG', 'HIS', 'CD', 'GLU', 35.41), ('CG', 'HIS', 'OE1', 'GLU', 35.26), ('CG', 'HIS', 'OE2', 'GLU', 34.62)], [('ND1', 'HIS', 'CB', 'GLU', 37.11), ('ND1', 'HIS', 'CG', 'GLU', 36.19), ('ND1', 'HIS', 'CD', 'GLU', 34.76), ('ND1', 'HIS', 'OE1', 'GLU', 34.57), ('ND1', 'HIS', 'OE2', 'GLU', 34.02)], [('CD2', 'HIS', 'CB', 'GLU', 38.83), ('CD2', 'HIS', 'CG', 'GLU', 37.88), ('CD2', 'HIS', 'CD', 'GLU', 36.48), ('CD2', 'HIS', 'OE1', 'GLU', 36.34), ('CD2', 'HIS', 'OE2', 'GLU', 35.69)], [('CE1', 'HIS', 'CB', 'GLU', 37.72), ('CE1', 'HIS', 'CG', 'GLU', 36.83), ('CE1', 'HIS', 'CD', 'GLU', 35.41), ('CE1', 'HIS', 'OE1', 'GLU', 35.2), ('CE1', 'HIS', 'OE2', 'GLU', 34.68)], [('NE2', 'HIS', 'CB', 'GLU', 38.79), ('NE2', 'HIS', 'CG', 'GLU', 37.88), ('NE2', 'HIS', 'CD', 'GLU', 36.48), ('NE2', 'HIS', 'OE1', 'GLU', 36.3), ('NE2', 'HIS', 'OE2', 'GLU', 35.72)]]}
HIS_HIS = { 
	'distances':
		[[7.06, 6.42, 6.71, 6.12, 6.66, 6.28], [7.33, 6.36, 6.23, 6.08, 5.91, 5.77], [7.77, 6.85, 6.38, 6.87, 6.14, 6.43], [7.81, 6.58, 6.33, 6.01, 5.58, 5.3], [8.4, 7.27, 6.53, 7.22, 5.99, 6.44], [8.45, 7.15, 6.53, 6.78, 5.66, 5.81], [7.06, 7.33, 7.77, 7.81, 8.4, 8.45], [6.42, 6.36, 6.85, 6.58, 7.27, 7.15], [6.71, 6.23, 6.38, 6.33, 6.53, 6.53], [6.12, 6.08, 6.87, 6.01, 7.22, 6.78], [6.66, 5.91, 6.14, 5.58, 5.99, 5.66], [6.28, 5.77, 6.43, 5.3, 6.44, 5.81]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 7.06), ('CB', 'HIS', 'CG', 'HIS', 6.42), ('CB', 'HIS', 'ND1', 'HIS', 6.71), ('CB', 'HIS', 'CD2', 'HIS', 6.12), ('CB', 'HIS', 'CE1', 'HIS', 6.66), ('CB', 'HIS', 'NE2', 'HIS', 6.28)], [('CG', 'HIS', 'CB', 'HIS', 7.33), ('CG', 'HIS', 'CG', 'HIS', 6.36), ('CG', 'HIS', 'ND1', 'HIS', 6.23), ('CG', 'HIS', 'CD2', 'HIS', 6.08), ('CG', 'HIS', 'CE1', 'HIS', 5.91), ('CG', 'HIS', 'NE2', 'HIS', 5.77)], [('ND1', 'HIS', 'CB', 'HIS', 7.77), ('ND1', 'HIS', 'CG', 'HIS', 6.85), ('ND1', 'HIS', 'ND1', 'HIS', 6.38), ('ND1', 'HIS', 'CD2', 'HIS', 6.87), ('ND1', 'HIS', 'CE1', 'HIS', 6.14), ('ND1', 'HIS', 'NE2', 'HIS', 6.43)], [('CD2', 'HIS', 'CB', 'HIS', 7.81), ('CD2', 'HIS', 'CG', 'HIS', 6.58), ('CD2', 'HIS', 'ND1', 'HIS', 6.33), ('CD2', 'HIS', 'CD2', 'HIS', 6.01), ('CD2', 'HIS', 'CE1', 'HIS', 5.58), ('CD2', 'HIS', 'NE2', 'HIS', 5.3)], [('CE1', 'HIS', 'CB', 'HIS', 8.4), ('CE1', 'HIS', 'CG', 'HIS', 7.27), ('CE1', 'HIS', 'ND1', 'HIS', 6.53), ('CE1', 'HIS', 'CD2', 'HIS', 7.22), ('CE1', 'HIS', 'CE1', 'HIS', 5.99), ('CE1', 'HIS', 'NE2', 'HIS', 6.44)], [('NE2', 'HIS', 'CB', 'HIS', 8.45), ('NE2', 'HIS', 'CG', 'HIS', 7.15), ('NE2', 'HIS', 'ND1', 'HIS', 6.53), ('NE2', 'HIS', 'CD2', 'HIS', 6.78), ('NE2', 'HIS', 'CE1', 'HIS', 5.66), ('NE2', 'HIS', 'NE2', 'HIS', 5.81)], [('CB', 'HIS', 'CB', 'HIS', 7.06), ('CB', 'HIS', 'CG', 'HIS', 7.33), ('CB', 'HIS', 'ND1', 'HIS', 7.77), ('CB', 'HIS', 'CD2', 'HIS', 7.81), ('CB', 'HIS', 'CE1', 'HIS', 8.4), ('CB', 'HIS', 'NE2', 'HIS', 8.45)], [('CG', 'HIS', 'CB', 'HIS', 6.42), ('CG', 'HIS', 'CG', 'HIS', 6.36), ('CG', 'HIS', 'ND1', 'HIS', 6.85), ('CG', 'HIS', 'CD2', 'HIS', 6.58), ('CG', 'HIS', 'CE1', 'HIS', 7.27), ('CG', 'HIS', 'NE2', 'HIS', 7.15)], [('ND1', 'HIS', 'CB', 'HIS', 6.71), ('ND1', 'HIS', 'CG', 'HIS', 6.23), ('ND1', 'HIS', 'ND1', 'HIS', 6.38), ('ND1', 'HIS', 'CD2', 'HIS', 6.33), ('ND1', 'HIS', 'CE1', 'HIS', 6.53), ('ND1', 'HIS', 'NE2', 'HIS', 6.53)], [('CD2', 'HIS', 'CB', 'HIS', 6.12), ('CD2', 'HIS', 'CG', 'HIS', 6.08), ('CD2', 'HIS', 'ND1', 'HIS', 6.87), ('CD2', 'HIS', 'CD2', 'HIS', 6.01), ('CD2', 'HIS', 'CE1', 'HIS', 7.22), ('CD2', 'HIS', 'NE2', 'HIS', 6.78)], [('CE1', 'HIS', 'CB', 'HIS', 6.66), ('CE1', 'HIS', 'CG', 'HIS', 5.91), ('CE1', 'HIS', 'ND1', 'HIS', 6.14), ('CE1', 'HIS', 'CD2', 'HIS', 5.58), ('CE1', 'HIS', 'CE1', 'HIS', 5.99), ('CE1', 'HIS', 'NE2', 'HIS', 5.66)], [('NE2', 'HIS', 'CB', 'HIS', 6.28), ('NE2', 'HIS', 'CG', 'HIS', 5.77), ('NE2', 'HIS', 'ND1', 'HIS', 6.43), ('NE2', 'HIS', 'CD2', 'HIS', 5.3), ('NE2', 'HIS', 'CE1', 'HIS', 6.44), ('NE2', 'HIS', 'NE2', 'HIS', 5.81)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_MG, d, 'M_1pvd_4_1_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'M_1pvd_4_1_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLU, d, 'M_1pvd_4_1_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_MG, d, 'M_1pvd_4_1_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(MG_HISI, d, 'M_1pvd_4_1_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_MG, d, 'M_1pvd_4_1_1_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLU_HISI, d, 'M_1pvd_4_1_1_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(HIS_GLU, d, 'M_1pvd_4_1_1_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(HIS_HIS, d, 'M_1pvd_4_1_1_1')
	if match9 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_MG' :  match1,
		'ASP_HIS' :  match2,
		'ASP_GLU' :  match3,
		'ASP_MG' :  match4,
		'MG_HISI' :  match5,
		'GLU_MG' :  match6,
		'GLU_HISI' :  match7,
		'HIS_GLU' :  match8,
		'HIS_HIS' :  match9}