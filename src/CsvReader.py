import csv
import pprint


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        if self.data is not None:
            self.data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass
