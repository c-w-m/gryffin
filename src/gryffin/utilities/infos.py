#!/usr/bin/env python
"""
Refactor infos.py to use psutil as a drop in for resource making it compatible
for Windows.

`psutil` also accounts for

ref: https://fa.bianp.net/blog/2013/different-ways-to-get-memory-consumption-or-lessons-learned-from-memory_profiler/

https://docs.python.org/3/library/resource.html

resource.RUSAGE_SELF
Pass to getrusage() to request resources consumed by the calling process, which is the sum of resources used by all threads in the process.

https://docs.python.org/3/library/resource.html#resource-usage

| Index | Field       | Resource                            |
|-------|-------------|-------------------------------------|
|     0 | ru_utime    | time in user mode (float seconds)   |
|     1 | ru_stime    | time in system mode (float seconds) |
|     2 | ru_maxrss   | maximum resident set size           |
|     3 | ru_ixrss    | shared memory size                  |
|     4 | ru_idrss    | unshared memory size                |
|     5 | ru_isrss    | unshared stack size                 |
|     6 | ru_minflt   | page faults not requiring I/O       |
|     7 | ru_majflt   | page faults requiring I/O           |
|     8 | ru_nswap    | number of swap outs                 |
|     9 | ru_inblock  | block input operations              |
|    10 | ru_oublock  | block output operations             |
|    11 | ru_msgsnd   | messages sent                       |
|    12 | ru_msgrcv   | messages received                   |
|    13 | ru_nsignals | signals received                    |
|    14 | ru_nvcsw    | voluntary context switches          |
|    15 | ru_nivcsw   | involuntary context switches        |

---

def format_bytes(butes, unit, SI-False)
ref: https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
"""

import os
# import resource  # FIXME resource does not work on Windows
import psutil     # FIX psutil works on nix and win


def parse_time(start, end):
    elapsed = end - start  # elapsed time in seconds
    if elapsed <= 1.0:
        ms = elapsed * 1000.
        time_string = f"{ms:.1f} ms"
    elif 1.0 < elapsed < 60.0:
        time_string = f"{elapsed:.1f} s"
    else:
        m, s = divmod(elapsed, 60)
        time_string = f"{m:.0f} min {s:.0f} s"
    return time_string

def format_bytes(mem_size: int, unit: str, SI=False) -> float:
    if unit.lower() in "b bit bits".split():
        return f"{mem_size*8} {unit}"
    unitN = unit[0].upper() + unit[1:].replace("s", "")  # Normalised
    reference = {"Kb Kib Kibibit Kilobit": (7, 1),
                 "KB KiB Kibibyte Kilobyte": (10, 1),
                 "Mb Mib Mebibit Megabit": (17, 2),
                 "MB MiB Mebibyte Megabyte": (20, 2),
                 "Gb Gib Gibibit Gigabit": (27, 3),
                 "GB GiB Gibibyte Gigabyte": (30, 3),
                 "Tb Tib Tebibit Terabit": (37, 4),
                 "TB TiB Tebibyte Terabyte": (40, 4),
                 "Pb Pib Pebibit Petabit": (47, 5),
                 "PB PiB Pebibyte Petabyte": (50, 5),
                 "Eb Eib Exbibit Exabit": (57, 6),
                 "EB EiB Exbibyte Exabyte": (60, 6),
                 "Zb Zib Zebibit Zettabit": (67, 7),
                 "ZB ZiB Zebibyte Zettabyte": (70, 7),
                 "Yb Yib Yobibit Yottabit": (77, 8),
                 "YB YiB Yobibyte Yottabyte": (80, 8),
                 }
    key_list = '\n'.join(["     b Bit"] + [x for x in reference.keys()]) + "\n"
    if unitN not in key_list:
        raise IndexError(f"\n\nConversion unit must be one of:\n\n{key_list}")
    units, divisors = [(k, v) for k, v in reference.items() if unitN in k][0]
    if SI:
        divisor = 1000**divisors[1] / 8 if "bit" in units else 1000**divisors[1]
    else:
        divisor = float(1 << divisors[0])
    value = mem_size / divisor
    # return f"{value:,.0f} {unitN}{(value != 1 and len(unitN) > 3)*'s'}"
    return value


def memory_usage():
    """
    return the memory usage in GB, MB, and kB
    """
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss  # in bytes

    GB = format_bytes(mem, "GB")  # kB // 1000000.
    MB = format_bytes(mem, "MB")  # kB // 1000.
    kB = format_bytes(mem, "kB")  # kB % 1000.

    return GB, MB, kB


# def memory_usage():
# """deprecated"""
#     if sys.platform == 'darwin':  # MacOS --> memory in bytes
#         kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
#     else:  # Linux --> memory in kilobytes
#         kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

#     GB = kB // 1000000.
#     MB = kB // 1000.
#     kB = kB % 1000.
#     return GB, MB, kB


def print_memory_usage():
    GB, MB, kB = memory_usage()
    print(f'==> MEMORY USAGE: {GB:.0f} GB, {MB:.0f} MB, {kB:.0f} kB')
