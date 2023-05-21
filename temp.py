__all__ = ['temp']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['myFunction'])
@Js
def PyJsHoisted_myFunction_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['x'])
    var.put('x', var.get('document').callprop('getElementById', Js('myfile')).get('value'))
    var.get('console').callprop('log', var.get('x'))
    return var.get('x')
PyJsHoisted_myFunction_.func_name = 'myFunction'
var.put('myFunction', PyJsHoisted_myFunction_)
pass
pass


# Add lib to the module scope
temp = var.to_python()