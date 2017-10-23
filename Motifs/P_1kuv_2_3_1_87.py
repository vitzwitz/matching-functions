'''
FUNC:P_1kuv_2_3_1_87
PDB:1kuv
EC:2.3.1.87
RESI:ser,leu,his,leu,tyr
LOCI:a-97,111,122,124,168;
'''
import motifFunctions as cmd
LEU_LEU = { 
	'distances':
		[[19.66, 20.83, 21.4, 21.94], [21.15, 22.33, 22.9, 23.44], [21.52, 22.75, 23.39, 23.79], [21.54, 22.74, 23.21, 23.89], [19.66, 21.15, 21.52, 21.54], [20.83, 22.33, 22.75, 22.74], [21.4, 22.9, 23.39, 23.21], [21.94, 23.44, 23.79, 23.89]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'LEU', 19.66), ('CB', 'LEU', 'CG', 'LEU', 20.83), ('CB', 'LEU', 'CD1', 'LEU', 21.4), ('CB', 'LEU', 'CD2', 'LEU', 21.94)], [('CG', 'LEU', 'CB', 'LEU', 21.15), ('CG', 'LEU', 'CG', 'LEU', 22.33), ('CG', 'LEU', 'CD1', 'LEU', 22.9), ('CG', 'LEU', 'CD2', 'LEU', 23.44)], [('CD1', 'LEU', 'CB', 'LEU', 21.52), ('CD1', 'LEU', 'CG', 'LEU', 22.75), ('CD1', 'LEU', 'CD1', 'LEU', 23.39), ('CD1', 'LEU', 'CD2', 'LEU', 23.79)], [('CD2', 'LEU', 'CB', 'LEU', 21.54), ('CD2', 'LEU', 'CG', 'LEU', 22.74), ('CD2', 'LEU', 'CD1', 'LEU', 23.21), ('CD2', 'LEU', 'CD2', 'LEU', 23.89)], [('CB', 'LEU', 'CB', 'LEU', 19.66), ('CB', 'LEU', 'CG', 'LEU', 21.15), ('CB', 'LEU', 'CD1', 'LEU', 21.52), ('CB', 'LEU', 'CD2', 'LEU', 21.54)], [('CG', 'LEU', 'CB', 'LEU', 20.83), ('CG', 'LEU', 'CG', 'LEU', 22.33), ('CG', 'LEU', 'CD1', 'LEU', 22.75), ('CG', 'LEU', 'CD2', 'LEU', 22.74)], [('CD1', 'LEU', 'CB', 'LEU', 21.4), ('CD1', 'LEU', 'CG', 'LEU', 22.9), ('CD1', 'LEU', 'CD1', 'LEU', 23.39), ('CD1', 'LEU', 'CD2', 'LEU', 23.21)], [('CD2', 'LEU', 'CB', 'LEU', 21.94), ('CD2', 'LEU', 'CG', 'LEU', 23.44), ('CD2', 'LEU', 'CD1', 'LEU', 23.79), ('CD2', 'LEU', 'CD2', 'LEU', 23.89)]]}
