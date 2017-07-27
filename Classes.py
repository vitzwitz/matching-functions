"""
Classes : Classes for parsing PDB files
Reference : http://swift.cmbi.ru.nl/gv/whatcheck/HTML/Format.pdf
"""

# Title Section

class Header:
    def __init__(self, line):
        try:
            self.classification = str(line[10:50])
            self.depDate        = str(line[50:59])
            self.idCode         = str(line[62:66])
        except:
            raise Warning
class Title:
    def __init__(self, line):
        try:
            self.title = str(line[10:70])
        except:
            raise Warning
class Author:
        def _init_(self, line):
            try:
                self.authors = str(line[10:70]).split(",")
            except:
                raise Warning
class Keywds:
    def _init_(self, line):
        try:
            self.keywords = str(line[10:70]).strip().split(",")
        except:
            raise Warning
class Jrnl:
    def _init_(self, line):
        try:
            self.mainRef = str(line[12:70])
        except:
            raise Warning
class Source:
    def __init__(self, line):
        try:
            self.source = str(line[10:70])
        except:
            raise Warning
class Remark:
    def __init__(self, line):
        try:
            self.REMARKS = {}
            self.remarkInt = int(line[7:10])
            if self.remarkInt == 1:
                label = str(line[13:16])
                txt = str(line[19:70])
                if str(line[11:20]) == "Reference":
                    if self.remarkInt not in self.REMARKS:
                        self.REMARKS['refNum'] = str(line[21:70])
                    else:
                        self.REMARKS['refNum'] += str(line[21:70])
                elif label == "AUTH":
                    if self.remarkInt not in self.REMARKS:
                        self.REMARKS["authors"] = txt.split(",")
                    else:
                        self.REMARKS["authors"].append(txt.split(","))
                elif label == "TITL":
                    if self.remarkInt not in self.REMARKS:
                        self.REMARKS["title"] = txt
                    else:
                        self.REMARKS["title"] += txt
                elif label == "EDIT":
                    if self.remarkInt not in self.REMARKS:
                        self.REMARKS["editors"] = txt.split(",")
                    else:
                        self.REMARKS["editors"] += txt.split(",")
                elif label == "REF":
                    if self.remarkInt not in self.REMARKS:
                        self.REMARKS["ref"] = str(line[19:66])
                    else:
                        self.REMARKS["ref"] += str(line[19:66])
                elif label == "PUBL":
                    if self.remarkInt not in self.REMARKS:
                        self.REMARKS["publ"] = txt
                    else:
                        self.REMARKS["publ"] += txt
                elif label == "REFN":
                    if self.remarkInt not in self.REMARKS:
                        self.REMARKS["refn"] = txt[35:65]
                    else:
                        self.REMARKS["refn"] += txt[35:65]
            elif self.remarkInt == 2:
                if str(line[11:27]) == "RESOLUTION. NOT":
                    if self.remarkInt not in self.REMARKS:
                        self.comments = str(line[23:70])
                    else:
                        self.comments += str(line[23:70])
                elif str(line[12:22]) == "RESOLUTION":
                    if self.remarkInt not in self.REMARKS:
                        self.REMARKS["Angstroms"] = str(line[31:41])
                    else:
                        self.REMARKS["Angstroms"] += str(line[31:41])
            else:
                if self.remarkInt not in self.REMARKS:
                    self.REMARKS["text"] = line
                else:
                    self.REMARKS["text"] += line
        except:
            raise Warning
class Expdta:
    def __init__(self, line):
        try:
            self.technique = str(line[10:70])
        except:
            raise Warning
class Revdat:
    def __init__(self, line):
        try:
            self.modNum  = int(line[7:10])
            self.modDate = str(line[13:22])
            self.modID   = str(line[23:28])
            self.modType = int(line[32])
            self.record  = str(line[39:66])
        except:
            raise Warning
class SPRSDE:
    def __init__(self, line):
        try:
            self.date   = str(line[11:20])
            self.IDcode = str(line[21:70])
        except:
            raise Warning
class Obslte:
    def __init__(self, line):
        try:
            self.date   = str(line[11:20])
            self.IDcode = str(line[21:70])
        except:
            raise Warning
class Caveat:
    def _init_(self, line):
        try:
            self.IDcode  = str(line[11:15])
            self.comment = str(line[19:70])
        except:
            raise Warning
class Split:
    def __init__(self, line):
        try:
            self.title = str(line[10:80])
        except:
            raise Warning
