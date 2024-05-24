from anagram1 import lookup

def aerst_test():
    aerst = lookup("aerst")
    tsrea = lookup("tsrea")
    assert aerst == tsrea
    answer = {"resat", "tares", "rates", "stare",
               "tears", "satre", "aster"}
    assert aerst == answer

def aceprs_test():
    aercps = lookup("aercps")
    reaspc = lookup("reaspc")
    assert aercps == reaspc
    answer = {"capers", "crapes", "scrape", "spacer",
              "parsec", "recaps", "pacers"}
    assert aercps == answer

aerst_test()
aceprs_test()
