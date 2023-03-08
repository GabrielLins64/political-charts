import csv


def open_xy_csv(filepath: str, num_of_header_rows: int = 1) -> tuple[list, list]:
    """Reads a csv file with only 2 columns
    representing respectively x and y.

    Parameters
    ----------
    filepath : str
    num_of_header_rows : int, optional
        number of header rows for skipping, by default 1

    Returns
    -------
    tuple(list, list)
        x and y data
    """
    with open(filepath, 'r') as file:
        reader = csv.reader(file)

        for row in range(num_of_header_rows):
            next(reader)

        x = []
        y = []

        for row in reader:
            x.append(row[0])
            y.append(float(row[1]))

    return x, y
