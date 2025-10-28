from uz_lieliem import lielie

def test_lielie():
    try:
        assert lielie("sakne") == "SAKNE"
    except AssertionError:
        print("Kļūda ar sakni")
    try:
        assert lielie("sēne") == "SĒNE"
    except AssertionError:
        print("Kļūda ar sēni")

test_lielie()