class Compound:
    def __init__(self, line):
        try:
            label = str(line[10:16])
            if label == "MOL_ID":
                self.Mol_ID = int(line[18])
            elif label == " MOLEC":
                self.molecule = str(line[22:-1])
            elif label == " CHAIN":
                self.chains = str(line[18:28]).split(",")
            elif label[:3] == " EC":
                try:
                    self.ec = str(line[15:-1]).strip(",")
                except:
                    self.ec = str(line[15:-1])
            elif label == " ENGIN":
                if str(line[23]) == "Y":
                    self.engineered = True
                elif str(line[23]) == "N":
                    self.engineered = False
                else:
                    raise Warning
            elif label == "MUTAT":
                if str(line[21]) == "Y":
                    self.engineered = True
                elif str(line[21]) == "N":
                    self.engineered = False
                else:
                    raise Warning
            else:
                self.otherDetails = str(line[25:-1])
        except:
            raise Warning
class NumModels:
    def __init__(self, line):
        self.totNum = int(line[11:14])
class ModelType:
    def __init__(self, line):
        self.comment = str(line[11:80])


# Primary Structure Section
class DBRef:
    def __init__(self, line):
        self.idCode      = str(line[8:11])
        self.chainID     = str(line[13])
        self.seqBegin    = int(line[15:18])
        self.insertBegin = str(line[19])
        self.seqEnd      = int(line[21:24])
        self.insertEnd   = str(line[25])
        self.database    = str(line[27:32])
        self.dbAccession = str(line[34:41])
        self.dbIDCode    = str(line[43:54])
        self.dbSeqBegin  = int(line[56:60])
        self.InsCodeBeg  = str(line[61])
        self.dbSeqEnd    = int(line[63:67])
        self.InsCodeEnd  = str(line[68])
class SeqAdv:
    def __init__(self, line):
        try:
            self.IDCode   = str(line[8:11])
            self.resName  = str(line[13:15])
            self.chainID  = str(line[17])
            self.seqNum   = int(line[19:22])
            self.insCode  = str(line[23])
            self.database = str(line[25:28])
            self.dbIDCode = str(line[30:38])
            self.dbRes    = str(line[40:42])
            self.dbSeq    = int(line[44:48])
            self.conflict = str(line[50:70])
        except:
            raise Warning
class SeqRes:
    def __init__(self, line):
        try:
            self.serNum  = int(line[8:10])
            self.chainID = str(line[12])
            self.numRes  = int(line[14:17])
            try:
                self.resName = []
                self.resName.append(str(line[20:22]))
                self.resName.append(str(line[24:26]))
                self.resName.append(str(line[28:30]))
                self.resName.append(str(line[32:34]))
                self.resName.append(str(line[36:38]))
                self.resName.append(str(line[40:42]))
                self.resName.append(str(line[44:46]))
                self.resName.append(str(line[48:50]))
                self.resName.append(str(line[52:54]))
                self.resName.append(str(line[56:58]))
                self.resName.append(str(line[60:62]))
                self.resName.append(str(line[64:66]))
                self.resName.append(str(line[68:70]))
            except:
                raise Warning
        except:
            raise Warning
class ModRes:
    def __init__(self, line):
        try:
            self.IDCode          = str(line[8:11])
            self.ResName         = str(line[13:15])
            self.chainID         = str(line[17])
            self.seqNum          = int(line[19:22])
            self.insCode         = str(line[23])
            self.StandardResName = str(line[25:27])
            self.comment         = str(line[30:70])
        except:
            raise Warning

# Heterogen Section

class Het:
    def _init_(self, line):
        try:
            self.hetID       = str(line[8:10])
            self.chainID     = str(line[13])
            self.seqNum      = int(line[14:17])
            self.insCode     = str(line[18])
            self.numHetAtoms = int(line[21:25])
            self.text        = str(line[31:70])
        except:
            raise Warning

class HetCompound:
    # HET
    def __init__(self, line):
        try:
            self.hetID        = str(line[12:14])
            self.chemicalName = str(line[16:70])
        except:
            raise Warning

class HetSynon:
    # HETSYN
    def __init__(self, line):
        try:
            self.hetID       = str(line[12:14])
            self.hetSynonyms = str(line[16:70]).split(",")
        except:
            raise Warning

class Formul:
    # FORMUL
    def __init__(self, line):
        try:
            self.compNum         = int(line[9:10])
            self.hetID           = str(line[13:18])
            self.asterik         = str(line[19])
            self.chemicalFormula = str(line[20:70])
        except:
            raise Warning
