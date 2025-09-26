from teksta_apstrade import apstrada_datus

def main():
    test_teksta_apstrade()


def test_teksta_apstrade():
    try:
        assert apstrada_datus(["  kannas "]) == "kannas"
    except AssertionError:
        print("Neatbilst rezultāts kannas.")


if __name__ == "__main__":
    main()