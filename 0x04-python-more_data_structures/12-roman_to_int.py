#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    list_rom = list(roman_string)
    total = 0

    for i in range(len(list_rom)):
        if i < len(list_rom) - 1:
            if rom_n.get(list_rom[i]) >= rom_n.get(list_rom[i + 1]):
                total += rom_n.get(list_rom[i])
            else:
                total -= rom_n.get(list_rom[i])
        else:
            total += rom_n.get(list_rom[i])

    return total
