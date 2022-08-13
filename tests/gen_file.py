import csv


def get_auth_endpoints():
    with open("data1.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for el in reader:
            yield el


auth_endpoints = get_auth_endpoints()
