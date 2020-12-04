from pandas import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
import time 


class Cl_Ca:
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