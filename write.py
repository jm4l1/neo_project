"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s',
                  'designation', 'name', 'diameter_km', 'potentially_hazardous')
    with open(filename, 'w') as csv_out_file:
        csv_writer = csv.writer(csv_out_file)
        csv_writer.writerow(fieldnames)
        for approach in results:
            serialized_approach = approach.serialize()
            serialized_neo = approach.neo.serialize()
            row = [serialized_approach['datetime_utc'],
                   serialized_approach['distance_au'], serialized_approach['velocity_km_s'],
                   serialized_neo['designation'], serialized_neo['name'], serialized_neo[
                       'diameter_km'], serialized_neo['potentially_hazardous']
                   ]
            csv_writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    with open(filename, 'w') as json_out_file:
        results_array = []
        for approach in results:
            approach_object = {
                **approach.serialize(),
                "neo": {
                    **(approach.neo.serialize())
                }
            }
            results_array.append(approach_object)
        json_out_file.write(json.dumps(results_array))
