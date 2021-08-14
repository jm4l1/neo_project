"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_collection = []
    with open(neo_csv_path, 'r') as neo_file:
        reader = csv.DictReader(neo_file)
        for row in reader:
            pha = row['pha'].upper() == 'Y'
            neo = NearEarthObject(
                row['pdes'], row['name'], row['diameter'], pha)
            neo_collection.append(neo)
    return tuple(neo_collection)


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    neo_approaches = []
    with open(cad_json_path, 'r') as cad_file:
        file_contents = cad_file.read()
        file_contents = json.loads(file_contents)
        cad_data = file_contents['data']
        for entry in cad_data:
            cad = CloseApproach(entry[0], entry[3], entry[4], entry[7])
            neo_approaches.append(cad)

    return tuple(neo_approaches)
