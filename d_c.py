import m_d


data_var = m_d.Method_Data

class C_Dat(data_var):
    def t_mass(self, compound):
        self.detail_d = {}
        self.out_ls = []
        temp_v = compound.split()
        for i in range(int(len(temp_v)/2)):
            self.out_ls += [(self.e_mass[temp_v[i+i]])*float(temp_v[i+i+1])]
            self.detail_d['total'] = sum(self.out_ls)
            self.detail_d[temp_v[i+i]] = {'ammount':temp_v[i+i+1], 'g/m':self.e_mass[temp_v[i+i]], 'result':(self.e_mass[temp_v[i+i]])*float(temp_v[i+i+1])}
        return (sum(self.out_ls), self.detail_d)
    def a_mass(self, p_name):
        mass_ls = []
        for i in p_name:
            if i in self.a_stat:
                mass_ls+= [self.t_mass(self.a_stat[i]['ef'])[0]]
        mass_ls += [self.t_mass('H 2 O 1')[0]]
        return sum(mass_ls)