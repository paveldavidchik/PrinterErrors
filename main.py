def printer_error(s):
    return f'{len([ch for ch in s if ch > "m"])}/{len(s)}'


print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
