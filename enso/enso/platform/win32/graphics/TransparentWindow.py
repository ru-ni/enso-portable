# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_TransparentWindow')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_TransparentWindow')
    _TransparentWindow = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TransparentWindow', [dirname(__file__)])
        except ImportError:
            import _TransparentWindow
            return _TransparentWindow
        try:
            _mod = imp.load_module('_TransparentWindow', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _TransparentWindow = swig_import_helper()
    del swig_import_helper
else:
    import _TransparentWindow
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

BITS_PER_PIXEL = _TransparentWindow.BITS_PER_PIXEL
BYTES_PER_PIXEL = _TransparentWindow.BYTES_PER_PIXEL
MAX_OPACITY = _TransparentWindow.MAX_OPACITY
class TransparentWindowError(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TransparentWindowError, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TransparentWindowError, name)
    __repr__ = _swig_repr

    def __init__(self, what):
        this = _TransparentWindow.new_TransparentWindowError(what)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def what(self):
        return _TransparentWindow.TransparentWindowError_what(self)
    __swig_destroy__ = _TransparentWindow.delete_TransparentWindowError
    __del__ = lambda self: None
TransparentWindowError_swigregister = _TransparentWindow.TransparentWindowError_swigregister
TransparentWindowError_swigregister(TransparentWindowError)

class FatalError(TransparentWindowError):
    __swig_setmethods__ = {}
    for _s in [TransparentWindowError]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FatalError, name, value)
    __swig_getmethods__ = {}
    for _s in [TransparentWindowError]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, FatalError, name)
    __repr__ = _swig_repr

    def __init__(self, what):
        this = _TransparentWindow.new_FatalError(what)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _TransparentWindow.delete_FatalError
    __del__ = lambda self: None
FatalError_swigregister = _TransparentWindow.FatalError_swigregister
FatalError_swigregister(FatalError)

class RangeError(TransparentWindowError):
    __swig_setmethods__ = {}
    for _s in [TransparentWindowError]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RangeError, name, value)
    __swig_getmethods__ = {}
    for _s in [TransparentWindowError]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RangeError, name)
    __repr__ = _swig_repr

    def __init__(self, what):
        this = _TransparentWindow.new_RangeError(what)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _TransparentWindow.delete_RangeError
    __del__ = lambda self: None
RangeError_swigregister = _TransparentWindow.RangeError_swigregister
RangeError_swigregister(RangeError)

class TransparentWindow(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TransparentWindow, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TransparentWindow, name)
    __repr__ = _swig_repr

    def __init__(self, x, y, maxWidth, maxHeight):
        this = _TransparentWindow.new_TransparentWindow(x, y, maxWidth, maxHeight)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _TransparentWindow.delete_TransparentWindow
    __del__ = lambda self: None

    def update(self):
        return _TransparentWindow.TransparentWindow_update(self)

    def setOpacity(self, opacity):
        return _TransparentWindow.TransparentWindow_setOpacity(self, opacity)

    def getOpacity(self):
        return _TransparentWindow.TransparentWindow_getOpacity(self)

    def setPosition(self, x, y):
        return _TransparentWindow.TransparentWindow_setPosition(self, x, y)

    def getX(self):
        return _TransparentWindow.TransparentWindow_getX(self)

    def getY(self):
        return _TransparentWindow.TransparentWindow_getY(self)

    def setSize(self, width, height):
        return _TransparentWindow.TransparentWindow_setSize(self, width, height)

    def getWidth(self):
        return _TransparentWindow.TransparentWindow_getWidth(self)

    def getHeight(self):
        return _TransparentWindow.TransparentWindow_getHeight(self)

    def getMaxWidth(self):
        return _TransparentWindow.TransparentWindow_getMaxWidth(self)

    def getMaxHeight(self):
        return _TransparentWindow.TransparentWindow_getMaxHeight(self)

    def makeCairoSurface(self):
        return _TransparentWindow.TransparentWindow_makeCairoSurface(self)
TransparentWindow_swigregister = _TransparentWindow.TransparentWindow_swigregister
TransparentWindow_swigregister(TransparentWindow)


def _getDesktopSize():
    return _TransparentWindow._getDesktopSize()
_getDesktopSize = _TransparentWindow._getDesktopSize

def _getDesktopOffset():
    return _TransparentWindow._getDesktopOffset()
_getDesktopOffset = _TransparentWindow._getDesktopOffset
# This file is compatible with both classic and new-style classes.


