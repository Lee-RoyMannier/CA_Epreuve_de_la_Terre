# Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.


# Exemples d’utilisation :
# $> ruby exo.rb 23:40
# 11:40PM

# Attention : midi et minuit.


import sys


def time_prefix(time: int):
    if time < 12:
        return "am"
    return "pm"


def hour_minut_to_int(time: str) -> tuple:
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


def time_transformation(h: int, m: int) -> str:
    prefix = time_prefix(h)
    hour: str = ""

    if h < 12:
        if h < 9:
            hour = f"0{h}"
        else:
            hour = f"{h}"
    else:
        print(h)
        h = h - 12

    hour = "00" if h == 12 else f"0{h}" if h < 10 else f"{h}"

    return f"{hour}:{m} {prefix}"


h, m = hour_minut_to_int(sys.argv[1])
print(time_transformation(h, m))
