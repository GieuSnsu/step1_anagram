from anagram1 import lookup

# aerst anagrams
def aerst_test():
    aerst = lookup("aerst")
    tsrea = lookup("tsrea")
    assert aerst == tsrea
    answer = {"resat", "tares", "rates", "stare",
               "tears", "satre", "aster"}
    assert aerst == answer

# aceprs anagrams
def aceprs_test():
    aercps = lookup("aercps")
    reaspc = lookup("reaspc")
    assert aercps == reaspc
    answer = {"capers", "crapes", "scrape", "spacer",
              "parsec", "recaps", "pacers"}
    assert aercps == answer

# bb anagrams
def bb_test():
    bb = lookup("bb")
    assert not bb

# run all tests
aerst_test()
aceprs_test()
bb_test()
