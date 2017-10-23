'''
FUNC:M_1n20_5_5_1_8
PDB:1n20
EC:5.5.1.8
RESI:trp,phe,mg,mg,mg
LOCI:a-323,578,701,702,703;
'''
import motifFunctions as cmd
TRP_MG = { 
	'distances':
		[[18.08], [17.34], [17.66], [16.32], [16.95], [16.09], [15.72], [15.29], [14.88], [14.66], [16.83], [16.21], [16.77], [15.1], [16.13], [15.08], [14.25], [14.27], [13.36], [13.38], [15.87], [14.86], [15.17], [13.52], [14.17], [13.08], [12.78], [11.87], [11.52], [11.02]],
	'comparisons':
		[[('CB', 'TRP', 'MG', 'MG', 18.08)], [('CG', 'TRP', 'MG', 'MG', 17.34)], [('CD1', 'TRP', 'MG', 'MG', 17.66)], [('CD2', 'TRP', 'MG', 'MG', 16.32)], [('NE1', 'TRP', 'MG', 'MG', 16.95)], [('CE2', 'TRP', 'MG', 'MG', 16.09)], [('CE3', 'TRP', 'MG', 'MG', 15.72)], [('CZ2', 'TRP', 'MG', 'MG', 15.29)], [('CZ3', 'TRP', 'MG', 'MG', 14.88)], [('CH2', 'TRP', 'MG', 'MG', 14.66)], [('CB', 'TRP', 'MG', 'MG', 16.83)], [('CG', 'TRP', 'MG', 'MG', 16.21)], [('CD1', 'TRP', 'MG', 'MG', 16.77)], [('CD2', 'TRP', 'MG', 'MG', 15.1)], [('NE1', 'TRP', 'MG', 'MG', 16.13)], [('CE2', 'TRP', 'MG', 'MG', 15.08)], [('CE3', 'TRP', 'MG', 'MG', 14.25)], [('CZ2', 'TRP', 'MG', 'MG', 14.27)], [('CZ3', 'TRP', 'MG', 'MG', 13.36)], [('CH2', 'TRP', 'MG', 'MG', 13.38)], [('CB', 'TRP', 'MG', 'MG', 15.87)], [('CG', 'TRP', 'MG', 'MG', 14.86)], [('CD1', 'TRP', 'MG', 'MG', 15.17)], [('CD2', 'TRP', 'MG', 'MG', 13.52)], [('NE1', 'TRP', 'MG', 'MG', 14.17)], [('CE2', 'TRP', 'MG', 'MG', 13.08)], [('CE3', 'TRP', 'MG', 'MG', 12.78)], [('CZ2', 'TRP', 'MG', 'MG', 11.87)], [('CZ3', 'TRP', 'MG', 'MG', 11.52)], [('CH2', 'TRP', 'MG', 'MG', 11.02)]]}
