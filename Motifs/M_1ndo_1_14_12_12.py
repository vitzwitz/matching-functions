'''
FUNC:M_1ndo_1_14_12_12
PDB:1ndo
EC:1.14.12.12
RESI:asp,his,fes,fe,his
LOCI:a-205,208,451,452;c-104;
'''
import motifFunctions as cmd
HIS_FES = { 
	'distances':
		[[51.23, 48.99, 51.23, 49.0], [50.18, 47.9, 50.13, 47.96], [49.86, 47.54, 49.77, 47.66], [49.42, 47.14, 49.36, 47.2], [48.91, 46.57, 48.78, 46.72], [48.64, 46.32, 48.53, 46.44], [54.42, 52.29, 54.57, 52.14], [53.01, 50.88, 53.16, 50.74], [52.14, 50.05, 52.33, 49.86], [52.34, 50.18, 52.45, 50.09], [50.96, 48.86, 51.14, 48.69], [51.08, 48.93, 51.2, 48.82]],
	'comparisons':
		[[('CB', 'HIS', 'FE1', 'FES', 51.23), ('CB', 'HIS', 'FE2', 'FES', 48.99), ('CB', 'HIS', 'S1', 'FES', 51.23), ('CB', 'HIS', 'S2', 'FES', 49.0)], [('CG', 'HIS', 'FE1', 'FES', 50.18), ('CG', 'HIS', 'FE2', 'FES', 47.9), ('CG', 'HIS', 'S1', 'FES', 50.13), ('CG', 'HIS', 'S2', 'FES', 47.96)], [('ND1', 'HIS', 'FE1', 'FES', 49.86), ('ND1', 'HIS', 'FE2', 'FES', 47.54), ('ND1', 'HIS', 'S1', 'FES', 49.77), ('ND1', 'HIS', 'S2', 'FES', 47.66)], [('CD2', 'HIS', 'FE1', 'FES', 49.42), ('CD2', 'HIS', 'FE2', 'FES', 47.14), ('CD2', 'HIS', 'S1', 'FES', 49.36), ('CD2', 'HIS', 'S2', 'FES', 47.2)], [('CE1', 'HIS', 'FE1', 'FES', 48.91), ('CE1', 'HIS', 'FE2', 'FES', 46.57), ('CE1', 'HIS', 'S1', 'FES', 48.78), ('CE1', 'HIS', 'S2', 'FES', 46.72)], [('NE2', 'HIS', 'FE1', 'FES', 48.64), ('NE2', 'HIS', 'FE2', 'FES', 46.32), ('NE2', 'HIS', 'S1', 'FES', 48.53), ('NE2', 'HIS', 'S2', 'FES', 46.44)], [('CB', 'HIS', 'FE1', 'FES', 54.42), ('CB', 'HIS', 'FE2', 'FES', 52.29), ('CB', 'HIS', 'S1', 'FES', 54.57), ('CB', 'HIS', 'S2', 'FES', 52.14)], [('CG', 'HIS', 'FE1', 'FES', 53.01), ('CG', 'HIS', 'FE2', 'FES', 50.88), ('CG', 'HIS', 'S1', 'FES', 53.16), ('CG', 'HIS', 'S2', 'FES', 50.74)], [('ND1', 'HIS', 'FE1', 'FES', 52.14), ('ND1', 'HIS', 'FE2', 'FES', 50.05), ('ND1', 'HIS', 'S1', 'FES', 52.33), ('ND1', 'HIS', 'S2', 'FES', 49.86)], [('CD2', 'HIS', 'FE1', 'FES', 52.34), ('CD2', 'HIS', 'FE2', 'FES', 50.18), ('CD2', 'HIS', 'S1', 'FES', 52.45), ('CD2', 'HIS', 'S2', 'FES', 50.09)], [('CE1', 'HIS', 'FE1', 'FES', 50.96), ('CE1', 'HIS', 'FE2', 'FES', 48.86), ('CE1', 'HIS', 'S1', 'FES', 51.14), ('CE1', 'HIS', 'S2', 'FES', 48.69)], [('NE2', 'HIS', 'FE1', 'FES', 51.08), ('NE2', 'HIS', 'FE2', 'FES', 48.93), ('NE2', 'HIS', 'S1', 'FES', 51.2), ('NE2', 'HIS', 'S2', 'FES', 48.82)]]}
