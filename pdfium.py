r"""Wrapper for fpdf_annot.h

Generated with:
/Users/thead/miniconda/envs/sk-playground/bin/ctypesgen -lpdfium -L /Users/thead/Downloads/pdfium-darwin/lib /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_catalog.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_flatten.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_javascript.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_ppo.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_searchex.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_thumbnail.h /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h -o PDFIUM.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}

HERE = os.path.dirname(os.path.abspath(__file__))
_libdirs = [HERE + '/lib']

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([HERE + '/lib'])

# Begin libraries
_libs["pdfium"] = load_library("pdfium")

# 1 libraries
# End libraries

# No modules

enum_anon_1 = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_UNKNOWN = (-1)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_FILL = 0# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_STROKE = 1# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_FILL_STROKE = 2# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_INVISIBLE = 3# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_FILL_CLIP = 4# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_STROKE_CLIP = 5# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_FILL_STROKE_CLIP = 6# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_CLIP = 7# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXTRENDERMODE_LAST = FPDF_TEXTRENDERMODE_CLIP# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

FPDF_TEXT_RENDERMODE = enum_anon_1# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 51

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 54
class struct_fpdf_action_t__(Structure):
    pass

FPDF_ACTION = POINTER(struct_fpdf_action_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 54

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 55
class struct_fpdf_annotation_t__(Structure):
    pass

FPDF_ANNOTATION = POINTER(struct_fpdf_annotation_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 55

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 56
class struct_fpdf_attachment_t__(Structure):
    pass

FPDF_ATTACHMENT = POINTER(struct_fpdf_attachment_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 56

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 57
class struct_fpdf_bitmap_t__(Structure):
    pass

FPDF_BITMAP = POINTER(struct_fpdf_bitmap_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 57

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 58
class struct_fpdf_bookmark_t__(Structure):
    pass

FPDF_BOOKMARK = POINTER(struct_fpdf_bookmark_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 58

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 59
class struct_fpdf_clippath_t__(Structure):
    pass

FPDF_CLIPPATH = POINTER(struct_fpdf_clippath_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 59

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 60
class struct_fpdf_dest_t__(Structure):
    pass

FPDF_DEST = POINTER(struct_fpdf_dest_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 60

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 61
class struct_fpdf_document_t__(Structure):
    pass

FPDF_DOCUMENT = POINTER(struct_fpdf_document_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 61

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 62
class struct_fpdf_font_t__(Structure):
    pass

FPDF_FONT = POINTER(struct_fpdf_font_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 62

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 63
class struct_fpdf_form_handle_t__(Structure):
    pass

FPDF_FORMHANDLE = POINTER(struct_fpdf_form_handle_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 63

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 64
class struct_fpdf_javascript_action_t(Structure):
    pass

FPDF_JAVASCRIPT_ACTION = POINTER(struct_fpdf_javascript_action_t)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 64

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 65
class struct_fpdf_link_t__(Structure):
    pass

FPDF_LINK = POINTER(struct_fpdf_link_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 65

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 66
class struct_fpdf_page_t__(Structure):
    pass

FPDF_PAGE = POINTER(struct_fpdf_page_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 66

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 67
class struct_fpdf_pagelink_t__(Structure):
    pass

FPDF_PAGELINK = POINTER(struct_fpdf_pagelink_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 67

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 68
class struct_fpdf_pageobject_t__(Structure):
    pass

FPDF_PAGEOBJECT = POINTER(struct_fpdf_pageobject_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 68

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 69
class struct_fpdf_pageobjectmark_t__(Structure):
    pass

FPDF_PAGEOBJECTMARK = POINTER(struct_fpdf_pageobjectmark_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 69

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 70
class struct_fpdf_pagerange_t__(Structure):
    pass

FPDF_PAGERANGE = POINTER(struct_fpdf_pagerange_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 70

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 71
class struct_fpdf_pathsegment_t(Structure):
    pass

FPDF_PATHSEGMENT = POINTER(struct_fpdf_pathsegment_t)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 71

FPDF_RECORDER = POINTER(None)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 72

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 73
class struct_fpdf_schhandle_t__(Structure):
    pass

FPDF_SCHHANDLE = POINTER(struct_fpdf_schhandle_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 73

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 74
class struct_fpdf_structelement_t__(Structure):
    pass

FPDF_STRUCTELEMENT = POINTER(struct_fpdf_structelement_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 74

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 75
class struct_fpdf_structtree_t__(Structure):
    pass

FPDF_STRUCTTREE = POINTER(struct_fpdf_structtree_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 75

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 76
class struct_fpdf_textpage_t__(Structure):
    pass

FPDF_TEXTPAGE = POINTER(struct_fpdf_textpage_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 76

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 77
class struct_fpdf_widget_t__(Structure):
    pass

FPDF_WIDGET = POINTER(struct_fpdf_widget_t__)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 77

FPDF_BOOL = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 80

FPDF_RESULT = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 81

FPDF_DWORD = c_ulong# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 82

FS_FLOAT = c_float# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 83

enum__FPDF_DUPLEXTYPE_ = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 91

DuplexUndefined = 0# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 91

Simplex = (DuplexUndefined + 1)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 91

DuplexFlipShortEdge = (Simplex + 1)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 91

DuplexFlipLongEdge = (DuplexFlipShortEdge + 1)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 91

FPDF_DUPLEXTYPE = enum__FPDF_DUPLEXTYPE_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 91

FPDF_WCHAR = c_ushort# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 94

FPDF_BYTESTRING = String# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 98

FPDF_WIDESTRING = POINTER(c_ushort)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 102

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 110
class struct_FPDF_BSTR_(Structure):
    pass

struct_FPDF_BSTR_.__slots__ = [
    'str',
    'len',
]
struct_FPDF_BSTR_._fields_ = [
    ('str', String),
    ('len', c_int),
]

FPDF_BSTR = struct_FPDF_BSTR_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 110

FPDF_STRING = String# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 119

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 136
class struct__FS_MATRIX_(Structure):
    pass

struct__FS_MATRIX_.__slots__ = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
]
struct__FS_MATRIX_._fields_ = [
    ('a', c_float),
    ('b', c_float),
    ('c', c_float),
    ('d', c_float),
    ('e', c_float),
    ('f', c_float),
]

FS_MATRIX = struct__FS_MATRIX_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 136

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 139
class struct__FS_RECTF_(Structure):
    pass

struct__FS_RECTF_.__slots__ = [
    'left',
    'top',
    'right',
    'bottom',
]
struct__FS_RECTF_._fields_ = [
    ('left', c_float),
    ('top', c_float),
    ('right', c_float),
    ('bottom', c_float),
]

FS_LPRECTF = POINTER(struct__FS_RECTF_)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 148

FS_RECTF = struct__FS_RECTF_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 148

FS_LPCRECTF = POINTER(FS_RECTF)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 151

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 154
class struct_FS_SIZEF_(Structure):
    pass

struct_FS_SIZEF_.__slots__ = [
    'width',
    'height',
]
struct_FS_SIZEF_._fields_ = [
    ('width', c_float),
    ('height', c_float),
]

FS_LPSIZEF = POINTER(struct_FS_SIZEF_)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 157

FS_SIZEF = struct_FS_SIZEF_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 157

FS_LPCSIZEF = POINTER(FS_SIZEF)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 160

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 163
class struct_FS_POINTF_(Structure):
    pass

struct_FS_POINTF_.__slots__ = [
    'x',
    'y',
]
struct_FS_POINTF_._fields_ = [
    ('x', c_float),
    ('y', c_float),
]

FS_LPPOINTF = POINTER(struct_FS_POINTF_)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 166

FS_POINTF = struct_FS_POINTF_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 166

FS_LPCPOINTF = POINTER(FS_POINTF)# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 169

FPDF_ANNOTATION_SUBTYPE = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 172

FPDF_ANNOT_APPEARANCEMODE = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 173

FPDF_OBJECT_TYPE = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 176

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 213
if _libs["pdfium"].has("FPDF_InitLibrary", "cdecl"):
    FPDF_InitLibrary = _libs["pdfium"].get("FPDF_InitLibrary", "cdecl")
    FPDF_InitLibrary.argtypes = []
    FPDF_InitLibrary.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 237
class struct_FPDF_LIBRARY_CONFIG_(Structure):
    pass

struct_FPDF_LIBRARY_CONFIG_.__slots__ = [
    'version',
    'm_pUserFontPaths',
    'm_pIsolate',
    'm_v8EmbedderSlot',
]
struct_FPDF_LIBRARY_CONFIG_._fields_ = [
    ('version', c_int),
    ('m_pUserFontPaths', POINTER(POINTER(c_char))),
    ('m_pIsolate', POINTER(None)),
    ('m_v8EmbedderSlot', c_uint),
]

FPDF_LIBRARY_CONFIG = struct_FPDF_LIBRARY_CONFIG_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 237

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 249
if _libs["pdfium"].has("FPDF_InitLibraryWithConfig", "cdecl"):
    FPDF_InitLibraryWithConfig = _libs["pdfium"].get("FPDF_InitLibraryWithConfig", "cdecl")
    FPDF_InitLibraryWithConfig.argtypes = [POINTER(FPDF_LIBRARY_CONFIG)]
    FPDF_InitLibraryWithConfig.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 262
if _libs["pdfium"].has("FPDF_DestroyLibrary", "cdecl"):
    FPDF_DestroyLibrary = _libs["pdfium"].get("FPDF_DestroyLibrary", "cdecl")
    FPDF_DestroyLibrary.argtypes = []
    FPDF_DestroyLibrary.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 275
if _libs["pdfium"].has("FPDF_SetSandBoxPolicy", "cdecl"):
    FPDF_SetSandBoxPolicy = _libs["pdfium"].get("FPDF_SetSandBoxPolicy", "cdecl")
    FPDF_SetSandBoxPolicy.argtypes = [FPDF_DWORD, FPDF_BOOL]
    FPDF_SetSandBoxPolicy.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 347
if _libs["pdfium"].has("FPDF_LoadDocument", "cdecl"):
    FPDF_LoadDocument = _libs["pdfium"].get("FPDF_LoadDocument", "cdecl")
    FPDF_LoadDocument.argtypes = [FPDF_STRING, FPDF_BYTESTRING]
    FPDF_LoadDocument.restype = FPDF_DOCUMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 371
if _libs["pdfium"].has("FPDF_LoadMemDocument", "cdecl"):
    FPDF_LoadMemDocument = _libs["pdfium"].get("FPDF_LoadMemDocument", "cdecl")
    FPDF_LoadMemDocument.argtypes = [POINTER(None), c_int, FPDF_BYTESTRING]
    FPDF_LoadMemDocument.restype = FPDF_DOCUMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 393
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'm_FileLen',
    'm_GetBlock',
    'm_Param',
]
struct_anon_2._fields_ = [
    ('m_FileLen', c_ulong),
    ('m_GetBlock', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_ulong, POINTER(c_ubyte), c_ulong)),
    ('m_Param', POINTER(None)),
]

FPDF_FILEACCESS = struct_anon_2# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 393

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 489
class struct_FPDF_FILEHANDLER_(Structure):
    pass

struct_FPDF_FILEHANDLER_.__slots__ = [
    'clientData',
    'Release',
    'GetSize',
    'ReadBlock',
    'WriteBlock',
    'Flush',
    'Truncate',
]
struct_FPDF_FILEHANDLER_._fields_ = [
    ('clientData', POINTER(None)),
    ('Release', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('GetSize', CFUNCTYPE(UNCHECKED(FPDF_DWORD), POINTER(None))),
    ('ReadBlock', CFUNCTYPE(UNCHECKED(FPDF_RESULT), POINTER(None), FPDF_DWORD, POINTER(None), FPDF_DWORD)),
    ('WriteBlock', CFUNCTYPE(UNCHECKED(FPDF_RESULT), POINTER(None), FPDF_DWORD, POINTER(None), FPDF_DWORD)),
    ('Flush', CFUNCTYPE(UNCHECKED(FPDF_RESULT), POINTER(None))),
    ('Truncate', CFUNCTYPE(UNCHECKED(FPDF_RESULT), POINTER(None), FPDF_DWORD)),
]

FPDF_FILEHANDLER = struct_FPDF_FILEHANDLER_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 489

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 512
if _libs["pdfium"].has("FPDF_LoadCustomDocument", "cdecl"):
    FPDF_LoadCustomDocument = _libs["pdfium"].get("FPDF_LoadCustomDocument", "cdecl")
    FPDF_LoadCustomDocument.argtypes = [POINTER(FPDF_FILEACCESS), FPDF_BYTESTRING]
    FPDF_LoadCustomDocument.restype = FPDF_DOCUMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 525
if _libs["pdfium"].has("FPDF_GetFileVersion", "cdecl"):
    FPDF_GetFileVersion = _libs["pdfium"].get("FPDF_GetFileVersion", "cdecl")
    FPDF_GetFileVersion.argtypes = [FPDF_DOCUMENT, POINTER(c_int)]
    FPDF_GetFileVersion.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 549
if _libs["pdfium"].has("FPDF_GetLastError", "cdecl"):
    FPDF_GetLastError = _libs["pdfium"].get("FPDF_GetLastError", "cdecl")
    FPDF_GetLastError.argtypes = []
    FPDF_GetLastError.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 564
if _libs["pdfium"].has("FPDF_DocumentHasValidCrossReferenceTable", "cdecl"):
    FPDF_DocumentHasValidCrossReferenceTable = _libs["pdfium"].get("FPDF_DocumentHasValidCrossReferenceTable", "cdecl")
    FPDF_DocumentHasValidCrossReferenceTable.argtypes = [FPDF_DOCUMENT]
    FPDF_DocumentHasValidCrossReferenceTable.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 575
if _libs["pdfium"].has("FPDF_GetDocPermissions", "cdecl"):
    FPDF_GetDocPermissions = _libs["pdfium"].get("FPDF_GetDocPermissions", "cdecl")
    FPDF_GetDocPermissions.argtypes = [FPDF_DOCUMENT]
    FPDF_GetDocPermissions.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 586
if _libs["pdfium"].has("FPDF_GetSecurityHandlerRevision", "cdecl"):
    FPDF_GetSecurityHandlerRevision = _libs["pdfium"].get("FPDF_GetSecurityHandlerRevision", "cdecl")
    FPDF_GetSecurityHandlerRevision.argtypes = [FPDF_DOCUMENT]
    FPDF_GetSecurityHandlerRevision.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 594
if _libs["pdfium"].has("FPDF_GetPageCount", "cdecl"):
    FPDF_GetPageCount = _libs["pdfium"].get("FPDF_GetPageCount", "cdecl")
    FPDF_GetPageCount.argtypes = [FPDF_DOCUMENT]
    FPDF_GetPageCount.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 606
if _libs["pdfium"].has("FPDF_LoadPage", "cdecl"):
    FPDF_LoadPage = _libs["pdfium"].get("FPDF_LoadPage", "cdecl")
    FPDF_LoadPage.argtypes = [FPDF_DOCUMENT, c_int]
    FPDF_LoadPage.restype = FPDF_PAGE

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 617
if _libs["pdfium"].has("FPDF_GetPageWidthF", "cdecl"):
    FPDF_GetPageWidthF = _libs["pdfium"].get("FPDF_GetPageWidthF", "cdecl")
    FPDF_GetPageWidthF.argtypes = [FPDF_PAGE]
    FPDF_GetPageWidthF.restype = c_float

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 629
if _libs["pdfium"].has("FPDF_GetPageWidth", "cdecl"):
    FPDF_GetPageWidth = _libs["pdfium"].get("FPDF_GetPageWidth", "cdecl")
    FPDF_GetPageWidth.argtypes = [FPDF_PAGE]
    FPDF_GetPageWidth.restype = c_double

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 639
if _libs["pdfium"].has("FPDF_GetPageHeightF", "cdecl"):
    FPDF_GetPageHeightF = _libs["pdfium"].get("FPDF_GetPageHeightF", "cdecl")
    FPDF_GetPageHeightF.argtypes = [FPDF_PAGE]
    FPDF_GetPageHeightF.restype = c_float

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 651
if _libs["pdfium"].has("FPDF_GetPageHeight", "cdecl"):
    FPDF_GetPageHeight = _libs["pdfium"].get("FPDF_GetPageHeight", "cdecl")
    FPDF_GetPageHeight.argtypes = [FPDF_PAGE]
    FPDF_GetPageHeight.restype = c_double

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 663
if _libs["pdfium"].has("FPDF_GetPageBoundingBox", "cdecl"):
    FPDF_GetPageBoundingBox = _libs["pdfium"].get("FPDF_GetPageBoundingBox", "cdecl")
    FPDF_GetPageBoundingBox.argtypes = [FPDF_PAGE, POINTER(FS_RECTF)]
    FPDF_GetPageBoundingBox.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 677
if _libs["pdfium"].has("FPDF_GetPageSizeByIndexF", "cdecl"):
    FPDF_GetPageSizeByIndexF = _libs["pdfium"].get("FPDF_GetPageSizeByIndexF", "cdecl")
    FPDF_GetPageSizeByIndexF.argtypes = [FPDF_DOCUMENT, c_int, POINTER(FS_SIZEF)]
    FPDF_GetPageSizeByIndexF.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 695
if _libs["pdfium"].has("FPDF_GetPageSizeByIndex", "cdecl"):
    FPDF_GetPageSizeByIndex = _libs["pdfium"].get("FPDF_GetPageSizeByIndex", "cdecl")
    FPDF_GetPageSizeByIndex.argtypes = [FPDF_DOCUMENT, c_int, POINTER(c_double), POINTER(c_double)]
    FPDF_GetPageSizeByIndex.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 788
if _libs["pdfium"].has("FPDF_RenderPageBitmap", "cdecl"):
    FPDF_RenderPageBitmap = _libs["pdfium"].get("FPDF_RenderPageBitmap", "cdecl")
    FPDF_RenderPageBitmap.argtypes = [FPDF_BITMAP, FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int]
    FPDF_RenderPageBitmap.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 816
if _libs["pdfium"].has("FPDF_RenderPageBitmapWithMatrix", "cdecl"):
    FPDF_RenderPageBitmapWithMatrix = _libs["pdfium"].get("FPDF_RenderPageBitmapWithMatrix", "cdecl")
    FPDF_RenderPageBitmapWithMatrix.argtypes = [FPDF_BITMAP, FPDF_PAGE, POINTER(FS_MATRIX), POINTER(FS_RECTF), c_int]
    FPDF_RenderPageBitmapWithMatrix.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 834
if _libs["pdfium"].has("FPDF_ClosePage", "cdecl"):
    FPDF_ClosePage = _libs["pdfium"].get("FPDF_ClosePage", "cdecl")
    FPDF_ClosePage.argtypes = [FPDF_PAGE]
    FPDF_ClosePage.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 842
if _libs["pdfium"].has("FPDF_CloseDocument", "cdecl"):
    FPDF_CloseDocument = _libs["pdfium"].get("FPDF_CloseDocument", "cdecl")
    FPDF_CloseDocument.argtypes = [FPDF_DOCUMENT]
    FPDF_CloseDocument.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 885
if _libs["pdfium"].has("FPDF_DeviceToPage", "cdecl"):
    FPDF_DeviceToPage = _libs["pdfium"].get("FPDF_DeviceToPage", "cdecl")
    FPDF_DeviceToPage.argtypes = [FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int, c_int, POINTER(c_double), POINTER(c_double)]
    FPDF_DeviceToPage.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 922
if _libs["pdfium"].has("FPDF_PageToDevice", "cdecl"):
    FPDF_PageToDevice = _libs["pdfium"].get("FPDF_PageToDevice", "cdecl")
    FPDF_PageToDevice.argtypes = [FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_double, c_double, POINTER(c_int), POINTER(c_int)]
    FPDF_PageToDevice.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 963
if _libs["pdfium"].has("FPDFBitmap_Create", "cdecl"):
    FPDFBitmap_Create = _libs["pdfium"].get("FPDFBitmap_Create", "cdecl")
    FPDFBitmap_Create.argtypes = [c_int, c_int, c_int]
    FPDFBitmap_Create.restype = FPDF_BITMAP

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1004
if _libs["pdfium"].has("FPDFBitmap_CreateEx", "cdecl"):
    FPDFBitmap_CreateEx = _libs["pdfium"].get("FPDFBitmap_CreateEx", "cdecl")
    FPDFBitmap_CreateEx.argtypes = [c_int, c_int, c_int, POINTER(None), c_int]
    FPDFBitmap_CreateEx.restype = FPDF_BITMAP

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1020
if _libs["pdfium"].has("FPDFBitmap_GetFormat", "cdecl"):
    FPDFBitmap_GetFormat = _libs["pdfium"].get("FPDFBitmap_GetFormat", "cdecl")
    FPDFBitmap_GetFormat.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetFormat.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1046
if _libs["pdfium"].has("FPDFBitmap_FillRect", "cdecl"):
    FPDFBitmap_FillRect = _libs["pdfium"].get("FPDFBitmap_FillRect", "cdecl")
    FPDFBitmap_FillRect.argtypes = [FPDF_BITMAP, c_int, c_int, c_int, c_int, FPDF_DWORD]
    FPDFBitmap_FillRect.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1069
if _libs["pdfium"].has("FPDFBitmap_GetBuffer", "cdecl"):
    FPDFBitmap_GetBuffer = _libs["pdfium"].get("FPDFBitmap_GetBuffer", "cdecl")
    FPDFBitmap_GetBuffer.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetBuffer.restype = POINTER(c_ubyte)
    FPDFBitmap_GetBuffer.errcheck = lambda v,*a : cast(v, c_void_p)

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1078
if _libs["pdfium"].has("FPDFBitmap_GetWidth", "cdecl"):
    FPDFBitmap_GetWidth = _libs["pdfium"].get("FPDFBitmap_GetWidth", "cdecl")
    FPDFBitmap_GetWidth.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetWidth.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1087
if _libs["pdfium"].has("FPDFBitmap_GetHeight", "cdecl"):
    FPDFBitmap_GetHeight = _libs["pdfium"].get("FPDFBitmap_GetHeight", "cdecl")
    FPDFBitmap_GetHeight.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetHeight.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1098
if _libs["pdfium"].has("FPDFBitmap_GetStride", "cdecl"):
    FPDFBitmap_GetStride = _libs["pdfium"].get("FPDFBitmap_GetStride", "cdecl")
    FPDFBitmap_GetStride.argtypes = [FPDF_BITMAP]
    FPDFBitmap_GetStride.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1110
if _libs["pdfium"].has("FPDFBitmap_Destroy", "cdecl"):
    FPDFBitmap_Destroy = _libs["pdfium"].get("FPDFBitmap_Destroy", "cdecl")
    FPDFBitmap_Destroy.argtypes = [FPDF_BITMAP]
    FPDFBitmap_Destroy.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1119
if _libs["pdfium"].has("FPDF_VIEWERREF_GetPrintScaling", "cdecl"):
    FPDF_VIEWERREF_GetPrintScaling = _libs["pdfium"].get("FPDF_VIEWERREF_GetPrintScaling", "cdecl")
    FPDF_VIEWERREF_GetPrintScaling.argtypes = [FPDF_DOCUMENT]
    FPDF_VIEWERREF_GetPrintScaling.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1128
if _libs["pdfium"].has("FPDF_VIEWERREF_GetNumCopies", "cdecl"):
    FPDF_VIEWERREF_GetNumCopies = _libs["pdfium"].get("FPDF_VIEWERREF_GetNumCopies", "cdecl")
    FPDF_VIEWERREF_GetNumCopies.argtypes = [FPDF_DOCUMENT]
    FPDF_VIEWERREF_GetNumCopies.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1137
if _libs["pdfium"].has("FPDF_VIEWERREF_GetPrintPageRange", "cdecl"):
    FPDF_VIEWERREF_GetPrintPageRange = _libs["pdfium"].get("FPDF_VIEWERREF_GetPrintPageRange", "cdecl")
    FPDF_VIEWERREF_GetPrintPageRange.argtypes = [FPDF_DOCUMENT]
    FPDF_VIEWERREF_GetPrintPageRange.restype = FPDF_PAGERANGE

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1147
if _libs["pdfium"].has("FPDF_VIEWERREF_GetPrintPageRangeCount", "cdecl"):
    FPDF_VIEWERREF_GetPrintPageRangeCount = _libs["pdfium"].get("FPDF_VIEWERREF_GetPrintPageRangeCount", "cdecl")
    FPDF_VIEWERREF_GetPrintPageRangeCount.argtypes = [FPDF_PAGERANGE]
    FPDF_VIEWERREF_GetPrintPageRangeCount.restype = c_size_t

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1159
if _libs["pdfium"].has("FPDF_VIEWERREF_GetPrintPageRangeElement", "cdecl"):
    FPDF_VIEWERREF_GetPrintPageRangeElement = _libs["pdfium"].get("FPDF_VIEWERREF_GetPrintPageRangeElement", "cdecl")
    FPDF_VIEWERREF_GetPrintPageRangeElement.argtypes = [FPDF_PAGERANGE, c_size_t]
    FPDF_VIEWERREF_GetPrintPageRangeElement.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1169
if _libs["pdfium"].has("FPDF_VIEWERREF_GetDuplex", "cdecl"):
    FPDF_VIEWERREF_GetDuplex = _libs["pdfium"].get("FPDF_VIEWERREF_GetDuplex", "cdecl")
    FPDF_VIEWERREF_GetDuplex.argtypes = [FPDF_DOCUMENT]
    FPDF_VIEWERREF_GetDuplex.restype = FPDF_DUPLEXTYPE

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1187
if _libs["pdfium"].has("FPDF_VIEWERREF_GetName", "cdecl"):
    FPDF_VIEWERREF_GetName = _libs["pdfium"].get("FPDF_VIEWERREF_GetName", "cdecl")
    FPDF_VIEWERREF_GetName.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING, String, c_ulong]
    FPDF_VIEWERREF_GetName.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1199
if _libs["pdfium"].has("FPDF_CountNamedDests", "cdecl"):
    FPDF_CountNamedDests = _libs["pdfium"].get("FPDF_CountNamedDests", "cdecl")
    FPDF_CountNamedDests.argtypes = [FPDF_DOCUMENT]
    FPDF_CountNamedDests.restype = FPDF_DWORD

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1209
if _libs["pdfium"].has("FPDF_GetNamedDestByName", "cdecl"):
    FPDF_GetNamedDestByName = _libs["pdfium"].get("FPDF_GetNamedDestByName", "cdecl")
    FPDF_GetNamedDestByName.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING]
    FPDF_GetNamedDestByName.restype = FPDF_DEST

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 1232
if _libs["pdfium"].has("FPDF_GetNamedDest", "cdecl"):
    FPDF_GetNamedDest = _libs["pdfium"].get("FPDF_GetNamedDest", "cdecl")
    FPDF_GetNamedDest.argtypes = [FPDF_DOCUMENT, c_int, POINTER(None), POINTER(c_long)]
    FPDF_GetNamedDest.restype = FPDF_DEST

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 48
class struct__FS_QUADPOINTSF(Structure):
    pass

struct__FS_QUADPOINTSF.__slots__ = [
    'x1',
    'y1',
    'x2',
    'y2',
    'x3',
    'y3',
    'x4',
    'y4',
]
struct__FS_QUADPOINTSF._fields_ = [
    ('x1', FS_FLOAT),
    ('y1', FS_FLOAT),
    ('x2', FS_FLOAT),
    ('y2', FS_FLOAT),
    ('x3', FS_FLOAT),
    ('y3', FS_FLOAT),
    ('x4', FS_FLOAT),
    ('y4', FS_FLOAT),
]

FS_QUADPOINTSF = struct__FS_QUADPOINTSF# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 48

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 59
if _libs["pdfium"].has("FPDFBookmark_GetFirstChild", "cdecl"):
    FPDFBookmark_GetFirstChild = _libs["pdfium"].get("FPDFBookmark_GetFirstChild", "cdecl")
    FPDFBookmark_GetFirstChild.argtypes = [FPDF_DOCUMENT, FPDF_BOOKMARK]
    FPDFBookmark_GetFirstChild.restype = FPDF_BOOKMARK

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 69
if _libs["pdfium"].has("FPDFBookmark_GetNextSibling", "cdecl"):
    FPDFBookmark_GetNextSibling = _libs["pdfium"].get("FPDFBookmark_GetNextSibling", "cdecl")
    FPDFBookmark_GetNextSibling.argtypes = [FPDF_DOCUMENT, FPDF_BOOKMARK]
    FPDFBookmark_GetNextSibling.restype = FPDF_BOOKMARK

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 85
if _libs["pdfium"].has("FPDFBookmark_GetTitle", "cdecl"):
    FPDFBookmark_GetTitle = _libs["pdfium"].get("FPDFBookmark_GetTitle", "cdecl")
    FPDFBookmark_GetTitle.argtypes = [FPDF_BOOKMARK, POINTER(None), c_ulong]
    FPDFBookmark_GetTitle.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 99
if _libs["pdfium"].has("FPDFBookmark_Find", "cdecl"):
    FPDFBookmark_Find = _libs["pdfium"].get("FPDFBookmark_Find", "cdecl")
    FPDFBookmark_Find.argtypes = [FPDF_DOCUMENT, FPDF_WIDESTRING]
    FPDFBookmark_Find.restype = FPDF_BOOKMARK

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 109
if _libs["pdfium"].has("FPDFBookmark_GetDest", "cdecl"):
    FPDFBookmark_GetDest = _libs["pdfium"].get("FPDFBookmark_GetDest", "cdecl")
    FPDFBookmark_GetDest.argtypes = [FPDF_DOCUMENT, FPDF_BOOKMARK]
    FPDFBookmark_GetDest.restype = FPDF_DEST

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 119
if _libs["pdfium"].has("FPDFBookmark_GetAction", "cdecl"):
    FPDFBookmark_GetAction = _libs["pdfium"].get("FPDFBookmark_GetAction", "cdecl")
    FPDFBookmark_GetAction.argtypes = [FPDF_BOOKMARK]
    FPDFBookmark_GetAction.restype = FPDF_ACTION

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 131
if _libs["pdfium"].has("FPDFAction_GetType", "cdecl"):
    FPDFAction_GetType = _libs["pdfium"].get("FPDFAction_GetType", "cdecl")
    FPDFAction_GetType.argtypes = [FPDF_ACTION]
    FPDFAction_GetType.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 145
if _libs["pdfium"].has("FPDFAction_GetDest", "cdecl"):
    FPDFAction_GetDest = _libs["pdfium"].get("FPDFAction_GetDest", "cdecl")
    FPDFAction_GetDest.argtypes = [FPDF_DOCUMENT, FPDF_ACTION]
    FPDFAction_GetDest.restype = FPDF_DEST

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 163
if _libs["pdfium"].has("FPDFAction_GetFilePath", "cdecl"):
    FPDFAction_GetFilePath = _libs["pdfium"].get("FPDFAction_GetFilePath", "cdecl")
    FPDFAction_GetFilePath.argtypes = [FPDF_ACTION, POINTER(None), c_ulong]
    FPDFAction_GetFilePath.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 179
if _libs["pdfium"].has("FPDFAction_GetURIPath", "cdecl"):
    FPDFAction_GetURIPath = _libs["pdfium"].get("FPDFAction_GetURIPath", "cdecl")
    FPDFAction_GetURIPath.argtypes = [FPDF_DOCUMENT, FPDF_ACTION, POINTER(None), c_ulong]
    FPDFAction_GetURIPath.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 190
if _libs["pdfium"].has("FPDFDest_GetDestPageIndex", "cdecl"):
    FPDFDest_GetDestPageIndex = _libs["pdfium"].get("FPDFDest_GetDestPageIndex", "cdecl")
    FPDFDest_GetDestPageIndex.argtypes = [FPDF_DOCUMENT, FPDF_DEST]
    FPDFDest_GetDestPageIndex.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 203
if _libs["pdfium"].has("FPDFDest_GetView", "cdecl"):
    FPDFDest_GetView = _libs["pdfium"].get("FPDFDest_GetView", "cdecl")
    FPDFDest_GetView.argtypes = [FPDF_DEST, POINTER(c_ulong), POINTER(FS_FLOAT)]
    FPDFDest_GetView.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 220
if _libs["pdfium"].has("FPDFDest_GetLocationInPage", "cdecl"):
    FPDFDest_GetLocationInPage = _libs["pdfium"].get("FPDFDest_GetLocationInPage", "cdecl")
    FPDFDest_GetLocationInPage.argtypes = [FPDF_DEST, POINTER(FPDF_BOOL), POINTER(FPDF_BOOL), POINTER(FPDF_BOOL), POINTER(FS_FLOAT), POINTER(FS_FLOAT), POINTER(FS_FLOAT)]
    FPDFDest_GetLocationInPage.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 238
if _libs["pdfium"].has("FPDFLink_GetLinkAtPoint", "cdecl"):
    FPDFLink_GetLinkAtPoint = _libs["pdfium"].get("FPDFLink_GetLinkAtPoint", "cdecl")
    FPDFLink_GetLinkAtPoint.argtypes = [FPDF_PAGE, c_double, c_double]
    FPDFLink_GetLinkAtPoint.restype = FPDF_LINK

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 253
if _libs["pdfium"].has("FPDFLink_GetLinkZOrderAtPoint", "cdecl"):
    FPDFLink_GetLinkZOrderAtPoint = _libs["pdfium"].get("FPDFLink_GetLinkZOrderAtPoint", "cdecl")
    FPDFLink_GetLinkZOrderAtPoint.argtypes = [FPDF_PAGE, c_double, c_double]
    FPDFLink_GetLinkZOrderAtPoint.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 265
if _libs["pdfium"].has("FPDFLink_GetDest", "cdecl"):
    FPDFLink_GetDest = _libs["pdfium"].get("FPDFLink_GetDest", "cdecl")
    FPDFLink_GetDest.argtypes = [FPDF_DOCUMENT, FPDF_LINK]
    FPDFLink_GetDest.restype = FPDF_DEST

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 273
if _libs["pdfium"].has("FPDFLink_GetAction", "cdecl"):
    FPDFLink_GetAction = _libs["pdfium"].get("FPDFLink_GetAction", "cdecl")
    FPDFLink_GetAction.argtypes = [FPDF_LINK]
    FPDFLink_GetAction.restype = FPDF_ACTION

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 283
if _libs["pdfium"].has("FPDFLink_Enumerate", "cdecl"):
    FPDFLink_Enumerate = _libs["pdfium"].get("FPDFLink_Enumerate", "cdecl")
    FPDFLink_Enumerate.argtypes = [FPDF_PAGE, POINTER(c_int), POINTER(FPDF_LINK)]
    FPDFLink_Enumerate.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 293
if _libs["pdfium"].has("FPDFLink_GetAnnotRect", "cdecl"):
    FPDFLink_GetAnnotRect = _libs["pdfium"].get("FPDFLink_GetAnnotRect", "cdecl")
    FPDFLink_GetAnnotRect.argtypes = [FPDF_LINK, POINTER(FS_RECTF)]
    FPDFLink_GetAnnotRect.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 301
if _libs["pdfium"].has("FPDFLink_CountQuadPoints", "cdecl"):
    FPDFLink_CountQuadPoints = _libs["pdfium"].get("FPDFLink_CountQuadPoints", "cdecl")
    FPDFLink_CountQuadPoints.argtypes = [FPDF_LINK]
    FPDFLink_CountQuadPoints.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 311
if _libs["pdfium"].has("FPDFLink_GetQuadPoints", "cdecl"):
    FPDFLink_GetQuadPoints = _libs["pdfium"].get("FPDFLink_GetQuadPoints", "cdecl")
    FPDFLink_GetQuadPoints.argtypes = [FPDF_LINK, c_int, POINTER(FS_QUADPOINTSF)]
    FPDFLink_GetQuadPoints.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 336
if _libs["pdfium"].has("FPDF_GetMetaText", "cdecl"):
    FPDF_GetMetaText = _libs["pdfium"].get("FPDF_GetMetaText", "cdecl")
    FPDF_GetMetaText.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING, POINTER(None), c_ulong]
    FPDF_GetMetaText.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 354
if _libs["pdfium"].has("FPDF_GetPageLabel", "cdecl"):
    FPDF_GetPageLabel = _libs["pdfium"].get("FPDF_GetPageLabel", "cdecl")
    FPDF_GetPageLabel.argtypes = [FPDF_DOCUMENT, c_int, POINTER(None), c_ulong]
    FPDF_GetPageLabel.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 52
class struct__IPDF_JsPlatform(Structure):
    pass

struct__IPDF_JsPlatform.__slots__ = [
    'version',
    'app_alert',
    'app_beep',
    'app_response',
    'Doc_getFilePath',
    'Doc_mail',
    'Doc_print',
    'Doc_submitForm',
    'Doc_gotoPage',
    'Field_browse',
    'm_pFormfillinfo',
    'm_isolate',
    'm_v8EmbedderSlot',
]
struct__IPDF_JsPlatform._fields_ = [
    ('version', c_int),
    ('app_alert', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__IPDF_JsPlatform), FPDF_WIDESTRING, FPDF_WIDESTRING, c_int, c_int)),
    ('app_beep', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), c_int)),
    ('app_response', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__IPDF_JsPlatform), FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_BOOL, POINTER(None), c_int)),
    ('Doc_getFilePath', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__IPDF_JsPlatform), POINTER(None), c_int)),
    ('Doc_mail', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), POINTER(None), c_int, FPDF_BOOL, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING)),
    ('Doc_print', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), FPDF_BOOL, c_int, c_int, FPDF_BOOL, FPDF_BOOL, FPDF_BOOL, FPDF_BOOL, FPDF_BOOL)),
    ('Doc_submitForm', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), POINTER(None), c_int, FPDF_WIDESTRING)),
    ('Doc_gotoPage', CFUNCTYPE(UNCHECKED(None), POINTER(struct__IPDF_JsPlatform), c_int)),
    ('Field_browse', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__IPDF_JsPlatform), POINTER(None), c_int)),
    ('m_pFormfillinfo', POINTER(None)),
    ('m_isolate', POINTER(None)),
    ('m_v8EmbedderSlot', c_uint),
]

IPDF_JSPLATFORM = struct__IPDF_JsPlatform# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 321

TimerCallback = CFUNCTYPE(UNCHECKED(None), c_int)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 339

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 353
class struct__FPDF_SYSTEMTIME(Structure):
    pass

struct__FPDF_SYSTEMTIME.__slots__ = [
    'wYear',
    'wMonth',
    'wDayOfWeek',
    'wDay',
    'wHour',
    'wMinute',
    'wSecond',
    'wMilliseconds',
]
struct__FPDF_SYSTEMTIME._fields_ = [
    ('wYear', c_ushort),
    ('wMonth', c_ushort),
    ('wDayOfWeek', c_ushort),
    ('wDay', c_ushort),
    ('wHour', c_ushort),
    ('wMinute', c_ushort),
    ('wSecond', c_ushort),
    ('wMilliseconds', c_ushort),
]

FPDF_SYSTEMTIME = struct__FPDF_SYSTEMTIME# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 353

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 375
class struct__FPDF_FORMFILLINFO(Structure):
    pass

struct__FPDF_FORMFILLINFO.__slots__ = [
    'version',
    'Release',
    'FFI_Invalidate',
    'FFI_OutputSelectedRect',
    'FFI_SetCursor',
    'FFI_SetTimer',
    'FFI_KillTimer',
    'FFI_GetLocalTime',
    'FFI_OnChange',
    'FFI_GetPage',
    'FFI_GetCurrentPage',
    'FFI_GetRotation',
    'FFI_ExecuteNamedAction',
    'FFI_SetTextFieldFocus',
    'FFI_DoURIAction',
    'FFI_DoGoToAction',
    'm_pJsPlatform',
    'xfa_disabled',
    'FFI_DisplayCaret',
    'FFI_GetCurrentPageIndex',
    'FFI_SetCurrentPage',
    'FFI_GotoURL',
    'FFI_GetPageViewRect',
    'FFI_PageEvent',
    'FFI_PopupMenu',
    'FFI_OpenFile',
    'FFI_EmailTo',
    'FFI_UploadTo',
    'FFI_GetPlatform',
    'FFI_GetLanguage',
    'FFI_DownloadFromURL',
    'FFI_PostRequestURL',
    'FFI_PutRequestURL',
]
struct__FPDF_FORMFILLINFO._fields_ = [
    ('version', c_int),
    ('Release', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO))),
    ('FFI_Invalidate', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, c_double, c_double, c_double, c_double)),
    ('FFI_OutputSelectedRect', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, c_double, c_double, c_double, c_double)),
    ('FFI_SetCursor', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), c_int)),
    ('FFI_SetTimer', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), c_int, TimerCallback)),
    ('FFI_KillTimer', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), c_int)),
    ('FFI_GetLocalTime', CFUNCTYPE(UNCHECKED(FPDF_SYSTEMTIME), POINTER(struct__FPDF_FORMFILLINFO))),
    ('FFI_OnChange', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO))),
    ('FFI_GetPage', CFUNCTYPE(UNCHECKED(FPDF_PAGE), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT, c_int)),
    ('FFI_GetCurrentPage', CFUNCTYPE(UNCHECKED(FPDF_PAGE), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT)),
    ('FFI_GetRotation', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE)),
    ('FFI_ExecuteNamedAction', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_BYTESTRING)),
    ('FFI_SetTextFieldFocus', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_WIDESTRING, FPDF_DWORD, FPDF_BOOL)),
    ('FFI_DoURIAction', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_BYTESTRING)),
    ('FFI_DoGoToAction', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), c_int, c_int, POINTER(c_float), c_int)),
    ('m_pJsPlatform', POINTER(IPDF_JSPLATFORM)),
    ('xfa_disabled', FPDF_BOOL),
    ('FFI_DisplayCaret', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, FPDF_BOOL, c_double, c_double, c_double, c_double)),
    ('FFI_GetCurrentPageIndex', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT)),
    ('FFI_SetCurrentPage', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT, c_int)),
    ('FFI_GotoURL', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_DOCUMENT, FPDF_WIDESTRING)),
    ('FFI_GetPageViewRect', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double))),
    ('FFI_PageEvent', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), c_int, FPDF_DWORD)),
    ('FFI_PopupMenu', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__FPDF_FORMFILLINFO), FPDF_PAGE, FPDF_WIDGET, c_int, c_float, c_float)),
    ('FFI_OpenFile', CFUNCTYPE(UNCHECKED(POINTER(FPDF_FILEHANDLER)), POINTER(struct__FPDF_FORMFILLINFO), c_int, FPDF_WIDESTRING, String)),
    ('FFI_EmailTo', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), POINTER(FPDF_FILEHANDLER), FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING)),
    ('FFI_UploadTo', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_FORMFILLINFO), POINTER(FPDF_FILEHANDLER), c_int, FPDF_WIDESTRING)),
    ('FFI_GetPlatform', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), POINTER(None), c_int)),
    ('FFI_GetLanguage', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_FORMFILLINFO), POINTER(None), c_int)),
    ('FFI_DownloadFromURL', CFUNCTYPE(UNCHECKED(POINTER(FPDF_FILEHANDLER)), POINTER(struct__FPDF_FORMFILLINFO), FPDF_WIDESTRING)),
    ('FFI_PostRequestURL', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__FPDF_FORMFILLINFO), FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING, POINTER(FPDF_BSTR))),
    ('FFI_PutRequestURL', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__FPDF_FORMFILLINFO), FPDF_WIDESTRING, FPDF_WIDESTRING, FPDF_WIDESTRING)),
]

FPDF_FORMFILLINFO = struct__FPDF_FORMFILLINFO# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1072

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1086
if _libs["pdfium"].has("FPDFDOC_InitFormFillEnvironment", "cdecl"):
    FPDFDOC_InitFormFillEnvironment = _libs["pdfium"].get("FPDFDOC_InitFormFillEnvironment", "cdecl")
    FPDFDOC_InitFormFillEnvironment.argtypes = [FPDF_DOCUMENT, POINTER(FPDF_FORMFILLINFO)]
    FPDFDOC_InitFormFillEnvironment.restype = FPDF_FORMHANDLE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1101
if _libs["pdfium"].has("FPDFDOC_ExitFormFillEnvironment", "cdecl"):
    FPDFDOC_ExitFormFillEnvironment = _libs["pdfium"].get("FPDFDOC_ExitFormFillEnvironment", "cdecl")
    FPDFDOC_ExitFormFillEnvironment.argtypes = [FPDF_FORMHANDLE]
    FPDFDOC_ExitFormFillEnvironment.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1114
if _libs["pdfium"].has("FORM_OnAfterLoadPage", "cdecl"):
    FORM_OnAfterLoadPage = _libs["pdfium"].get("FORM_OnAfterLoadPage", "cdecl")
    FORM_OnAfterLoadPage.argtypes = [FPDF_PAGE, FPDF_FORMHANDLE]
    FORM_OnAfterLoadPage.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1128
if _libs["pdfium"].has("FORM_OnBeforeClosePage", "cdecl"):
    FORM_OnBeforeClosePage = _libs["pdfium"].get("FORM_OnBeforeClosePage", "cdecl")
    FORM_OnBeforeClosePage.argtypes = [FPDF_PAGE, FPDF_FORMHANDLE]
    FORM_OnBeforeClosePage.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1146
if _libs["pdfium"].has("FORM_DoDocumentJSAction", "cdecl"):
    FORM_DoDocumentJSAction = _libs["pdfium"].get("FORM_DoDocumentJSAction", "cdecl")
    FORM_DoDocumentJSAction.argtypes = [FPDF_FORMHANDLE]
    FORM_DoDocumentJSAction.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1162
if _libs["pdfium"].has("FORM_DoDocumentOpenAction", "cdecl"):
    FORM_DoDocumentOpenAction = _libs["pdfium"].get("FORM_DoDocumentOpenAction", "cdecl")
    FORM_DoDocumentOpenAction.argtypes = [FPDF_FORMHANDLE]
    FORM_DoDocumentOpenAction.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1191
if _libs["pdfium"].has("FORM_DoDocumentAAction", "cdecl"):
    FORM_DoDocumentAAction = _libs["pdfium"].get("FORM_DoDocumentAAction", "cdecl")
    FORM_DoDocumentAAction.argtypes = [FPDF_FORMHANDLE, c_int]
    FORM_DoDocumentAAction.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1216
if _libs["pdfium"].has("FORM_DoPageAAction", "cdecl"):
    FORM_DoPageAAction = _libs["pdfium"].get("FORM_DoPageAAction", "cdecl")
    FORM_DoPageAAction.argtypes = [FPDF_PAGE, FPDF_FORMHANDLE, c_int]
    FORM_DoPageAAction.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1235
if _libs["pdfium"].has("FORM_OnMouseMove", "cdecl"):
    FORM_OnMouseMove = _libs["pdfium"].get("FORM_OnMouseMove", "cdecl")
    FORM_OnMouseMove.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnMouseMove.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1258
if _libs["pdfium"].has("FORM_OnFocus", "cdecl"):
    FORM_OnFocus = _libs["pdfium"].get("FORM_OnFocus", "cdecl")
    FORM_OnFocus.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnFocus.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1280
if _libs["pdfium"].has("FORM_OnLButtonDown", "cdecl"):
    FORM_OnLButtonDown = _libs["pdfium"].get("FORM_OnLButtonDown", "cdecl")
    FORM_OnLButtonDown.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnLButtonDown.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1293
if _libs["pdfium"].has("FORM_OnRButtonDown", "cdecl"):
    FORM_OnRButtonDown = _libs["pdfium"].get("FORM_OnRButtonDown", "cdecl")
    FORM_OnRButtonDown.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnRButtonDown.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1312
if _libs["pdfium"].has("FORM_OnLButtonUp", "cdecl"):
    FORM_OnLButtonUp = _libs["pdfium"].get("FORM_OnLButtonUp", "cdecl")
    FORM_OnLButtonUp.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnLButtonUp.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1325
if _libs["pdfium"].has("FORM_OnRButtonUp", "cdecl"):
    FORM_OnRButtonUp = _libs["pdfium"].get("FORM_OnRButtonUp", "cdecl")
    FORM_OnRButtonUp.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnRButtonUp.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1348
if _libs["pdfium"].has("FORM_OnLButtonDoubleClick", "cdecl"):
    FORM_OnLButtonDoubleClick = _libs["pdfium"].get("FORM_OnLButtonDoubleClick", "cdecl")
    FORM_OnLButtonDoubleClick.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_double, c_double]
    FORM_OnLButtonDoubleClick.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1367
if _libs["pdfium"].has("FORM_OnKeyDown", "cdecl"):
    FORM_OnKeyDown = _libs["pdfium"].get("FORM_OnKeyDown", "cdecl")
    FORM_OnKeyDown.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_int]
    FORM_OnKeyDown.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1385
if _libs["pdfium"].has("FORM_OnKeyUp", "cdecl"):
    FORM_OnKeyUp = _libs["pdfium"].get("FORM_OnKeyUp", "cdecl")
    FORM_OnKeyUp.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_int]
    FORM_OnKeyUp.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1404
if _libs["pdfium"].has("FORM_OnChar", "cdecl"):
    FORM_OnChar = _libs["pdfium"].get("FORM_OnChar", "cdecl")
    FORM_OnChar.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, c_int]
    FORM_OnChar.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1427
if _libs["pdfium"].has("FORM_GetFocusedText", "cdecl"):
    FORM_GetFocusedText = _libs["pdfium"].get("FORM_GetFocusedText", "cdecl")
    FORM_GetFocusedText.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, POINTER(None), c_ulong]
    FORM_GetFocusedText.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1450
if _libs["pdfium"].has("FORM_GetSelectedText", "cdecl"):
    FORM_GetSelectedText = _libs["pdfium"].get("FORM_GetSelectedText", "cdecl")
    FORM_GetSelectedText.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, POINTER(None), c_ulong]
    FORM_GetSelectedText.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1470
if _libs["pdfium"].has("FORM_ReplaceSelection", "cdecl"):
    FORM_ReplaceSelection = _libs["pdfium"].get("FORM_ReplaceSelection", "cdecl")
    FORM_ReplaceSelection.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, FPDF_WIDESTRING]
    FORM_ReplaceSelection.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1485
if _libs["pdfium"].has("FORM_CanUndo", "cdecl"):
    FORM_CanUndo = _libs["pdfium"].get("FORM_CanUndo", "cdecl")
    FORM_CanUndo.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_CanUndo.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1499
if _libs["pdfium"].has("FORM_CanRedo", "cdecl"):
    FORM_CanRedo = _libs["pdfium"].get("FORM_CanRedo", "cdecl")
    FORM_CanRedo.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_CanRedo.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1512
if _libs["pdfium"].has("FORM_Undo", "cdecl"):
    FORM_Undo = _libs["pdfium"].get("FORM_Undo", "cdecl")
    FORM_Undo.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_Undo.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1525
if _libs["pdfium"].has("FORM_Redo", "cdecl"):
    FORM_Redo = _libs["pdfium"].get("FORM_Redo", "cdecl")
    FORM_Redo.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE]
    FORM_Redo.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1540
if _libs["pdfium"].has("FORM_ForceToKillFocus", "cdecl"):
    FORM_ForceToKillFocus = _libs["pdfium"].get("FORM_ForceToKillFocus", "cdecl")
    FORM_ForceToKillFocus.argtypes = [FPDF_FORMHANDLE]
    FORM_ForceToKillFocus.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1596
if _libs["pdfium"].has("FPDFPage_HasFormFieldAtPoint", "cdecl"):
    FPDFPage_HasFormFieldAtPoint = _libs["pdfium"].get("FPDFPage_HasFormFieldAtPoint", "cdecl")
    FPDFPage_HasFormFieldAtPoint.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_double, c_double]
    FPDFPage_HasFormFieldAtPoint.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1615
if _libs["pdfium"].has("FPDFPage_FormFieldZOrderAtPoint", "cdecl"):
    FPDFPage_FormFieldZOrderAtPoint = _libs["pdfium"].get("FPDFPage_FormFieldZOrderAtPoint", "cdecl")
    FPDFPage_FormFieldZOrderAtPoint.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_double, c_double]
    FPDFPage_FormFieldZOrderAtPoint.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1643
if _libs["pdfium"].has("FPDF_SetFormFieldHighlightColor", "cdecl"):
    FPDF_SetFormFieldHighlightColor = _libs["pdfium"].get("FPDF_SetFormFieldHighlightColor", "cdecl")
    FPDF_SetFormFieldHighlightColor.argtypes = [FPDF_FORMHANDLE, c_int, c_ulong]
    FPDF_SetFormFieldHighlightColor.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1662
if _libs["pdfium"].has("FPDF_SetFormFieldHighlightAlpha", "cdecl"):
    FPDF_SetFormFieldHighlightAlpha = _libs["pdfium"].get("FPDF_SetFormFieldHighlightAlpha", "cdecl")
    FPDF_SetFormFieldHighlightAlpha.argtypes = [FPDF_FORMHANDLE, c_ubyte]
    FPDF_SetFormFieldHighlightAlpha.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1677
if _libs["pdfium"].has("FPDF_RemoveFormFieldHighlight", "cdecl"):
    FPDF_RemoveFormFieldHighlight = _libs["pdfium"].get("FPDF_RemoveFormFieldHighlight", "cdecl")
    FPDF_RemoveFormFieldHighlight.argtypes = [FPDF_FORMHANDLE]
    FPDF_RemoveFormFieldHighlight.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1716
if _libs["pdfium"].has("FPDF_FFLDraw", "cdecl"):
    FPDF_FFLDraw = _libs["pdfium"].get("FPDF_FFLDraw", "cdecl")
    FPDF_FFLDraw.argtypes = [FPDF_FORMHANDLE, FPDF_BITMAP, FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int]
    FPDF_FFLDraw.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1749
if _libs["pdfium"].has("FPDF_GetFormType", "cdecl"):
    FPDF_GetFormType = _libs["pdfium"].get("FPDF_GetFormType", "cdecl")
    FPDF_GetFormType.argtypes = [FPDF_DOCUMENT]
    FPDF_GetFormType.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1775
if _libs["pdfium"].has("FORM_SetIndexSelected", "cdecl"):
    FORM_SetIndexSelected = _libs["pdfium"].get("FORM_SetIndexSelected", "cdecl")
    FORM_SetIndexSelected.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int, FPDF_BOOL]
    FORM_SetIndexSelected.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1800
if _libs["pdfium"].has("FORM_IsIndexSelected", "cdecl"):
    FORM_IsIndexSelected = _libs["pdfium"].get("FORM_IsIndexSelected", "cdecl")
    FORM_IsIndexSelected.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, c_int]
    FORM_IsIndexSelected.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1812
if _libs["pdfium"].has("FPDF_LoadXFA", "cdecl"):
    FPDF_LoadXFA = _libs["pdfium"].get("FPDF_LoadXFA", "cdecl")
    FPDF_LoadXFA.argtypes = [FPDF_DOCUMENT]
    FPDF_LoadXFA.restype = FPDF_BOOL

enum_FPDFANNOT_COLORTYPE = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 88

FPDFANNOT_COLORTYPE_Color = 0# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 88

FPDFANNOT_COLORTYPE_InteriorColor = (FPDFANNOT_COLORTYPE_Color + 1)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 88

FPDFANNOT_COLORTYPE = enum_FPDFANNOT_COLORTYPE# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 88

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 99
if _libs["pdfium"].has("FPDFAnnot_IsSupportedSubtype", "cdecl"):
    FPDFAnnot_IsSupportedSubtype = _libs["pdfium"].get("FPDFAnnot_IsSupportedSubtype", "cdecl")
    FPDFAnnot_IsSupportedSubtype.argtypes = [FPDF_ANNOTATION_SUBTYPE]
    FPDFAnnot_IsSupportedSubtype.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 112
if _libs["pdfium"].has("FPDFPage_CreateAnnot", "cdecl"):
    FPDFPage_CreateAnnot = _libs["pdfium"].get("FPDFPage_CreateAnnot", "cdecl")
    FPDFPage_CreateAnnot.argtypes = [FPDF_PAGE, FPDF_ANNOTATION_SUBTYPE]
    FPDFPage_CreateAnnot.restype = FPDF_ANNOTATION

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 120
if _libs["pdfium"].has("FPDFPage_GetAnnotCount", "cdecl"):
    FPDFPage_GetAnnotCount = _libs["pdfium"].get("FPDFPage_GetAnnotCount", "cdecl")
    FPDFPage_GetAnnotCount.argtypes = [FPDF_PAGE]
    FPDFPage_GetAnnotCount.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 130
if _libs["pdfium"].has("FPDFPage_GetAnnot", "cdecl"):
    FPDFPage_GetAnnot = _libs["pdfium"].get("FPDFPage_GetAnnot", "cdecl")
    FPDFPage_GetAnnot.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_GetAnnot.restype = FPDF_ANNOTATION

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 141
if _libs["pdfium"].has("FPDFPage_GetAnnotIndex", "cdecl"):
    FPDFPage_GetAnnotIndex = _libs["pdfium"].get("FPDFPage_GetAnnotIndex", "cdecl")
    FPDFPage_GetAnnotIndex.argtypes = [FPDF_PAGE, FPDF_ANNOTATION]
    FPDFPage_GetAnnotIndex.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 150
if _libs["pdfium"].has("FPDFPage_CloseAnnot", "cdecl"):
    FPDFPage_CloseAnnot = _libs["pdfium"].get("FPDFPage_CloseAnnot", "cdecl")
    FPDFPage_CloseAnnot.argtypes = [FPDF_ANNOTATION]
    FPDFPage_CloseAnnot.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 159
if _libs["pdfium"].has("FPDFPage_RemoveAnnot", "cdecl"):
    FPDFPage_RemoveAnnot = _libs["pdfium"].get("FPDFPage_RemoveAnnot", "cdecl")
    FPDFPage_RemoveAnnot.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_RemoveAnnot.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 169
if _libs["pdfium"].has("FPDFAnnot_GetSubtype", "cdecl"):
    FPDFAnnot_GetSubtype = _libs["pdfium"].get("FPDFAnnot_GetSubtype", "cdecl")
    FPDFAnnot_GetSubtype.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_GetSubtype.restype = FPDF_ANNOTATION_SUBTYPE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 180
if _libs["pdfium"].has("FPDFAnnot_IsObjectSupportedSubtype", "cdecl"):
    FPDFAnnot_IsObjectSupportedSubtype = _libs["pdfium"].get("FPDFAnnot_IsObjectSupportedSubtype", "cdecl")
    FPDFAnnot_IsObjectSupportedSubtype.argtypes = [FPDF_ANNOTATION_SUBTYPE]
    FPDFAnnot_IsObjectSupportedSubtype.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 194
if _libs["pdfium"].has("FPDFAnnot_UpdateObject", "cdecl"):
    FPDFAnnot_UpdateObject = _libs["pdfium"].get("FPDFAnnot_UpdateObject", "cdecl")
    FPDFAnnot_UpdateObject.argtypes = [FPDF_ANNOTATION, FPDF_PAGEOBJECT]
    FPDFAnnot_UpdateObject.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 208
if _libs["pdfium"].has("FPDFAnnot_AppendObject", "cdecl"):
    FPDFAnnot_AppendObject = _libs["pdfium"].get("FPDFAnnot_AppendObject", "cdecl")
    FPDFAnnot_AppendObject.argtypes = [FPDF_ANNOTATION, FPDF_PAGEOBJECT]
    FPDFAnnot_AppendObject.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 217
if _libs["pdfium"].has("FPDFAnnot_GetObjectCount", "cdecl"):
    FPDFAnnot_GetObjectCount = _libs["pdfium"].get("FPDFAnnot_GetObjectCount", "cdecl")
    FPDFAnnot_GetObjectCount.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_GetObjectCount.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 227
if _libs["pdfium"].has("FPDFAnnot_GetObject", "cdecl"):
    FPDFAnnot_GetObject = _libs["pdfium"].get("FPDFAnnot_GetObject", "cdecl")
    FPDFAnnot_GetObject.argtypes = [FPDF_ANNOTATION, c_int]
    FPDFAnnot_GetObject.restype = FPDF_PAGEOBJECT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 237
if _libs["pdfium"].has("FPDFAnnot_RemoveObject", "cdecl"):
    FPDFAnnot_RemoveObject = _libs["pdfium"].get("FPDFAnnot_RemoveObject", "cdecl")
    FPDFAnnot_RemoveObject.argtypes = [FPDF_ANNOTATION, c_int]
    FPDFAnnot_RemoveObject.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 250
if _libs["pdfium"].has("FPDFAnnot_SetColor", "cdecl"):
    FPDFAnnot_SetColor = _libs["pdfium"].get("FPDFAnnot_SetColor", "cdecl")
    FPDFAnnot_SetColor.argtypes = [FPDF_ANNOTATION, FPDFANNOT_COLORTYPE, c_uint, c_uint, c_uint, c_uint]
    FPDFAnnot_SetColor.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 269
if _libs["pdfium"].has("FPDFAnnot_GetColor", "cdecl"):
    FPDFAnnot_GetColor = _libs["pdfium"].get("FPDFAnnot_GetColor", "cdecl")
    FPDFAnnot_GetColor.argtypes = [FPDF_ANNOTATION, FPDFANNOT_COLORTYPE, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFAnnot_GetColor.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 289
if _libs["pdfium"].has("FPDFAnnot_HasAttachmentPoints", "cdecl"):
    FPDFAnnot_HasAttachmentPoints = _libs["pdfium"].get("FPDFAnnot_HasAttachmentPoints", "cdecl")
    FPDFAnnot_HasAttachmentPoints.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_HasAttachmentPoints.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 305
if _libs["pdfium"].has("FPDFAnnot_SetAttachmentPoints", "cdecl"):
    FPDFAnnot_SetAttachmentPoints = _libs["pdfium"].get("FPDFAnnot_SetAttachmentPoints", "cdecl")
    FPDFAnnot_SetAttachmentPoints.argtypes = [FPDF_ANNOTATION, c_size_t, POINTER(FS_QUADPOINTSF)]
    FPDFAnnot_SetAttachmentPoints.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 320
if _libs["pdfium"].has("FPDFAnnot_AppendAttachmentPoints", "cdecl"):
    FPDFAnnot_AppendAttachmentPoints = _libs["pdfium"].get("FPDFAnnot_AppendAttachmentPoints", "cdecl")
    FPDFAnnot_AppendAttachmentPoints.argtypes = [FPDF_ANNOTATION, POINTER(FS_QUADPOINTSF)]
    FPDFAnnot_AppendAttachmentPoints.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 330
if _libs["pdfium"].has("FPDFAnnot_CountAttachmentPoints", "cdecl"):
    FPDFAnnot_CountAttachmentPoints = _libs["pdfium"].get("FPDFAnnot_CountAttachmentPoints", "cdecl")
    FPDFAnnot_CountAttachmentPoints.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_CountAttachmentPoints.restype = c_size_t

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 341
if _libs["pdfium"].has("FPDFAnnot_GetAttachmentPoints", "cdecl"):
    FPDFAnnot_GetAttachmentPoints = _libs["pdfium"].get("FPDFAnnot_GetAttachmentPoints", "cdecl")
    FPDFAnnot_GetAttachmentPoints.argtypes = [FPDF_ANNOTATION, c_size_t, POINTER(FS_QUADPOINTSF)]
    FPDFAnnot_GetAttachmentPoints.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 355
if _libs["pdfium"].has("FPDFAnnot_SetRect", "cdecl"):
    FPDFAnnot_SetRect = _libs["pdfium"].get("FPDFAnnot_SetRect", "cdecl")
    FPDFAnnot_SetRect.argtypes = [FPDF_ANNOTATION, POINTER(FS_RECTF)]
    FPDFAnnot_SetRect.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 365
if _libs["pdfium"].has("FPDFAnnot_GetRect", "cdecl"):
    FPDFAnnot_GetRect = _libs["pdfium"].get("FPDFAnnot_GetRect", "cdecl")
    FPDFAnnot_GetRect.argtypes = [FPDF_ANNOTATION, POINTER(FS_RECTF)]
    FPDFAnnot_GetRect.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 375
if _libs["pdfium"].has("FPDFAnnot_HasKey", "cdecl"):
    FPDFAnnot_HasKey = _libs["pdfium"].get("FPDFAnnot_HasKey", "cdecl")
    FPDFAnnot_HasKey.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING]
    FPDFAnnot_HasKey.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 386
if _libs["pdfium"].has("FPDFAnnot_GetValueType", "cdecl"):
    FPDFAnnot_GetValueType = _libs["pdfium"].get("FPDFAnnot_GetValueType", "cdecl")
    FPDFAnnot_GetValueType.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING]
    FPDFAnnot_GetValueType.restype = FPDF_OBJECT_TYPE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 399
if _libs["pdfium"].has("FPDFAnnot_SetStringValue", "cdecl"):
    FPDFAnnot_SetStringValue = _libs["pdfium"].get("FPDFAnnot_SetStringValue", "cdecl")
    FPDFAnnot_SetStringValue.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING, FPDF_WIDESTRING]
    FPDFAnnot_SetStringValue.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 419
if _libs["pdfium"].has("FPDFAnnot_GetStringValue", "cdecl"):
    FPDFAnnot_GetStringValue = _libs["pdfium"].get("FPDFAnnot_GetStringValue", "cdecl")
    FPDFAnnot_GetStringValue.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetStringValue.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 436
if _libs["pdfium"].has("FPDFAnnot_GetNumberValue", "cdecl"):
    FPDFAnnot_GetNumberValue = _libs["pdfium"].get("FPDFAnnot_GetNumberValue", "cdecl")
    FPDFAnnot_GetNumberValue.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING, POINTER(c_float)]
    FPDFAnnot_GetNumberValue.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 453
if _libs["pdfium"].has("FPDFAnnot_SetAP", "cdecl"):
    FPDFAnnot_SetAP = _libs["pdfium"].get("FPDFAnnot_SetAP", "cdecl")
    FPDFAnnot_SetAP.argtypes = [FPDF_ANNOTATION, FPDF_ANNOT_APPEARANCEMODE, FPDF_WIDESTRING]
    FPDFAnnot_SetAP.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 475
if _libs["pdfium"].has("FPDFAnnot_GetAP", "cdecl"):
    FPDFAnnot_GetAP = _libs["pdfium"].get("FPDFAnnot_GetAP", "cdecl")
    FPDFAnnot_GetAP.argtypes = [FPDF_ANNOTATION, FPDF_ANNOT_APPEARANCEMODE, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetAP.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 491
if _libs["pdfium"].has("FPDFAnnot_GetLinkedAnnot", "cdecl"):
    FPDFAnnot_GetLinkedAnnot = _libs["pdfium"].get("FPDFAnnot_GetLinkedAnnot", "cdecl")
    FPDFAnnot_GetLinkedAnnot.argtypes = [FPDF_ANNOTATION, FPDF_BYTESTRING]
    FPDFAnnot_GetLinkedAnnot.restype = FPDF_ANNOTATION

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 499
if _libs["pdfium"].has("FPDFAnnot_GetFlags", "cdecl"):
    FPDFAnnot_GetFlags = _libs["pdfium"].get("FPDFAnnot_GetFlags", "cdecl")
    FPDFAnnot_GetFlags.argtypes = [FPDF_ANNOTATION]
    FPDFAnnot_GetFlags.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 508
if _libs["pdfium"].has("FPDFAnnot_SetFlags", "cdecl"):
    FPDFAnnot_SetFlags = _libs["pdfium"].get("FPDFAnnot_SetFlags", "cdecl")
    FPDFAnnot_SetFlags.argtypes = [FPDF_ANNOTATION, c_int]
    FPDFAnnot_SetFlags.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 520
if _libs["pdfium"].has("FPDFAnnot_GetFormFieldFlags", "cdecl"):
    FPDFAnnot_GetFormFieldFlags = _libs["pdfium"].get("FPDFAnnot_GetFormFieldFlags", "cdecl")
    FPDFAnnot_GetFormFieldFlags.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_GetFormFieldFlags.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 537
if _libs["pdfium"].has("FPDFAnnot_GetFormFieldAtPoint", "cdecl"):
    FPDFAnnot_GetFormFieldAtPoint = _libs["pdfium"].get("FPDFAnnot_GetFormFieldAtPoint", "cdecl")
    FPDFAnnot_GetFormFieldAtPoint.argtypes = [FPDF_FORMHANDLE, FPDF_PAGE, POINTER(FS_POINTF)]
    FPDFAnnot_GetFormFieldAtPoint.restype = FPDF_ANNOTATION

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 555
if _libs["pdfium"].has("FPDFAnnot_GetFormFieldName", "cdecl"):
    FPDFAnnot_GetFormFieldName = _libs["pdfium"].get("FPDFAnnot_GetFormFieldName", "cdecl")
    FPDFAnnot_GetFormFieldName.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetFormFieldName.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 571
if _libs["pdfium"].has("FPDFAnnot_GetFormFieldType", "cdecl"):
    FPDFAnnot_GetFormFieldType = _libs["pdfium"].get("FPDFAnnot_GetFormFieldType", "cdecl")
    FPDFAnnot_GetFormFieldType.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_GetFormFieldType.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 587
if _libs["pdfium"].has("FPDFAnnot_GetFormFieldValue", "cdecl"):
    FPDFAnnot_GetFormFieldValue = _libs["pdfium"].get("FPDFAnnot_GetFormFieldValue", "cdecl")
    FPDFAnnot_GetFormFieldValue.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetFormFieldValue.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 602
if _libs["pdfium"].has("FPDFAnnot_GetOptionCount", "cdecl"):
    FPDFAnnot_GetOptionCount = _libs["pdfium"].get("FPDFAnnot_GetOptionCount", "cdecl")
    FPDFAnnot_GetOptionCount.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_GetOptionCount.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 624
if _libs["pdfium"].has("FPDFAnnot_GetOptionLabel", "cdecl"):
    FPDFAnnot_GetOptionLabel = _libs["pdfium"].get("FPDFAnnot_GetOptionLabel", "cdecl")
    FPDFAnnot_GetOptionLabel.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, c_int, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAnnot_GetOptionLabel.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 643
if _libs["pdfium"].has("FPDFAnnot_GetFontSize", "cdecl"):
    FPDFAnnot_GetFontSize = _libs["pdfium"].get("FPDFAnnot_GetFontSize", "cdecl")
    FPDFAnnot_GetFontSize.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION, POINTER(c_float)]
    FPDFAnnot_GetFontSize.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 656
if _libs["pdfium"].has("FPDFAnnot_IsChecked", "cdecl"):
    FPDFAnnot_IsChecked = _libs["pdfium"].get("FPDFAnnot_IsChecked", "cdecl")
    FPDFAnnot_IsChecked.argtypes = [FPDF_FORMHANDLE, FPDF_ANNOTATION]
    FPDFAnnot_IsChecked.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 22
if _libs["pdfium"].has("FPDFDoc_GetAttachmentCount", "cdecl"):
    FPDFDoc_GetAttachmentCount = _libs["pdfium"].get("FPDFDoc_GetAttachmentCount", "cdecl")
    FPDFDoc_GetAttachmentCount.argtypes = [FPDF_DOCUMENT]
    FPDFDoc_GetAttachmentCount.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 35
if _libs["pdfium"].has("FPDFDoc_AddAttachment", "cdecl"):
    FPDFDoc_AddAttachment = _libs["pdfium"].get("FPDFDoc_AddAttachment", "cdecl")
    FPDFDoc_AddAttachment.argtypes = [FPDF_DOCUMENT, FPDF_WIDESTRING]
    FPDFDoc_AddAttachment.restype = FPDF_ATTACHMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 46
if _libs["pdfium"].has("FPDFDoc_GetAttachment", "cdecl"):
    FPDFDoc_GetAttachment = _libs["pdfium"].get("FPDFDoc_GetAttachment", "cdecl")
    FPDFDoc_GetAttachment.argtypes = [FPDF_DOCUMENT, c_int]
    FPDFDoc_GetAttachment.restype = FPDF_ATTACHMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 59
if _libs["pdfium"].has("FPDFDoc_DeleteAttachment", "cdecl"):
    FPDFDoc_DeleteAttachment = _libs["pdfium"].get("FPDFDoc_DeleteAttachment", "cdecl")
    FPDFDoc_DeleteAttachment.argtypes = [FPDF_DOCUMENT, c_int]
    FPDFDoc_DeleteAttachment.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 72
if _libs["pdfium"].has("FPDFAttachment_GetName", "cdecl"):
    FPDFAttachment_GetName = _libs["pdfium"].get("FPDFAttachment_GetName", "cdecl")
    FPDFAttachment_GetName.argtypes = [FPDF_ATTACHMENT, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAttachment_GetName.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 84
if _libs["pdfium"].has("FPDFAttachment_HasKey", "cdecl"):
    FPDFAttachment_HasKey = _libs["pdfium"].get("FPDFAttachment_HasKey", "cdecl")
    FPDFAttachment_HasKey.argtypes = [FPDF_ATTACHMENT, FPDF_BYTESTRING]
    FPDFAttachment_HasKey.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 95
if _libs["pdfium"].has("FPDFAttachment_GetValueType", "cdecl"):
    FPDFAttachment_GetValueType = _libs["pdfium"].get("FPDFAttachment_GetValueType", "cdecl")
    FPDFAttachment_GetValueType.argtypes = [FPDF_ATTACHMENT, FPDF_BYTESTRING]
    FPDFAttachment_GetValueType.restype = FPDF_OBJECT_TYPE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 108
if _libs["pdfium"].has("FPDFAttachment_SetStringValue", "cdecl"):
    FPDFAttachment_SetStringValue = _libs["pdfium"].get("FPDFAttachment_SetStringValue", "cdecl")
    FPDFAttachment_SetStringValue.argtypes = [FPDF_ATTACHMENT, FPDF_BYTESTRING, FPDF_WIDESTRING]
    FPDFAttachment_SetStringValue.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 129
if _libs["pdfium"].has("FPDFAttachment_GetStringValue", "cdecl"):
    FPDFAttachment_GetStringValue = _libs["pdfium"].get("FPDFAttachment_GetStringValue", "cdecl")
    FPDFAttachment_GetStringValue.argtypes = [FPDF_ATTACHMENT, FPDF_BYTESTRING, POINTER(FPDF_WCHAR), c_ulong]
    FPDFAttachment_GetStringValue.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 146
if _libs["pdfium"].has("FPDFAttachment_SetFile", "cdecl"):
    FPDFAttachment_SetFile = _libs["pdfium"].get("FPDFAttachment_SetFile", "cdecl")
    FPDFAttachment_SetFile.argtypes = [FPDF_ATTACHMENT, FPDF_DOCUMENT, POINTER(None), c_ulong]
    FPDFAttachment_SetFile.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_attachment.h: 162
if _libs["pdfium"].has("FPDFAttachment_GetFile", "cdecl"):
    FPDFAttachment_GetFile = _libs["pdfium"].get("FPDFAttachment_GetFile", "cdecl")
    FPDFAttachment_GetFile.argtypes = [FPDF_ATTACHMENT, POINTER(None), c_ulong]
    FPDFAttachment_GetFile.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_catalog.h: 28
if _libs["pdfium"].has("FPDFCatalog_IsTagged", "cdecl"):
    FPDFCatalog_IsTagged = _libs["pdfium"].get("FPDFCatalog_IsTagged", "cdecl")
    FPDFCatalog_IsTagged.argtypes = [FPDF_DOCUMENT]
    FPDFCatalog_IsTagged.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 33
class struct__FX_FILEAVAIL(Structure):
    pass

struct__FX_FILEAVAIL.__slots__ = [
    'version',
    'IsDataAvail',
]
struct__FX_FILEAVAIL._fields_ = [
    ('version', c_int),
    ('IsDataAvail', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__FX_FILEAVAIL), c_size_t, c_size_t)),
]

FX_FILEAVAIL = struct__FX_FILEAVAIL# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 52

FPDF_AVAIL = POINTER(None)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 53

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 63
if _libs["pdfium"].has("FPDFAvail_Create", "cdecl"):
    FPDFAvail_Create = _libs["pdfium"].get("FPDFAvail_Create", "cdecl")
    FPDFAvail_Create.argtypes = [POINTER(FX_FILEAVAIL), POINTER(FPDF_FILEACCESS)]
    FPDFAvail_Create.restype = FPDF_AVAIL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 69
if _libs["pdfium"].has("FPDFAvail_Destroy", "cdecl"):
    FPDFAvail_Destroy = _libs["pdfium"].get("FPDFAvail_Destroy", "cdecl")
    FPDFAvail_Destroy.argtypes = [FPDF_AVAIL]
    FPDFAvail_Destroy.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 72
class struct__FX_DOWNLOADHINTS(Structure):
    pass

struct__FX_DOWNLOADHINTS.__slots__ = [
    'version',
    'AddSegment',
]
struct__FX_DOWNLOADHINTS._fields_ = [
    ('version', c_int),
    ('AddSegment', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FX_DOWNLOADHINTS), c_size_t, c_size_t)),
]

FX_DOWNLOADHINTS = struct__FX_DOWNLOADHINTS# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 91

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 110
if _libs["pdfium"].has("FPDFAvail_IsDocAvail", "cdecl"):
    FPDFAvail_IsDocAvail = _libs["pdfium"].get("FPDFAvail_IsDocAvail", "cdecl")
    FPDFAvail_IsDocAvail.argtypes = [FPDF_AVAIL, POINTER(FX_DOWNLOADHINTS)]
    FPDFAvail_IsDocAvail.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 125
if _libs["pdfium"].has("FPDFAvail_GetDocument", "cdecl"):
    FPDFAvail_GetDocument = _libs["pdfium"].get("FPDFAvail_GetDocument", "cdecl")
    FPDFAvail_GetDocument.argtypes = [FPDF_AVAIL, FPDF_BYTESTRING]
    FPDFAvail_GetDocument.restype = FPDF_DOCUMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 136
if _libs["pdfium"].has("FPDFAvail_GetFirstPageNum", "cdecl"):
    FPDFAvail_GetFirstPageNum = _libs["pdfium"].get("FPDFAvail_GetFirstPageNum", "cdecl")
    FPDFAvail_GetFirstPageNum.argtypes = [FPDF_DOCUMENT]
    FPDFAvail_GetFirstPageNum.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 158
if _libs["pdfium"].has("FPDFAvail_IsPageAvail", "cdecl"):
    FPDFAvail_IsPageAvail = _libs["pdfium"].get("FPDFAvail_IsPageAvail", "cdecl")
    FPDFAvail_IsPageAvail.argtypes = [FPDF_AVAIL, c_int, POINTER(FX_DOWNLOADHINTS)]
    FPDFAvail_IsPageAvail.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 183
if _libs["pdfium"].has("FPDFAvail_IsFormAvail", "cdecl"):
    FPDFAvail_IsFormAvail = _libs["pdfium"].get("FPDFAvail_IsFormAvail", "cdecl")
    FPDFAvail_IsFormAvail.argtypes = [FPDF_AVAIL, POINTER(FX_DOWNLOADHINTS)]
    FPDFAvail_IsFormAvail.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 199
if _libs["pdfium"].has("FPDFAvail_IsLinearized", "cdecl"):
    FPDFAvail_IsLinearized = _libs["pdfium"].get("FPDFAvail_IsLinearized", "cdecl")
    FPDFAvail_IsLinearized.argtypes = [FPDF_AVAIL]
    FPDFAvail_IsLinearized.restype = c_int

__darwin_time_t = c_long# /Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/usr/include/i386/_types.h: 120

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 89
class struct_FPDF_IMAGEOBJ_METADATA(Structure):
    pass

struct_FPDF_IMAGEOBJ_METADATA.__slots__ = [
    'width',
    'height',
    'horizontal_dpi',
    'vertical_dpi',
    'bits_per_pixel',
    'colorspace',
    'marked_content_id',
]
struct_FPDF_IMAGEOBJ_METADATA._fields_ = [
    ('width', c_uint),
    ('height', c_uint),
    ('horizontal_dpi', c_float),
    ('vertical_dpi', c_float),
    ('bits_per_pixel', c_uint),
    ('colorspace', c_int),
    ('marked_content_id', c_int),
]

FPDF_IMAGEOBJ_METADATA = struct_FPDF_IMAGEOBJ_METADATA# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 89

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 98
if _libs["pdfium"].has("FPDF_CreateNewDocument", "cdecl"):
    FPDF_CreateNewDocument = _libs["pdfium"].get("FPDF_CreateNewDocument", "cdecl")
    FPDF_CreateNewDocument.argtypes = []
    FPDF_CreateNewDocument.restype = FPDF_DOCUMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 113
if _libs["pdfium"].has("FPDFPage_New", "cdecl"):
    FPDFPage_New = _libs["pdfium"].get("FPDFPage_New", "cdecl")
    FPDFPage_New.argtypes = [FPDF_DOCUMENT, c_int, c_double, c_double]
    FPDFPage_New.restype = FPDF_PAGE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 122
if _libs["pdfium"].has("FPDFPage_Delete", "cdecl"):
    FPDFPage_Delete = _libs["pdfium"].get("FPDFPage_Delete", "cdecl")
    FPDFPage_Delete.argtypes = [FPDF_DOCUMENT, c_int]
    FPDFPage_Delete.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 134
if _libs["pdfium"].has("FPDFPage_GetRotation", "cdecl"):
    FPDFPage_GetRotation = _libs["pdfium"].get("FPDFPage_GetRotation", "cdecl")
    FPDFPage_GetRotation.argtypes = [FPDF_PAGE]
    FPDFPage_GetRotation.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 144
if _libs["pdfium"].has("FPDFPage_SetRotation", "cdecl"):
    FPDFPage_SetRotation = _libs["pdfium"].get("FPDFPage_SetRotation", "cdecl")
    FPDFPage_SetRotation.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_SetRotation.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 151
if _libs["pdfium"].has("FPDFPage_InsertObject", "cdecl"):
    FPDFPage_InsertObject = _libs["pdfium"].get("FPDFPage_InsertObject", "cdecl")
    FPDFPage_InsertObject.argtypes = [FPDF_PAGE, FPDF_PAGEOBJECT]
    FPDFPage_InsertObject.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 165
if _libs["pdfium"].has("FPDFPage_RemoveObject", "cdecl"):
    FPDFPage_RemoveObject = _libs["pdfium"].get("FPDFPage_RemoveObject", "cdecl")
    FPDFPage_RemoveObject.argtypes = [FPDF_PAGE, FPDF_PAGEOBJECT]
    FPDFPage_RemoveObject.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 172
if _libs["pdfium"].has("FPDFPage_CountObjects", "cdecl"):
    FPDFPage_CountObjects = _libs["pdfium"].get("FPDFPage_CountObjects", "cdecl")
    FPDFPage_CountObjects.argtypes = [FPDF_PAGE]
    FPDFPage_CountObjects.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 180
if _libs["pdfium"].has("FPDFPage_GetObject", "cdecl"):
    FPDFPage_GetObject = _libs["pdfium"].get("FPDFPage_GetObject", "cdecl")
    FPDFPage_GetObject.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_GetObject.restype = FPDF_PAGEOBJECT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 188
if _libs["pdfium"].has("FPDFPage_HasTransparency", "cdecl"):
    FPDFPage_HasTransparency = _libs["pdfium"].get("FPDFPage_HasTransparency", "cdecl")
    FPDFPage_HasTransparency.argtypes = [FPDF_PAGE]
    FPDFPage_HasTransparency.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 198
if _libs["pdfium"].has("FPDFPage_GenerateContent", "cdecl"):
    FPDFPage_GenerateContent = _libs["pdfium"].get("FPDFPage_GenerateContent", "cdecl")
    FPDFPage_GenerateContent.argtypes = [FPDF_PAGE]
    FPDFPage_GenerateContent.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 207
if _libs["pdfium"].has("FPDFPageObj_Destroy", "cdecl"):
    FPDFPageObj_Destroy = _libs["pdfium"].get("FPDFPageObj_Destroy", "cdecl")
    FPDFPageObj_Destroy.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_Destroy.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 215
if _libs["pdfium"].has("FPDFPageObj_HasTransparency", "cdecl"):
    FPDFPageObj_HasTransparency = _libs["pdfium"].get("FPDFPageObj_HasTransparency", "cdecl")
    FPDFPageObj_HasTransparency.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_HasTransparency.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 223
if _libs["pdfium"].has("FPDFPageObj_GetType", "cdecl"):
    FPDFPageObj_GetType = _libs["pdfium"].get("FPDFPageObj_GetType", "cdecl")
    FPDFPageObj_GetType.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetType.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 240
if _libs["pdfium"].has("FPDFPageObj_Transform", "cdecl"):
    FPDFPageObj_Transform = _libs["pdfium"].get("FPDFPageObj_Transform", "cdecl")
    FPDFPageObj_Transform.argtypes = [FPDF_PAGEOBJECT, c_double, c_double, c_double, c_double, c_double, c_double]
    FPDFPageObj_Transform.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 262
if _libs["pdfium"].has("FPDFPage_TransformAnnots", "cdecl"):
    FPDFPage_TransformAnnots = _libs["pdfium"].get("FPDFPage_TransformAnnots", "cdecl")
    FPDFPage_TransformAnnots.argtypes = [FPDF_PAGE, c_double, c_double, c_double, c_double, c_double, c_double]
    FPDFPage_TransformAnnots.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 276
if _libs["pdfium"].has("FPDFPageObj_NewImageObj", "cdecl"):
    FPDFPageObj_NewImageObj = _libs["pdfium"].get("FPDFPageObj_NewImageObj", "cdecl")
    FPDFPageObj_NewImageObj.argtypes = [FPDF_DOCUMENT]
    FPDFPageObj_NewImageObj.restype = FPDF_PAGEOBJECT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 286
if _libs["pdfium"].has("FPDFPageObj_CountMarks", "cdecl"):
    FPDFPageObj_CountMarks = _libs["pdfium"].get("FPDFPageObj_CountMarks", "cdecl")
    FPDFPageObj_CountMarks.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_CountMarks.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 299
if _libs["pdfium"].has("FPDFPageObj_GetMark", "cdecl"):
    FPDFPageObj_GetMark = _libs["pdfium"].get("FPDFPageObj_GetMark", "cdecl")
    FPDFPageObj_GetMark.argtypes = [FPDF_PAGEOBJECT, c_ulong]
    FPDFPageObj_GetMark.restype = FPDF_PAGEOBJECTMARK

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 312
if _libs["pdfium"].has("FPDFPageObj_AddMark", "cdecl"):
    FPDFPageObj_AddMark = _libs["pdfium"].get("FPDFPageObj_AddMark", "cdecl")
    FPDFPageObj_AddMark.argtypes = [FPDF_PAGEOBJECT, FPDF_BYTESTRING]
    FPDFPageObj_AddMark.restype = FPDF_PAGEOBJECTMARK

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 323
if _libs["pdfium"].has("FPDFPageObj_RemoveMark", "cdecl"):
    FPDFPageObj_RemoveMark = _libs["pdfium"].get("FPDFPageObj_RemoveMark", "cdecl")
    FPDFPageObj_RemoveMark.argtypes = [FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK]
    FPDFPageObj_RemoveMark.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 339
if _libs["pdfium"].has("FPDFPageObjMark_GetName", "cdecl"):
    FPDFPageObjMark_GetName = _libs["pdfium"].get("FPDFPageObjMark_GetName", "cdecl")
    FPDFPageObjMark_GetName.argtypes = [FPDF_PAGEOBJECTMARK, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFPageObjMark_GetName.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 352
if _libs["pdfium"].has("FPDFPageObjMark_CountParams", "cdecl"):
    FPDFPageObjMark_CountParams = _libs["pdfium"].get("FPDFPageObjMark_CountParams", "cdecl")
    FPDFPageObjMark_CountParams.argtypes = [FPDF_PAGEOBJECTMARK]
    FPDFPageObjMark_CountParams.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 369
if _libs["pdfium"].has("FPDFPageObjMark_GetParamKey", "cdecl"):
    FPDFPageObjMark_GetParamKey = _libs["pdfium"].get("FPDFPageObjMark_GetParamKey", "cdecl")
    FPDFPageObjMark_GetParamKey.argtypes = [FPDF_PAGEOBJECTMARK, c_ulong, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFPageObjMark_GetParamKey.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 383
if _libs["pdfium"].has("FPDFPageObjMark_GetParamValueType", "cdecl"):
    FPDFPageObjMark_GetParamValueType = _libs["pdfium"].get("FPDFPageObjMark_GetParamValueType", "cdecl")
    FPDFPageObjMark_GetParamValueType.argtypes = [FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING]
    FPDFPageObjMark_GetParamValueType.restype = FPDF_OBJECT_TYPE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 398
if _libs["pdfium"].has("FPDFPageObjMark_GetParamIntValue", "cdecl"):
    FPDFPageObjMark_GetParamIntValue = _libs["pdfium"].get("FPDFPageObjMark_GetParamIntValue", "cdecl")
    FPDFPageObjMark_GetParamIntValue.argtypes = [FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, POINTER(c_int)]
    FPDFPageObjMark_GetParamIntValue.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 418
if _libs["pdfium"].has("FPDFPageObjMark_GetParamStringValue", "cdecl"):
    FPDFPageObjMark_GetParamStringValue = _libs["pdfium"].get("FPDFPageObjMark_GetParamStringValue", "cdecl")
    FPDFPageObjMark_GetParamStringValue.argtypes = [FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFPageObjMark_GetParamStringValue.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 439
if _libs["pdfium"].has("FPDFPageObjMark_GetParamBlobValue", "cdecl"):
    FPDFPageObjMark_GetParamBlobValue = _libs["pdfium"].get("FPDFPageObjMark_GetParamBlobValue", "cdecl")
    FPDFPageObjMark_GetParamBlobValue.argtypes = [FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, POINTER(None), c_ulong, POINTER(c_ulong)]
    FPDFPageObjMark_GetParamBlobValue.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 458
if _libs["pdfium"].has("FPDFPageObjMark_SetIntParam", "cdecl"):
    FPDFPageObjMark_SetIntParam = _libs["pdfium"].get("FPDFPageObjMark_SetIntParam", "cdecl")
    FPDFPageObjMark_SetIntParam.argtypes = [FPDF_DOCUMENT, FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, c_int]
    FPDFPageObjMark_SetIntParam.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 477
if _libs["pdfium"].has("FPDFPageObjMark_SetStringParam", "cdecl"):
    FPDFPageObjMark_SetStringParam = _libs["pdfium"].get("FPDFPageObjMark_SetStringParam", "cdecl")
    FPDFPageObjMark_SetStringParam.argtypes = [FPDF_DOCUMENT, FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, FPDF_BYTESTRING]
    FPDFPageObjMark_SetStringParam.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 497
if _libs["pdfium"].has("FPDFPageObjMark_SetBlobParam", "cdecl"):
    FPDFPageObjMark_SetBlobParam = _libs["pdfium"].get("FPDFPageObjMark_SetBlobParam", "cdecl")
    FPDFPageObjMark_SetBlobParam.argtypes = [FPDF_DOCUMENT, FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING, POINTER(None), c_ulong]
    FPDFPageObjMark_SetBlobParam.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 513
if _libs["pdfium"].has("FPDFPageObjMark_RemoveParam", "cdecl"):
    FPDFPageObjMark_RemoveParam = _libs["pdfium"].get("FPDFPageObjMark_RemoveParam", "cdecl")
    FPDFPageObjMark_RemoveParam.argtypes = [FPDF_PAGEOBJECT, FPDF_PAGEOBJECTMARK, FPDF_BYTESTRING]
    FPDFPageObjMark_RemoveParam.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 532
if _libs["pdfium"].has("FPDFImageObj_LoadJpegFile", "cdecl"):
    FPDFImageObj_LoadJpegFile = _libs["pdfium"].get("FPDFImageObj_LoadJpegFile", "cdecl")
    FPDFImageObj_LoadJpegFile.argtypes = [POINTER(FPDF_PAGE), c_int, FPDF_PAGEOBJECT, POINTER(FPDF_FILEACCESS)]
    FPDFImageObj_LoadJpegFile.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 554
if _libs["pdfium"].has("FPDFImageObj_LoadJpegFileInline", "cdecl"):
    FPDFImageObj_LoadJpegFileInline = _libs["pdfium"].get("FPDFImageObj_LoadJpegFileInline", "cdecl")
    FPDFImageObj_LoadJpegFileInline.argtypes = [POINTER(FPDF_PAGE), c_int, FPDF_PAGEOBJECT, POINTER(FPDF_FILEACCESS)]
    FPDFImageObj_LoadJpegFileInline.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 577
if _libs["pdfium"].has("FPDFImageObj_GetMatrix", "cdecl"):
    FPDFImageObj_GetMatrix = _libs["pdfium"].get("FPDFImageObj_GetMatrix", "cdecl")
    FPDFImageObj_GetMatrix.argtypes = [FPDF_PAGEOBJECT, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    FPDFImageObj_GetMatrix.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 602
if _libs["pdfium"].has("FPDFImageObj_SetMatrix", "cdecl"):
    FPDFImageObj_SetMatrix = _libs["pdfium"].get("FPDFImageObj_SetMatrix", "cdecl")
    FPDFImageObj_SetMatrix.argtypes = [FPDF_PAGEOBJECT, c_double, c_double, c_double, c_double, c_double, c_double]
    FPDFImageObj_SetMatrix.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 619
if _libs["pdfium"].has("FPDFImageObj_SetBitmap", "cdecl"):
    FPDFImageObj_SetBitmap = _libs["pdfium"].get("FPDFImageObj_SetBitmap", "cdecl")
    FPDFImageObj_SetBitmap.argtypes = [POINTER(FPDF_PAGE), c_int, FPDF_PAGEOBJECT, FPDF_BITMAP]
    FPDFImageObj_SetBitmap.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 632
if _libs["pdfium"].has("FPDFImageObj_GetBitmap", "cdecl"):
    FPDFImageObj_GetBitmap = _libs["pdfium"].get("FPDFImageObj_GetBitmap", "cdecl")
    FPDFImageObj_GetBitmap.argtypes = [FPDF_PAGEOBJECT]
    FPDFImageObj_GetBitmap.restype = FPDF_BITMAP

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 645
if _libs["pdfium"].has("FPDFImageObj_GetImageDataDecoded", "cdecl"):
    FPDFImageObj_GetImageDataDecoded = _libs["pdfium"].get("FPDFImageObj_GetImageDataDecoded", "cdecl")
    FPDFImageObj_GetImageDataDecoded.argtypes = [FPDF_PAGEOBJECT, POINTER(None), c_ulong]
    FPDFImageObj_GetImageDataDecoded.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 659
if _libs["pdfium"].has("FPDFImageObj_GetImageDataRaw", "cdecl"):
    FPDFImageObj_GetImageDataRaw = _libs["pdfium"].get("FPDFImageObj_GetImageDataRaw", "cdecl")
    FPDFImageObj_GetImageDataRaw.argtypes = [FPDF_PAGEOBJECT, POINTER(None), c_ulong]
    FPDFImageObj_GetImageDataRaw.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 669
if _libs["pdfium"].has("FPDFImageObj_GetImageFilterCount", "cdecl"):
    FPDFImageObj_GetImageFilterCount = _libs["pdfium"].get("FPDFImageObj_GetImageFilterCount", "cdecl")
    FPDFImageObj_GetImageFilterCount.argtypes = [FPDF_PAGEOBJECT]
    FPDFImageObj_GetImageFilterCount.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 683
if _libs["pdfium"].has("FPDFImageObj_GetImageFilter", "cdecl"):
    FPDFImageObj_GetImageFilter = _libs["pdfium"].get("FPDFImageObj_GetImageFilter", "cdecl")
    FPDFImageObj_GetImageFilter.argtypes = [FPDF_PAGEOBJECT, c_int, POINTER(None), c_ulong]
    FPDFImageObj_GetImageFilter.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 700
if _libs["pdfium"].has("FPDFImageObj_GetImageMetadata", "cdecl"):
    FPDFImageObj_GetImageMetadata = _libs["pdfium"].get("FPDFImageObj_GetImageMetadata", "cdecl")
    FPDFImageObj_GetImageMetadata.argtypes = [FPDF_PAGEOBJECT, FPDF_PAGE, POINTER(FPDF_IMAGEOBJ_METADATA)]
    FPDFImageObj_GetImageMetadata.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 710
if _libs["pdfium"].has("FPDFPageObj_CreateNewPath", "cdecl"):
    FPDFPageObj_CreateNewPath = _libs["pdfium"].get("FPDFPageObj_CreateNewPath", "cdecl")
    FPDFPageObj_CreateNewPath.argtypes = [c_float, c_float]
    FPDFPageObj_CreateNewPath.restype = FPDF_PAGEOBJECT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 721
if _libs["pdfium"].has("FPDFPageObj_CreateNewRect", "cdecl"):
    FPDFPageObj_CreateNewRect = _libs["pdfium"].get("FPDFPageObj_CreateNewRect", "cdecl")
    FPDFPageObj_CreateNewRect.argtypes = [c_float, c_float, c_float, c_float]
    FPDFPageObj_CreateNewRect.restype = FPDF_PAGEOBJECT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 736
if _libs["pdfium"].has("FPDFPageObj_GetBounds", "cdecl"):
    FPDFPageObj_GetBounds = _libs["pdfium"].get("FPDFPageObj_GetBounds", "cdecl")
    FPDFPageObj_GetBounds.argtypes = [FPDF_PAGEOBJECT, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPageObj_GetBounds.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 751
if _libs["pdfium"].has("FPDFPageObj_SetBlendMode", "cdecl"):
    FPDFPageObj_SetBlendMode = _libs["pdfium"].get("FPDFPageObj_SetBlendMode", "cdecl")
    FPDFPageObj_SetBlendMode.argtypes = [FPDF_PAGEOBJECT, FPDF_BYTESTRING]
    FPDFPageObj_SetBlendMode.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 764
if _libs["pdfium"].has("FPDFPageObj_SetStrokeColor", "cdecl"):
    FPDFPageObj_SetStrokeColor = _libs["pdfium"].get("FPDFPageObj_SetStrokeColor", "cdecl")
    FPDFPageObj_SetStrokeColor.argtypes = [FPDF_PAGEOBJECT, c_uint, c_uint, c_uint, c_uint]
    FPDFPageObj_SetStrokeColor.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 780
if _libs["pdfium"].has("FPDFPageObj_GetStrokeColor", "cdecl"):
    FPDFPageObj_GetStrokeColor = _libs["pdfium"].get("FPDFPageObj_GetStrokeColor", "cdecl")
    FPDFPageObj_GetStrokeColor.argtypes = [FPDF_PAGEOBJECT, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFPageObj_GetStrokeColor.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 793
if _libs["pdfium"].has("FPDFPageObj_SetStrokeWidth", "cdecl"):
    FPDFPageObj_SetStrokeWidth = _libs["pdfium"].get("FPDFPageObj_SetStrokeWidth", "cdecl")
    FPDFPageObj_SetStrokeWidth.argtypes = [FPDF_PAGEOBJECT, c_float]
    FPDFPageObj_SetStrokeWidth.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 803
if _libs["pdfium"].has("FPDFPageObj_GetStrokeWidth", "cdecl"):
    FPDFPageObj_GetStrokeWidth = _libs["pdfium"].get("FPDFPageObj_GetStrokeWidth", "cdecl")
    FPDFPageObj_GetStrokeWidth.argtypes = [FPDF_PAGEOBJECT, POINTER(c_float)]
    FPDFPageObj_GetStrokeWidth.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 813
if _libs["pdfium"].has("FPDFPageObj_GetLineJoin", "cdecl"):
    FPDFPageObj_GetLineJoin = _libs["pdfium"].get("FPDFPageObj_GetLineJoin", "cdecl")
    FPDFPageObj_GetLineJoin.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetLineJoin.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 823
if _libs["pdfium"].has("FPDFPageObj_SetLineJoin", "cdecl"):
    FPDFPageObj_SetLineJoin = _libs["pdfium"].get("FPDFPageObj_SetLineJoin", "cdecl")
    FPDFPageObj_SetLineJoin.argtypes = [FPDF_PAGEOBJECT, c_int]
    FPDFPageObj_SetLineJoin.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 833
if _libs["pdfium"].has("FPDFPageObj_GetLineCap", "cdecl"):
    FPDFPageObj_GetLineCap = _libs["pdfium"].get("FPDFPageObj_GetLineCap", "cdecl")
    FPDFPageObj_GetLineCap.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetLineCap.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 843
if _libs["pdfium"].has("FPDFPageObj_SetLineCap", "cdecl"):
    FPDFPageObj_SetLineCap = _libs["pdfium"].get("FPDFPageObj_SetLineCap", "cdecl")
    FPDFPageObj_SetLineCap.argtypes = [FPDF_PAGEOBJECT, c_int]
    FPDFPageObj_SetLineCap.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 855
if _libs["pdfium"].has("FPDFPageObj_SetFillColor", "cdecl"):
    FPDFPageObj_SetFillColor = _libs["pdfium"].get("FPDFPageObj_SetFillColor", "cdecl")
    FPDFPageObj_SetFillColor.argtypes = [FPDF_PAGEOBJECT, c_uint, c_uint, c_uint, c_uint]
    FPDFPageObj_SetFillColor.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 871
if _libs["pdfium"].has("FPDFPageObj_GetFillColor", "cdecl"):
    FPDFPageObj_GetFillColor = _libs["pdfium"].get("FPDFPageObj_GetFillColor", "cdecl")
    FPDFPageObj_GetFillColor.argtypes = [FPDF_PAGEOBJECT, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFPageObj_GetFillColor.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 886
if _libs["pdfium"].has("FPDFPath_CountSegments", "cdecl"):
    FPDFPath_CountSegments = _libs["pdfium"].get("FPDFPath_CountSegments", "cdecl")
    FPDFPath_CountSegments.argtypes = [FPDF_PAGEOBJECT]
    FPDFPath_CountSegments.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 896
if _libs["pdfium"].has("FPDFPath_GetPathSegment", "cdecl"):
    FPDFPath_GetPathSegment = _libs["pdfium"].get("FPDFPath_GetPathSegment", "cdecl")
    FPDFPath_GetPathSegment.argtypes = [FPDF_PAGEOBJECT, c_int]
    FPDFPath_GetPathSegment.restype = FPDF_PATHSEGMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 907
if _libs["pdfium"].has("FPDFPathSegment_GetPoint", "cdecl"):
    FPDFPathSegment_GetPoint = _libs["pdfium"].get("FPDFPathSegment_GetPoint", "cdecl")
    FPDFPathSegment_GetPoint.argtypes = [FPDF_PATHSEGMENT, POINTER(c_float), POINTER(c_float)]
    FPDFPathSegment_GetPoint.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 916
if _libs["pdfium"].has("FPDFPathSegment_GetType", "cdecl"):
    FPDFPathSegment_GetType = _libs["pdfium"].get("FPDFPathSegment_GetType", "cdecl")
    FPDFPathSegment_GetType.argtypes = [FPDF_PATHSEGMENT]
    FPDFPathSegment_GetType.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 925
if _libs["pdfium"].has("FPDFPathSegment_GetClose", "cdecl"):
    FPDFPathSegment_GetClose = _libs["pdfium"].get("FPDFPathSegment_GetClose", "cdecl")
    FPDFPathSegment_GetClose.argtypes = [FPDF_PATHSEGMENT]
    FPDFPathSegment_GetClose.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 937
if _libs["pdfium"].has("FPDFPath_MoveTo", "cdecl"):
    FPDFPath_MoveTo = _libs["pdfium"].get("FPDFPath_MoveTo", "cdecl")
    FPDFPath_MoveTo.argtypes = [FPDF_PAGEOBJECT, c_float, c_float]
    FPDFPath_MoveTo.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 950
if _libs["pdfium"].has("FPDFPath_LineTo", "cdecl"):
    FPDFPath_LineTo = _libs["pdfium"].get("FPDFPath_LineTo", "cdecl")
    FPDFPath_LineTo.argtypes = [FPDF_PAGEOBJECT, c_float, c_float]
    FPDFPath_LineTo.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 965
if _libs["pdfium"].has("FPDFPath_BezierTo", "cdecl"):
    FPDFPath_BezierTo = _libs["pdfium"].get("FPDFPath_BezierTo", "cdecl")
    FPDFPath_BezierTo.argtypes = [FPDF_PAGEOBJECT, c_float, c_float, c_float, c_float, c_float, c_float]
    FPDFPath_BezierTo.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 981
if _libs["pdfium"].has("FPDFPath_Close", "cdecl"):
    FPDFPath_Close = _libs["pdfium"].get("FPDFPath_Close", "cdecl")
    FPDFPath_Close.argtypes = [FPDF_PAGEOBJECT]
    FPDFPath_Close.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 990
if _libs["pdfium"].has("FPDFPath_SetDrawMode", "cdecl"):
    FPDFPath_SetDrawMode = _libs["pdfium"].get("FPDFPath_SetDrawMode", "cdecl")
    FPDFPath_SetDrawMode.argtypes = [FPDF_PAGEOBJECT, c_int, FPDF_BOOL]
    FPDFPath_SetDrawMode.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1002
if _libs["pdfium"].has("FPDFPath_GetDrawMode", "cdecl"):
    FPDFPath_GetDrawMode = _libs["pdfium"].get("FPDFPath_GetDrawMode", "cdecl")
    FPDFPath_GetDrawMode.argtypes = [FPDF_PAGEOBJECT, POINTER(c_int), POINTER(FPDF_BOOL)]
    FPDFPath_GetDrawMode.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1018
if _libs["pdfium"].has("FPDFPath_GetMatrix", "cdecl"):
    FPDFPath_GetMatrix = _libs["pdfium"].get("FPDFPath_GetMatrix", "cdecl")
    FPDFPath_GetMatrix.argtypes = [FPDF_PAGEOBJECT, POINTER(FS_MATRIX)]
    FPDFPath_GetMatrix.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1033
if _libs["pdfium"].has("FPDFPath_SetMatrix", "cdecl"):
    FPDFPath_SetMatrix = _libs["pdfium"].get("FPDFPath_SetMatrix", "cdecl")
    FPDFPath_SetMatrix.argtypes = [FPDF_PAGEOBJECT, POINTER(FS_MATRIX)]
    FPDFPath_SetMatrix.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1044
if _libs["pdfium"].has("FPDFPageObj_NewTextObj", "cdecl"):
    FPDFPageObj_NewTextObj = _libs["pdfium"].get("FPDFPageObj_NewTextObj", "cdecl")
    FPDFPageObj_NewTextObj.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING, c_float]
    FPDFPageObj_NewTextObj.restype = FPDF_PAGEOBJECT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1055
if _libs["pdfium"].has("FPDFText_SetText", "cdecl"):
    FPDFText_SetText = _libs["pdfium"].get("FPDFText_SetText", "cdecl")
    FPDFText_SetText.argtypes = [FPDF_PAGEOBJECT, FPDF_WIDESTRING]
    FPDFText_SetText.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1070
if _libs["pdfium"].has("FPDFText_LoadFont", "cdecl"):
    FPDFText_LoadFont = _libs["pdfium"].get("FPDFText_LoadFont", "cdecl")
    FPDFText_LoadFont.argtypes = [FPDF_DOCUMENT, POINTER(c_uint8), c_uint32, c_int, FPDF_BOOL]
    FPDFText_LoadFont.restype = FPDF_FONT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1088
if _libs["pdfium"].has("FPDFText_LoadStandardFont", "cdecl"):
    FPDFText_LoadStandardFont = _libs["pdfium"].get("FPDFText_LoadStandardFont", "cdecl")
    FPDFText_LoadStandardFont.argtypes = [FPDF_DOCUMENT, FPDF_BYTESTRING]
    FPDFText_LoadStandardFont.restype = FPDF_FONT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1102
if _libs["pdfium"].has("FPDFTextObj_GetMatrix", "cdecl"):
    FPDFTextObj_GetMatrix = _libs["pdfium"].get("FPDFTextObj_GetMatrix", "cdecl")
    FPDFTextObj_GetMatrix.argtypes = [FPDF_PAGEOBJECT, POINTER(FS_MATRIX)]
    FPDFTextObj_GetMatrix.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1112
if _libs["pdfium"].has("FPDFTextObj_GetFontSize", "cdecl"):
    FPDFTextObj_GetFontSize = _libs["pdfium"].get("FPDFTextObj_GetFontSize", "cdecl")
    FPDFTextObj_GetFontSize.argtypes = [FPDF_PAGEOBJECT]
    FPDFTextObj_GetFontSize.restype = c_float

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1117
if _libs["pdfium"].has("FPDFFont_Close", "cdecl"):
    FPDFFont_Close = _libs["pdfium"].get("FPDFFont_Close", "cdecl")
    FPDFFont_Close.argtypes = [FPDF_FONT]
    FPDFFont_Close.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1127
if _libs["pdfium"].has("FPDFPageObj_CreateTextObj", "cdecl"):
    FPDFPageObj_CreateTextObj = _libs["pdfium"].get("FPDFPageObj_CreateTextObj", "cdecl")
    FPDFPageObj_CreateTextObj.argtypes = [FPDF_DOCUMENT, FPDF_FONT, c_float]
    FPDFPageObj_CreateTextObj.restype = FPDF_PAGEOBJECT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1139
if _libs["pdfium"].has("FPDFTextObj_GetTextRenderMode", "cdecl"):
    FPDFTextObj_GetTextRenderMode = _libs["pdfium"].get("FPDFTextObj_GetTextRenderMode", "cdecl")
    FPDFTextObj_GetTextRenderMode.argtypes = [FPDF_PAGEOBJECT]
    FPDFTextObj_GetTextRenderMode.restype = FPDF_TEXT_RENDERMODE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1150
if _libs["pdfium"].has("FPDFTextObj_SetTextRenderMode", "cdecl"):
    FPDFTextObj_SetTextRenderMode = _libs["pdfium"].get("FPDFTextObj_SetTextRenderMode", "cdecl")
    FPDFTextObj_SetTextRenderMode.argtypes = [FPDF_PAGEOBJECT, FPDF_TEXT_RENDERMODE]
    FPDFTextObj_SetTextRenderMode.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1167
if _libs["pdfium"].has("FPDFTextObj_GetFontName", "cdecl"):
    FPDFTextObj_GetFontName = _libs["pdfium"].get("FPDFTextObj_GetFontName", "cdecl")
    FPDFTextObj_GetFontName.argtypes = [FPDF_PAGEOBJECT, POINTER(None), c_ulong]
    FPDFTextObj_GetFontName.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1186
if _libs["pdfium"].has("FPDFTextObj_GetText", "cdecl"):
    FPDFTextObj_GetText = _libs["pdfium"].get("FPDFTextObj_GetText", "cdecl")
    FPDFTextObj_GetText.argtypes = [FPDF_PAGEOBJECT, FPDF_TEXTPAGE, POINTER(None), c_ulong]
    FPDFTextObj_GetText.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1198
if _libs["pdfium"].has("FPDFFormObj_CountObjects", "cdecl"):
    FPDFFormObj_CountObjects = _libs["pdfium"].get("FPDFFormObj_CountObjects", "cdecl")
    FPDFFormObj_CountObjects.argtypes = [FPDF_PAGEOBJECT]
    FPDFFormObj_CountObjects.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1208
if _libs["pdfium"].has("FPDFFormObj_GetObject", "cdecl"):
    FPDFFormObj_GetObject = _libs["pdfium"].get("FPDFFormObj_GetObject", "cdecl")
    FPDFFormObj_GetObject.argtypes = [FPDF_PAGEOBJECT, c_ulong]
    FPDFFormObj_GetObject.restype = FPDF_PAGEOBJECT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 1223
if _libs["pdfium"].has("FPDFFormObj_GetMatrix", "cdecl"):
    FPDFFormObj_GetMatrix = _libs["pdfium"].get("FPDFFormObj_GetMatrix", "cdecl")
    FPDFFormObj_GetMatrix.argtypes = [FPDF_PAGEOBJECT, POINTER(FS_MATRIX)]
    FPDFFormObj_GetMatrix.restype = FPDF_BOOL

time_t = __darwin_time_t# /Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/usr/include/sys/_types/_time_t.h: 31

# /Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/usr/include/time.h: 74
class struct_tm(Structure):
    pass

struct_tm.__slots__ = [
    'tm_sec',
    'tm_min',
    'tm_hour',
    'tm_mday',
    'tm_mon',
    'tm_year',
    'tm_wday',
    'tm_yday',
    'tm_isdst',
    'tm_gmtoff',
    'tm_zone',
]
struct_tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', String),
]

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 51
class struct__UNSUPPORT_INFO(Structure):
    pass

struct__UNSUPPORT_INFO.__slots__ = [
    'version',
    'FSDK_UnSupport_Handler',
]
struct__UNSUPPORT_INFO._fields_ = [
    ('version', c_int),
    ('FSDK_UnSupport_Handler', CFUNCTYPE(UNCHECKED(None), POINTER(struct__UNSUPPORT_INFO), c_int)),
]

UNSUPPORT_INFO = struct__UNSUPPORT_INFO# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 62

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 70
if _libs["pdfium"].has("FSDK_SetUnSpObjProcessHandler", "cdecl"):
    FSDK_SetUnSpObjProcessHandler = _libs["pdfium"].get("FSDK_SetUnSpObjProcessHandler", "cdecl")
    FSDK_SetUnSpObjProcessHandler.argtypes = [POINTER(UNSUPPORT_INFO)]
    FSDK_SetUnSpObjProcessHandler.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 79
if _libs["pdfium"].has("FSDK_SetTimeFunction", "cdecl"):
    FSDK_SetTimeFunction = _libs["pdfium"].get("FSDK_SetTimeFunction", "cdecl")
    FSDK_SetTimeFunction.argtypes = [CFUNCTYPE(UNCHECKED(time_t), )]
    FSDK_SetTimeFunction.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 89
if _libs["pdfium"].has("FSDK_SetLocaltimeFunction", "cdecl"):
    FSDK_SetLocaltimeFunction = _libs["pdfium"].get("FSDK_SetLocaltimeFunction", "cdecl")
    FSDK_SetLocaltimeFunction.argtypes = [CFUNCTYPE(UNCHECKED(POINTER(struct_tm)), POINTER(time_t))]
    FSDK_SetLocaltimeFunction.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 113
if _libs["pdfium"].has("FPDFDoc_GetPageMode", "cdecl"):
    FPDFDoc_GetPageMode = _libs["pdfium"].get("FPDFDoc_GetPageMode", "cdecl")
    FPDFDoc_GetPageMode.argtypes = [FPDF_DOCUMENT]
    FPDFDoc_GetPageMode.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_flatten.h: 38
if _libs["pdfium"].has("FPDFPage_Flatten", "cdecl"):
    FPDFPage_Flatten = _libs["pdfium"].get("FPDFPage_Flatten", "cdecl")
    FPDFPage_Flatten.argtypes = [FPDF_PAGE, c_int]
    FPDFPage_Flatten.restype = c_int

enum_anon_4 = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_ShiftKey = (1 << 0)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_ControlKey = (1 << 1)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_AltKey = (1 << 2)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_MetaKey = (1 << 3)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_KeyPad = (1 << 4)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_AutoRepeat = (1 << 5)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_LeftButtonDown = (1 << 6)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_MiddleButtonDown = (1 << 7)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG_RightButtonDown = (1 << 8)# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

FWL_EVENTFLAG = enum_anon_4# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 28

enum_anon_5 = c_int# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Back = 8# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Tab = 9# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NewLine = 10# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Clear = 12# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Return = 13# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Shift = 16# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Control = 17# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Menu = 18# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Pause = 19# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Capital = 20# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Kana = 21# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Hangul = 21# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Junja = 23# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Final = 24# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Hanja = 25# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Kanji = 25# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Escape = 27# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Convert = 28# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NonConvert = 29# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Accept = 30# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_ModeChange = 31# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Space = 32# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Prior = 33# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Next = 34# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_End = 35# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Home = 36# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Left = 37# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Up = 38# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Right = 39# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Down = 40# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Select = 41# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Print = 42# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Execute = 43# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Snapshot = 44# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Insert = 45# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Delete = 46# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Help = 47# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_0 = 48# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_1 = 49# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_2 = 50# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_3 = 51# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_4 = 52# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_5 = 53# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_6 = 54# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_7 = 55# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_8 = 56# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_9 = 57# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_A = 65# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_B = 66# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_C = 67# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_D = 68# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_E = 69# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F = 70# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_G = 71# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_H = 72# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_I = 73# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_J = 74# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_K = 75# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_L = 76# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_M = 77# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_N = 78# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_O = 79# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_P = 80# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Q = 81# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_R = 82# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_S = 83# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_T = 84# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_U = 85# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_V = 86# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_W = 87# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_X = 88# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Y = 89# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Z = 90# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_LWin = 91# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Command = 91# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_RWin = 92# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Apps = 93# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Sleep = 95# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad0 = 96# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad1 = 97# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad2 = 98# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad3 = 99# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad4 = 100# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad5 = 101# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad6 = 102# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad7 = 103# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad8 = 104# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NumPad9 = 105# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Multiply = 106# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Add = 107# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Separator = 108# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Subtract = 109# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Decimal = 110# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Divide = 111# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F1 = 112# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F2 = 113# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F3 = 114# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F4 = 115# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F5 = 116# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F6 = 117# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F7 = 118# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F8 = 119# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F9 = 120# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F10 = 121# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F11 = 122# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F12 = 123# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F13 = 124# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F14 = 125# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F15 = 126# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F16 = 127# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F17 = 128# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F18 = 129# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F19 = 130# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F20 = 131# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F21 = 132# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F22 = 133# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F23 = 134# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_F24 = 135# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NunLock = 144# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Scroll = 145# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_LShift = 160# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_RShift = 161# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_LControl = 162# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_RControl = 163# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_LMenu = 164# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_RMenu = 165# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Back = 166# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Forward = 167# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Refresh = 168# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Stop = 169# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Search = 170# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Favorites = 171# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_BROWSER_Home = 172# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_VOLUME_Mute = 173# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_VOLUME_Down = 174# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_VOLUME_Up = 175# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_NEXT_Track = 176# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_PREV_Track = 177# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_Stop = 178# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_PLAY_Pause = 179# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_LAUNCH_Mail = 180# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_LAUNCH_MEDIA_Select = 181# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_LAUNCH_APP1 = 182# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_MEDIA_LAUNCH_APP2 = 183# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_1 = 186# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Plus = 187# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Comma = 188# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Minus = 189# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Period = 190# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_2 = 191# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_3 = 192# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_4 = 219# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_5 = 220# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_6 = 221# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_7 = 222# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_8 = 223# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_102 = 226# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_ProcessKey = 229# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Packet = 231# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Attn = 246# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Crsel = 247# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Exsel = 248# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Ereof = 249# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Play = 250# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Zoom = 251# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_NoName = 252# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_PA1 = 253# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_OEM_Clear = 254# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEY_Unknown = 0# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

FWL_VKEYCODE = enum_anon_5# /Users/thead/Downloads/pdfium-darwin/include/fpdf_fwlevent.h: 201

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_javascript.h: 22
if _libs["pdfium"].has("FPDFDoc_GetJavaScriptActionCount", "cdecl"):
    FPDFDoc_GetJavaScriptActionCount = _libs["pdfium"].get("FPDFDoc_GetJavaScriptActionCount", "cdecl")
    FPDFDoc_GetJavaScriptActionCount.argtypes = [FPDF_DOCUMENT]
    FPDFDoc_GetJavaScriptActionCount.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_javascript.h: 34
if _libs["pdfium"].has("FPDFDoc_GetJavaScriptAction", "cdecl"):
    FPDFDoc_GetJavaScriptAction = _libs["pdfium"].get("FPDFDoc_GetJavaScriptAction", "cdecl")
    FPDFDoc_GetJavaScriptAction.argtypes = [FPDF_DOCUMENT, c_int]
    FPDFDoc_GetJavaScriptAction.restype = FPDF_JAVASCRIPT_ACTION

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_javascript.h: 41
if _libs["pdfium"].has("FPDFDoc_CloseJavaScriptAction", "cdecl"):
    FPDFDoc_CloseJavaScriptAction = _libs["pdfium"].get("FPDFDoc_CloseJavaScriptAction", "cdecl")
    FPDFDoc_CloseJavaScriptAction.argtypes = [FPDF_JAVASCRIPT_ACTION]
    FPDFDoc_CloseJavaScriptAction.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_javascript.h: 54
if _libs["pdfium"].has("FPDFJavaScriptAction_GetName", "cdecl"):
    FPDFJavaScriptAction_GetName = _libs["pdfium"].get("FPDFJavaScriptAction_GetName", "cdecl")
    FPDFJavaScriptAction_GetName.argtypes = [FPDF_JAVASCRIPT_ACTION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFJavaScriptAction_GetName.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_javascript.h: 69
if _libs["pdfium"].has("FPDFJavaScriptAction_GetScript", "cdecl"):
    FPDFJavaScriptAction_GetScript = _libs["pdfium"].get("FPDFJavaScriptAction_GetScript", "cdecl")
    FPDFJavaScriptAction_GetScript.argtypes = [FPDF_JAVASCRIPT_ACTION, POINTER(FPDF_WCHAR), c_ulong]
    FPDFJavaScriptAction_GetScript.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ppo.h: 26
if _libs["pdfium"].has("FPDF_ImportPages", "cdecl"):
    FPDF_ImportPages = _libs["pdfium"].get("FPDF_ImportPages", "cdecl")
    FPDF_ImportPages.argtypes = [FPDF_DOCUMENT, FPDF_DOCUMENT, FPDF_BYTESTRING, c_int]
    FPDF_ImportPages.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ppo.h: 49
if _libs["pdfium"].has("FPDF_ImportNPagesToOne", "cdecl"):
    FPDF_ImportNPagesToOne = _libs["pdfium"].get("FPDF_ImportNPagesToOne", "cdecl")
    FPDF_ImportNPagesToOne.argtypes = [FPDF_DOCUMENT, c_float, c_float, c_size_t, c_size_t]
    FPDF_ImportNPagesToOne.restype = FPDF_DOCUMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ppo.h: 62
if _libs["pdfium"].has("FPDF_CopyViewerPreferences", "cdecl"):
    FPDF_CopyViewerPreferences = _libs["pdfium"].get("FPDF_CopyViewerPreferences", "cdecl")
    FPDF_CopyViewerPreferences.argtypes = [FPDF_DOCUMENT, FPDF_DOCUMENT]
    FPDF_CopyViewerPreferences.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 25
class struct__IFSDK_PAUSE(Structure):
    pass

struct__IFSDK_PAUSE.__slots__ = [
    'version',
    'NeedToPauseNow',
    'user',
]
struct__IFSDK_PAUSE._fields_ = [
    ('version', c_int),
    ('NeedToPauseNow', CFUNCTYPE(UNCHECKED(FPDF_BOOL), POINTER(struct__IFSDK_PAUSE))),
    ('user', POINTER(None)),
]

IFSDK_PAUSE = struct__IFSDK_PAUSE# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 47

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 77
if _libs["pdfium"].has("FPDF_RenderPageBitmap_Start", "cdecl"):
    FPDF_RenderPageBitmap_Start = _libs["pdfium"].get("FPDF_RenderPageBitmap_Start", "cdecl")
    FPDF_RenderPageBitmap_Start.argtypes = [FPDF_BITMAP, FPDF_PAGE, c_int, c_int, c_int, c_int, c_int, c_int, POINTER(IFSDK_PAUSE)]
    FPDF_RenderPageBitmap_Start.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 98
if _libs["pdfium"].has("FPDF_RenderPage_Continue", "cdecl"):
    FPDF_RenderPage_Continue = _libs["pdfium"].get("FPDF_RenderPage_Continue", "cdecl")
    FPDF_RenderPage_Continue.argtypes = [FPDF_PAGE, POINTER(IFSDK_PAUSE)]
    FPDF_RenderPage_Continue.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 109
if _libs["pdfium"].has("FPDF_RenderPage_Close", "cdecl"):
    FPDF_RenderPage_Close = _libs["pdfium"].get("FPDF_RenderPage_Close", "cdecl")
    FPDF_RenderPage_Close.argtypes = [FPDF_PAGE]
    FPDF_RenderPage_Close.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h: 19
class struct_FPDF_FILEWRITE_(Structure):
    pass

struct_FPDF_FILEWRITE_.__slots__ = [
    'version',
    'WriteBlock',
]
struct_FPDF_FILEWRITE_._fields_ = [
    ('version', c_int),
    ('WriteBlock', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_FPDF_FILEWRITE_), POINTER(None), c_ulong)),
]

FPDF_FILEWRITE = struct_FPDF_FILEWRITE_# /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h: 42

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h: 59
if _libs["pdfium"].has("FPDF_SaveAsCopy", "cdecl"):
    FPDF_SaveAsCopy = _libs["pdfium"].get("FPDF_SaveAsCopy", "cdecl")
    FPDF_SaveAsCopy.argtypes = [FPDF_DOCUMENT, POINTER(FPDF_FILEWRITE), FPDF_DWORD]
    FPDF_SaveAsCopy.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h: 76
if _libs["pdfium"].has("FPDF_SaveWithVersion", "cdecl"):
    FPDF_SaveWithVersion = _libs["pdfium"].get("FPDF_SaveWithVersion", "cdecl")
    FPDF_SaveWithVersion.argtypes = [FPDF_DOCUMENT, POINTER(FPDF_FILEWRITE), FPDF_DWORD, c_int]
    FPDF_SaveWithVersion.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_searchex.h: 24
if _libs["pdfium"].has("FPDFText_GetCharIndexFromTextIndex", "cdecl"):
    FPDFText_GetCharIndexFromTextIndex = _libs["pdfium"].get("FPDFText_GetCharIndexFromTextIndex", "cdecl")
    FPDFText_GetCharIndexFromTextIndex.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetCharIndexFromTextIndex.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_searchex.h: 33
if _libs["pdfium"].has("FPDFText_GetTextIndexFromCharIndex", "cdecl"):
    FPDFText_GetTextIndexFromCharIndex = _libs["pdfium"].get("FPDFText_GetTextIndexFromCharIndex", "cdecl")
    FPDFText_GetTextIndexFromCharIndex.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetTextIndexFromCharIndex.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 25
if _libs["pdfium"].has("FPDF_StructTree_GetForPage", "cdecl"):
    FPDF_StructTree_GetForPage = _libs["pdfium"].get("FPDF_StructTree_GetForPage", "cdecl")
    FPDF_StructTree_GetForPage.argtypes = [FPDF_PAGE]
    FPDF_StructTree_GetForPage.restype = FPDF_STRUCTTREE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 35
if _libs["pdfium"].has("FPDF_StructTree_Close", "cdecl"):
    FPDF_StructTree_Close = _libs["pdfium"].get("FPDF_StructTree_Close", "cdecl")
    FPDF_StructTree_Close.argtypes = [FPDF_STRUCTTREE]
    FPDF_StructTree_Close.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 45
if _libs["pdfium"].has("FPDF_StructTree_CountChildren", "cdecl"):
    FPDF_StructTree_CountChildren = _libs["pdfium"].get("FPDF_StructTree_CountChildren", "cdecl")
    FPDF_StructTree_CountChildren.argtypes = [FPDF_STRUCTTREE]
    FPDF_StructTree_CountChildren.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 56
if _libs["pdfium"].has("FPDF_StructTree_GetChildAtIndex", "cdecl"):
    FPDF_StructTree_GetChildAtIndex = _libs["pdfium"].get("FPDF_StructTree_GetChildAtIndex", "cdecl")
    FPDF_StructTree_GetChildAtIndex.argtypes = [FPDF_STRUCTTREE, c_int]
    FPDF_StructTree_GetChildAtIndex.restype = FPDF_STRUCTELEMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 74
if _libs["pdfium"].has("FPDF_StructElement_GetAltText", "cdecl"):
    FPDF_StructElement_GetAltText = _libs["pdfium"].get("FPDF_StructElement_GetAltText", "cdecl")
    FPDF_StructElement_GetAltText.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetAltText.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 86
if _libs["pdfium"].has("FPDF_StructElement_GetMarkedContentID", "cdecl"):
    FPDF_StructElement_GetMarkedContentID = _libs["pdfium"].get("FPDF_StructElement_GetMarkedContentID", "cdecl")
    FPDF_StructElement_GetMarkedContentID.argtypes = [FPDF_STRUCTELEMENT]
    FPDF_StructElement_GetMarkedContentID.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 104
if _libs["pdfium"].has("FPDF_StructElement_GetType", "cdecl"):
    FPDF_StructElement_GetType = _libs["pdfium"].get("FPDF_StructElement_GetType", "cdecl")
    FPDF_StructElement_GetType.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetType.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 124
if _libs["pdfium"].has("FPDF_StructElement_GetTitle", "cdecl"):
    FPDF_StructElement_GetTitle = _libs["pdfium"].get("FPDF_StructElement_GetTitle", "cdecl")
    FPDF_StructElement_GetTitle.argtypes = [FPDF_STRUCTELEMENT, POINTER(None), c_ulong]
    FPDF_StructElement_GetTitle.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 135
if _libs["pdfium"].has("FPDF_StructElement_CountChildren", "cdecl"):
    FPDF_StructElement_CountChildren = _libs["pdfium"].get("FPDF_StructElement_CountChildren", "cdecl")
    FPDF_StructElement_CountChildren.argtypes = [FPDF_STRUCTELEMENT]
    FPDF_StructElement_CountChildren.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_structtree.h: 148
if _libs["pdfium"].has("FPDF_StructElement_GetChildAtIndex", "cdecl"):
    FPDF_StructElement_GetChildAtIndex = _libs["pdfium"].get("FPDF_StructElement_GetChildAtIndex", "cdecl")
    FPDF_StructElement_GetChildAtIndex.argtypes = [FPDF_STRUCTELEMENT, c_int]
    FPDF_StructElement_GetChildAtIndex.restype = FPDF_STRUCTELEMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 44
class struct__FPDF_SYSFONTINFO(Structure):
    pass

struct__FPDF_SYSFONTINFO.__slots__ = [
    'version',
    'Release',
    'EnumFonts',
    'MapFont',
    'GetFont',
    'GetFontData',
    'GetFaceName',
    'GetFontCharset',
    'DeleteFont',
]
struct__FPDF_SYSFONTINFO._fields_ = [
    ('version', c_int),
    ('Release', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_SYSFONTINFO))),
    ('EnumFonts', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None))),
    ('MapFont', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(struct__FPDF_SYSFONTINFO), c_int, FPDF_BOOL, c_int, c_int, String, POINTER(FPDF_BOOL))),
    ('GetFont', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(struct__FPDF_SYSFONTINFO), String)),
    ('GetFontData', CFUNCTYPE(UNCHECKED(c_ulong), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None), c_uint, POINTER(c_ubyte), c_ulong)),
    ('GetFaceName', CFUNCTYPE(UNCHECKED(c_ulong), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None), String, c_ulong)),
    ('GetFontCharset', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None))),
    ('DeleteFont', CFUNCTYPE(UNCHECKED(None), POINTER(struct__FPDF_SYSFONTINFO), POINTER(None))),
]

FPDF_SYSFONTINFO = struct__FPDF_SYSFONTINFO# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 223

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 232
class struct_FPDF_CharsetFontMap_(Structure):
    pass

struct_FPDF_CharsetFontMap_.__slots__ = [
    'charset',
    'fontname',
]
struct_FPDF_CharsetFontMap_._fields_ = [
    ('charset', c_int),
    ('fontname', String),
]

FPDF_CharsetFontMap = struct_FPDF_CharsetFontMap_# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 232

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 244
if _libs["pdfium"].has("FPDF_GetDefaultTTFMap", "cdecl"):
    FPDF_GetDefaultTTFMap = _libs["pdfium"].get("FPDF_GetDefaultTTFMap", "cdecl")
    FPDF_GetDefaultTTFMap.argtypes = []
    FPDF_GetDefaultTTFMap.restype = POINTER(FPDF_CharsetFontMap)

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 259
if _libs["pdfium"].has("FPDF_AddInstalledFont", "cdecl"):
    FPDF_AddInstalledFont = _libs["pdfium"].get("FPDF_AddInstalledFont", "cdecl")
    FPDF_AddInstalledFont.argtypes = [POINTER(None), String, c_int]
    FPDF_AddInstalledFont.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 276
if _libs["pdfium"].has("FPDF_SetSystemFontInfo", "cdecl"):
    FPDF_SetSystemFontInfo = _libs["pdfium"].get("FPDF_SetSystemFontInfo", "cdecl")
    FPDF_SetSystemFontInfo.argtypes = [POINTER(FPDF_SYSFONTINFO)]
    FPDF_SetSystemFontInfo.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 293
if _libs["pdfium"].has("FPDF_GetDefaultSystemFontInfo", "cdecl"):
    FPDF_GetDefaultSystemFontInfo = _libs["pdfium"].get("FPDF_GetDefaultSystemFontInfo", "cdecl")
    FPDF_GetDefaultSystemFontInfo.argtypes = []
    FPDF_GetDefaultSystemFontInfo.restype = POINTER(FPDF_SYSFONTINFO)

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 307
if _libs["pdfium"].has("FPDF_FreeDefaultSystemFontInfo", "cdecl"):
    FPDF_FreeDefaultSystemFontInfo = _libs["pdfium"].get("FPDF_FreeDefaultSystemFontInfo", "cdecl")
    FPDF_FreeDefaultSystemFontInfo.argtypes = [POINTER(FPDF_SYSFONTINFO)]
    FPDF_FreeDefaultSystemFontInfo.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 31
if _libs["pdfium"].has("FPDFText_LoadPage", "cdecl"):
    FPDFText_LoadPage = _libs["pdfium"].get("FPDFText_LoadPage", "cdecl")
    FPDFText_LoadPage.argtypes = [FPDF_PAGE]
    FPDFText_LoadPage.restype = FPDF_TEXTPAGE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 42
if _libs["pdfium"].has("FPDFText_ClosePage", "cdecl"):
    FPDFText_ClosePage = _libs["pdfium"].get("FPDFText_ClosePage", "cdecl")
    FPDFText_ClosePage.argtypes = [FPDF_TEXTPAGE]
    FPDFText_ClosePage.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 60
if _libs["pdfium"].has("FPDFText_CountChars", "cdecl"):
    FPDFText_CountChars = _libs["pdfium"].get("FPDFText_CountChars", "cdecl")
    FPDFText_CountChars.argtypes = [FPDF_TEXTPAGE]
    FPDFText_CountChars.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 75
if _libs["pdfium"].has("FPDFText_GetUnicode", "cdecl"):
    FPDFText_GetUnicode = _libs["pdfium"].get("FPDFText_GetUnicode", "cdecl")
    FPDFText_GetUnicode.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetUnicode.restype = c_uint

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 88
if _libs["pdfium"].has("FPDFText_GetFontSize", "cdecl"):
    FPDFText_GetFontSize = _libs["pdfium"].get("FPDFText_GetFontSize", "cdecl")
    FPDFText_GetFontSize.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetFontSize.restype = c_double

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 111
if _libs["pdfium"].has("FPDFText_GetFontInfo", "cdecl"):
    FPDFText_GetFontInfo = _libs["pdfium"].get("FPDFText_GetFontInfo", "cdecl")
    FPDFText_GetFontInfo.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(None), c_ulong, POINTER(c_int)]
    FPDFText_GetFontInfo.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 129
if _libs["pdfium"].has("FPDFText_GetFontWeight", "cdecl"):
    FPDFText_GetFontWeight = _libs["pdfium"].get("FPDFText_GetFontWeight", "cdecl")
    FPDFText_GetFontWeight.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetFontWeight.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 146
if _libs["pdfium"].has("FPDFText_GetTextRenderMode", "cdecl"):
    FPDFText_GetTextRenderMode = _libs["pdfium"].get("FPDFText_GetTextRenderMode", "cdecl")
    FPDFText_GetTextRenderMode.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetTextRenderMode.restype = FPDF_TEXT_RENDERMODE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 168
if _libs["pdfium"].has("FPDFText_GetFillColor", "cdecl"):
    FPDFText_GetFillColor = _libs["pdfium"].get("FPDFText_GetFillColor", "cdecl")
    FPDFText_GetFillColor.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFText_GetFillColor.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 195
if _libs["pdfium"].has("FPDFText_GetStrokeColor", "cdecl"):
    FPDFText_GetStrokeColor = _libs["pdfium"].get("FPDFText_GetStrokeColor", "cdecl")
    FPDFText_GetStrokeColor.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint)]
    FPDFText_GetStrokeColor.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 214
if _libs["pdfium"].has("FPDFText_GetCharAngle", "cdecl"):
    FPDFText_GetCharAngle = _libs["pdfium"].get("FPDFText_GetCharAngle", "cdecl")
    FPDFText_GetCharAngle.argtypes = [FPDF_TEXTPAGE, c_int]
    FPDFText_GetCharAngle.restype = c_float

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 238
if _libs["pdfium"].has("FPDFText_GetCharBox", "cdecl"):
    FPDFText_GetCharBox = _libs["pdfium"].get("FPDFText_GetCharBox", "cdecl")
    FPDFText_GetCharBox.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    FPDFText_GetCharBox.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 263
if _libs["pdfium"].has("FPDFText_GetLooseCharBox", "cdecl"):
    FPDFText_GetLooseCharBox = _libs["pdfium"].get("FPDFText_GetLooseCharBox", "cdecl")
    FPDFText_GetLooseCharBox.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(FS_RECTF)]
    FPDFText_GetLooseCharBox.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 279
if _libs["pdfium"].has("FPDFText_GetMatrix", "cdecl"):
    FPDFText_GetMatrix = _libs["pdfium"].get("FPDFText_GetMatrix", "cdecl")
    FPDFText_GetMatrix.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(FS_MATRIX)]
    FPDFText_GetMatrix.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 299
if _libs["pdfium"].has("FPDFText_GetCharOrigin", "cdecl"):
    FPDFText_GetCharOrigin = _libs["pdfium"].get("FPDFText_GetCharOrigin", "cdecl")
    FPDFText_GetCharOrigin.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_double), POINTER(c_double)]
    FPDFText_GetCharOrigin.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 322
if _libs["pdfium"].has("FPDFText_GetCharIndexAtPos", "cdecl"):
    FPDFText_GetCharIndexAtPos = _libs["pdfium"].get("FPDFText_GetCharIndexAtPos", "cdecl")
    FPDFText_GetCharIndexAtPos.argtypes = [FPDF_TEXTPAGE, c_double, c_double, c_double, c_double]
    FPDFText_GetCharIndexAtPos.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 345
if _libs["pdfium"].has("FPDFText_GetText", "cdecl"):
    FPDFText_GetText = _libs["pdfium"].get("FPDFText_GetText", "cdecl")
    FPDFText_GetText.argtypes = [FPDF_TEXTPAGE, c_int, c_int, POINTER(c_ushort)]
    FPDFText_GetText.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 366
if _libs["pdfium"].has("FPDFText_CountRects", "cdecl"):
    FPDFText_CountRects = _libs["pdfium"].get("FPDFText_CountRects", "cdecl")
    FPDFText_CountRects.argtypes = [FPDF_TEXTPAGE, c_int, c_int]
    FPDFText_CountRects.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 392
if _libs["pdfium"].has("FPDFText_GetRect", "cdecl"):
    FPDFText_GetRect = _libs["pdfium"].get("FPDFText_GetRect", "cdecl")
    FPDFText_GetRect.argtypes = [FPDF_TEXTPAGE, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    FPDFText_GetRect.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 423
if _libs["pdfium"].has("FPDFText_GetBoundedText", "cdecl"):
    FPDFText_GetBoundedText = _libs["pdfium"].get("FPDFText_GetBoundedText", "cdecl")
    FPDFText_GetBoundedText.argtypes = [FPDF_TEXTPAGE, c_double, c_double, c_double, c_double, POINTER(c_ushort), c_int]
    FPDFText_GetBoundedText.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 453
if _libs["pdfium"].has("FPDFText_FindStart", "cdecl"):
    FPDFText_FindStart = _libs["pdfium"].get("FPDFText_FindStart", "cdecl")
    FPDFText_FindStart.argtypes = [FPDF_TEXTPAGE, FPDF_WIDESTRING, c_ulong, c_int]
    FPDFText_FindStart.restype = FPDF_SCHHANDLE

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 466
if _libs["pdfium"].has("FPDFText_FindNext", "cdecl"):
    FPDFText_FindNext = _libs["pdfium"].get("FPDFText_FindNext", "cdecl")
    FPDFText_FindNext.argtypes = [FPDF_SCHHANDLE]
    FPDFText_FindNext.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 476
if _libs["pdfium"].has("FPDFText_FindPrev", "cdecl"):
    FPDFText_FindPrev = _libs["pdfium"].get("FPDFText_FindPrev", "cdecl")
    FPDFText_FindPrev.argtypes = [FPDF_SCHHANDLE]
    FPDFText_FindPrev.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 486
if _libs["pdfium"].has("FPDFText_GetSchResultIndex", "cdecl"):
    FPDFText_GetSchResultIndex = _libs["pdfium"].get("FPDFText_GetSchResultIndex", "cdecl")
    FPDFText_GetSchResultIndex.argtypes = [FPDF_SCHHANDLE]
    FPDFText_GetSchResultIndex.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 496
if _libs["pdfium"].has("FPDFText_GetSchCount", "cdecl"):
    FPDFText_GetSchCount = _libs["pdfium"].get("FPDFText_GetSchCount", "cdecl")
    FPDFText_GetSchCount.argtypes = [FPDF_SCHHANDLE]
    FPDFText_GetSchCount.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 506
if _libs["pdfium"].has("FPDFText_FindClose", "cdecl"):
    FPDFText_FindClose = _libs["pdfium"].get("FPDFText_FindClose", "cdecl")
    FPDFText_FindClose.argtypes = [FPDF_SCHHANDLE]
    FPDFText_FindClose.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 528
if _libs["pdfium"].has("FPDFLink_LoadWebLinks", "cdecl"):
    FPDFLink_LoadWebLinks = _libs["pdfium"].get("FPDFLink_LoadWebLinks", "cdecl")
    FPDFLink_LoadWebLinks.argtypes = [FPDF_TEXTPAGE]
    FPDFLink_LoadWebLinks.restype = FPDF_PAGELINK

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 537
if _libs["pdfium"].has("FPDFLink_CountWebLinks", "cdecl"):
    FPDFLink_CountWebLinks = _libs["pdfium"].get("FPDFLink_CountWebLinks", "cdecl")
    FPDFLink_CountWebLinks.argtypes = [FPDF_PAGELINK]
    FPDFLink_CountWebLinks.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 558
if _libs["pdfium"].has("FPDFLink_GetURL", "cdecl"):
    FPDFLink_GetURL = _libs["pdfium"].get("FPDFLink_GetURL", "cdecl")
    FPDFLink_GetURL.argtypes = [FPDF_PAGELINK, c_int, POINTER(c_ushort), c_int]
    FPDFLink_GetURL.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 572
if _libs["pdfium"].has("FPDFLink_CountRects", "cdecl"):
    FPDFLink_CountRects = _libs["pdfium"].get("FPDFLink_CountRects", "cdecl")
    FPDFLink_CountRects.argtypes = [FPDF_PAGELINK, c_int]
    FPDFLink_CountRects.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 595
if _libs["pdfium"].has("FPDFLink_GetRect", "cdecl"):
    FPDFLink_GetRect = _libs["pdfium"].get("FPDFLink_GetRect", "cdecl")
    FPDFLink_GetRect.argtypes = [FPDF_PAGELINK, c_int, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    FPDFLink_GetRect.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 618
if _libs["pdfium"].has("FPDFLink_GetTextRange", "cdecl"):
    FPDFLink_GetTextRange = _libs["pdfium"].get("FPDFLink_GetTextRange", "cdecl")
    FPDFLink_GetTextRange.argtypes = [FPDF_PAGELINK, c_int, POINTER(c_int), POINTER(c_int)]
    FPDFLink_GetTextRange.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 630
if _libs["pdfium"].has("FPDFLink_CloseWebLinks", "cdecl"):
    FPDFLink_CloseWebLinks = _libs["pdfium"].get("FPDFLink_CloseWebLinks", "cdecl")
    FPDFLink_CloseWebLinks.argtypes = [FPDF_PAGELINK]
    FPDFLink_CloseWebLinks.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_thumbnail.h: 28
if _libs["pdfium"].has("FPDFPage_GetDecodedThumbnailData", "cdecl"):
    FPDFPage_GetDecodedThumbnailData = _libs["pdfium"].get("FPDFPage_GetDecodedThumbnailData", "cdecl")
    FPDFPage_GetDecodedThumbnailData.argtypes = [FPDF_PAGE, POINTER(None), c_ulong]
    FPDFPage_GetDecodedThumbnailData.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_thumbnail.h: 43
if _libs["pdfium"].has("FPDFPage_GetRawThumbnailData", "cdecl"):
    FPDFPage_GetRawThumbnailData = _libs["pdfium"].get("FPDFPage_GetRawThumbnailData", "cdecl")
    FPDFPage_GetRawThumbnailData.argtypes = [FPDF_PAGE, POINTER(None), c_ulong]
    FPDFPage_GetRawThumbnailData.restype = c_ulong

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_thumbnail.h: 53
if _libs["pdfium"].has("FPDFPage_GetThumbnailAsBitmap", "cdecl"):
    FPDFPage_GetThumbnailAsBitmap = _libs["pdfium"].get("FPDFPage_GetThumbnailAsBitmap", "cdecl")
    FPDFPage_GetThumbnailAsBitmap.argtypes = [FPDF_PAGE]
    FPDFPage_GetThumbnailAsBitmap.restype = FPDF_BITMAP

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 26
if _libs["pdfium"].has("FPDFPage_SetMediaBox", "cdecl"):
    FPDFPage_SetMediaBox = _libs["pdfium"].get("FPDFPage_SetMediaBox", "cdecl")
    FPDFPage_SetMediaBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetMediaBox.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 41
if _libs["pdfium"].has("FPDFPage_SetCropBox", "cdecl"):
    FPDFPage_SetCropBox = _libs["pdfium"].get("FPDFPage_SetCropBox", "cdecl")
    FPDFPage_SetCropBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetCropBox.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 56
if _libs["pdfium"].has("FPDFPage_SetBleedBox", "cdecl"):
    FPDFPage_SetBleedBox = _libs["pdfium"].get("FPDFPage_SetBleedBox", "cdecl")
    FPDFPage_SetBleedBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetBleedBox.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 71
if _libs["pdfium"].has("FPDFPage_SetTrimBox", "cdecl"):
    FPDFPage_SetTrimBox = _libs["pdfium"].get("FPDFPage_SetTrimBox", "cdecl")
    FPDFPage_SetTrimBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetTrimBox.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 86
if _libs["pdfium"].has("FPDFPage_SetArtBox", "cdecl"):
    FPDFPage_SetArtBox = _libs["pdfium"].get("FPDFPage_SetArtBox", "cdecl")
    FPDFPage_SetArtBox.argtypes = [FPDF_PAGE, c_float, c_float, c_float, c_float]
    FPDFPage_SetArtBox.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 104
if _libs["pdfium"].has("FPDFPage_GetMediaBox", "cdecl"):
    FPDFPage_GetMediaBox = _libs["pdfium"].get("FPDFPage_GetMediaBox", "cdecl")
    FPDFPage_GetMediaBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetMediaBox.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 122
if _libs["pdfium"].has("FPDFPage_GetCropBox", "cdecl"):
    FPDFPage_GetCropBox = _libs["pdfium"].get("FPDFPage_GetCropBox", "cdecl")
    FPDFPage_GetCropBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetCropBox.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 140
if _libs["pdfium"].has("FPDFPage_GetBleedBox", "cdecl"):
    FPDFPage_GetBleedBox = _libs["pdfium"].get("FPDFPage_GetBleedBox", "cdecl")
    FPDFPage_GetBleedBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetBleedBox.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 158
if _libs["pdfium"].has("FPDFPage_GetTrimBox", "cdecl"):
    FPDFPage_GetTrimBox = _libs["pdfium"].get("FPDFPage_GetTrimBox", "cdecl")
    FPDFPage_GetTrimBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetTrimBox.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 176
if _libs["pdfium"].has("FPDFPage_GetArtBox", "cdecl"):
    FPDFPage_GetArtBox = _libs["pdfium"].get("FPDFPage_GetArtBox", "cdecl")
    FPDFPage_GetArtBox.argtypes = [FPDF_PAGE, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    FPDFPage_GetArtBox.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 198
if _libs["pdfium"].has("FPDFPage_TransFormWithClip", "cdecl"):
    FPDFPage_TransFormWithClip = _libs["pdfium"].get("FPDFPage_TransFormWithClip", "cdecl")
    FPDFPage_TransFormWithClip.argtypes = [FPDF_PAGE, POINTER(FS_MATRIX), POINTER(FS_RECTF)]
    FPDFPage_TransFormWithClip.restype = FPDF_BOOL

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 215
if _libs["pdfium"].has("FPDFPageObj_TransformClipPath", "cdecl"):
    FPDFPageObj_TransformClipPath = _libs["pdfium"].get("FPDFPageObj_TransformClipPath", "cdecl")
    FPDFPageObj_TransformClipPath.argtypes = [FPDF_PAGEOBJECT, c_double, c_double, c_double, c_double, c_double, c_double]
    FPDFPageObj_TransformClipPath.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 233
if _libs["pdfium"].has("FPDFPageObj_GetClipPath", "cdecl"):
    FPDFPageObj_GetClipPath = _libs["pdfium"].get("FPDFPageObj_GetClipPath", "cdecl")
    FPDFPageObj_GetClipPath.argtypes = [FPDF_PAGEOBJECT]
    FPDFPageObj_GetClipPath.restype = FPDF_CLIPPATH

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 241
if _libs["pdfium"].has("FPDFClipPath_CountPaths", "cdecl"):
    FPDFClipPath_CountPaths = _libs["pdfium"].get("FPDFClipPath_CountPaths", "cdecl")
    FPDFClipPath_CountPaths.argtypes = [FPDF_CLIPPATH]
    FPDFClipPath_CountPaths.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 251
if _libs["pdfium"].has("FPDFClipPath_CountPathSegments", "cdecl"):
    FPDFClipPath_CountPathSegments = _libs["pdfium"].get("FPDFClipPath_CountPathSegments", "cdecl")
    FPDFClipPath_CountPathSegments.argtypes = [FPDF_CLIPPATH, c_int]
    FPDFClipPath_CountPathSegments.restype = c_int

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 264
if _libs["pdfium"].has("FPDFClipPath_GetPathSegment", "cdecl"):
    FPDFClipPath_GetPathSegment = _libs["pdfium"].get("FPDFClipPath_GetPathSegment", "cdecl")
    FPDFClipPath_GetPathSegment.argtypes = [FPDF_CLIPPATH, c_int, c_int]
    FPDFClipPath_GetPathSegment.restype = FPDF_PATHSEGMENT

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 279
if _libs["pdfium"].has("FPDF_CreateClipPath", "cdecl"):
    FPDF_CreateClipPath = _libs["pdfium"].get("FPDF_CreateClipPath", "cdecl")
    FPDF_CreateClipPath.argtypes = [c_float, c_float, c_float, c_float]
    FPDF_CreateClipPath.restype = FPDF_CLIPPATH

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 289
if _libs["pdfium"].has("FPDF_DestroyClipPath", "cdecl"):
    FPDF_DestroyClipPath = _libs["pdfium"].get("FPDF_DestroyClipPath", "cdecl")
    FPDF_DestroyClipPath.argtypes = [FPDF_CLIPPATH]
    FPDF_DestroyClipPath.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_transformpage.h: 301
if _libs["pdfium"].has("FPDFPage_InsertClipPath", "cdecl"):
    FPDFPage_InsertClipPath = _libs["pdfium"].get("FPDFPage_InsertClipPath", "cdecl")
    FPDFPage_InsertClipPath.argtypes = [FPDF_PAGE, FPDF_CLIPPATH]
    FPDFPage_InsertClipPath.restype = None

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 28
try:
    FPDF_OBJECT_UNKNOWN = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 29
try:
    FPDF_OBJECT_BOOLEAN = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 30
try:
    FPDF_OBJECT_NUMBER = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 31
try:
    FPDF_OBJECT_STRING = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 32
try:
    FPDF_OBJECT_NAME = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 33
try:
    FPDF_OBJECT_ARRAY = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 34
try:
    FPDF_OBJECT_DICTIONARY = 6
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 35
try:
    FPDF_OBJECT_STREAM = 7
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 36
try:
    FPDF_OBJECT_NULLOBJ = 8
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 37
try:
    FPDF_OBJECT_REFERENCE = 9
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 265
try:
    FPDF_POLICY_MACHINETIME_ACCESS = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 528
try:
    FPDF_ERR_SUCCESS = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 529
try:
    FPDF_ERR_UNKNOWN = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 530
try:
    FPDF_ERR_FILE = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 531
try:
    FPDF_ERR_FORMAT = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 532
try:
    FPDF_ERR_PASSWORD = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 533
try:
    FPDF_ERR_SECURITY = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 534
try:
    FPDF_ERR_PAGE = 6
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 703
try:
    FPDF_ANNOT = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 705
try:
    FPDF_LCD_TEXT = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 707
try:
    FPDF_NO_NATIVETEXT = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 709
try:
    FPDF_GRAYSCALE = 8
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 711
try:
    FPDF_DEBUG_INFO = 128
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 713
try:
    FPDF_NO_CATCH = 256
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 715
try:
    FPDF_RENDER_LIMITEDIMAGECACHE = 512
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 717
try:
    FPDF_RENDER_FORCEHALFTONE = 1024
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 719
try:
    FPDF_PRINTING = 2048
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 721
try:
    FPDF_RENDER_NO_SMOOTHTEXT = 4096
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 723
try:
    FPDF_RENDER_NO_SMOOTHIMAGE = 8192
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 725
try:
    FPDF_RENDER_NO_SMOOTHPATH = 16384
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 728
try:
    FPDF_REVERSE_BYTE_ORDER = 16
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 969
try:
    FPDFBitmap_Unknown = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 971
try:
    FPDFBitmap_Gray = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 973
try:
    FPDFBitmap_BGR = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 975
try:
    FPDFBitmap_BGRx = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 977
try:
    FPDFBitmap_BGRA = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 18
try:
    PDFACTION_UNSUPPORTED = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 20
try:
    PDFACTION_GOTO = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 22
try:
    PDFACTION_REMOTEGOTO = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 24
try:
    PDFACTION_URI = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 26
try:
    PDFACTION_LAUNCH = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 29
try:
    PDFDEST_VIEW_UNKNOWN_MODE = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 30
try:
    PDFDEST_VIEW_XYZ = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 31
try:
    PDFDEST_VIEW_FIT = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 32
try:
    PDFDEST_VIEW_FITH = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 33
try:
    PDFDEST_VIEW_FITV = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 34
try:
    PDFDEST_VIEW_FITR = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 35
try:
    PDFDEST_VIEW_FITB = 6
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 36
try:
    PDFDEST_VIEW_FITBH = 7
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 37
try:
    PDFDEST_VIEW_FITBV = 8
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 16
try:
    FORMTYPE_NONE = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 17
try:
    FORMTYPE_ACRO_FORM = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 18
try:
    FORMTYPE_XFA_FULL = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 19
try:
    FORMTYPE_XFA_FOREGROUND = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 21
try:
    FORMTYPE_COUNT = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 23
try:
    JSPLATFORM_ALERT_BUTTON_OK = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 24
try:
    JSPLATFORM_ALERT_BUTTON_OKCANCEL = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 25
try:
    JSPLATFORM_ALERT_BUTTON_YESNO = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 26
try:
    JSPLATFORM_ALERT_BUTTON_YESNOCANCEL = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 27
try:
    JSPLATFORM_ALERT_BUTTON_DEFAULT = JSPLATFORM_ALERT_BUTTON_OK
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 29
try:
    JSPLATFORM_ALERT_ICON_ERROR = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 30
try:
    JSPLATFORM_ALERT_ICON_WARNING = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 31
try:
    JSPLATFORM_ALERT_ICON_QUESTION = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 32
try:
    JSPLATFORM_ALERT_ICON_STATUS = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 33
try:
    JSPLATFORM_ALERT_ICON_ASTERISK = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 34
try:
    JSPLATFORM_ALERT_ICON_DEFAULT = JSPLATFORM_ALERT_ICON_ERROR
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 36
try:
    JSPLATFORM_ALERT_RETURN_OK = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 37
try:
    JSPLATFORM_ALERT_RETURN_CANCEL = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 38
try:
    JSPLATFORM_ALERT_RETURN_NO = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 39
try:
    JSPLATFORM_ALERT_RETURN_YES = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 41
try:
    JSPLATFORM_BEEP_ERROR = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 42
try:
    JSPLATFORM_BEEP_WARNING = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 43
try:
    JSPLATFORM_BEEP_QUESTION = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 44
try:
    JSPLATFORM_BEEP_STATUS = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 45
try:
    JSPLATFORM_BEEP_DEFAULT = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 324
try:
    FXCT_ARROW = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 325
try:
    FXCT_NESW = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 326
try:
    FXCT_NWSE = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 327
try:
    FXCT_VBEAM = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 328
try:
    FXCT_HBEAM = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 329
try:
    FXCT_HAND = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1170
try:
    FPDFDOC_AACTION_WC = 16
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1171
try:
    FPDFDOC_AACTION_WS = 17
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1172
try:
    FPDFDOC_AACTION_DS = 18
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1173
try:
    FPDFDOC_AACTION_WP = 19
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1174
try:
    FPDFDOC_AACTION_DP = 20
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1197
try:
    FPDFPAGE_AACTION_OPEN = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1198
try:
    FPDFPAGE_AACTION_CLOSE = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1545
try:
    FPDF_FORMFIELD_UNKNOWN = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1546
try:
    FPDF_FORMFIELD_PUSHBUTTON = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1547
try:
    FPDF_FORMFIELD_CHECKBOX = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1548
try:
    FPDF_FORMFIELD_RADIOBUTTON = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1549
try:
    FPDF_FORMFIELD_COMBOBOX = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1550
try:
    FPDF_FORMFIELD_LISTBOX = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1551
try:
    FPDF_FORMFIELD_TEXTFIELD = 6
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1552
try:
    FPDF_FORMFIELD_SIGNATURE = 7
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 1567
try:
    FPDF_FORMFIELD_COUNT = 8
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 22
try:
    FPDF_ANNOT_UNKNOWN = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 23
try:
    FPDF_ANNOT_TEXT = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 24
try:
    FPDF_ANNOT_LINK = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 25
try:
    FPDF_ANNOT_FREETEXT = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 26
try:
    FPDF_ANNOT_LINE = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 27
try:
    FPDF_ANNOT_SQUARE = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 28
try:
    FPDF_ANNOT_CIRCLE = 6
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 29
try:
    FPDF_ANNOT_POLYGON = 7
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 30
try:
    FPDF_ANNOT_POLYLINE = 8
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 31
try:
    FPDF_ANNOT_HIGHLIGHT = 9
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 32
try:
    FPDF_ANNOT_UNDERLINE = 10
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 33
try:
    FPDF_ANNOT_SQUIGGLY = 11
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 34
try:
    FPDF_ANNOT_STRIKEOUT = 12
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 35
try:
    FPDF_ANNOT_STAMP = 13
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 36
try:
    FPDF_ANNOT_CARET = 14
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 37
try:
    FPDF_ANNOT_INK = 15
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 38
try:
    FPDF_ANNOT_POPUP = 16
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 39
try:
    FPDF_ANNOT_FILEATTACHMENT = 17
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 40
try:
    FPDF_ANNOT_SOUND = 18
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 41
try:
    FPDF_ANNOT_MOVIE = 19
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 42
try:
    FPDF_ANNOT_WIDGET = 20
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 43
try:
    FPDF_ANNOT_SCREEN = 21
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 44
try:
    FPDF_ANNOT_PRINTERMARK = 22
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 45
try:
    FPDF_ANNOT_TRAPNET = 23
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 46
try:
    FPDF_ANNOT_WATERMARK = 24
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 47
try:
    FPDF_ANNOT_THREED = 25
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 48
try:
    FPDF_ANNOT_RICHMEDIA = 26
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 49
try:
    FPDF_ANNOT_XFAWIDGET = 27
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 52
try:
    FPDF_ANNOT_FLAG_NONE = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 53
try:
    FPDF_ANNOT_FLAG_INVISIBLE = (1 << 0)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 54
try:
    FPDF_ANNOT_FLAG_HIDDEN = (1 << 1)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 55
try:
    FPDF_ANNOT_FLAG_PRINT = (1 << 2)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 56
try:
    FPDF_ANNOT_FLAG_NOZOOM = (1 << 3)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 57
try:
    FPDF_ANNOT_FLAG_NOROTATE = (1 << 4)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 58
try:
    FPDF_ANNOT_FLAG_NOVIEW = (1 << 5)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 59
try:
    FPDF_ANNOT_FLAG_READONLY = (1 << 6)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 60
try:
    FPDF_ANNOT_FLAG_LOCKED = (1 << 7)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 61
try:
    FPDF_ANNOT_FLAG_TOGGLENOVIEW = (1 << 8)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 63
try:
    FPDF_ANNOT_APPEARANCEMODE_NORMAL = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 64
try:
    FPDF_ANNOT_APPEARANCEMODE_ROLLOVER = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 65
try:
    FPDF_ANNOT_APPEARANCEMODE_DOWN = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 66
try:
    FPDF_ANNOT_APPEARANCEMODE_COUNT = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 70
try:
    FPDF_FORMFLAG_NONE = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 71
try:
    FPDF_FORMFLAG_READONLY = (1 << 0)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 72
try:
    FPDF_FORMFLAG_REQUIRED = (1 << 1)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 73
try:
    FPDF_FORMFLAG_NOEXPORT = (1 << 2)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 77
try:
    FPDF_FORMFLAG_TEXT_MULTILINE = (1 << 12)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 78
try:
    FPDF_FORMFLAG_TEXT_PASSWORD = (1 << 13)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 82
try:
    FPDF_FORMFLAG_CHOICE_COMBO = (1 << 17)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_annot.h: 83
try:
    FPDF_FORMFLAG_CHOICE_EDIT = (1 << 18)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 15
try:
    PDF_LINEARIZATION_UNKNOWN = (-1)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 16
try:
    PDF_NOT_LINEARIZED = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 17
try:
    PDF_LINEARIZED = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 19
try:
    PDF_DATA_ERROR = (-1)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 20
try:
    PDF_DATA_NOTAVAIL = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 21
try:
    PDF_DATA_AVAIL = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 23
try:
    PDF_FORM_ERROR = (-1)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 24
try:
    PDF_FORM_NOTAVAIL = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 25
try:
    PDF_FORM_AVAIL = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 26
try:
    PDF_FORM_NOTEXIST = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 15
def FPDF_ARGB(a, r, g, b):
    return (c_uint32 (ord_if_char((((((c_uint32 (ord_if_char(b))).value & 255) | (((c_uint32 (ord_if_char(g))).value & 255) << 8)) | (((c_uint32 (ord_if_char(r))).value & 255) << 16)) | (((c_uint32 (ord_if_char(a))).value & 255) << 24))))).value

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 18
def FPDF_GetBValue(argb):
    return (c_uint8 (ord_if_char(argb))).value

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 19
def FPDF_GetGValue(argb):
    return (c_uint8 (ord_if_char(((c_uint16 (ord_if_char(argb))).value >> 8)))).value

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 20
def FPDF_GetRValue(argb):
    return (c_uint8 (ord_if_char((argb >> 16)))).value

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 21
def FPDF_GetAValue(argb):
    return (c_uint8 (ord_if_char((argb >> 24)))).value

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 24
try:
    FPDF_COLORSPACE_UNKNOWN = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 25
try:
    FPDF_COLORSPACE_DEVICEGRAY = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 26
try:
    FPDF_COLORSPACE_DEVICERGB = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 27
try:
    FPDF_COLORSPACE_DEVICECMYK = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 28
try:
    FPDF_COLORSPACE_CALGRAY = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 29
try:
    FPDF_COLORSPACE_CALRGB = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 30
try:
    FPDF_COLORSPACE_LAB = 6
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 31
try:
    FPDF_COLORSPACE_ICCBASED = 7
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 32
try:
    FPDF_COLORSPACE_SEPARATION = 8
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 33
try:
    FPDF_COLORSPACE_DEVICEN = 9
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 34
try:
    FPDF_COLORSPACE_INDEXED = 10
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 35
try:
    FPDF_COLORSPACE_PATTERN = 11
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 38
try:
    FPDF_PAGEOBJ_UNKNOWN = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 39
try:
    FPDF_PAGEOBJ_TEXT = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 40
try:
    FPDF_PAGEOBJ_PATH = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 41
try:
    FPDF_PAGEOBJ_IMAGE = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 42
try:
    FPDF_PAGEOBJ_SHADING = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 43
try:
    FPDF_PAGEOBJ_FORM = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 46
try:
    FPDF_SEGMENT_UNKNOWN = (-1)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 47
try:
    FPDF_SEGMENT_LINETO = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 48
try:
    FPDF_SEGMENT_BEZIERTO = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 49
try:
    FPDF_SEGMENT_MOVETO = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 51
try:
    FPDF_FILLMODE_NONE = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 52
try:
    FPDF_FILLMODE_ALTERNATE = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 53
try:
    FPDF_FILLMODE_WINDING = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 55
try:
    FPDF_FONT_TYPE1 = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 56
try:
    FPDF_FONT_TRUETYPE = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 58
try:
    FPDF_LINECAP_BUTT = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 59
try:
    FPDF_LINECAP_ROUND = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 60
try:
    FPDF_LINECAP_PROJECTING_SQUARE = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 62
try:
    FPDF_LINEJOIN_MITER = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 63
try:
    FPDF_LINEJOIN_ROUND = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 64
try:
    FPDF_LINEJOIN_BEVEL = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 66
try:
    FPDF_PRINTMODE_EMF = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 67
try:
    FPDF_PRINTMODE_TEXTONLY = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 68
try:
    FPDF_PRINTMODE_POSTSCRIPT2 = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 69
try:
    FPDF_PRINTMODE_POSTSCRIPT3 = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 70
try:
    FPDF_PRINTMODE_POSTSCRIPT2_PASSTHROUGH = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 71
try:
    FPDF_PRINTMODE_POSTSCRIPT3_PASSTHROUGH = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 20
try:
    FPDF_UNSP_DOC_XFAFORM = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 22
try:
    FPDF_UNSP_DOC_PORTABLECOLLECTION = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 24
try:
    FPDF_UNSP_DOC_ATTACHMENT = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 26
try:
    FPDF_UNSP_DOC_SECURITY = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 28
try:
    FPDF_UNSP_DOC_SHAREDREVIEW = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 30
try:
    FPDF_UNSP_DOC_SHAREDFORM_ACROBAT = 6
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 32
try:
    FPDF_UNSP_DOC_SHAREDFORM_FILESYSTEM = 7
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 34
try:
    FPDF_UNSP_DOC_SHAREDFORM_EMAIL = 8
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 36
try:
    FPDF_UNSP_ANNOT_3DANNOT = 11
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 38
try:
    FPDF_UNSP_ANNOT_MOVIE = 12
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 40
try:
    FPDF_UNSP_ANNOT_SOUND = 13
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 42
try:
    FPDF_UNSP_ANNOT_SCREEN_MEDIA = 14
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 44
try:
    FPDF_UNSP_ANNOT_SCREEN_RICHMEDIA = 15
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 46
try:
    FPDF_UNSP_ANNOT_ATTACHMENT = 16
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 48
try:
    FPDF_UNSP_ANNOT_SIG = 17
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 92
try:
    PAGEMODE_UNKNOWN = (-1)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 94
try:
    PAGEMODE_USENONE = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 96
try:
    PAGEMODE_USEOUTLINES = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 98
try:
    PAGEMODE_USETHUMBS = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 100
try:
    PAGEMODE_FULLSCREEN = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 102
try:
    PAGEMODE_USEOC = 4
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 104
try:
    PAGEMODE_USEATTACHMENTS = 5
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_flatten.h: 14
try:
    FLATTEN_FAIL = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_flatten.h: 16
try:
    FLATTEN_SUCCESS = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_flatten.h: 18
try:
    FLATTEN_NOTHINGTODO = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_flatten.h: 21
try:
    FLAT_NORMALDISPLAY = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_flatten.h: 23
try:
    FLAT_PRINT = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 15
try:
    FPDF_RENDER_READY = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 16
try:
    FPDF_RENDER_TOBECONTINUED = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 17
try:
    FPDF_RENDER_DONE = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 18
try:
    FPDF_RENDER_FAILED = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h: 45
try:
    FPDF_INCREMENTAL = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h: 46
try:
    FPDF_NO_INCREMENTAL = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h: 47
try:
    FPDF_REMOVE_SECURITY = 3
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 15
try:
    FXFONT_ANSI_CHARSET = 0
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 16
try:
    FXFONT_DEFAULT_CHARSET = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 17
try:
    FXFONT_SYMBOL_CHARSET = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 18
try:
    FXFONT_SHIFTJIS_CHARSET = 128
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 19
try:
    FXFONT_HANGEUL_CHARSET = 129
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 20
try:
    FXFONT_GB2312_CHARSET = 134
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 21
try:
    FXFONT_CHINESEBIG5_CHARSET = 136
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 22
try:
    FXFONT_ARABIC_CHARSET = 178
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 23
try:
    FXFONT_CYRILLIC_CHARSET = 204
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 24
try:
    FXFONT_EASTERNEUROPEAN_CHARSET = 238
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 27
try:
    FXFONT_FF_FIXEDPITCH = (1 << 0)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 28
try:
    FXFONT_FF_ROMAN = (1 << 4)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 29
try:
    FXFONT_FF_SCRIPT = (4 << 4)
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 32
try:
    FXFONT_FW_NORMAL = 400
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 33
try:
    FXFONT_FW_BOLD = 700
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 434
try:
    FPDF_MATCHCASE = 1
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 436
try:
    FPDF_MATCHWHOLEWORD = 2
except:
    pass

# /Users/thead/Downloads/pdfium-darwin/include/fpdf_text.h: 438
try:
    FPDF_CONSECUTIVE = 4
except:
    pass

fpdf_action_t__ = struct_fpdf_action_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 54

fpdf_annotation_t__ = struct_fpdf_annotation_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 55

fpdf_attachment_t__ = struct_fpdf_attachment_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 56

fpdf_bitmap_t__ = struct_fpdf_bitmap_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 57

fpdf_bookmark_t__ = struct_fpdf_bookmark_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 58

fpdf_clippath_t__ = struct_fpdf_clippath_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 59

fpdf_dest_t__ = struct_fpdf_dest_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 60

fpdf_document_t__ = struct_fpdf_document_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 61

fpdf_font_t__ = struct_fpdf_font_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 62

fpdf_form_handle_t__ = struct_fpdf_form_handle_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 63

fpdf_javascript_action_t = struct_fpdf_javascript_action_t# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 64

fpdf_link_t__ = struct_fpdf_link_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 65

fpdf_page_t__ = struct_fpdf_page_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 66

fpdf_pagelink_t__ = struct_fpdf_pagelink_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 67

fpdf_pageobject_t__ = struct_fpdf_pageobject_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 68

fpdf_pageobjectmark_t__ = struct_fpdf_pageobjectmark_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 69

fpdf_pagerange_t__ = struct_fpdf_pagerange_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 70

fpdf_pathsegment_t = struct_fpdf_pathsegment_t# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 71

fpdf_schhandle_t__ = struct_fpdf_schhandle_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 73

fpdf_structelement_t__ = struct_fpdf_structelement_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 74

fpdf_structtree_t__ = struct_fpdf_structtree_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 75

fpdf_textpage_t__ = struct_fpdf_textpage_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 76

fpdf_widget_t__ = struct_fpdf_widget_t__# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 77

FPDF_BSTR_ = struct_FPDF_BSTR_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 110

_FS_MATRIX_ = struct__FS_MATRIX_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 136

_FS_RECTF_ = struct__FS_RECTF_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 139

FS_SIZEF_ = struct_FS_SIZEF_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 154

FS_POINTF_ = struct_FS_POINTF_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 163

FPDF_LIBRARY_CONFIG_ = struct_FPDF_LIBRARY_CONFIG_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 237

FPDF_FILEHANDLER_ = struct_FPDF_FILEHANDLER_# /Users/thead/Downloads/pdfium-darwin/include/fpdfview.h: 489

_FS_QUADPOINTSF = struct__FS_QUADPOINTSF# /Users/thead/Downloads/pdfium-darwin/include/fpdf_doc.h: 48

_IPDF_JsPlatform = struct__IPDF_JsPlatform# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 52

_FPDF_SYSTEMTIME = struct__FPDF_SYSTEMTIME# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 353

_FPDF_FORMFILLINFO = struct__FPDF_FORMFILLINFO# /Users/thead/Downloads/pdfium-darwin/include/fpdf_formfill.h: 375

_FX_FILEAVAIL = struct__FX_FILEAVAIL# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 33

_FX_DOWNLOADHINTS = struct__FX_DOWNLOADHINTS# /Users/thead/Downloads/pdfium-darwin/include/fpdf_dataavail.h: 72

FPDF_IMAGEOBJ_METADATA = struct_FPDF_IMAGEOBJ_METADATA# /Users/thead/Downloads/pdfium-darwin/include/fpdf_edit.h: 89

_UNSUPPORT_INFO = struct__UNSUPPORT_INFO# /Users/thead/Downloads/pdfium-darwin/include/fpdf_ext.h: 51

_IFSDK_PAUSE = struct__IFSDK_PAUSE# /Users/thead/Downloads/pdfium-darwin/include/fpdf_progressive.h: 25

FPDF_FILEWRITE_ = struct_FPDF_FILEWRITE_# /Users/thead/Downloads/pdfium-darwin/include/fpdf_save.h: 19

_FPDF_SYSFONTINFO = struct__FPDF_SYSFONTINFO# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 44

FPDF_CharsetFontMap_ = struct_FPDF_CharsetFontMap_# /Users/thead/Downloads/pdfium-darwin/include/fpdf_sysfontinfo.h: 232

# No inserted files

# No prefix-stripping
