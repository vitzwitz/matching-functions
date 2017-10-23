'''
FUNC:P_5yas_4_1_2_39
PDB:5yas
EC:4.1.2.39
RESI:thr,ser,asp,his
LOCI:a-11,80,207,235;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[6.77, 7.18, 6.72, 8.51, 7.84, 8.79], [5.78, 5.87, 5.28, 7.15, 6.36, 7.33], [5.35, 5.43, 5.03, 6.62, 6.07, 6.88], [5.96, 5.71, 4.84, 6.92, 5.79, 6.9]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.77), ('CB', 'ASP', 'CG', 'HIS', 7.18), ('CB', 'ASP', 'ND1', 'HIS', 6.72), ('CB', 'ASP', 'CD2', 'HIS', 8.51), ('CB', 'ASP', 'CE1', 'HIS', 7.84), ('CB', 'ASP', 'NE2', 'HIS', 8.79)], [('CG', 'ASP', 'CB', 'HIS', 5.78), ('CG', 'ASP', 'CG', 'HIS', 5.87), ('CG', 'ASP', 'ND1', 'HIS', 5.28), ('CG', 'ASP', 'CD2', 'HIS', 7.15), ('CG', 'ASP', 'CE1', 'HIS', 6.36), ('CG', 'ASP', 'NE2', 'HIS', 7.33)], [('OD1', 'ASP', 'CB', 'HIS', 5.35), ('OD1', 'ASP', 'CG', 'HIS', 5.43), ('OD1', 'ASP', 'ND1', 'HIS', 5.03), ('OD1', 'ASP', 'CD2', 'HIS', 6.62), ('OD1', 'ASP', 'CE1', 'HIS', 6.07), ('OD1', 'ASP', 'NE2', 'HIS', 6.88)], [('OD2', 'ASP', 'CB', 'HIS', 5.96), ('OD2', 'ASP', 'CG', 'HIS', 5.71), ('OD2', 'ASP', 'ND1', 'HIS', 4.84), ('OD2', 'ASP', 'CD2', 'HIS', 6.92), ('OD2', 'ASP', 'CE1', 'HIS', 5.79), ('OD2', 'ASP', 'NE2', 'HIS', 6.9)]]}
THR_HIS = { 
	'distances':
		[[11.36, 10.06, 10.03, 8.88, 8.9, 8.1], [11.5, 10.11, 9.91, 8.96, 8.69, 8.02], [10.78, 9.6, 9.8, 8.31, 8.78, 7.77]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'HIS', 11.36), ('CB', 'THR', 'CG', 'HIS', 10.06), ('CB', 'THR', 'ND1', 'HIS', 10.03), ('CB', 'THR', 'CD2', 'HIS', 8.88), ('CB', 'THR', 'CE1', 'HIS', 8.9), ('CB', 'THR', 'NE2', 'HIS', 8.1)], [('OG1', 'THR', 'CB', 'HIS', 11.5), ('OG1', 'THR', 'CG', 'HIS', 10.11), ('OG1', 'THR', 'ND1', 'HIS', 9.91), ('OG1', 'THR', 'CD2', 'HIS', 8.96), ('OG1', 'THR', 'CE1', 'HIS', 8.69), ('OG1', 'THR', 'NE2', 'HIS', 8.02)], [('CG2', 'THR', 'CB', 'HIS', 10.78), ('CG2', 'THR', 'CG', 'HIS', 9.6), ('CG2', 'THR', 'ND1', 'HIS', 9.8), ('CG2', 'THR', 'CD2', 'HIS', 8.31), ('CG2', 'THR', 'CE1', 'HIS', 8.78), ('CG2', 'THR', 'NE2', 'HIS', 7.77)]]}
THR_ASP = { 
	'distances':
		[[14.69, 13.24, 12.92, 12.53], [14.51, 13.02, 12.66, 12.34], [14.52, 13.07, 12.63, 12.5]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 14.69), ('CB', 'THR', 'CG', 'ASP', 13.24), ('CB', 'THR', 'OD1', 'ASP', 12.92), ('CB', 'THR', 'OD2', 'ASP', 12.53)], [('OG1', 'THR', 'CB', 'ASP', 14.51), ('OG1', 'THR', 'CG', 'ASP', 13.02), ('OG1', 'THR', 'OD1', 'ASP', 12.66), ('OG1', 'THR', 'OD2', 'ASP', 12.34)], [('CG2', 'THR', 'CB', 'ASP', 14.52), ('CG2', 'THR', 'CG', 'ASP', 13.07), ('CG2', 'THR', 'OD1', 'ASP', 12.63), ('CG2', 'THR', 'OD2', 'ASP', 12.5)]]}
THR_SER = { 
	'distances':
		[[5.62, 6.19], [5.3, 5.52], [6.15, 6.48]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'SER', 5.62), ('CB', 'THR', 'OG', 'SER', 6.19)], [('OG1', 'THR', 'CB', 'SER', 5.3), ('OG1', 'THR', 'OG', 'SER', 5.52)], [('CG2', 'THR', 'CB', 'SER', 6.15), ('CG2', 'THR', 'OG', 'SER', 6.48)]]}
SER_HIS = { 
	'distances':
		[[8.9, 7.42, 6.94, 6.6, 5.72, 5.43], [8.75, 7.25, 6.75, 6.4, 5.46, 5.16]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.9), ('CB', 'SER', 'CG', 'HIS', 7.42), ('CB', 'SER', 'ND1', 'HIS', 6.94), ('CB', 'SER', 'CD2', 'HIS', 6.6), ('CB', 'SER', 'CE1', 'HIS', 5.72), ('CB', 'SER', 'NE2', 'HIS', 5.43)], [('OG', 'SER', 'CB', 'HIS', 8.75), ('OG', 'SER', 'CG', 'HIS', 7.25), ('OG', 'SER', 'ND1', 'HIS', 6.75), ('OG', 'SER', 'CD2', 'HIS', 6.4), ('OG', 'SER', 'CE1', 'HIS', 5.46), ('OG', 'SER', 'NE2', 'HIS', 5.16)]]}
SER_ASP = { 
	'distances':
		[[11.38, 9.94, 9.75, 9.14], [11.15, 9.65, 9.28, 9.01]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.38), ('CB', 'SER', 'CG', 'ASP', 9.94), ('CB', 'SER', 'OD1', 'ASP', 9.75), ('CB', 'SER', 'OD2', 'ASP', 9.14)], [('OG', 'SER', 'CB', 'ASP', 11.15), ('OG', 'SER', 'CG', 'ASP', 9.65), ('OG', 'SER', 'OD1', 'ASP', 9.28), ('OG', 'SER', 'OD2', 'ASP', 9.01)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'P_5yas_4_1_2_39')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(THR_HIS, d, 'P_5yas_4_1_2_39')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_ASP, d, 'P_5yas_4_1_2_39')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_SER, d, 'P_5yas_4_1_2_39')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_HIS, d, 'P_5yas_4_1_2_39')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_ASP, d, 'P_5yas_4_1_2_39')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'THR_HIS' :  match2,
		'THR_ASP' :  match3,
		'THR_SER' :  match4,
		'SER_HIS' :  match5,
		'SER_ASP' :  match6}