HIS_FE = { 
	'distances':
		[[7.55], [6.16], [6.14], [5.01], [5.04], [4.04], [12.52], [11.68], [11.9], [10.81], [11.25], [10.55]],
	'comparisons':
		[[('CB', 'HIS', 'FE', 'FE', 7.55)], [('CG', 'HIS', 'FE', 'FE', 6.16)], [('ND1', 'HIS', 'FE', 'FE', 6.14)], [('CD2', 'HIS', 'FE', 'FE', 5.01)], [('CE1', 'HIS', 'FE', 'FE', 5.04)], [('NE2', 'HIS', 'FE', 'FE', 4.04)], [('CB', 'HIS', 'FE', 'FE', 12.52)], [('CG', 'HIS', 'FE', 'FE', 11.68)], [('ND1', 'HIS', 'FE', 'FE', 11.9)], [('CD2', 'HIS', 'FE', 'FE', 10.81)], [('CE1', 'HIS', 'FE', 'FE', 11.25)], [('NE2', 'HIS', 'FE', 'FE', 10.55)]]}
HIS_ASP = { 
	'distances':
		[[7.06, 5.83, 5.44, 5.72], [6.7, 5.84, 5.71, 5.86], [5.79, 5.28, 5.2, 5.66], [7.57, 6.92, 6.97, 6.81], [6.32, 6.2, 6.35, 6.54], [7.35, 7.08, 7.26, 7.15], [10.05, 8.54, 7.96, 8.14], [8.82, 7.33, 6.95, 6.79], [9.08, 7.68, 7.59, 6.88], [7.49, 5.99, 5.59, 5.56], [8.07, 6.77, 6.94, 5.82], [6.97, 5.58, 5.64, 4.79]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.06), ('CB', 'HIS', 'CG', 'ASP', 5.83), ('CB', 'HIS', 'OD1', 'ASP', 5.44), ('CB', 'HIS', 'OD2', 'ASP', 5.72)], [('CG', 'HIS', 'CB', 'ASP', 6.7), ('CG', 'HIS', 'CG', 'ASP', 5.84), ('CG', 'HIS', 'OD1', 'ASP', 5.71), ('CG', 'HIS', 'OD2', 'ASP', 5.86)], [('ND1', 'HIS', 'CB', 'ASP', 5.79), ('ND1', 'HIS', 'CG', 'ASP', 5.28), ('ND1', 'HIS', 'OD1', 'ASP', 5.2), ('ND1', 'HIS', 'OD2', 'ASP', 5.66)], [('CD2', 'HIS', 'CB', 'ASP', 7.57), ('CD2', 'HIS', 'CG', 'ASP', 6.92), ('CD2', 'HIS', 'OD1', 'ASP', 6.97), ('CD2', 'HIS', 'OD2', 'ASP', 6.81)], [('CE1', 'HIS', 'CB', 'ASP', 6.32), ('CE1', 'HIS', 'CG', 'ASP', 6.2), ('CE1', 'HIS', 'OD1', 'ASP', 6.35), ('CE1', 'HIS', 'OD2', 'ASP', 6.54)], [('NE2', 'HIS', 'CB', 'ASP', 7.35), ('NE2', 'HIS', 'CG', 'ASP', 7.08), ('NE2', 'HIS', 'OD1', 'ASP', 7.26), ('NE2', 'HIS', 'OD2', 'ASP', 7.15)], [('CB', 'HIS', 'CB', 'ASP', 10.05), ('CB', 'HIS', 'CG', 'ASP', 8.54), ('CB', 'HIS', 'OD1', 'ASP', 7.96), ('CB', 'HIS', 'OD2', 'ASP', 8.14)], [('CG', 'HIS', 'CB', 'ASP', 8.82), ('CG', 'HIS', 'CG', 'ASP', 7.33), ('CG', 'HIS', 'OD1', 'ASP', 6.95), ('CG', 'HIS', 'OD2', 'ASP', 6.79)], [('ND1', 'HIS', 'CB', 'ASP', 9.08), ('ND1', 'HIS', 'CG', 'ASP', 7.68), ('ND1', 'HIS', 'OD1', 'ASP', 7.59), ('ND1', 'HIS', 'OD2', 'ASP', 6.88)], [('CD2', 'HIS', 'CB', 'ASP', 7.49), ('CD2', 'HIS', 'CG', 'ASP', 5.99), ('CD2', 'HIS', 'OD1', 'ASP', 5.59), ('CD2', 'HIS', 'OD2', 'ASP', 5.56)], [('CE1', 'HIS', 'CB', 'ASP', 8.07), ('CE1', 'HIS', 'CG', 'ASP', 6.77), ('CE1', 'HIS', 'OD1', 'ASP', 6.94), ('CE1', 'HIS', 'OD2', 'ASP', 5.82)], [('NE2', 'HIS', 'CB', 'ASP', 6.97), ('NE2', 'HIS', 'CG', 'ASP', 5.58), ('NE2', 'HIS', 'OD1', 'ASP', 5.64), ('NE2', 'HIS', 'OD2', 'ASP', 4.79)]]}
