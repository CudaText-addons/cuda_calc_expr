import math
from cudatext import *

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
    }

def do_eval(s):
    r = eval(s, {"__builtins__": None}, safe_dict)
    return str(r)


class Command:
    def replace(self):
        self.do_work('rep')

    def show(self):
        self.do_work('show')

    def do_work(self, mode):

        carets = ed.get_carets()
        if len(carets)>1:
            msg_status('[Calc Expression] Multi-carets not supported')
            return

        s = ed.get_text_sel()
        if not s: return

        try:
            s = do_eval(s)
        except:
            msg_status('[Calc Expression] Cannot evaluate')
            return

        if mode=='rep':
            #sort coord
            x0, y0, x1, y1 = carets[0]
            if (y0, x0)>(y1, x1):
                x0, y0, x1, y1 = x1, y1, x0, y0

            ed.set_caret(x0, y0)
            ed.replace(x0, y0, x1, y1, s)
            msg_status('[Calc Expression] Replaced to: %s' %s)

        if mode=='show':
            msg_status('[Calc Expression] Result: %s' %s)