TYR_LEU = { 
	'distances':
		[[10.32, 10.09, 11.19, 8.74], [8.86, 8.68, 9.84, 7.38], [8.68, 8.58, 9.89, 7.44], [7.86, 7.63, 8.69, 6.27], [7.5, 7.46, 8.85, 6.48], [6.49, 6.3, 7.45, 5.01], [6.28, 6.2, 7.55, 5.16], [5.13, 5.15, 6.6, 4.39], [23.21, 24.28, 24.24, 25.66], [22.43, 23.5, 23.55, 24.87], [22.33, 23.35, 23.41, 24.73], [21.98, 23.11, 23.23, 24.43], [21.81, 22.82, 22.97, 24.18], [21.44, 22.58, 22.78, 23.88], [21.36, 22.44, 22.66, 23.75], [21.0, 22.06, 22.37, 23.35]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LEU', 10.32), ('CB', 'TYR', 'CG', 'LEU', 10.09), ('CB', 'TYR', 'CD1', 'LEU', 11.19), ('CB', 'TYR', 'CD2', 'LEU', 8.74)], [('CG', 'TYR', 'CB', 'LEU', 8.86), ('CG', 'TYR', 'CG', 'LEU', 8.68), ('CG', 'TYR', 'CD1', 'LEU', 9.84), ('CG', 'TYR', 'CD2', 'LEU', 7.38)], [('CD1', 'TYR', 'CB', 'LEU', 8.68), ('CD1', 'TYR', 'CG', 'LEU', 8.58), ('CD1', 'TYR', 'CD1', 'LEU', 9.89), ('CD1', 'TYR', 'CD2', 'LEU', 7.44)], [('CD2', 'TYR', 'CB', 'LEU', 7.86), ('CD2', 'TYR', 'CG', 'LEU', 7.63), ('CD2', 'TYR', 'CD1', 'LEU', 8.69), ('CD2', 'TYR', 'CD2', 'LEU', 6.27)], [('CE1', 'TYR', 'CB', 'LEU', 7.5), ('CE1', 'TYR', 'CG', 'LEU', 7.46), ('CE1', 'TYR', 'CD1', 'LEU', 8.85), ('CE1', 'TYR', 'CD2', 'LEU', 6.48)], [('CE2', 'TYR', 'CB', 'LEU', 6.49), ('CE2', 'TYR', 'CG', 'LEU', 6.3), ('CE2', 'TYR', 'CD1', 'LEU', 7.45), ('CE2', 'TYR', 'CD2', 'LEU', 5.01)], [('CZ', 'TYR', 'CB', 'LEU', 6.28), ('CZ', 'TYR', 'CG', 'LEU', 6.2), ('CZ', 'TYR', 'CD1', 'LEU', 7.55), ('CZ', 'TYR', 'CD2', 'LEU', 5.16)], [('OH', 'TYR', 'CB', 'LEU', 5.13), ('OH', 'TYR', 'CG', 'LEU', 5.15), ('OH', 'TYR', 'CD1', 'LEU', 6.6), ('OH', 'TYR', 'CD2', 'LEU', 4.39)], [('CB', 'TYR', 'CB', 'LEU', 23.21), ('CB', 'TYR', 'CG', 'LEU', 24.28), ('CB', 'TYR', 'CD1', 'LEU', 24.24), ('CB', 'TYR', 'CD2', 'LEU', 25.66)], [('CG', 'TYR', 'CB', 'LEU', 22.43), ('CG', 'TYR', 'CG', 'LEU', 23.5), ('CG', 'TYR', 'CD1', 'LEU', 23.55), ('CG', 'TYR', 'CD2', 'LEU', 24.87)], [('CD1', 'TYR', 'CB', 'LEU', 22.33), ('CD1', 'TYR', 'CG', 'LEU', 23.35), ('CD1', 'TYR', 'CD1', 'LEU', 23.41), ('CD1', 'TYR', 'CD2', 'LEU', 24.73)], [('CD2', 'TYR', 'CB', 'LEU', 21.98), ('CD2', 'TYR', 'CG', 'LEU', 23.11), ('CD2', 'TYR', 'CD1', 'LEU', 23.23), ('CD2', 'TYR', 'CD2', 'LEU', 24.43)], [('CE1', 'TYR', 'CB', 'LEU', 21.81), ('CE1', 'TYR', 'CG', 'LEU', 22.82), ('CE1', 'TYR', 'CD1', 'LEU', 22.97), ('CE1', 'TYR', 'CD2', 'LEU', 24.18)], [('CE2', 'TYR', 'CB', 'LEU', 21.44), ('CE2', 'TYR', 'CG', 'LEU', 22.58), ('CE2', 'TYR', 'CD1', 'LEU', 22.78), ('CE2', 'TYR', 'CD2', 'LEU', 23.88)], [('CZ', 'TYR', 'CB', 'LEU', 21.36), ('CZ', 'TYR', 'CG', 'LEU', 22.44), ('CZ', 'TYR', 'CD1', 'LEU', 22.66), ('CZ', 'TYR', 'CD2', 'LEU', 23.75)], [('OH', 'TYR', 'CB', 'LEU', 21.0), ('OH', 'TYR', 'CG', 'LEU', 22.06), ('OH', 'TYR', 'CD1', 'LEU', 22.37), ('OH', 'TYR', 'CD2', 'LEU', 23.35)]]}
TYR_HIS = { 
	'distances':
		[[15.59, 16.3, 16.3, 17.16, 17.12, 17.63], [14.37, 15.17, 15.23, 16.06, 16.12, 16.62], [14.09, 14.95, 15.15, 15.8, 16.06, 16.45], [13.69, 14.51, 14.51, 15.5, 15.45, 16.03], [13.15, 14.11, 14.39, 14.99, 15.37, 15.73], [12.71, 13.63, 13.7, 14.66, 14.72, 15.28], [12.43, 13.43, 13.65, 14.4, 14.68, 15.13], [11.66, 12.76, 13.06, 13.77, 14.17, 14.58]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 15.59), ('CB', 'TYR', 'CG', 'HIS', 16.3), ('CB', 'TYR', 'ND1', 'HIS', 16.3), ('CB', 'TYR', 'CD2', 'HIS', 17.16), ('CB', 'TYR', 'CE1', 'HIS', 17.12), ('CB', 'TYR', 'NE2', 'HIS', 17.63)], [('CG', 'TYR', 'CB', 'HIS', 14.37), ('CG', 'TYR', 'CG', 'HIS', 15.17), ('CG', 'TYR', 'ND1', 'HIS', 15.23), ('CG', 'TYR', 'CD2', 'HIS', 16.06), ('CG', 'TYR', 'CE1', 'HIS', 16.12), ('CG', 'TYR', 'NE2', 'HIS', 16.62)], [('CD1', 'TYR', 'CB', 'HIS', 14.09), ('CD1', 'TYR', 'CG', 'HIS', 14.95), ('CD1', 'TYR', 'ND1', 'HIS', 15.15), ('CD1', 'TYR', 'CD2', 'HIS', 15.8), ('CD1', 'TYR', 'CE1', 'HIS', 16.06), ('CD1', 'TYR', 'NE2', 'HIS', 16.45)], [('CD2', 'TYR', 'CB', 'HIS', 13.69), ('CD2', 'TYR', 'CG', 'HIS', 14.51), ('CD2', 'TYR', 'ND1', 'HIS', 14.51), ('CD2', 'TYR', 'CD2', 'HIS', 15.5), ('CD2', 'TYR', 'CE1', 'HIS', 15.45), ('CD2', 'TYR', 'NE2', 'HIS', 16.03)], [('CE1', 'TYR', 'CB', 'HIS', 13.15), ('CE1', 'TYR', 'CG', 'HIS', 14.11), ('CE1', 'TYR', 'ND1', 'HIS', 14.39), ('CE1', 'TYR', 'CD2', 'HIS', 14.99), ('CE1', 'TYR', 'CE1', 'HIS', 15.37), ('CE1', 'TYR', 'NE2', 'HIS', 15.73)], [('CE2', 'TYR', 'CB', 'HIS', 12.71), ('CE2', 'TYR', 'CG', 'HIS', 13.63), ('CE2', 'TYR', 'ND1', 'HIS', 13.7), ('CE2', 'TYR', 'CD2', 'HIS', 14.66), ('CE2', 'TYR', 'CE1', 'HIS', 14.72), ('CE2', 'TYR', 'NE2', 'HIS', 15.28)], [('CZ', 'TYR', 'CB', 'HIS', 12.43), ('CZ', 'TYR', 'CG', 'HIS', 13.43), ('CZ', 'TYR', 'ND1', 'HIS', 13.65), ('CZ', 'TYR', 'CD2', 'HIS', 14.4), ('CZ', 'TYR', 'CE1', 'HIS', 14.68), ('CZ', 'TYR', 'NE2', 'HIS', 15.13)], [('OH', 'TYR', 'CB', 'HIS', 11.66), ('OH', 'TYR', 'CG', 'HIS', 12.76), ('OH', 'TYR', 'ND1', 'HIS', 13.06), ('OH', 'TYR', 'CD2', 'HIS', 13.77), ('OH', 'TYR', 'CE1', 'HIS', 14.17), ('OH', 'TYR', 'NE2', 'HIS', 14.58)]]}