ASP_FES = { 
	'distances':
		[[48.86, 46.56, 48.8, 46.66], [49.82, 47.55, 49.8, 47.6], [51.02, 48.74, 50.98, 48.8], [49.34, 47.11, 49.37, 47.11]],
	'comparisons':
		[[('CB', 'ASP', 'FE1', 'FES', 48.86), ('CB', 'ASP', 'FE2', 'FES', 46.56), ('CB', 'ASP', 'S1', 'FES', 48.8), ('CB', 'ASP', 'S2', 'FES', 46.66)], [('CG', 'ASP', 'FE1', 'FES', 49.82), ('CG', 'ASP', 'FE2', 'FES', 47.55), ('CG', 'ASP', 'S1', 'FES', 49.8), ('CG', 'ASP', 'S2', 'FES', 47.6)], [('OD1', 'ASP', 'FE1', 'FES', 51.02), ('OD1', 'ASP', 'FE2', 'FES', 48.74), ('OD1', 'ASP', 'S1', 'FES', 50.98), ('OD1', 'ASP', 'S2', 'FES', 48.8)], [('OD2', 'ASP', 'FE1', 'FES', 49.34), ('OD2', 'ASP', 'FE2', 'FES', 47.11), ('OD2', 'ASP', 'S1', 'FES', 49.37), ('OD2', 'ASP', 'S2', 'FES', 47.11)]]}
FES_FE = { 
	'distances':
		[[47.44], [45.11], [47.3], [45.26]],
	'comparisons':
		[[('FE1', 'FES', 'FE', 'FE', 47.44)], [('FE2', 'FES', 'FE', 'FE', 45.11)], [('S1', 'FES', 'FE', 'FE', 47.3)], [('S2', 'FES', 'FE', 'FE', 45.26)]]}
FE_HISI = { 
	'distances':
		[12.52, 11.68, 11.9, 10.81, 11.25, 10.55],
	'comparisons':
		[('FE', 'FE', 'CB', 'HISI', 12.52), ('FE', 'FE', 'CG', 'HISI', 11.68), ('FE', 'FE', 'ND1', 'HISI', 11.9), ('FE', 'FE', 'CD2', 'HISI', 10.81), ('FE', 'FE', 'CE1', 'HISI', 11.25), ('FE', 'FE', 'NE2', 'HISI', 10.55)]}
ASP_FE = { 
	'distances':
		[[9.01], [8.95], [9.25], [8.95]],
	'comparisons':
		[[('CB', 'ASP', 'FE', 'FE', 9.01)], [('CG', 'ASP', 'FE', 'FE', 8.95)], [('OD1', 'ASP', 'FE', 'FE', 9.25)], [('OD2', 'ASP', 'FE', 'FE', 8.95)]]}
