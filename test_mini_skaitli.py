from mini_skaitli import parbaude   

def main():
    test_pareizi_skaitli()

def test_pareizi_skaitli():
    try:
        assert parbaude("25") == 25
    except AssertionError:
        print("nepareiza ievade skaitlim 25")
    try:
        assert parbaude("1") == 1
    except AssertionError:
        print("nepareiza ievade skaitlim 1")
    try:
        assert parbaude("50") == 50
    except AssertionError:
        print("nepareiza ievade skaitlim 50")


if __name__ == "__main__":
    main()