# Secondary Structure Section
class Helix:
    # HELIX
    def __init__(self, line):
        try:
            self.serial    = int(line[8:10])
            self.ID        = str(line[12:14])
            self.ResName_i = str(line[16:18])
            self.ChainID_i = str(line[20])
            self.seqNum_i  = int(line[22:25])
            self.insCode_i = str(line[26])
            self.ResName_f = str(line[28:30])
            self.chainID_f = str(line[32])
            self.seqNum_f  = int(line[34:37])
            self.insCode_f = str(line[38])
            self.Class     = int(line[39:40])
            self.comment   = str(line[41:70])
            self.length    = int(line[72:76])
        except:
            raise Warning

class Sheet:
    # SHEET
    def _init_(self, line):
        try:
            self.strand      = int(line[8:10])
            self.ID          = str(line[12:14])
            self.numStrands  = int(line[15:16])
            self.ResName_i   = str(line[18:20])
            self.ChainID_i   = str(line[22])
            self.seqNum_i    = int(line[23:26])
            self.insCode_i   = str(line[27])
            self.ResName_f   = str(line[29:31])
            self.chainID_f   = str(line[33])
            self.seqNum_f    = int(line[34:37])
            self.insCode_f   = str(line[38])
            self.sense       = int(line[39:40])
            self.currAtom    = str(line[42:45])
            self.currResName = str(line[46:48])
            self.currChainID = str(line[50])
            self.currResSeq  = int(line[51:54])
            self.currInsCode = str(line[55])
            self.prevAtom    = str(line[57:60])
            self.prevResName = str(line[61:63])
            self.prevChainID = str(line[65])
            self.prevResSeq  = int(line[66:69])
            self.prevInsCode = str(line[70])
        except:
            raise Warning

class Turn:
    def __init__(self, line):
        try:
            self.seq = int(line[7:10])
            self.turnId = str(line[11:14])
            self.initResName = str(line[15:18])
            self.initChainId = str(line[19])
            self.initSeqNum = int((line[20:24]))
            self.initICode = str(line[24])
            self.endResName = str(line[26:29])
            self.endChainId = str(line[30])
            self.endSeqNum = int((line[31:35]))
            self.insCode = str(line[35])
            self.comment = str(line[40:70])
        except:
            raise Warning

# Connectivity Annotation Section

class S2Bond:
    # SSBOND
    def __init__(self, line):
        try:
            self.serial   = int(line[8:10])
            self.chainID1 = str(line[16])
            self.seqNum1  = int(line[18:21])
            self.insCode1 = str(line[22])
            self.chainID2 = str(line[30])
            self.seqNum2  = int(line[32:25])
            self.insCode2 = str(line[36])
            self.symm1    = str(line[60:65])
            self.symm2    = str(line[67:72])
            self.length   = float(line[74:78])
        except:
            raise Warning
class Link:
    # LINK
    def __init__(self, line):
        try:
            self.atomName1 = str(line[13:16])
            self.altLoc1   = str(line[17])
            self.resName1  = str(line[18:20])
            self.chainID1  = str(line[22])
            self.resSeq1   = int(line[23:26])
            self.insCode1  = str(line[27])
            self.atomName2 = str(line[43:46])
            self.altLoc2   = str(line[47])
            self.resName2  = str(line[48:50])
            self.chainID2  = str(line[52])
            self.resSeq2   = int(line[53:56])
            self.insCode2  = str(line[57])
            self.symm1     = str(line[60:65])
            self.symm2     = str(line[67:72])
            self.length    = float(line[74:78])
        except:
            raise Warning
class CisPep:
    # CISPEP
    def __init__(self, line):
        try:
            self.serial   = int(line[8:10])
            self.pep1     = str(line[12:14])
            self.chainID1 = str(line[16])
            self.seqNum1  = int(line[18:21])
            self.inscode1 = str(line[22])
            self.pep2     = str(line[26:28])
            self.chainID2 = str(line[30])
            self.seqNum2  = int(line[32:35])
            self.inscode2 = str(line[36])
            self.modelNum = int(line[44:46])
            self.measure  = float(line[54:59])
        except:
            raise Warning

# Miscellaneous Features Section

class Site:
    # SITE
    def __init__(self, line):
        try:
            self.seqNum   = int(line[8:10])
            self.ID       = str(line[12:14])
            self.numRes   = int(line[16:17])
            self.resName1 = str(line[19:21])
            self.chainID1 = str(line[23])
            self.resSeq1  = int(line[24:27])
            self.insCode1 = str(line[28])
            self.resName2 = str(line[30:32])
            self.chainID2 = str(line[34])
            self.resSeq2  = int(line[35:38])
            self.insCode2 = str(line[39])
            self.resName3 = str(line[41:43])
            self.chainID3 = str(line[45])
            self.resSeq3  = int(line[46:49])
            self.insCode3 = str(line[50])
            self.resName4 = str(line[52:54])
            self.chainID4 = str(line[256])
            self.resSeq4  = int(line[57:60])
            self.insCode4 = str(line[61])
        except:
            raise Warning