FES_HISI = { 
	'distances':
		[[54.42, 53.01, 52.14, 52.34, 50.96, 51.08], [52.29, 50.88, 50.05, 50.18, 48.86, 48.93], [54.57, 53.16, 52.33, 52.45, 51.14, 51.2], [52.14, 50.74, 49.86, 50.09, 48.69, 48.82]],
	'comparisons':
		[[('FE1', 'FES', 'CB', 'HISI', 54.42), ('FE1', 'FES', 'CG', 'HISI', 53.01), ('FE1', 'FES', 'ND1', 'HISI', 52.14), ('FE1', 'FES', 'CD2', 'HISI', 52.34), ('FE1', 'FES', 'CE1', 'HISI', 50.96), ('FE1', 'FES', 'NE2', 'HISI', 51.08)], [('FE2', 'FES', 'CB', 'HISI', 52.29), ('FE2', 'FES', 'CG', 'HISI', 50.88), ('FE2', 'FES', 'ND1', 'HISI', 50.05), ('FE2', 'FES', 'CD2', 'HISI', 50.18), ('FE2', 'FES', 'CE1', 'HISI', 48.86), ('FE2', 'FES', 'NE2', 'HISI', 48.93)], [('S1', 'FES', 'CB', 'HISI', 54.57), ('S1', 'FES', 'CG', 'HISI', 53.16), ('S1', 'FES', 'ND1', 'HISI', 52.33), ('S1', 'FES', 'CD2', 'HISI', 52.45), ('S1', 'FES', 'CE1', 'HISI', 51.14), ('S1', 'FES', 'NE2', 'HISI', 51.2)], [('S2', 'FES', 'CB', 'HISI', 52.14), ('S2', 'FES', 'CG', 'HISI', 50.74), ('S2', 'FES', 'ND1', 'HISI', 49.86), ('S2', 'FES', 'CD2', 'HISI', 50.09), ('S2', 'FES', 'CE1', 'HISI', 48.69), ('S2', 'FES', 'NE2', 'HISI', 48.82)]]}
