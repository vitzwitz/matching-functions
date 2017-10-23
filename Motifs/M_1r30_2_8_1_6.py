'''
FUNC:M_1r30_2_8_1_6
PDB:1r30
EC:2.8.1.6
RESI:cys,cys,cys,arg,fes
LOCI:a-53,57,60,260,402;
'''
import motifFunctions as cmd
ARG_CYSI = { 
	'distances':
		[[24.59, 23.96], [23.93, 23.41], [22.89, 22.35], [23.47, 22.86], [22.88, 22.23], [21.59, 20.96], [23.64, 22.93]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYSI', 24.59), ('CB', 'ARG', 'SG', 'CYSI', 23.96)], [('CG', 'ARG', 'CB', 'CYSI', 23.93), ('CG', 'ARG', 'SG', 'CYSI', 23.41)], [('CD', 'ARG', 'CB', 'CYSI', 22.89), ('CD', 'ARG', 'SG', 'CYSI', 22.35)], [('NE', 'ARG', 'CB', 'CYSI', 23.47), ('NE', 'ARG', 'SG', 'CYSI', 22.86)], [('CZ', 'ARG', 'CB', 'CYSI', 22.88), ('CZ', 'ARG', 'SG', 'CYSI', 22.23)], [('NH1', 'ARG', 'CB', 'CYSI', 21.59), ('NH1', 'ARG', 'SG', 'CYSI', 20.96)], [('NH2', 'ARG', 'CB', 'CYSI', 23.64), ('NH2', 'ARG', 'SG', 'CYSI', 22.93)]]}
CYS_CYS = { 
	'distances':
		[[9.21, 9.37], [8.01, 8.35], [6.01, 6.99], [7.37, 7.93], [9.21, 8.01], [9.37, 8.35], [10.36, 9.97], [9.84, 9.08], [6.01, 7.37], [6.99, 7.93]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 9.21), ('CB', 'CYS', 'SG', 'CYS', 9.37)], [('SG', 'CYS', 'CB', 'CYS', 8.01), ('SG', 'CYS', 'SG', 'CYS', 8.35)], [('CB', 'CYS', 'CB', 'CYS', 6.01), ('CB', 'CYS', 'SG', 'CYS', 6.99)], [('SG', 'CYS', 'CB', 'CYS', 7.37), ('SG', 'CYS', 'SG', 'CYS', 7.93)], [('CB', 'CYS', 'CB', 'CYS', 9.21), ('CB', 'CYS', 'SG', 'CYS', 8.01)], [('SG', 'CYS', 'CB', 'CYS', 9.37), ('SG', 'CYS', 'SG', 'CYS', 8.35)], [('CB', 'CYS', 'CB', 'CYS', 10.36), ('CB', 'CYS', 'SG', 'CYS', 9.97)], [('SG', 'CYS', 'CB', 'CYS', 9.84), ('SG', 'CYS', 'SG', 'CYS', 9.08)], [('CB', 'CYS', 'CB', 'CYS', 6.01), ('CB', 'CYS', 'SG', 'CYS', 7.37)], [('SG', 'CYS', 'CB', 'CYS', 6.99), ('SG', 'CYS', 'SG', 'CYS', 7.93)]]}
CYS_FES = { 
	'distances':
		[[18.21, 18.78, 19.89, 16.95], [17.87, 18.1, 19.39, 16.41], [20.84, 20.32, 21.88, 19.15], [20.03, 19.6, 21.05, 18.43], [19.24, 20.2, 20.99, 18.33], [18.57, 19.45, 20.23, 17.67]],
	'comparisons':
		[[('CB', 'CYS', 'FE1', 'FES', 18.21), ('CB', 'CYS', 'FE2', 'FES', 18.78), ('CB', 'CYS', 'S1', 'FES', 19.89), ('CB', 'CYS', 'S2', 'FES', 16.95)], [('SG', 'CYS', 'FE1', 'FES', 17.87), ('SG', 'CYS', 'FE2', 'FES', 18.1), ('SG', 'CYS', 'S1', 'FES', 19.39), ('SG', 'CYS', 'S2', 'FES', 16.41)], [('CB', 'CYS', 'FE1', 'FES', 20.84), ('CB', 'CYS', 'FE2', 'FES', 20.32), ('CB', 'CYS', 'S1', 'FES', 21.88), ('CB', 'CYS', 'S2', 'FES', 19.15)], [('SG', 'CYS', 'FE1', 'FES', 20.03), ('SG', 'CYS', 'FE2', 'FES', 19.6), ('SG', 'CYS', 'S1', 'FES', 21.05), ('SG', 'CYS', 'S2', 'FES', 18.43)], [('CB', 'CYS', 'FE1', 'FES', 19.24), ('CB', 'CYS', 'FE2', 'FES', 20.2), ('CB', 'CYS', 'S1', 'FES', 20.99), ('CB', 'CYS', 'S2', 'FES', 18.33)], [('SG', 'CYS', 'FE1', 'FES', 18.57), ('SG', 'CYS', 'FE2', 'FES', 19.45), ('SG', 'CYS', 'S1', 'FES', 20.23), ('SG', 'CYS', 'S2', 'FES', 17.67)]]}
