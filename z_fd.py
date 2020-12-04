import os
import zipfile


class Z_Dr:
    def z_f(self):
        remove_var =  "client.run"
        index_var = int
        r_fl = open('Science_Discord_Bot/source.py', 'r')
        str_r = r_fl.read()
        r_fl.close()
        ls_r = str_r.split('\n')
        for i in ls_r:
            if remove_var in i:
                index_var = ls_r.index(i)
        ls_r.remove(ls_r[index_var])
        ls_r += ["client.run('')"]
        new_str = '\n'.join(ls_r)
        r_fl = open('Science_Discord_Bot/source.py', 'w')
        r_fl.write(new_str)
        r_fl.close()
        ls_dir_raw = os.listdir('Science_Discord_Bot/')
        ls_dir_py = []
        for i in ls_dir_raw:
            if '.py' in i:
                ls_dir_py += ['Science_Discord_Bot/{}'.format(i)]
        zip_f = zipfile.ZipFile('Science_Discord_Bot/source.zip', 'w')
        for i in ls_dir_py:
            zip_f.write('{}'.format(i))
        zip_f.close()