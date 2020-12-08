class Mt_Out:
    def get_rawr(self):
        rawr_1 = '𒁂𐦠𑀕𐡔Ꝛ෴'
        return '{}'.format(rawr_1)
    def get_help(self):
        help_cmd = []
        help_cmd += "!('mma'/'mmd') <Elements>: mass g/mol (example :C 6 H 12 O 6) \n"
        help_cmd += "!('prs'/'prd'/'pra') <peptide> ('cg'/'at'/'any'): Peptide to DNA  \n"
        help_cmd += "!('trs'/'trd'/'tra') <DNA/RNA>:  DNA to peptide \n"
        help_cmd += "!'plot' xmin, xmax, f(x) (example: -1 1 x*2) \n"
        help_cmd +=  "!'m2km/km2m': Miles to Kilometer to Miles \n"
        help_cmd +=  "!'i2m/m2i': Inch to Meter to Inch \n"
        help_cmd += "!'kg2p/p2kg': Kilogram to Pound to Kilogram \n"
        help_cmd += "!'k2c/c2k': Celcius to Kelvin to Celcius \n"
        help_cmd += "!'f2c/c2f': Farenheit to Celcius to Farenheit \n"
        help_cmd += "!'k2f/f2k': Kelvin to Pound to Kelvin \n"
        help_cmd += "!'getnote': Get your personal notes \n"
        help_cmd += "!'setnote': Set your personal notes \n"
        help_cmd += "!'resetnote': Set your personal notes \n"
        help_cmd += "!'f2m/m2f': Feet to Meter to Feet \n"
        help_cmd += "!'scale': SI Standard Unit system scale \n"
        help_cmd +=  "!'trivia': Scientific trivia  \n"
        help_cmd +=  "!'ggif': Display a random gif \n"
        help_cmd += "!'gmeme': Display a random meme \n"
        help_cmd += "!'rawr': Have the bot roar back at you \n"
        help_cmd +=  "!'matpc': Links to syllabus and material for plasmid club \n"
        help_cmd +=  "!'jcgm': When does the next journal club happen \n"
        help_cmd +=  "!'pcgm': When does the next plasmid club happen \n"
        help_cmd +=  "!'linkpc': Links to all plasmid club vid \n"
        help_cmd +=  "!'linkjc': Links to all journal club vid \n"
        help_cmd +=  "!'subjc': Links to inscription and scheduling for journal club \n"
        help_cmd +=  "!'linklib': links to the library \n"
        help_cmd +=  "!'est': Eastern Standard Time (EST) \n"
        help_cmd +=  "!'help' with Soizik's part of the bot: \n"
        return ''.join(help_cmd)
    def get_journal_club(self):
        jclub_cmd = []
        jclub_cmd += '```'
        jclub_cmd += 'https://youtu.be/4Qf6eLCdL_Q : Nacre, Gabriel \n'
        jclub_cmd += 'https://youtu.be/H4nxDmWbjwU : Synthetic Seeds, Diego \n'
        jclub_cmd += 'https://youtu.be/OKl6N-jzoSw : Immobilised yeast, Sy \n'
        jclub_cmd += 'https://youtu.be/eDHdK5bGkpg : Synthetic Biology, Koeng \n'
        jclub_cmd += 'https://youtu.be/VDrM-N8yTqc : Biosensing of Phosphonates, Bast \n'
        jclub_cmd += 'https://youtu.be/NfBLW5qgIIU : Structural Materials, Gabriel \n'
        jclub_cmd += 'https://youtu.be/xzUVmeDNbMM : Yamanaka and IPSCs, Soizik \n'
        jclub_cmd += 'https://youtu.be/eN6KKLWXHbA : Arcologies, Veronw \n'
        jclub_cmd += 'https://youtu.be/tCpDOOYCSbQ : Plant microbial fuel cell, Olly \n'
        jclub_cmd += 'https://youtu.be/m0HDmHrqFgo : Enhanced Damascus steel, WitchDr \n'
        jclub_cmd += 'https://youtu.be/G_WN_CCRulY : Radiative cooling, Baconator \n'
        jclub_cmd += 'https://youtu.be/qFaP6mH2TB8 : Protein tagging, Aquanker \n'
        jclub_cmd += 'https://youtu.be/dfJcgYU-lDg : Algal Biodiesel, Olly'
        jclub_cmd += '```'
        return ''.join(jclub_cmd)
    def get_plasmid_club(self):
        pclub_cmd = []
        pclub_cmd += '```'
        pclub_cmd += 'https://youtu.be/zlGy9YHAK3A : Course 1 part 1 \n'
        pclub_cmd += 'https://youtu.be/pqCZobaBcWM : Course 1 part 2 \n'
        pclub_cmd += 'https://youtu.be/FZ6iOs84tf8 : Course 2 part 1 \n'
        pclub_cmd += 'https://youtu.be/KpDAOy0uZ_Y : Course 2 part 2 \n'
        pclub_cmd += 'https://youtu.be/-l84QXialOY : Course 3 part 1 \n'
        pclub_cmd += '```'
        return ''.join(pclub_cmd)
    def get_algae_brew(self):
        ab_cmd = []
        ab_cmd += '```'
        ab_cmd += 'Algae Brew github repo:'
        ab_cmd += 'https://github.com/Olly-Fallows/Algae-Brew'
        ab_cmd += 'Algae Brew google doc:'
        ab_cmd += 'https://drive.google.com/drive/folders/1znpyHunydGwEJ19bpVoC-SyJFd021UOr'
        ab_cmd += '```'
        return ''.join(pclub_cmd)
    def get_library(self):
        plib_cmd = []
        plib_cmd += 'This link leads to the Scihouse Library main door! \n'
        plib_cmd += 'https://drive.google.com/drive/folders/1inAhfU9W18A83YqVI6A5uFO8eHyeKC3W \n'  
        return ''.join(plib_cmd)
    def get_pc_library(self):
        pclib_cmd = []
        pclib_cmd += 'Plasmid Creation Club Folder: \n'
        pclib_cmd += '(Will come back after course 6 when the plasmid club actually begins) \n'
        pclib_cmd += 'Modular Biology Crash Course Folder: \n'
        pclib_cmd += 'https://drive.google.com/drive/folders/1-dE35fvJzSC39XoU0Vs3gboGEKOH2SaN \n'  
        return ''.join(pclib_cmd)
    def get_jc_library(self):
        jclib_cmd = []
        jclib_cmd += 'This link leads you to the Journal Club schedule that you can subscribe to: \n'
        jclib_cmd += 'https://docs.google.com/document/d/1K1r38sXHWSG-a2UKZ-PqsU5PeMWFeKtTuOLMBZ4DmlE/edit \n'  
        return ''.join(jclib_cmd)
    def get_scale(self):
        help_scale_cmd = []
        help_scale_cmd += 'Units prefixes and scale of measures \n'
        help_scale_cmd += 'Prefix, Symbol, Scale & formulation \n'
        help_scale_cmd += ' tera-    T      1 000 000 000 000 or 10^12 \n'
        help_scale_cmd += ' giga-    G      1 000 000 000 or 10^9 \n'
        help_scale_cmd += ' mega-    M      1 000 000 or 10^6 \n'
        help_scale_cmd += ' kilo-    k      1 000 or 10^3 \n'
        help_scale_cmd += ' deci-    d      0.1 or 1/10 or 10^-1 \n'
        help_scale_cmd += ' centi-   c      0.01 or 1/10 or 10^-2 \n'
        help_scale_cmd += ' milli-   m      0.001 or 1/10 or 10^-3 \n'
        help_scale_cmd += ' micro-   µ      0.000 001 or 1/10 or 10^-6 \n'
        help_scale_cmd += ' nano-    n      1/1 000 000 000 or 10^-9 \n'
        help_scale_cmd += ' pico-    p      1/1 000 000 000 000 or 10^-12'
        return ''.join(help_scale_cmd)