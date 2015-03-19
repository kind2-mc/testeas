"""Entry point."""

from stdout import (
    new_line, log, log_lines,
    error, warning, info,
    error_lines, warning_lines, info_lines
)
import conf
import flags

new_line()

flags.parse_arguments()

for lvl in [0,1,2,3]:

    new_line()
    new_line()
    conf.set_log_lvl(lvl)
    conf.print_conf()

    log("testing log default")
    new_line()
    log("testing log 0", 0)
    new_line(0)
    log("testing log 1", 1)
    new_line(1)
    log("testing log 2", 2)
    new_line(2)
    log("testing log 3", 3)
    new_line(3)

    error("testing error")
    warning("testing warning")
    info("testing info default")
    info("testing info 0", 0)
    info("testing info 1", 1)
    info("testing info 2", 2)
    info("testing info 3", 3)

    error_lines(["testing", "error", "lines"])
    warning_lines(["testing", "warning", "lines"])
    info_lines(["testing", "info", "lines"])

    try: input()
    except: pass

new_line()