HIS_HIS = { 
	'distances':
		[[7.09, 6.37, 7.01, 5.54, 6.74, 5.85], [8.55, 7.74, 8.24, 6.8, 7.75, 6.84], [9.35, 8.47, 9.01, 7.34, 8.38, 7.32], [9.52, 8.73, 9.08, 7.92, 8.58, 7.83], [10.62, 9.71, 10.14, 8.6, 9.44, 8.45], [10.71, 9.85, 10.18, 8.9, 9.55, 8.72], [7.09, 8.55, 9.35, 9.52, 10.62, 10.71], [6.37, 7.74, 8.47, 8.73, 9.71, 9.85], [7.01, 8.24, 9.01, 9.08, 10.14, 10.18], [5.54, 6.8, 7.34, 7.92, 8.6, 8.9], [6.74, 7.75, 8.38, 8.58, 9.44, 9.55], [5.85, 6.84, 7.32, 7.83, 8.45, 8.72]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 7.09), ('CB', 'HIS', 'CG', 'HIS', 6.37), ('CB', 'HIS', 'ND1', 'HIS', 7.01), ('CB', 'HIS', 'CD2', 'HIS', 5.54), ('CB', 'HIS', 'CE1', 'HIS', 6.74), ('CB', 'HIS', 'NE2', 'HIS', 5.85)], [('CG', 'HIS', 'CB', 'HIS', 8.55), ('CG', 'HIS', 'CG', 'HIS', 7.74), ('CG', 'HIS', 'ND1', 'HIS', 8.24), ('CG', 'HIS', 'CD2', 'HIS', 6.8), ('CG', 'HIS', 'CE1', 'HIS', 7.75), ('CG', 'HIS', 'NE2', 'HIS', 6.84)], [('ND1', 'HIS', 'CB', 'HIS', 9.35), ('ND1', 'HIS', 'CG', 'HIS', 8.47), ('ND1', 'HIS', 'ND1', 'HIS', 9.01), ('ND1', 'HIS', 'CD2', 'HIS', 7.34), ('ND1', 'HIS', 'CE1', 'HIS', 8.38), ('ND1', 'HIS', 'NE2', 'HIS', 7.32)], [('CD2', 'HIS', 'CB', 'HIS', 9.52), ('CD2', 'HIS', 'CG', 'HIS', 8.73), ('CD2', 'HIS', 'ND1', 'HIS', 9.08), ('CD2', 'HIS', 'CD2', 'HIS', 7.92), ('CD2', 'HIS', 'CE1', 'HIS', 8.58), ('CD2', 'HIS', 'NE2', 'HIS', 7.83)], [('CE1', 'HIS', 'CB', 'HIS', 10.62), ('CE1', 'HIS', 'CG', 'HIS', 9.71), ('CE1', 'HIS', 'ND1', 'HIS', 10.14), ('CE1', 'HIS', 'CD2', 'HIS', 8.6), ('CE1', 'HIS', 'CE1', 'HIS', 9.44), ('CE1', 'HIS', 'NE2', 'HIS', 8.45)], [('NE2', 'HIS', 'CB', 'HIS', 10.71), ('NE2', 'HIS', 'CG', 'HIS', 9.85), ('NE2', 'HIS', 'ND1', 'HIS', 10.18), ('NE2', 'HIS', 'CD2', 'HIS', 8.9), ('NE2', 'HIS', 'CE1', 'HIS', 9.55), ('NE2', 'HIS', 'NE2', 'HIS', 8.72)], [('CB', 'HIS', 'CB', 'HIS', 7.09), ('CB', 'HIS', 'CG', 'HIS', 8.55), ('CB', 'HIS', 'ND1', 'HIS', 9.35), ('CB', 'HIS', 'CD2', 'HIS', 9.52), ('CB', 'HIS', 'CE1', 'HIS', 10.62), ('CB', 'HIS', 'NE2', 'HIS', 10.71)], [('CG', 'HIS', 'CB', 'HIS', 6.37), ('CG', 'HIS', 'CG', 'HIS', 7.74), ('CG', 'HIS', 'ND1', 'HIS', 8.47), ('CG', 'HIS', 'CD2', 'HIS', 8.73), ('CG', 'HIS', 'CE1', 'HIS', 9.71), ('CG', 'HIS', 'NE2', 'HIS', 9.85)], [('ND1', 'HIS', 'CB', 'HIS', 7.01), ('ND1', 'HIS', 'CG', 'HIS', 8.24), ('ND1', 'HIS', 'ND1', 'HIS', 9.01), ('ND1', 'HIS', 'CD2', 'HIS', 9.08), ('ND1', 'HIS', 'CE1', 'HIS', 10.14), ('ND1', 'HIS', 'NE2', 'HIS', 10.18)], [('CD2', 'HIS', 'CB', 'HIS', 5.54), ('CD2', 'HIS', 'CG', 'HIS', 6.8), ('CD2', 'HIS', 'ND1', 'HIS', 7.34), ('CD2', 'HIS', 'CD2', 'HIS', 7.92), ('CD2', 'HIS', 'CE1', 'HIS', 8.6), ('CD2', 'HIS', 'NE2', 'HIS', 8.9)], [('CE1', 'HIS', 'CB', 'HIS', 6.74), ('CE1', 'HIS', 'CG', 'HIS', 7.75), ('CE1', 'HIS', 'ND1', 'HIS', 8.38), ('CE1', 'HIS', 'CD2', 'HIS', 8.58), ('CE1', 'HIS', 'CE1', 'HIS', 9.44), ('CE1', 'HIS', 'NE2', 'HIS', 9.55)], [('NE2', 'HIS', 'CB', 'HIS', 5.85), ('NE2', 'HIS', 'CG', 'HIS', 6.84), ('NE2', 'HIS', 'ND1', 'HIS', 7.32), ('NE2', 'HIS', 'CD2', 'HIS', 7.83), ('NE2', 'HIS', 'CE1', 'HIS', 8.45), ('NE2', 'HIS', 'NE2', 'HIS', 8.72)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_FES, d, 'M_1ndo_1_14_12_12')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_FE, d, 'M_1ndo_1_14_12_12')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'M_1ndo_1_14_12_12')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_FES, d, 'M_1ndo_1_14_12_12')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(FES_FE, d, 'M_1ndo_1_14_12_12')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(FE_HISI, d, 'M_1ndo_1_14_12_12')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASP_FE, d, 'M_1ndo_1_14_12_12')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(FES_HISI, d, 'M_1ndo_1_14_12_12')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(HIS_HIS, d, 'M_1ndo_1_14_12_12')
	if match9 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_FES' :  match1,
		'HIS_FE' :  match2,
		'HIS_ASP' :  match3,
		'ASP_FES' :  match4,
		'FES_FE' :  match5,
		'FE_HISI' :  match6,
		'ASP_FE' :  match7,
		'FES_HISI' :  match8,
		'HIS_HIS' :  match9}