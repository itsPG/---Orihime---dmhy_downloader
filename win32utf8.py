import os, sys, io, win32api, win32console, pywintypes

def change_file_encoding(f, encoding):
	"""
	TextIOWrapper is missing a way to change the file encoding, so we have to
	do it by creating a new one.
	"""

	errors = f.errors
	line_buffering = f.line_buffering
	# f.newlines is not the same as the newline parameter to TextIOWrapper.
	# newlines = f.newlines

	buf = f.detach()

	# TextIOWrapper defaults newline to \r\n on Windows, even though the underlying
	# file object is already doing that for us.  We need to explicitly say "\n" to
	# make sure we don't output \r\r\n; this is the same as the internal function
	# create_stdio.
	return io.TextIOWrapper(buf, encoding, errors, "\n", line_buffering)


class ConsoleFile:
    class FileNotConsole(Exception): pass

    def __init__(self, handle):
        handle = win32api.GetStdHandle(handle)
        self.screen = win32console.PyConsoleScreenBufferType(handle)
        try:
            self.screen.GetConsoleMode()
        except pywintypes.error as e:
            raise ConsoleFile.FileNotConsole

    def write(self, s):
        self.screen.WriteConsole(s)

    def close(self): pass
    def flush(self): pass
    def isatty(self): return True

    @staticmethod
    def wrap_standard_handles():
        sys.stdout.flush()
        try:
            # There seems to be no binding for _get_osfhandle.
            sys.stdout = ConsoleFile(win32api.STD_OUTPUT_HANDLE)
        except ConsoleFile.FileNotConsole:
            sys.stdout = change_file_encoding(sys.stdout, "utf-8")

        sys.stderr.flush()
        try:
            sys.stderr = ConsoleFile(win32api.STD_ERROR_HANDLE)
        except ConsoleFile.FileNotConsole:
            sys.stderr = change_file_encoding(sys.stderr, "utf-8")

ConsoleFile.wrap_standard_handles()