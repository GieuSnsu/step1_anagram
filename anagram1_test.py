from anagram1 import lookup

def aerst_test():
    aerst = lookup("aerst")
    tsrea = lookup("tsrea")
    assert aerst == tsrea
    assert "resat" in aerst and "resat" in tsrea
    assert "tares" in aerst and "tares" in tsrea
    assert "rates" in aerst and "rates" in tsrea
    assert "stare" in aerst and "stare" in tsrea
    assert "tears" in aerst and "tears" in tsrea
    assert "satre" in aerst and "satre" in tsrea
    assert "aster" in aerst and "aster" in tsrea

def aceprs_test():
    aercps = lookup("aercps")
    reaspc = lookup("reaspc")
    assert aercps == reaspc
    assert "capers" in aercps and "capers" in reaspc
    assert "crapes" in aercps and "crapes" in reaspc
    assert "scrape" in aercps and "scrape" in reaspc
    assert "spacer" in aercps and "spacer" in reaspc
    assert "parsec" in aercps and "parsec" in reaspc
    assert "recaps" in aercps and "recaps" in reaspc
    assert "pacers" in aercps and "pacers" in reaspc

aerst_test()
aceprs_test()