PHE_TRP = { 
	'distances':
		[[9.67, 9.44, 10.53, 8.29, 10.31, 8.99, 6.9, 8.57, 6.25, 7.27], [8.96, 8.88, 10.04, 7.88, 9.96, 8.72, 6.52, 8.52, 6.17, 7.33], [7.68, 7.75, 8.99, 6.92, 9.1, 7.96, 5.62, 8.03, 5.69, 7.02], [9.83, 9.76, 10.88, 8.8, 10.8, 9.6, 7.53, 9.36, 7.17, 8.21], [7.37, 7.64, 8.89, 7.07, 9.18, 8.21, 6.0, 8.49, 6.38, 7.68], [9.61, 9.69, 10.81, 8.92, 10.87, 9.79, 7.79, 9.74, 7.7, 8.76], [8.46, 8.7, 9.87, 8.13, 10.11, 9.15, 7.12, 9.34, 7.35, 8.52]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'TRP', 9.67), ('CB', 'PHE', 'CG', 'TRP', 9.44), ('CB', 'PHE', 'CD1', 'TRP', 10.53), ('CB', 'PHE', 'CD2', 'TRP', 8.29), ('CB', 'PHE', 'NE1', 'TRP', 10.31), ('CB', 'PHE', 'CE2', 'TRP', 8.99), ('CB', 'PHE', 'CE3', 'TRP', 6.9), ('CB', 'PHE', 'CZ2', 'TRP', 8.57), ('CB', 'PHE', 'CZ3', 'TRP', 6.25), ('CB', 'PHE', 'CH2', 'TRP', 7.27)], [('CG', 'PHE', 'CB', 'TRP', 8.96), ('CG', 'PHE', 'CG', 'TRP', 8.88), ('CG', 'PHE', 'CD1', 'TRP', 10.04), ('CG', 'PHE', 'CD2', 'TRP', 7.88), ('CG', 'PHE', 'NE1', 'TRP', 9.96), ('CG', 'PHE', 'CE2', 'TRP', 8.72), ('CG', 'PHE', 'CE3', 'TRP', 6.52), ('CG', 'PHE', 'CZ2', 'TRP', 8.52), ('CG', 'PHE', 'CZ3', 'TRP', 6.17), ('CG', 'PHE', 'CH2', 'TRP', 7.33)], [('CD1', 'PHE', 'CB', 'TRP', 7.68), ('CD1', 'PHE', 'CG', 'TRP', 7.75), ('CD1', 'PHE', 'CD1', 'TRP', 8.99), ('CD1', 'PHE', 'CD2', 'TRP', 6.92), ('CD1', 'PHE', 'NE1', 'TRP', 9.1), ('CD1', 'PHE', 'CE2', 'TRP', 7.96), ('CD1', 'PHE', 'CE3', 'TRP', 5.62), ('CD1', 'PHE', 'CZ2', 'TRP', 8.03), ('CD1', 'PHE', 'CZ3', 'TRP', 5.69), ('CD1', 'PHE', 'CH2', 'TRP', 7.02)], [('CD2', 'PHE', 'CB', 'TRP', 9.83), ('CD2', 'PHE', 'CG', 'TRP', 9.76), ('CD2', 'PHE', 'CD1', 'TRP', 10.88), ('CD2', 'PHE', 'CD2', 'TRP', 8.8), ('CD2', 'PHE', 'NE1', 'TRP', 10.8), ('CD2', 'PHE', 'CE2', 'TRP', 9.6), ('CD2', 'PHE', 'CE3', 'TRP', 7.53), ('CD2', 'PHE', 'CZ2', 'TRP', 9.36), ('CD2', 'PHE', 'CZ3', 'TRP', 7.17), ('CD2', 'PHE', 'CH2', 'TRP', 8.21)], [('CE1', 'PHE', 'CB', 'TRP', 7.37), ('CE1', 'PHE', 'CG', 'TRP', 7.64), ('CE1', 'PHE', 'CD1', 'TRP', 8.89), ('CE1', 'PHE', 'CD2', 'TRP', 7.07), ('CE1', 'PHE', 'NE1', 'TRP', 9.18), ('CE1', 'PHE', 'CE2', 'TRP', 8.21), ('CE1', 'PHE', 'CE3', 'TRP', 6.0), ('CE1', 'PHE', 'CZ2', 'TRP', 8.49), ('CE1', 'PHE', 'CZ3', 'TRP', 6.38), ('CE1', 'PHE', 'CH2', 'TRP', 7.68)], [('CE2', 'PHE', 'CB', 'TRP', 9.61), ('CE2', 'PHE', 'CG', 'TRP', 9.69), ('CE2', 'PHE', 'CD1', 'TRP', 10.81), ('CE2', 'PHE', 'CD2', 'TRP', 8.92), ('CE2', 'PHE', 'NE1', 'TRP', 10.87), ('CE2', 'PHE', 'CE2', 'TRP', 9.79), ('CE2', 'PHE', 'CE3', 'TRP', 7.79), ('CE2', 'PHE', 'CZ2', 'TRP', 9.74), ('CE2', 'PHE', 'CZ3', 'TRP', 7.7), ('CE2', 'PHE', 'CH2', 'TRP', 8.76)], [('CZ', 'PHE', 'CB', 'TRP', 8.46), ('CZ', 'PHE', 'CG', 'TRP', 8.7), ('CZ', 'PHE', 'CD1', 'TRP', 9.87), ('CZ', 'PHE', 'CD2', 'TRP', 8.13), ('CZ', 'PHE', 'NE1', 'TRP', 10.11), ('CZ', 'PHE', 'CE2', 'TRP', 9.15), ('CZ', 'PHE', 'CE3', 'TRP', 7.12), ('CZ', 'PHE', 'CZ2', 'TRP', 9.34), ('CZ', 'PHE', 'CZ3', 'TRP', 7.35), ('CZ', 'PHE', 'CH2', 'TRP', 8.52)]]}
