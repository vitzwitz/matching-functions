'''
FUNC:A_1a4s_1_2_1_8
PDB:1a4s
EC:1.2.1.8
RESI:asn,glu,cys
LOCI:a-166,263,297;
'''
import motifFunctions as cmd
import time as t

strtMotif = t.time()


cmd.match([d*8.79, d*9.87, d*9.67, d*8.65, d*10.70, d*8.10, d*8.26, d*9.12, d*10.47],
          'CYS', 'CB',
          'GLU', ['CB', 'CG', 'CD', 'OE1', 'OE2', 'O', 'C', 'CA', 'N'])

cmd.match([d*8.47, d*9.28, d*8.88, d*7.89, d*9.76, d*8.52, d*8.61, d*9.13, d*10.51],
          'CYS', 'SG',
          'GLU', ['CB', 'CG', 'CD', 'OE1', 'OE2', 'O', 'C', 'CA', 'N'])

cmd.match([d*11.14, d*12.15, d*11.72, d*10.52, d*12.68, d*10.37, d*10.24, d*11.13, d*12.51],
          'CYS', 'O',
          'GLU', ['CB', 'CG', 'CD', 'OE1', 'OE2', 'O', 'C', 'CA', 'N'])

cmd.match([d*10.74, d*11.71, d*11.25, d*10.08, d*12.18, d*10.17, d*10.12, d*10.93, d*12.33],
          'CYS', 'C',
          'GLU', ['CB', 'CG', 'CD', 'OE1', 'OE2', 'O', 'C', 'CA', 'N'])

cmd.match([d*10.30, d*11.37, d*11.11, d*10.03, d*12.10, d*9.49, d*9.64, d*10.56, d*11.90],
          'CYS', 'CA',
          'GLU', ['CB', 'CG', 'CD', 'OE1', 'OE2', 'O', 'C', 'CA', 'N'])

cmd.match([d*11.10, d*12.11, d*11.85, d*10.84, d*12.79, d*10.39, d*10.67, d*10.53, d*12.86],
          'CYS', 'N',
          'GLU', ['CB', 'CG', 'CD', 'OE1', 'OE2', 'O', 'C', 'CA', 'N'])

cmd.match([d*9.29, d*8.02, d*8.20, d*6.93, d*11.33, d*10.89, d*10.55, d*10.82],
          'CYS', 'C',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*9.35, d*7.99, d*8.06, d*6.98, d*10.87, d*10.49, d*10.44, d*10.80],
          'CYS', 'SG',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*11.57, d*10.57, d*11.04, d*9.32, d*13.61, d*13.40, d*12.99, d*13.46],
          'CYS', 'O',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*10.64, d*9.60, d*10.06, d*8.33, d*12.53, d*12.33, d*12.02, d*12.54],
          'CYS', 'C',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*9.28, d*8.22, d*8.67, d*6.98, d*11.35, d*11.07, d*10.67, d*11.12],
          'CYS', 'CA',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*8.19, d*7.24, d*7.87, d*5.94, d*10.09, d*9.93, d*9.59, d*10.22],
          'CYS', 'N',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*13.49, d*12.01, d*11.27, d*11.70, d*15.05, d*14.17, d*14.06, d*13.61],
          'GLU', 'CB',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*14.47, d*12.97, d*12.19, d*12.69, d*15.76, d*14.91, d*14.95, d*14.53],
          'GLU', 'CG',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*14.74, d*13.23, d*12.55, d*12.82, d*15.89, d*15.16, d*15.29, d*15.03],
          'GLU', 'CD',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*14.23, d*12.72, d*12.15, d*12.18, d*15.49, d*14.81, d*14.90, d*14.74],
          'GLU', 'OE1',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*15.59, d*14.09, d*13.39, d*13.71, d*16.53, d*15.83, d*16.07, d*15.84],
          'GLU', 'OE2',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*12.55, d*11.17, d*10.52, d*10.88, d*14.67, d*13.71, d*13.25, d*12.67],
          'GLU', 'O',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*13.44, d*12.02, d*11.42, d*11.61, d*15.49, d*14.58, d*14.19, d*13.70],
          'GLU', 'C',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*14.25, d*12.79, d*12.11, d*12.43, d*16.06, d*15.16, d*14.91, d*14.43],
          'GLU', 'CA',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])

cmd.match([d*15.15, d*13.72, d*12.96, d*13.47, d*16.96, d*15.99, d*15.71, d*15.10],
          'GLU', 'N',
          'ASN', ['CB', 'CG', 'OD1', 'ND2', 'O', 'C', 'CA', 'N'])


print "We succeeded!"
print "Time to go thru motif:", t.time() - strtMotif, "seconds"
