import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("meta/table.csv")
    print df.tail(10)


if __name__ == "__main__":
    test_run()
