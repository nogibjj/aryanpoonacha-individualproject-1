# importing the library
import lib


def full_describe(filepath):
    df = lib.readfile(filepath)
    lib.stats(df)
    lib.save_stats(df)
    lib.visualize_cars(df)
    return 0


def main():
    full_describe("tables/cars.csv")


if __name__ == "__main__":
    main()
