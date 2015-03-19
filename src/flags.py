""" Flag handling. """

import sys

from stdout import info, warning, error, new_line
import conf

# List of options. An option is a triplet of:
# * a list of string representations of the option,
# * a description of the option for help printing,
# * an action taking the tail of arguments and returning its new
#   state.
#
# Additionally, an option with an empty list of representations
# is understood as an option section header.
_options = []

def _print_help():
    """ Prints the options. """
    print("")
    print("Options:")
    for triplet in _options:
        if len(triplet[0]) < 1:
            new_line()
            for header_line in triplet[1]:
                print("|===| {}".format(header_line))
        else:
            print("> {}".format(triplet[0]))
            for desc_line in triplet[1]:
                print("  {}".format(desc_line))
    new_line()

def _print_help_exit(code):
    """ Prints the options and exits. """
    _print_help()
    sys.exit(code)

def _find_option_triplet(option):
    """ Finds the option triplet corresponding to an argument. """
    # Go through the list of options.
    for triplet in _options:
        # Return first match.
        if option in triplet[0]: return triplet

def parse_arguments():
    """ Parses the arguments and calls relevant actions. """

    # Ignore first package/file name argument.
    args = sys.argv[1:]

    def handle_options(args):
        """ Returns its input list if length of said list is one or
        less.
        Otherwise, finds the option triplet corresponding to
        the head of the list, applies the action, and loops on the
        resulting list. """
        if len(args) < 2:
            # One argument or less left, returning.
            return args
        else:
            option = args[0]
            triplet = _find_option_triplet(option)
            if triplet == None:
                # Unknown option, error.
                _print_help()
                error( "Unexpected option \"{}\".".format(option) )
                error("")
                sys.exit(1)
            else:
                # Looping with updated tail of arguments.
                handle_options( triplet[2](args[1:]) )

    args = handle_options(args)
    max_log_lvl = conf.max_log_lvl()

    info("Flags left: {}.".format(args), max_log_lvl)

    new_line(max_log_lvl)








# Building the list of options.


def _add_option(reps, desc, l4mbda):
    """ Adds an option to the option list. """
    _options.append((reps, desc, l4mbda))

def _add_option_header(lines):
    """ Adds an option header to the option list. """
    _options.append((
        [],
        lines,
        "" # lambda tail: assert false
    ))

# Help option.
_add_option(
    ["-h", "--help"],
    ["prints the help message and exits"],
    lambda tail: _print_help_exit(0)
)

# Verbose option section header.
_add_option_header((
    ["Verbosity options."]
))

# Verbose option.
def _v_action(tail):
    conf.set_log_lvl(3)
    return tail
_add_option(
    ["-v"],
    ["verbose output"],
    _v_action
)

# Quiet 1 option.
def _q1_action(tail):
    conf.set_log_lvl(1)
    return tail
_add_option(
    ["-q"],
    ["no output except errors and warnings"],
    _q1_action
)

# Quiet 2 option.
def _q2_action(tail):
    conf.set_log_lvl(0)
    return tail
_add_option(
    ["-qq"],
    ["no output at all"],
    _q2_action
)