# Crystallographic & Coordinate Tranformation Section

class Cryst1:
    def __init__(self, line):
        try:
            self.a = float(line[7:15])
            self.b = float(line[16:24])
            self.c = float(line[25:33])
            self.alpha = float(line[34:40])
            self.beta = float(line[41:47])
            self.gamma = float(line[48:54])
            self.spaceGrp = str(line[56:66])
            self.Z = int(line[67:70])
        except:
            raise Warning

class OrigX1:
    def __init__(self, line):
        try:
            self.O = []
            self.O.append(float(line[11:20]))
            self.O.append(float(line[21:30]))
            self.O.append(float(line[31:40]))
            self.t1 = (float(line[46:55]))
        except:
            raise Warning

class OrigX2:
    def __init__(self, line):
        try:
            self.O = []
            self.O.append(float(line[11:20]))
            self.O.append(float(line[21:30]))
            self.O.append(float(line[31:40]))
            self.t2 = (float(line[46:55]))
        except:
            raise Warning

class OrigX3:
    def __init__(self, line):
        try:
            self.O = []
            self.O.append(float(line[11:20]))
            self.O.append(float(line[21:30]))
            self.O.append(float(line[31:40]))
            self.t3 = (float(line[46:55]))
        except:
            raise Warning

class Scale1:
    def __init__(self, line):
        try:
            self.s1 = []
            self.s1.append(float(line[11:20]))
            self.s1.append(float(line[21:30]))
            self.s1.append(float(line[31:40]))
            self.u1 = (float(line[46:55]))
        except:
            raise Warning

class Scale2:
    def __init__(self, line):
        try:
            self.s2 = []
            self.s2.append(float(line[11:20]))
            self.s2.append(float(line[21:30]))
            self.s2.append(float(line[31:40]))
            self.u2 = (float(line[46:55]))
        except:
            raise Warning

class Scale3:
    def __init__(self, line):
        try:
            self.s3 = []
            self.s3.append(float(line[11:20]))
            self.s3.append(float(line[21:30]))
            self.s3.append(float(line[31:40]))
            self.u3 = (float(line[46:55]))
        except:
            raise Warning

class Matrix1:
    # MTRIX1
    def __init__(self, line):
        try:
            self.serial = int(line[8:10])
            self.m1 = []
            self.m1.append(float(line[11:20]))
            self.m1.append(float(line[21:30]))
            self.m1.append(float(line[31:40]))
            self.v1 = (float(line[46:55]))
        except:
            raise Warning

class Matrix2:
    # MTRIX2
    def __init__(self, line):
        try:
            self.serial = int(line[8:10])
            self.m2 = []
            self.m2.append(float(line[11:20]))
            self.m2.append(float(line[21:30]))
            self.m2.append(float(line[31:40]))
            self.v2 = (float(line[46:55]))
        except:
            raise Warning

class Matrix3:
    # MTRIX3
    def __init__(self, line):
        try:
            self.serial = int(line[8:10])
            self.m3 = []
            self.m3.append(float(line[11:20]))
            self.m3.append(float(line[21:30]))
            self.m3.append(float(line[31:40]))
            self.v3 = (float(line[46:55]))
        except:
            raise Warning

class TVector:
    def __init__(self, line):
        try:
            self.serial = int(line[7:10])
            self.t1 = float(line[10:20])
            self.t2 = float(line[20:30])
            self.t3 = float(line[30:40])
            self.text = str(line[40:70])
        except:
            raise Warning

# Cooordinate Section

class Model:
    def __init__(self, line):
        try:
            self.serial = int(line[11:14])
        except:
            raise Warning
class Atom:
    def __init__(self, line):
        try:
            if isinstance(line, str):
                self.serial    = int(line[7:11])
                self.name      = str(line[13:16]).strip()
                self.altLoc    = str(line[17])
                self.resName   = str(line[17:20]).strip()
                self.chainID   = str(line[22])
                self.resSeq    = int(line[23:26])
                self.insCode   = str(line[27])
                self.x         = float(line[31:38])
                self.y         = float(line[39:46])     # Orthogonal
                self.z         = float(line[47:54])
                self.position = (self.x, self.y, self.z)
                self.occupancy = float(line[55:60])
                self.tempFact  = float(line[61:66])
                self.element   = str(line[77:78])
                self.charge    = str(line[79:80])
        except:
            raise Warning