PHE_MG = { 
	'distances':
		[[14.21], [13.87], [14.74], [12.87], [14.7], [12.82], [13.77], [11.83], [11.61], [12.66], [10.55], [12.78], [10.68], [11.84], [10.87], [11.3], [12.34], [10.93], [12.98], [11.66], [12.67]],
	'comparisons':
		[[('CB', 'PHE', 'MG', 'MG', 14.21)], [('CG', 'PHE', 'MG', 'MG', 13.87)], [('CD1', 'PHE', 'MG', 'MG', 14.74)], [('CD2', 'PHE', 'MG', 'MG', 12.87)], [('CE1', 'PHE', 'MG', 'MG', 14.7)], [('CE2', 'PHE', 'MG', 'MG', 12.82)], [('CZ', 'PHE', 'MG', 'MG', 13.77)], [('CB', 'PHE', 'MG', 'MG', 11.83)], [('CG', 'PHE', 'MG', 'MG', 11.61)], [('CD1', 'PHE', 'MG', 'MG', 12.66)], [('CD2', 'PHE', 'MG', 'MG', 10.55)], [('CE1', 'PHE', 'MG', 'MG', 12.78)], [('CE2', 'PHE', 'MG', 'MG', 10.68)], [('CZ', 'PHE', 'MG', 'MG', 11.84)], [('CB', 'PHE', 'MG', 'MG', 10.87)], [('CG', 'PHE', 'MG', 'MG', 11.3)], [('CD1', 'PHE', 'MG', 'MG', 12.34)], [('CD2', 'PHE', 'MG', 'MG', 10.93)], [('CE1', 'PHE', 'MG', 'MG', 12.98)], [('CE2', 'PHE', 'MG', 'MG', 11.66)], [('CZ', 'PHE', 'MG', 'MG', 12.67)]]}
MG_MGI = { 
	'distances':
		[7.32],
	'comparisons':
		[('MG', 'MG', 'MG', 'MGI', 7.32)]}
MG_MG = { 
	'distances':
		[5.12, 8.41, 5.12, 7.32, 8.41],
	'comparisons':
		[('MG', 'MG', 'MG', 'MG', 5.12), ('MG', 'MG', 'MG', 'MG', 8.41), ('MG', 'MG', 'MG', 'MG', 5.12), ('MG', 'MG', 'MG', 'MG', 7.32), ('MG', 'MG', 'MG', 'MG', 8.41)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_MG, d, 'M_1n20_5_5_1_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(PHE_TRP, d, 'M_1n20_5_5_1_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_MG, d, 'M_1n20_5_5_1_8')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(MG_MGI, d, 'M_1n20_5_5_1_8')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(MG_MG, d, 'M_1n20_5_5_1_8')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_MG' :  match1,
		'PHE_TRP' :  match2,
		'PHE_MG' :  match3,
		'MG_MGI' :  match4,
		'MG_MG' :  match5}