FES_CYSI = { 
	'distances':
		[[20.84, 20.03], [20.32, 19.6], [21.88, 21.05], [19.15, 18.43]],
	'comparisons':
		[[('FE1', 'FES', 'CB', 'CYSI', 20.84), ('FE1', 'FES', 'SG', 'CYSI', 20.03)], [('FE2', 'FES', 'CB', 'CYSI', 20.32), ('FE2', 'FES', 'SG', 'CYSI', 19.6)], [('S1', 'FES', 'CB', 'CYSI', 21.88), ('S1', 'FES', 'SG', 'CYSI', 21.05)], [('S2', 'FES', 'CB', 'CYSI', 19.15), ('S2', 'FES', 'SG', 'CYSI', 18.43)]]}
ARG_FES = { 
	'distances':
		[[7.98, 10.62, 9.31, 9.51], [7.98, 10.28, 9.33, 9.11], [6.69, 8.83, 8.04, 7.66], [6.03, 8.11, 7.0, 7.33], [4.97, 6.81, 5.7, 6.23], [4.35, 5.98, 5.41, 5.06], [5.15, 6.64, 5.12, 6.62]],
	'comparisons':
		[[('CB', 'ARG', 'FE1', 'FES', 7.98), ('CB', 'ARG', 'FE2', 'FES', 10.62), ('CB', 'ARG', 'S1', 'FES', 9.31), ('CB', 'ARG', 'S2', 'FES', 9.51)], [('CG', 'ARG', 'FE1', 'FES', 7.98), ('CG', 'ARG', 'FE2', 'FES', 10.28), ('CG', 'ARG', 'S1', 'FES', 9.33), ('CG', 'ARG', 'S2', 'FES', 9.11)], [('CD', 'ARG', 'FE1', 'FES', 6.69), ('CD', 'ARG', 'FE2', 'FES', 8.83), ('CD', 'ARG', 'S1', 'FES', 8.04), ('CD', 'ARG', 'S2', 'FES', 7.66)], [('NE', 'ARG', 'FE1', 'FES', 6.03), ('NE', 'ARG', 'FE2', 'FES', 8.11), ('NE', 'ARG', 'S1', 'FES', 7.0), ('NE', 'ARG', 'S2', 'FES', 7.33)], [('CZ', 'ARG', 'FE1', 'FES', 4.97), ('CZ', 'ARG', 'FE2', 'FES', 6.81), ('CZ', 'ARG', 'S1', 'FES', 5.7), ('CZ', 'ARG', 'S2', 'FES', 6.23)], [('NH1', 'ARG', 'FE1', 'FES', 4.35), ('NH1', 'ARG', 'FE2', 'FES', 5.98), ('NH1', 'ARG', 'S1', 'FES', 5.41), ('NH1', 'ARG', 'S2', 'FES', 5.06)], [('NH2', 'ARG', 'FE1', 'FES', 5.15), ('NH2', 'ARG', 'FE2', 'FES', 6.64), ('NH2', 'ARG', 'S1', 'FES', 5.12), ('NH2', 'ARG', 'S2', 'FES', 6.62)]]}
