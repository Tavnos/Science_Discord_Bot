class Loc_D:
    ls_read = []
    def init_ls_list(self):
        save_txt = open('user_list.txt', 'r')
        str_read = save_txt.read()
        save_txt.close()
        str_read = str_read
        self.ls_read = str_read.split()
    def make_user_file(self):
        save_txt = open('user_list.txt', 'w')
        txt_nrw = ''
        save_txt.write(txt_nrw)
        save_txt.close()
    def add_user(self, username):
        username = username.replace('<','')
        username = username.replace('>','')
        save_txt = open('user_list.txt', 'r')
        str_read = save_txt.read()
        save_txt.close()
        str_read = str_read + '\n' + username
        self.ls_read = str_read.split()
        save_txt = open('user_list.txt', 'w')
        save_txt.write(str_read)
        save_txt.close()
        save_usr_txt = open('{}.txt'.format(username), 'w')
        usr_txt_nrw = 'personal note:'
        save_usr_txt.write(usr_txt_nrw)
        save_usr_txt.close()
    def display_user_file(self):
        save_txt = open('user_list.txt', 'r')
        str_read = save_txt.read()
        ls_read = str_read.split()
        u_read = ''
        for i in ls_read:
            u_read += "<{}> \n".format(i)
        return u_read
    def display_user_file_list(self):
        save_txt = open('user_list.txt', 'r')
        str_read = save_txt.read()
        ls_read = str_read.split()
        u_read = []
        for i in ls_read:
            u_read += ["{}".format(i)]
        return u_read
    def store_note(self, username, d_note):
        username = username.replace('<','')
        username = username.replace('>','')
        if username in self.ls_read:
            save_usr_txt = open('{}.txt'.format(username), 'r')
            save_usr_str_read = save_usr_txt.read()
            save_usr_txt.close()
            save_usr_str_read = save_usr_str_read + '\n' + d_note
            save_usr_txt = open('{}.txt'.format(username), 'w')
            save_usr_txt.write(save_usr_str_read)
            save_usr_txt.close()
    def get_note(self, username):
        username = username.replace('<','')
        username = username.replace('>','')
        if username in self.ls_read:
            save_usr_txt = open('{}.txt'.format(username), 'r')
            save_usr_str_read = save_usr_txt.read()
            save_usr_txt.close()
            return save_usr_str_read
    def reset_note(self, username):
        username = username.replace('<','')
        username = username.replace('>','')
        if username in self.ls_read:
            save_usr_txt = open('{}.txt'.format(username), 'w')
            usr_txt_nrw = 'personal note:'.format(username)
            save_usr_txt.write(usr_txt_nrw)
            save_usr_txt.close()