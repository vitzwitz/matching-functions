'''
FUNC:R_1yq4_1_3_5_1
PDB:1yq4
EC:1.3.5.1
RESI:sf4,f3s
LOCI:b-1003,1004;
'''
import motifFunctions as cmd
SF4_F3S = { 
	'distances':
		[[13.45, 11.3, 12.59, 12.95, 14.5, 11.54, 12.03], [14.82, 12.47, 14.18, 13.92, 15.99, 13.11, 13.29], [15.56, 13.57, 14.99, 15.0, 16.81, 13.71, 14.53], [16.35, 14.07, 15.31, 15.79, 17.28, 14.43, 14.6], [16.6, 14.35, 15.9, 15.83, 17.76, 14.8, 15.15], [15.23, 13.22, 14.3, 14.9, 16.24, 13.25, 13.9], [14.66, 12.24, 13.63, 13.96, 15.57, 12.83, 12.74], [13.74, 11.69, 13.32, 13.03, 15.06, 12.0, 12.76]],
	'comparisons':
		[[('FE1', 'SF4', 'FE1', 'F3S', 13.45), ('FE1', 'SF4', 'FE3', 'F3S', 11.3), ('FE1', 'SF4', 'FE4', 'F3S', 12.59), ('FE1', 'SF4', 'S1', 'F3S', 12.95), ('FE1', 'SF4', 'S2', 'F3S', 14.5), ('FE1', 'SF4', 'S3', 'F3S', 11.54), ('FE1', 'SF4', 'S4', 'F3S', 12.03)], [('FE2', 'SF4', 'FE1', 'F3S', 14.82), ('FE2', 'SF4', 'FE3', 'F3S', 12.47), ('FE2', 'SF4', 'FE4', 'F3S', 14.18), ('FE2', 'SF4', 'S1', 'F3S', 13.92), ('FE2', 'SF4', 'S2', 'F3S', 15.99), ('FE2', 'SF4', 'S3', 'F3S', 13.11), ('FE2', 'SF4', 'S4', 'F3S', 13.29)], [('FE3', 'SF4', 'FE1', 'F3S', 15.56), ('FE3', 'SF4', 'FE3', 'F3S', 13.57), ('FE3', 'SF4', 'FE4', 'F3S', 14.99), ('FE3', 'SF4', 'S1', 'F3S', 15.0), ('FE3', 'SF4', 'S2', 'F3S', 16.81), ('FE3', 'SF4', 'S3', 'F3S', 13.71), ('FE3', 'SF4', 'S4', 'F3S', 14.53)], [('FE4', 'SF4', 'FE1', 'F3S', 16.35), ('FE4', 'SF4', 'FE3', 'F3S', 14.07), ('FE4', 'SF4', 'FE4', 'F3S', 15.31), ('FE4', 'SF4', 'S1', 'F3S', 15.79), ('FE4', 'SF4', 'S2', 'F3S', 17.28), ('FE4', 'SF4', 'S3', 'F3S', 14.43), ('FE4', 'SF4', 'S4', 'F3S', 14.6)], [('S1', 'SF4', 'FE1', 'F3S', 16.6), ('S1', 'SF4', 'FE3', 'F3S', 14.35), ('S1', 'SF4', 'FE4', 'F3S', 15.9), ('S1', 'SF4', 'S1', 'F3S', 15.83), ('S1', 'SF4', 'S2', 'F3S', 17.76), ('S1', 'SF4', 'S3', 'F3S', 14.8), ('S1', 'SF4', 'S4', 'F3S', 15.15)], [('S2', 'SF4', 'FE1', 'F3S', 15.23), ('S2', 'SF4', 'FE3', 'F3S', 13.22), ('S2', 'SF4', 'FE4', 'F3S', 14.3), ('S2', 'SF4', 'S1', 'F3S', 14.9), ('S2', 'SF4', 'S2', 'F3S', 16.24), ('S2', 'SF4', 'S3', 'F3S', 13.25), ('S2', 'SF4', 'S4', 'F3S', 13.9)], [('S3', 'SF4', 'FE1', 'F3S', 14.66), ('S3', 'SF4', 'FE3', 'F3S', 12.24), ('S3', 'SF4', 'FE4', 'F3S', 13.63), ('S3', 'SF4', 'S1', 'F3S', 13.96), ('S3', 'SF4', 'S2', 'F3S', 15.57), ('S3', 'SF4', 'S3', 'F3S', 12.83), ('S3', 'SF4', 'S4', 'F3S', 12.74)], [('S4', 'SF4', 'FE1', 'F3S', 13.74), ('S4', 'SF4', 'FE3', 'F3S', 11.69), ('S4', 'SF4', 'FE4', 'F3S', 13.32), ('S4', 'SF4', 'S1', 'F3S', 13.03), ('S4', 'SF4', 'S2', 'F3S', 15.06), ('S4', 'SF4', 'S3', 'F3S', 12.0), ('S4', 'SF4', 'S4', 'F3S', 12.76)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SF4_F3S, d, 'R_1yq4_1_3_5_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SF4_F3S' :  match1}