CYS_CYSI = { 
	'distances':
		[[10.36, 9.84], [9.97, 9.08]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYSI', 10.36), ('CB', 'CYS', 'SG', 'CYSI', 9.84)], [('SG', 'CYS', 'CB', 'CYSI', 9.97), ('SG', 'CYS', 'SG', 'CYSI', 9.08)]]}
ARG_CYSII = { 
	'distances':
		[[21.33, 21.11], [20.97, 20.82], [20.38, 20.15], [21.22, 20.87], [21.03, 20.58], [19.99, 19.53], [21.98, 21.44]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYSII', 21.33), ('CB', 'ARG', 'SG', 'CYSII', 21.11)], [('CG', 'ARG', 'CB', 'CYSII', 20.97), ('CG', 'ARG', 'SG', 'CYSII', 20.82)], [('CD', 'ARG', 'CB', 'CYSII', 20.38), ('CD', 'ARG', 'SG', 'CYSII', 20.15)], [('NE', 'ARG', 'CB', 'CYSII', 21.22), ('NE', 'ARG', 'SG', 'CYSII', 20.87)], [('CZ', 'ARG', 'CB', 'CYSII', 21.03), ('CZ', 'ARG', 'SG', 'CYSII', 20.58)], [('NH1', 'ARG', 'CB', 'CYSII', 19.99), ('NH1', 'ARG', 'SG', 'CYSII', 19.53)], [('NH2', 'ARG', 'CB', 'CYSII', 21.98), ('NH2', 'ARG', 'SG', 'CYSII', 21.44)]]}
FES_CYSII = { 
	'distances':
		[[19.24, 18.57], [20.2, 19.45], [20.99, 20.23], [18.33, 17.67]],
	'comparisons':
		[[('FE1', 'FES', 'CB', 'CYSII', 19.24), ('FE1', 'FES', 'SG', 'CYSII', 18.57)], [('FE2', 'FES', 'CB', 'CYSII', 20.2), ('FE2', 'FES', 'SG', 'CYSII', 19.45)], [('S1', 'FES', 'CB', 'CYSII', 20.99), ('S1', 'FES', 'SG', 'CYSII', 20.23)], [('S2', 'FES', 'CB', 'CYSII', 18.33), ('S2', 'FES', 'SG', 'CYSII', 17.67)]]}
CYS_ARG = { 
	'distances':
		[[20.25, 19.59, 18.93, 19.86, 19.68, 18.54, 20.72], [20.32, 19.59, 18.8, 19.67, 19.38, 18.18, 20.39], [24.59, 23.93, 22.89, 23.47, 22.88, 21.59, 23.64], [23.96, 23.41, 22.35, 22.86, 22.23, 20.96, 22.93], [21.33, 20.97, 20.38, 21.22, 21.03, 19.99, 21.98], [21.11, 20.82, 20.15, 20.87, 20.58, 19.53, 21.44]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 20.25), ('CB', 'CYS', 'CG', 'ARG', 19.59), ('CB', 'CYS', 'CD', 'ARG', 18.93), ('CB', 'CYS', 'NE', 'ARG', 19.86), ('CB', 'CYS', 'CZ', 'ARG', 19.68), ('CB', 'CYS', 'NH1', 'ARG', 18.54), ('CB', 'CYS', 'NH2', 'ARG', 20.72)], [('SG', 'CYS', 'CB', 'ARG', 20.32), ('SG', 'CYS', 'CG', 'ARG', 19.59), ('SG', 'CYS', 'CD', 'ARG', 18.8), ('SG', 'CYS', 'NE', 'ARG', 19.67), ('SG', 'CYS', 'CZ', 'ARG', 19.38), ('SG', 'CYS', 'NH1', 'ARG', 18.18), ('SG', 'CYS', 'NH2', 'ARG', 20.39)], [('CB', 'CYS', 'CB', 'ARG', 24.59), ('CB', 'CYS', 'CG', 'ARG', 23.93), ('CB', 'CYS', 'CD', 'ARG', 22.89), ('CB', 'CYS', 'NE', 'ARG', 23.47), ('CB', 'CYS', 'CZ', 'ARG', 22.88), ('CB', 'CYS', 'NH1', 'ARG', 21.59), ('CB', 'CYS', 'NH2', 'ARG', 23.64)], [('SG', 'CYS', 'CB', 'ARG', 23.96), ('SG', 'CYS', 'CG', 'ARG', 23.41), ('SG', 'CYS', 'CD', 'ARG', 22.35), ('SG', 'CYS', 'NE', 'ARG', 22.86), ('SG', 'CYS', 'CZ', 'ARG', 22.23), ('SG', 'CYS', 'NH1', 'ARG', 20.96), ('SG', 'CYS', 'NH2', 'ARG', 22.93)], [('CB', 'CYS', 'CB', 'ARG', 21.33), ('CB', 'CYS', 'CG', 'ARG', 20.97), ('CB', 'CYS', 'CD', 'ARG', 20.38), ('CB', 'CYS', 'NE', 'ARG', 21.22), ('CB', 'CYS', 'CZ', 'ARG', 21.03), ('CB', 'CYS', 'NH1', 'ARG', 19.99), ('CB', 'CYS', 'NH2', 'ARG', 21.98)], [('SG', 'CYS', 'CB', 'ARG', 21.11), ('SG', 'CYS', 'CG', 'ARG', 20.82), ('SG', 'CYS', 'CD', 'ARG', 20.15), ('SG', 'CYS', 'NE', 'ARG', 20.87), ('SG', 'CYS', 'CZ', 'ARG', 20.58), ('SG', 'CYS', 'NH1', 'ARG', 19.53), ('SG', 'CYS', 'NH2', 'ARG', 21.44)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_CYSI, d, 'M_1r30_2_8_1_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_CYS, d, 'M_1r30_2_8_1_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_FES, d, 'M_1r30_2_8_1_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(FES_CYSI, d, 'M_1r30_2_8_1_6')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_FES, d, 'M_1r30_2_8_1_6')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_CYSI, d, 'M_1r30_2_8_1_6')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ARG_CYSII, d, 'M_1r30_2_8_1_6')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(FES_CYSII, d, 'M_1r30_2_8_1_6')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(CYS_ARG, d, 'M_1r30_2_8_1_6')
	if match9 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_CYSI' :  match1,
		'CYS_CYS' :  match2,
		'CYS_FES' :  match3,
		'FES_CYSI' :  match4,
		'ARG_FES' :  match5,
		'CYS_CYSI' :  match6,
		'ARG_CYSII' :  match7,
		'FES_CYSII' :  match8,
		'CYS_ARG' :  match9}