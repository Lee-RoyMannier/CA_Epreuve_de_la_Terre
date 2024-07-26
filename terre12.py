# Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.


# Exemples d’utilisation :
# $> ruby exo.rb 11:40PM
# 23:40

# Attention : midi et minuit.

import sys


def is_evening(time: str) -> bool:
    i: int = 5
    prefix: str = ""

    while i <= 6:
        prefix += time[i]
        i += 1
    print(prefix)
    return prefix == "PM"


def hour_minute_to_int(time: str) -> tuple:
    h: str = ""
    m: str = ""
    i: int = 0

    while i <= 4:
        i += 1
        if time[i - 1] != ":" and i - 1 < 2:
            h += time[i - 1]
        elif time[i - 1] == ":":
            continue
        else:
            m += time[i - 1]

    int_h = int(h)
    int_m = int(m)

    return (int_h, int_m)


def transform_hour(time: str) -> str:
    hour: str = ""
    h, m = hour_minute_to_int(time)

    if is_evening(time):
        if h == "00":
            hour += "12"
        else:
            hour += str(h + 12)
    else:
        hour = h

    return f"{hour}:{m}"


time = sys.argv[1]
x = transform_hour(time)
print(x)
