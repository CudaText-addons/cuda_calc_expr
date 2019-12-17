plugin for CudaText.
reads selected text as math expression, e.g. "2.4*sin(pi/3)" and evaluates it by Python.
tries to use "safe evaluation", without dangerous python functions enabled.
gives commands (menu Plugins / Calc Expression) to replace selection with number result,
or just show the result in the statusbar.

these Python functions are supported:

  abs      cosh       frexp      pow
  acos     degrees    hypot      radians
  asin     e          ldexp      sin
  atan     exp        log        sinh
  atan2    fabs       log10      sqrt
  ceil     floor      modf       tan
  cos      fmod       pi         tanh

  min(x1, x2, ...)
  max(x1, x2, ...)
  sum( [x1, x2, ...] )
  mean( [x1, x2, ...] )
  median( [x1, x2, ...] )

details:
https://docs.python.org/3/library/math.html
https://docs.python.org/3/library/statistics.html

plugin has config file, call menu item "Options / Settings-plugins / Calc Expression / Config".
it has separator options:
  [calc_expression]
  decimal_separator=.
  thousand_separator=
  list_separator=,

decimal_separator can be changed to e.g. "," or another.
thousand_separator can be set to non-empty, it will be skipped by Python anyway.
list_separator is used in functions with several arguments, e.g. min, max, mean.


author: Alexey Torgashin (CudaText)
license: MIT
