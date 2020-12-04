import d_c

c_data = d_c.C_Dat

class T_Dat(c_data):
    def t_nuc(self, str_input):
        self.dna_typed_ls = []
        self.rna_typed_ls = []
        self.amino_short_ls = []
        self.amino_abv_ls = []
        self.amino_aerobic_atp_ls = []
        self.amino_anaerobic_atp_ls = []
        self.amino_side_chain_ls = []
        self.nuc_transcript = str_input.lower()
        for i in self.nuc_transcript:
            self.dna_typed_ls += self.n_tr[i]['dna']
            self.rna_typed_ls += self.n_tr[i]['rna']
        self.dna_direct_str = ''.join(self.dna_typed_ls)
        self.rna_direct_str = ''.join(self.rna_typed_ls)
        for i in range(0, len(self.dna_direct_str), 3):
            for f in self.a_stat:
                if self.dna_direct_str[i:i+3] in self.a_stat[f]['cd']:
                    self.amino_short_ls += f
                    self.amino_abv_ls += self.a_stat[f]['abv']
                    self.amino_aerobic_atp_ls += [self.a_stat[f]['atp'][0]]
                    self.amino_anaerobic_atp_ls += [self.a_stat[f]['atp'][1]]
                    self.amino_side_chain_ls += [self.a_stat[f]['s_c']]
        self.amino_short_str = ''.join(self.amino_short_ls)
        self.amino_abv_str = ''.join(self.amino_abv_ls)
        self.amino_aerobic_atp_tot = sum(self.amino_aerobic_atp_ls)
        self.amino_anaerobic_atp_tot = sum(self.amino_anaerobic_atp_ls)
        self.amino_side_chain_str = '/'.join(self.amino_side_chain_ls)
    def p_tr(self, str_input, info_level=1):
        self.t_nuc(str_input)
        self.str_var_0 = self.amino_short_str
        self.str_var_1 = 'DNA: ' + self.dna_direct_str.upper()
        self.str_var_2 = 'RNA: ' + self.rna_direct_str.upper()
        self.str_var_3 = 'Short: ' + self.amino_short_str
        self.str_var_4 = 'Abbreviated: ' 
        self.str_var_5 = self.amino_abv_str
        self.str_var_6 = 'aerobic: ' + str(self.amino_aerobic_atp_tot) + ' ATP'
        self.str_var_7 = 'anaerobic: ' + str(self.amino_anaerobic_atp_tot) + ' ATP'
        self.str_var_8 = 'mass: ' + "{}".format(self.a_mass(self.amino_short_str)) + ' g/mol'
        self.str_var_9 = 'sidechain functional group:'
        self.str_var_10 = self.amino_side_chain_str 
        if info_level==1:
            return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(self.str_var_1, self.str_var_2, self.str_var_3, self.str_var_4, 
                 self.str_var_5, self.str_var_6, self.str_var_7, self.str_var_8, self.str_var_9, self.str_var_10) 
        if info_level==2:
            return '{}\n{}\n{}\n{}'.format(self.str_var_3, self.str_var_6, self.str_var_7, self.str_var_8) 
        if info_level==3:
            return '{}'.format(self.str_var_0)