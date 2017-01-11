import unicodedata as ud

def unicode_info(un_symbol):
    ds = un_symbol.encode('utf-8')
    print(ds)
    print(ud.category(un_symbol),  ud.name(un_symbol), ud.lookup(ud.name(un_symbol)), sep='\n')
    print(un_symbol.encode('ascii','backslashreplace'))
    print(un_symbol.encode('ascii','xmlcharrefreplace'))

snowball = '\u2603'
unicode_info(snowball)

