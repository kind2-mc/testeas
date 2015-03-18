""" Basic io operations. """

# Single line printing.

def error(txt):
    """ Prints some text prefixed by `[ error ] `. """
    print( "[ error ] " + txt )

def warning(txt):
    """ Prints some text prefixed by `[warning] `. """
    print( "[warning] " + txt )

def info(txt):
    """ Prints some text prefixed by `[ info  ] `. """
    print( "[ info  ] " + txt )


# Multi line printing.

def error_lines(lines) :
    """ Prints some lines prefixed by `[ error ] `. """
    for line in lines : error(line)

def warning_lines(lines) :
    """ Prints some lines prefixed by `[warning] `. """
    for line in lines : warning(line)


def info_lines(lines) :
    """ Prints some lines prefixed by `[ info  ] `. """
    for line in lines : info(line)