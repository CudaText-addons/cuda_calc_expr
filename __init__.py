import os
import math
import statistics
from cudatext import *
from cudax_lib import get_translation

_   = get_translation(__file__)  # I18N

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'plugins.ini')
fn_section = 'calc_expression'
sep_dec = '.'
sep_th = ''
sep_list = ','
digits_count = 4

safe_dict = {
    'acos': math.acos,
    'asin': math.asin,
    'atan': math.atan,
    'atan2': math.atan2,
    'ceil': math.ceil,
    'cos': math.cos,
    'cosh': math.cosh,
    'degrees': math.degrees,
    'e': math.e,
    'exp': math.exp,
    'fabs': math.fabs,
    'floor': math.floor,
    'fmod': math.fmod,
    'frexp': math.frexp,
    'hypot': math.hypot,
    'ldexp': math.ldexp,
    'log': math.log,
    'log10': math.log10,
    'modf': math.modf,
    'pi': math.pi,
    'pow': math.pow,
    'radians': math.radians,
    'sin': math.sin,
    'sinh': math.sinh,
    'sqrt': math.sqrt,
    'tan': math.tan,
    'tanh': math.tanh,
    'abs': abs,
    'min': min,
    'max': max,
    'sum': sum,
    'mean': statistics.mean,
    'median': statistics.median,
    }

def do_eval(s):
    r = eval(s, {"__builtins__": None}, safe_dict)
    if r:
        return str(r)


class Command:

    def __init__(self):
        global sep_dec
        global sep_th
        global sep_list
        global digits_count
        sep_dec = ini_read(fn_config, fn_section, 'decimal_separator', sep_dec)
        sep_th = ini_read(fn_config, fn_section, 'thousand_separator', sep_th)
        sep_list = ini_read(fn_config, fn_section, 'list_separator', sep_list)
        digits_count = int(ini_read(fn_config, fn_section, 'digits_precision', str(digits_count)))

    def replace(self):
        self.do_work('rep')

    def show(self):
        self.do_work('show')

    def ins_sel(self):
        self.do_work('ins_sel')

    def do_work(self, mode):

        carets = ed.get_carets()
        if len(carets)>1:
            msg_status(_('[Calc Expression] Multi-carets not supported'))
            return

        s = ed.get_text_sel()
        if not s: return

        if sep_dec!='':
            s = s.replace(sep_dec, chr(1))
        if sep_th!='':
            s = s.replace(sep_th, chr(2))
        if sep_list!='':
            s = s.replace(sep_list, chr(3))
        s = s.replace(chr(1), '.')
        s = s.replace(chr(2), '')
        s = s.replace(chr(3), ',')

        try:
            s = do_eval(s)
        except Exception as e:
            msg_status(_('[Calc Expression] ')+str(e))
            return

        try:
            n = float(s) # check is it number
        except:
            msg_status(_('[Calc Expression] Not a number result'))
            return

        if sep_th:
            if digits_count > 0:
                s = ('{:,.'+str(digits_count)+'f}').format(n)
            else:
                s = '{:,}'.format(n)
            s = s.replace(',', chr(1))
        else:
            if digits_count > 0:
                s = ('{:.'+str(digits_count)+'f}').format(n)

        if sep_dec:
            s = s.replace('.', chr(2))

        s = s.replace(chr(1), sep_th)
        s = s.replace(chr(2), sep_dec)


        if mode=='rep':
            #sort coord
            x0, y0, x1, y1 = carets[0]
            if (y0, x0)>(y1, x1):
                x0, y0, x1, y1 = x1, y1, x0, y0

            ed.set_caret(x0, y0)
            ed.replace(x0, y0, x1, y1, s)
            msg_status(_('[Calc Expression] Replaced to: %s') %s)

        if mode=='show':
            msg_status(_('[Calc Expression] Result: %s') %s)

        if mode=='ins_sel':
            #sort coord
            x0, y0, x1, y1 = carets[0]
            if (y0, x0)>(y1, x1):
                x0, y0, x1, y1 = x1, y1, x0, y0

            ed.insert(x1, y1, ' = ' + s)
            ed.set_sel_rect(x1 + 3, y1, x1 + 3 + len(s), y1)
            msg_status(_('[Calc Expression] Calculated to: %s') %s)

    def config(self):
        ini_write(fn_config, fn_section, 'decimal_separator', sep_dec)
        ini_write(fn_config, fn_section, 'thousand_separator', sep_th)
        ini_write(fn_config, fn_section, 'list_separator', sep_list)
        ini_write(fn_config, fn_section, 'digits_precision', str(digits_count))
        file_open(fn_config)
