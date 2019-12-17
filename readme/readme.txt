plugin for CudaText.
reads selected text as math expression, e.g. "2.4*sin(pi/3)" and evaluates it by Python.
tries to use "safe evaluation", without dangerous python functions enabled.
gives commands (menu Plugins / Calc Expression) to replace selection with number result,
or just show the result in the statusbar.
these math functions from Python are supported:

  abs           fabs           pi
  acos          floor          pow
  asin          fmod           radians
  atan          frexp          sin
  atan2         hypot          sinh
  ceil          ldexp          sqrt
  cos           log            tan
  cosh          log10          tanh
  degrees       modf
  e
  exp


details about those functions:
https://docs.python.org/3/library/math.html

author: Alexey Torgashin (CudaText)
license: MIT