LEU_HIS = { 
	'distances':
		[[9.58, 10.85, 11.11, 12.06, 12.38, 12.92], [11.11, 12.36, 12.58, 13.59, 13.84, 14.43], [11.52, 12.76, 12.87, 14.03, 14.15, 14.82], [11.78, 12.95, 13.07, 14.16, 14.29, 14.92], [11.42, 9.97, 9.66, 8.88, 8.38, 7.79], [12.49, 11.09, 10.92, 9.91, 9.66, 8.94], [13.26, 11.85, 11.65, 10.68, 10.38, 9.69], [13.53, 12.14, 11.93, 10.99, 10.68, 10.02]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'HIS', 9.58), ('CB', 'LEU', 'CG', 'HIS', 10.85), ('CB', 'LEU', 'ND1', 'HIS', 11.11), ('CB', 'LEU', 'CD2', 'HIS', 12.06), ('CB', 'LEU', 'CE1', 'HIS', 12.38), ('CB', 'LEU', 'NE2', 'HIS', 12.92)], [('CG', 'LEU', 'CB', 'HIS', 11.11), ('CG', 'LEU', 'CG', 'HIS', 12.36), ('CG', 'LEU', 'ND1', 'HIS', 12.58), ('CG', 'LEU', 'CD2', 'HIS', 13.59), ('CG', 'LEU', 'CE1', 'HIS', 13.84), ('CG', 'LEU', 'NE2', 'HIS', 14.43)], [('CD1', 'LEU', 'CB', 'HIS', 11.52), ('CD1', 'LEU', 'CG', 'HIS', 12.76), ('CD1', 'LEU', 'ND1', 'HIS', 12.87), ('CD1', 'LEU', 'CD2', 'HIS', 14.03), ('CD1', 'LEU', 'CE1', 'HIS', 14.15), ('CD1', 'LEU', 'NE2', 'HIS', 14.82)], [('CD2', 'LEU', 'CB', 'HIS', 11.78), ('CD2', 'LEU', 'CG', 'HIS', 12.95), ('CD2', 'LEU', 'ND1', 'HIS', 13.07), ('CD2', 'LEU', 'CD2', 'HIS', 14.16), ('CD2', 'LEU', 'CE1', 'HIS', 14.29), ('CD2', 'LEU', 'NE2', 'HIS', 14.92)], [('CB', 'LEU', 'CB', 'HIS', 11.42), ('CB', 'LEU', 'CG', 'HIS', 9.97), ('CB', 'LEU', 'ND1', 'HIS', 9.66), ('CB', 'LEU', 'CD2', 'HIS', 8.88), ('CB', 'LEU', 'CE1', 'HIS', 8.38), ('CB', 'LEU', 'NE2', 'HIS', 7.79)], [('CG', 'LEU', 'CB', 'HIS', 12.49), ('CG', 'LEU', 'CG', 'HIS', 11.09), ('CG', 'LEU', 'ND1', 'HIS', 10.92), ('CG', 'LEU', 'CD2', 'HIS', 9.91), ('CG', 'LEU', 'CE1', 'HIS', 9.66), ('CG', 'LEU', 'NE2', 'HIS', 8.94)], [('CD1', 'LEU', 'CB', 'HIS', 13.26), ('CD1', 'LEU', 'CG', 'HIS', 11.85), ('CD1', 'LEU', 'ND1', 'HIS', 11.65), ('CD1', 'LEU', 'CD2', 'HIS', 10.68), ('CD1', 'LEU', 'CE1', 'HIS', 10.38), ('CD1', 'LEU', 'NE2', 'HIS', 9.69)], [('CD2', 'LEU', 'CB', 'HIS', 13.53), ('CD2', 'LEU', 'CG', 'HIS', 12.14), ('CD2', 'LEU', 'ND1', 'HIS', 11.93), ('CD2', 'LEU', 'CD2', 'HIS', 10.99), ('CD2', 'LEU', 'CE1', 'HIS', 10.68), ('CD2', 'LEU', 'NE2', 'HIS', 10.02)]]}
