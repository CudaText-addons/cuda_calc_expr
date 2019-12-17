plugin for CudaText.
reads selected text as math expression, e.g. "2.4*sin(pi/3)" and evaluates it by Python.
tries to use "safe evaluation", without dangerous python functions enabled.
gives commands (menu Plugins / Calc Expression) to replace selection with number result,
or just show the result in the statusbar.
these math functions from Python are supported:

  abs      cosh       frexp      pow
  acos     degrees    hypot      radians
  asin     e          ldexp      sin
  atan     exp        log        sinh
  atan2    fabs       log10      sqrt
  ceil     floor      modf       tan
  cos      fmod       pi         tanh

details about those functions:
https://docs.python.org/3/library/math.html

author: Alexey Torgashin (CudaText)
license: MIT
