import d_c
import random as rd

c_data = d_c.C_Dat

class P_Dat(c_data):
    def g_spec(self, codon_config, desired_content):
        self.rd_set_ls = []
        self.index_max_ls = []
        self.codon_pref_ls = []
        if desired_content != 'any':
            for i in codon_config:
                self.rd_set_ls += [(i.count(desired_content[0])+i.count(desired_content[1]))]
            for i in range(len(self.rd_set_ls)):
                if self.rd_set_ls[i] == max(self.rd_set_ls):
                    self.index_max_ls += [i]
            for i in self.index_max_ls:
                self.codon_pref_ls += [codon_config[i]]
        if desired_content == 'any':
            self.codon_pref_ls = codon_config
        return rd.choice(self.codon_pref_ls)
    def p_seq(self, sequence_typed, desired_content, info_level=1):
        self.possible_config = []
        self.cg_count = 0
        self.at_count = 0
        for i in sequence_typed:
            self.temp_config = self.a_stat[i]['cd']
            self.possible_config += [self.g_spec(self.temp_config, desired_content)]
        self.predict_1 = "sequence typed:"
        self.predict_1_1 = (''.join(sequence_typed))
        self.predict_2 = "desired config:"
        self.predict_2_1 = ''.join(self.possible_config)
        self.chr_split = []
        for i in self.predict_2_1:
            self.chr_split += i
        self.cg_count = self.chr_split.count('c') + self.chr_split.count('g')
        self.at_count = self.chr_split.count('a') + self.chr_split.count('t')
        self.predict_3 = '{} % gc'.format((self.cg_count/len(self.chr_split))*100)
        self.predict_3_1 = '{} % at'.format((self.at_count/len(self.chr_split))*100)
        if info_level == 1:
            return '{}\n{}\n{}\n{}\n{}\n{}'.format(self.predict_1, self.predict_1_1, self.predict_2, self.predict_2_1, self.predict_3, self.predict_3_1)
        if info_level == 2:
            return '{}\n{}\n{}'.format(self.predict_2_1, self.predict_3, self.predict_3_1)
        if info_level == 3:
            return '{}'.format(self.predict_2_1)