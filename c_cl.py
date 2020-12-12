from pandas import DataFrame as df
import matplotlib.pyplot as plt
import primes_list
import numpy as np
import translate
import time 
import re

pot = primes_list.primesofthousands

class Cl_Ca:
    str_id = 'EUR, USD, JPY, BGN, CZK, DKK, GBP, HUF, PLN, RON, SEK, CHF, ISK, NOK, HRK, RUB, TRY, AUD, BRL, CAD, CNY, HKD, IDR, ILS, INR, KRW, MXN, MYR, NZD, PHP, SGD, THB, ZAR'
    set_val = [1, 1.2159, 126.44, 1.9558, 26.518, 7.4429, 0.90282, 358.57, 4.4769, 4.8725, 10.2578, 1.0822, 152.10, 10.6598, 7.5415, 90.0679, 9.4636, 1.6387, 6.2759, 1.5633, 7.9421, 9.4240, 17222.37, 3.9720, 89.6755, 1320.60, 24.1091, 4.9366, 1.7254, 58.430, 1.6206, 36.672, 18.4674]
    def get_est_time(self):
        tim_fx = time.asctime()  
        calced_time = int(tim_fx.split()[3][0:2])-5
        the_time = tim_fx.split()[3][0:2]   
        the_date = tim_fx.split()[2][0:2]
        if calced_time >= 0:
            new_fx = str(calced_time)
            tim_fx = tim_fx.replace(the_time, new_fx)
        else:
            new_fx = str(24 + calced_time)
            tim_fx = tim_fx.replace(the_time, new_fx)
            tim_fx = tim_fx.replace(the_date, str(int(the_date)-1))
        return tim_fx
    def get_uptime(self):
        upt_int = time.time()
        uptime = abs(new_upt - upt_int)
        return '{}'.format(round(uptime, 2))
    def km_miles(self, kilometer):
        return round(kilometer * 0.621371, 4)
    def miles_km(self, miles):
        return round(miles / 0.621371, 4)
    def meter_feet(self, meter):
        return round(meter / 0.3048, 4)
    def feet_meter(self, feet):
        return round(feet * 0.3048, 4)
    def inch_meter(self, meter):
        return round(meter / 39.3701, 4)
    def meter_inch(self, inch):
        return round(inch * 39.3701, 4)
    def pound_kilo(self, pound):
        return round(pound * 0.453592, 4)
    def kilo_pound(self, kilo):
        return round(kilo / 0.453592, 4)
    def kelvin_celcius(self, kelvin):
        return round(kelvin-273.15, 4)
    def celcius_kelvin(self, celcius):
        return round(273.15+celcius, 4)
    def farhenheit_celcius(self, farhenheit):
        return round((farhenheit-32)/(9/5),4)
    def celcius_farhenheit(self, celcius):
        return round((celcius*(9/5))+32,4)
    def kelvin_farhenheit(self, kelvin):
        return round(self.celcius_farhenheit(self.kelvin_celcius(kelvin)), 4)
    def farhenheit_kelvin(self, farhenheit):
        return round(self.celcius_kelvin(self.farhenheit_celcius(farhenheit)), 4)
    def volt_ohm_to_amp(self, volt, ohm):
        return round(volt/ohm,6)
    def volt_amp_to_ohm(self, volt, amp):
        return round(volt/amp,6)
    def ohm_amp_to_volt(self, ohm, amp):
        return round(ohm*amp, 6)
    def f(self, function):
        return eval(function)
    def graph(self, xlim_a, xlim_b, function, tangent=None, ylim=None):
        dfp = df()
        dfp['x'] = np.arange(xlim_a,xlim_b,(xlim_b-xlim_a)/100)
        dfp['y'] = eval(function.replace('x', "dfp['x']"))
        dfp = dfp.set_index('x')
        dfp.y.plot(ylim=ylim)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.savefig('Science_Discord_Bot/plotimg/imgraph', dpi=80)
        plt.close()
    def generate_5_complex(self, value_1, value_2, value_3, value_4,value_5, 
                           t_range=2000, t_spread=1000, 
                           color_1='black',color_2='cyan', color_3='blue', color_4='red',color_5='yellow', 
                           size_1=60, size_2=40,size_3=25,size_4=15, size_5=5, 
                           alpha_1=0.25,alpha_2=0.25, alpha_3=0.25, alpha_4=0.25,alpha_5=0.25, 
                           offset_1=1.45, offset_2=1.49,offset_3=1.505,offset_4=1.535, offset_5=1.57, 
                           enable_1=109751, enable_2=139891,enable_3=65063,enable_4=30059, enable_5=209311):
        value_1, value_2, value_3, value_4, value_5 = pot[value_1],pot[value_2], pot[value_3], pot[value_4], pot[value_5]
        self.hot_ls=[]
        for i in range(12):
            self.hot_ls+=[[]]
        (eq_0_r, eq_1_r, eq_2_r, eq_3_r, eq_4_r, eq_5_r, 
            eq_0_i, eq_1_i, eq_2_i, eq_3_i, eq_4_i, eq_5_i) = self.hot_ls
        for i in range(t_range):
            eq_r1, eq_r2, eq_r3, eq_r4, eq_r5 = ((np.real(np.e**(1j*2*np.pi*(i/t_spread)*value_1))*enable_1),
                                                 (np.real(np.e**(1j*2*np.pi*(i/t_spread)*value_2))*enable_2),
                                                 (np.real(np.e**(1j*2*np.pi*(i/t_spread)*value_3))*enable_3),
                                                 (np.real(np.e**(1j*2*np.pi*(i/t_spread)*value_4))*enable_4),
                                                 (np.real(np.e**(1j*2*np.pi*(i/t_spread)*value_5))*enable_5))
            eq_0_r += [eq_r1+eq_r2+eq_r3+eq_r4+eq_r5]
            eq_i1, eq_i2, eq_i3, eq_i4, eq_i5 = ((np.imag(np.e**(1j*2*np.pi*(i/t_spread)*value_1))*enable_1),
                                                 (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*value_2))*enable_2),
                                                 (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*value_3))*enable_3),
                                                 (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*value_4))*enable_4),
                                                 (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*value_5))*enable_5))
            eq_0_i += [eq_i1+eq_i2+eq_i3+eq_i4+eq_i5]
        for i in range(int((len(eq_0_i)+len(eq_0_r))/2)):
            eq_1_r += [(eq_0_r[i])/(offset_1)]
            eq_1_i += [(eq_0_i[i])/(offset_1)]
            eq_2_r += [(eq_0_r[i])/(offset_2)]
            eq_2_i += [(eq_0_i[i])/(offset_2)]
            eq_3_r += [(eq_0_r[i])/(offset_3)]
            eq_3_i += [(eq_0_i[i])/(offset_3)]
            eq_4_r += [(eq_0_r[i])/(offset_4)]
            eq_4_i += [(eq_0_i[i])/(offset_4)]
            eq_5_r += [(eq_0_r[i])/(offset_5)]
            eq_5_i += [(eq_0_i[i])/(offset_5)]
        plt.axis('off')
        plt.scatter(eq_1_r,eq_1_i,s=size_1,alpha=alpha_1,c=color_1)
        plt.scatter(eq_2_r,eq_2_i,s=size_2,alpha=alpha_2,c=color_2)
        plt.scatter(eq_3_r,eq_3_i,s=size_3,alpha=alpha_3,c=color_3)
        plt.scatter(eq_4_r,eq_4_i,s=size_4,alpha=alpha_4,c=color_4)
        plt.scatter(eq_5_r,eq_5_i,s=size_5,alpha=alpha_5,c=color_5)
        plt.savefig('Science_Discord_Bot/plotimg/imgraphgui', dpi=80)
        plt.close()
    def init_conv_dict(self, start_id, start_val, desired_id):
        dict_conv = {}
        ls_id = self.str_id.split(', ')
        for i in range(len(ls_id)):
            dict_conv[ls_id[i]] = self.set_val[i]
        return '{} {} is {} {}'.format(start_val, start_id, str(round(dict_conv[desired_id]/(dict_conv[start_id]/float(start_val)),2)), desired_id)
    def get_translation(self, start_lang, desired_lang, txt_input):
        ls_input = re.findall('[A-Z][^A-Z]*', txt_input)
        hot_list = []
        r_l = translate.translator(start_lang, desired_lang, txt_input)
        for i in range(len(ls_input)):
            hot_list += [r_l[0][i][0]]
        hot_string = " ".join(hot_list)
        return "{}".format(hot_string)
