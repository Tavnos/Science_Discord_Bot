import random as rd
import discord
import time
import p_dt, t_dt, d_c, c_cl, l_loc, o_mt, z_fd

c_pdat , c_tdat , c_cdat , c_clc , c_loc , out_m , c_z = p_dt.P_Dat(), t_dt.T_Dat(), d_c.C_Dat(), c_cl.Cl_Ca(), l_loc.Loc_D(), o_mt.Mt_Out(), z_fd.Z_Dr()
client = discord.Client()
new_upt = time.time()

try:
    c_loc.init_ls_list()
    print('file found, users initialized')
except FileNotFoundError:
    c_loc.make_user_file()
    print('file not found, new file created')


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        channel = message.channel
        msg = '{}'.format(out_m.get_help())
        await channel.send(msg)
    elif message.content.startswith('!helplang'):
        channel = message.channel
        msg = '{}'.format(out_m.get_lang())
        await channel.send(msg)
    elif message.content.startswith('!mmd '): 
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!mmd ','')
        msg = str(c_cdat.t_mass(new_str)[0]) + ' g/mol'
        await channel.send(msg)
    elif message.content.startswith('!mma '): 
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!mma ','')
        msg = str(c_cdat.t_mass(new_str)[1])
        await channel.send(msg)
    elif message.content.startswith('!trs '): 
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!trs ','')
        msg = c_tdat.p_tr(new_str, 3)
        await channel.send(msg)
    elif message.content.startswith('!trd '):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!trd ','')
        msg = c_tdat.p_tr(new_str, 2)
        await channel.send(msg)
    elif message.content.startswith('!tra '):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!tra ','')
        msg = c_tdat.p_tr(new_str, 1)
        await channel.send(msg)
    elif message.content.startswith('!prs'): 
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!prs ','')
        new_ls = new_str.split()
        msg = c_pdat.p_seq(new_ls[0], new_ls[1], 3)
        await channel.send(msg)
    elif message.content.startswith('!prd'): 
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!prd ','')
        new_ls = new_str.split()
        msg = c_pdat.p_seq(new_ls[0], new_ls[1], 2)
        await channel.send(msg)
    elif message.content.startswith('!pra'): 
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!pra ','')
        new_ls = new_str.split()
        msg = c_pdat.p_seq(new_ls[0], new_ls[1], 1)
        await channel.send(msg)
    elif message.content.startswith('!gupt'):
        channel = message.channel
        msg = 'I have been running for {} seconds'.format(c_clc.get_uptime())
        await channel.send(msg)
    elif message.content.startswith('!scale'):
        channel = message.channel
        msg = '{}'.format(out_m.get_scale())
        await channel.send(msg)
    elif message.content.startswith('!km2m'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!km2m ','')
        msg = '{} Kilometer is {} Miles'.format(float(new_str), c_clc.km_miles(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!m2km'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!m2km ','')
        msg = '{} Miles is {} Kilometer'.format(float(new_str), c_clc.miles_km(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!f2m'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!f2m ','')
        msg = '{} Feet is {} Meter'.format(float(new_str), c_clc.feet_meter(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!m2f'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!m2f ','')
        msg = '{} Meter is {} Feet'.format(float(new_str), c_clc.meter_feet(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!m2i'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!m2i ','')
        msg = '{} Meter is {} Inch'.format(float(new_str), c_clc.inch_meter(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!i2m'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!i2m ','')
        msg = '{} Inch is {} Meter'.format(float(new_str), c_clc.inch_meter(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!kg2p'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!kg2p ','')
        msg = '{} Kilogram is {} Pound'.format(float(new_str), c_clc.kilo_pound(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!p2kg'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!p2kg ','')
        msg = '{} Pound is {} Kilogram'.format(float(new_str), c_clc.pound_kilo(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!k2c'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!k2c ','')
        msg = '{} Kelvin is {} Celcius'.format(float(new_str), c_clc.kelvin_celcius(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!c2k'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!c2k ','')
        msg = '{} Celcius is {} Kelvin'.format(float(new_str), c_clc.celcius_kelvin(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!f2c'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!f2c ','')
        msg = '{} Farenheit is {} Celcius'.format(float(new_str), c_clc.farhenheit_celcius(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!c2f'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!c2f ','')
        msg = '{} Celcius is {} Farenheit'.format(float(new_str), c_clc.celcius_farhenheit(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!k2f'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!k2f ','')
        msg = '{} Kelvin is {} Farenheit'.format(float(new_str), c_clc.kelvin_farhenheit(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!f2k'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!f2k ','')
        msg = '{} Farenheit is {} Kelvin'.format(float(new_str), c_clc.farhenheit_kelvin(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!convert'): 
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!convert ','')
        new_ls = new_str.split()
        msg = c_clc.init_conv_dict(new_ls[0], new_ls[1], new_ls[2])
        await channel.send(msg)
    elif message.content.startswith('!translate'): 
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!translate ','')
        new_ls = new_str.split(" ")
        hot_str = " ".join(new_ls[2::])
        msg = c_clc.get_translation(new_ls[0], new_ls[1], hot_str)
        await channel.send(msg)
    elif message.content.startswith('!vo2a'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!vo2a ','')
        new_ls = new_str.split(' ')
        result = c_clc.volt_ohm_to_amp(float(new_ls[0]),float(new_ls[1]))
        msg = '{} Volt / {} Ohm = {} Amp'.format(new_ls[0],new_ls[1], result)
        await channel.send(msg)    
    elif message.content.startswith('!va2o'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!va2o ','')
        new_ls = new_str.split(' ')
        result = c_clc.volt_amp_to_ohm(float(new_ls[0]),float(new_ls[1]))
        msg = '{} Volt / {} Amp = {} Ohm'.format(new_ls[0],new_ls[1], result)
        await channel.send(msg)    
    elif message.content.startswith('!oa2v'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!oa2v ','')
        new_ls = new_str.split(' ')
        result = c_clc.ohm_amp_to_volt(float(new_ls[0]),float(new_ls[1]))
        msg = '{} Ohm * {} Amp = {} Volt'.format(new_ls[0],new_ls[1], result)
        await channel.send(msg)
    elif message.content.startswith('!est'):
        channel = message.channel
        eastern_time = c_clc.get_est_time()
        msg = 'Eastern Standard Time: \n{}'.format(eastern_time)
        await channel.send(msg)
    elif message.content.startswith('!linkjc'):
        channel = message.channel
        msg = '{}'.format(out_m.get_journal_club())
        await channel.send(msg)
    elif message.content.startswith('!linkpc'):
        channel = message.channel
        msg = '{}'.format(out_m.get_plasmid_club())
        await channel.send(msg)
    elif message.content.startswith('!linkab'):
        channel = message.channel
        msg = '{}'.format(out_m.get_algae_brew())
        await channel.send(msg)
    elif message.content.startswith('!subjc'):
        channel = message.channel
        msg = '{}'.format(out_m.get_jc_library())
        await channel.send(msg)
    elif message.content.startswith('!matpc'):
        channel = message.channel
        msg = '{}'.format(out_m.get_pc_library())
        await channel.send(msg)
    elif message.content.startswith('!linklib'):
        channel = message.channel
        msg = '{}'.format(out_m.get_library())
        await channel.send(msg)
    elif message.content.startswith('!jcgm'):
        channel = message.channel
        msg = '{}'.format(c_clc.jc_date_time)
        await channel.send(msg)    
    elif message.content.startswith('!pcgm'):
        channel = message.channel
        msg = '{}'.format(c_clc.pc_date_time)
        await channel.send(msg)
    elif message.content.startswith('!abgm'):
        channel = message.channel
        msg = '{}'.format(c_clc.ab_date_time)
        await channel.send(msg)
    elif message.content.startswith('!setnote'):
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!setnote ','')
        if author_str in c_loc.ls_read:
            c_loc.store_note(author_str, new_str)
            msg = 'Done.'.format(message.author.mention)
        else:
            c_loc.add_user(author_str)
            c_loc.store_note(author_str, new_str)
            msg = 'Nice to meet you {}, personal note saved.'.format(message.author.mention)
        await channel.send(msg)
    elif message.content.startswith('!resetnote'):
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        channel = message.channel
        if author_str in c_loc.ls_read:
            c_loc.reset_note(author_str)
            msg = 'Done.'.format(message.author.mention)
        else:
            c_loc.add_user(author_str)
            msg = 'No personal note saved'.format(message.author.mention)
        await channel.send(msg)
    elif message.content.startswith('!getnote'):
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        channel = message.channel
        if author_str in c_loc.ls_read:
            usr_note = c_loc.get_note(author_str)
            msg = '{}'.format(usr_note)
        else:
            c_loc.add_user(author_str)
            msg = 'I was unable to find your note'.format(message.author.mention)
        await channel.send(msg)
    elif message.content.startswith('!rawr'):
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        channel = message.channel
        msg = '{} {}'.format(out_m.get_rawr(), message.author.mention)
        if author_str in c_loc.ls_read:
            pass
        else:
            c_loc.add_user(author_str)
            msg = 'Well met {}!'.format(message.author.mention)+ '\n' + msg
        await channel.send(msg)
    elif message.content.startswith('!plot'):  
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!plot ','')
        new_ls = new_str.split(',')
        msg = c_clc.graph(int(new_ls[0]),int(new_ls[1]),new_ls[2])
        await channel.send(file = discord.File('Science_Discord_Bot/plotimg/imgraph.png'))
    elif message.content.startswith('!gmeme'):  
        channel = message.channel
        meme_str = ''.join(rd.choices(('meme1','meme2','meme3','meme4', 'meme5')))
        await channel.send(file = discord.File('Science_Discord_Bot/{}.jpg'.format(meme_str)))
    elif message.content.startswith('!trivia'):
        channel = message.channel
        meme_str = ''.join(rd.choices(('trivia1','trivia2','trivia3','trivia4')))
        await channel.send(file = discord.File('Science_Discord_Bot/{}.jpg'.format(meme_str)))
    elif message.content.startswith('!ggif'):
        channel = message.channel
        gif_str = ''.join(rd.choices(('rqyzSsF','JklBVCo','QF0tMXA')))
        msg = 'https://imgur.com/gallery/{}'.format(gif_str)
        await channel.send(msg)
    elif message.content.startswith('!friends'):
        channel = message.channel
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        if author_str == c_loc.ls_read[0]:
            msg = '{}'.format(c_loc.display_user_file())
            await channel.send(msg)
    elif message.content.startswith('!setjc'):
        channel = message.channel
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        if author_str == c_loc.ls_read[0]:
            new_str = message.content
            new_str = new_str.replace('!setjc ','')
            c_clc.jc_date_time = new_str
            msg = 'Journal Club Message set to: {}'.format(new_str)
            await channel.send(msg)    
    elif message.content.startswith('!setpc'):
        channel = message.channel
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        if author_str == c_loc.ls_read[0]:
            new_str = message.content
            new_str = new_str.replace('!setpc ','')
            c_clc.pc_date_time = new_str
            msg = 'Plasmid Club Message set to: {}'.format(new_str)
            await channel.send(msg)
    elif message.content.startswith('!setab'):
        channel = message.channel
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        if author_str == c_loc.ls_read[1] or author_str == c_loc.ls_read[0]:
            new_str = message.content
            new_str = new_str.replace('!setab ','')
            c_clc.ab_date_time = new_str
            msg = 'Algae Brew message set to: {}'.format(new_str)
            await channel.send(msg)
    elif message.content.startswith('!gsrc'):
        channel = message.channel
        author_str = message.author.mention
        author_str = author_str.replace('<', '')
        author_str = author_str.replace('>', '')
        if author_str == c_loc.ls_read[0]:
            c_z.z_f()
            await channel.send(file = discord.File('Science_Discord_Bot/source.zip'))


@client.event
async def on_ready():
    print('Funcky parmesan cheese')
    print(client.user.name)
    print(client.user.id)
    print('-------------')



client.run('')