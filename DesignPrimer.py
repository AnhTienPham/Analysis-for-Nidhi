from Bio.Seq import Seq
import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()
application_window.withdraw()

before = simpledialog.askstring("Input", "Enter the sequence before ORF. Note the start codon",
                                parent=application_window)

ORF = simpledialog.askstring("Input", "Enter the sequence of ORF to mutagenize?",
                                 parent=application_window)

after = simpledialog.askstring("Input", "Enter the sequence after ORF. Note the stop codon",
                                 parent=application_window)
deg = "NNK"
fullstring = Seq(before + ORF + after)
startnum = 0
endnum = 402 * 3 + 3

plist = list()
plistf = list()
plistrc = list()
text_file = open("Output_file.txt", "w")

for x in range(startnum, endnum, 3):
    pos = fullstring[(30 + x):(33 + x)]
    plist.append(str(pos))
    posf = deg + fullstring[(33 + x):(63 + x)]
    plistf.append(str(posf))
    posr = fullstring[(0 + x):(30 + x)]
    posrc = posr.reverse_complement()
    plistrc.append(str(posrc))

ntcount = 0

for x in range(0, 402):
    text_file.write("PTEN_f_%s\t%s\n" % (x+2, plistf[x]))
    ntcount = ntcount + len(plistf[x])

for x in range(0, 402):
    text_file.write("PTEN_r_%s\t%s\n" % (x+2, plistrc[x]))
    ntcount = ntcount + len(plistrc[x])

totalcost = simpledialog.askstring("Output", "The Total Cost is",
                                             initialvalue=str(ntcount*0.18))

text_file.close()