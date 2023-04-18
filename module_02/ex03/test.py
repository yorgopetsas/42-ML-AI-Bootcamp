from csvreader import CsvReader


if __name__ == "__main__":
    with CsvReader('good.csv', header=False, skip_top=0, skip_bottom=0) as file:
        # print('Header:', file.getheader(), end = "\n")

        if file:
            data = file.getdata()
            print(data)
            # header = file.getheader()
            # print(header)

        elif file == None:
            print("File is corrupted")