LEU_SER = { 
	'distances':
		[[14.48, 14.53], [15.81, 15.91], [15.83, 16.07], [16.21, 16.24], [8.04, 7.18], [9.54, 8.68], [10.36, 9.37], [10.16, 9.49]],
	'comparisons':
		[[('CB', 'LEU', 'CB', 'SER', 14.48), ('CB', 'LEU', 'OG', 'SER', 14.53)], [('CG', 'LEU', 'CB', 'SER', 15.81), ('CG', 'LEU', 'OG', 'SER', 15.91)], [('CD1', 'LEU', 'CB', 'SER', 15.83), ('CD1', 'LEU', 'OG', 'SER', 16.07)], [('CD2', 'LEU', 'CB', 'SER', 16.21), ('CD2', 'LEU', 'OG', 'SER', 16.24)], [('CB', 'LEU', 'CB', 'SER', 8.04), ('CB', 'LEU', 'OG', 'SER', 7.18)], [('CG', 'LEU', 'CB', 'SER', 9.54), ('CG', 'LEU', 'OG', 'SER', 8.68)], [('CD1', 'LEU', 'CB', 'SER', 10.36), ('CD1', 'LEU', 'OG', 'SER', 9.37)], [('CD2', 'LEU', 'CB', 'SER', 10.16), ('CD2', 'LEU', 'OG', 'SER', 9.49)]]}