class Anisou:
    def __init__(self, line):
        try:
            self.serial  = int(line[7:11])
            self.name    = str(line[13:16])
            self.altLoc  = str(line[17])
            self.resName = str(line[18:20])
            self.chainID = str(line[22])
            self.resSeq  = int(line[23:26])
            self.insCode = str(line[27])
            self.U11     = int(line[29:35])
            self.U22     = int(line[36:42])
            self.U33     = int(line[43:49])
            self.U12     = int(line[50:56])
            self.U13     = int(line[57:63])
            self.U23     = int(line[64:70])
            self.element = str(line[77:78])
            self.charge  = str(line[79:80])
        except:
            raise Warning

class Ter:
    def __init__(self, line):
        try:
            self.serial  = int(line[7:11])
            self.resName = str(line[18:20])
            self.chainID = str(line[line[22]])
            self.resSeq  = int(line[23:26])
            self.insCode = str(line[27])
        except:
            raise Warning

class HetAtom:
    def __init__(self, line):
        try:
            self.serial    = int(line[7:11])
            self.name      = str(line[13:16])
            self.altLoc    = str(line[17])
            self.resName   = str(line[18:20])
            self.chainID   = str(line[22])
            self.resSeq    = int(line[23:26])
            self.insCode   = str(line[27])
            self.x         = float(line[31:38])
            self.y         = float(line[39:46])     # Orthogonal
            self.z         = float(line[47:54])
            self.occupancy = float(line[55:60])
            self.tempFact  = float(line[61:66])
            self.element   = str(line[77:78])
            self.charge    = str(line[79:80])
        except:
            raise Warning

class HydroBond:
    """ HYDBND field
        The HYDBND records specify hydrogen bonds in the entry.
    """

    def __init__(self, line):
        record = str(line[0:6])
        if record == "HYDBND":
            self.name1 = str(line[12:16])
            self.altLoc1 = str(line[16])
            self.resName1 = str(line[17:20])
            self.ChainID1 = str(line[21])
            self.resSeq1 = int(line[22:27])
            self.InsCode1 = str(line[27])
            self.nameH = str(line[29:33])
            self.altLocH = str(line[33])
            self.ChainH = str(line[35])
            self.InsCodeH = str(line[41])
            self.name2 = str(line[43:47])
            self.altLoc2 = str(line[47])
            self.resName2 = str(line[48:51])
            self.ChainID2 = str(line[52])
            self.resSeq2 = int(line[53:58])
            self.InsCode2 = str(line[58])
            self.symm1 = str(line[59:65])
            self.symm2 = str(line[66:72])
        else:
            raise ValueError, record

class SaltBridge:
    def __init__(self, line):
        try:
            self.name1 = str(line[12:16])
            self.altLoc1 = str(line[16])
            self.resName1 = str(line[17:20])
            self.chainID1 = str(line[21])
            self.resSeq1 = int(line[22:26])
            self.insCode1 = str(line[26])
            self.name2 = str(line[42:46])
            self.altLoc2 = str(line[46])
            self.resName2 = str(line[47:50])
            self.chainID2 = str(line[51])
            self.resSeq2 = int(line[52:56])
            self.iCode2 = str(line[56])
            self.sym1 = str(line[59:65])
            self.sym2 = str(line[66:72])
        except:
            raise Warning

class EndModel:
    def __init__(self, line):
        pass

# Connectivity Section

class Connects:
    def __init__(self, line):
        try:
            self.serial = []
            try:
                self.serial.append(int(line[7:11]))
                self.serial.append(int(line[12:16]))
                self.serial.append(int(line[17:21]))
                self.serial.append(int(line[22:26]))
                self.serial.append(int(line[27:31]))
            except:
                raise Warning
        except:
            raise Warning

# Bookkeeping Section
class Master:
    def __init__(self, line):
        try:
            self.remarks  = int(line[11:15])
            self.hets     = int(line[21:25])
            self.helixes  = int(line[26:30])
            self.sheets   = int(line[31:35])
            self.turns    = int(line[36:40])
            self.sites    = int(line[41:45])
            self.Xforms   = int(line[46:50])
            self.coords   = int(line[51:55])
            self.ters     = int(line[56:60])
            self.connects = int(line[61:65])
            self.seqs     = int(line[66:70])
        except:
            raise Warning

class End:
    def __init__(self, line):
        pass