TYR_SER = { 
	'distances':
		[[19.22, 18.75], [18.33, 17.89], [18.48, 18.0], [17.51, 17.17], [17.88, 17.44], [16.85, 16.57], [17.05, 16.72], [16.61, 16.33]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'SER', 19.22), ('CB', 'TYR', 'OG', 'SER', 18.75)], [('CG', 'TYR', 'CB', 'SER', 18.33), ('CG', 'TYR', 'OG', 'SER', 17.89)], [('CD1', 'TYR', 'CB', 'SER', 18.48), ('CD1', 'TYR', 'OG', 'SER', 18.0)], [('CD2', 'TYR', 'CB', 'SER', 17.51), ('CD2', 'TYR', 'OG', 'SER', 17.17)], [('CE1', 'TYR', 'CB', 'SER', 17.88), ('CE1', 'TYR', 'OG', 'SER', 17.44)], [('CE2', 'TYR', 'CB', 'SER', 16.85), ('CE2', 'TYR', 'OG', 'SER', 16.57)], [('CZ', 'TYR', 'CB', 'SER', 17.05), ('CZ', 'TYR', 'OG', 'SER', 16.72)], [('OH', 'TYR', 'CB', 'SER', 16.61), ('OH', 'TYR', 'OG', 'SER', 16.33)]]}
HIS_SER = { 
	'distances':
		[[7.6, 7.36], [6.38, 5.99], [5.21, 4.89], [6.43, 5.83], [4.45, 3.82], [5.34, 4.56]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 7.6), ('CB', 'HIS', 'OG', 'SER', 7.36)], [('CG', 'HIS', 'CB', 'SER', 6.38), ('CG', 'HIS', 'OG', 'SER', 5.99)], [('ND1', 'HIS', 'CB', 'SER', 5.21), ('ND1', 'HIS', 'OG', 'SER', 4.89)], [('CD2', 'HIS', 'CB', 'SER', 6.43), ('CD2', 'HIS', 'OG', 'SER', 5.83)], [('CE1', 'HIS', 'CB', 'SER', 4.45), ('CE1', 'HIS', 'OG', 'SER', 3.82)], [('NE2', 'HIS', 'CB', 'SER', 5.34), ('NE2', 'HIS', 'OG', 'SER', 4.56)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LEU_LEU, d, 'P_1kuv_2_3_1_87')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_LEU, d, 'P_1kuv_2_3_1_87')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_HIS, d, 'P_1kuv_2_3_1_87')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LEU_HIS, d, 'P_1kuv_2_3_1_87')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(LEU_SER, d, 'P_1kuv_2_3_1_87')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_SER, d, 'P_1kuv_2_3_1_87')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_SER, d, 'P_1kuv_2_3_1_87')
	if match7 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LEU_LEU' :  match1,
		'TYR_LEU' :  match2,
		'TYR_HIS' :  match3,
		'LEU_HIS' :  match4,
		'LEU_SER' :  match5,
		'TYR_SER' :  match6,
		'HIS_SER' :  match7}