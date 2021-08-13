"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.

    def __init__(self, designation, name='', diameter='nan', hazardous=False):
        """Create a new `NearEarthObject`.

        :param designation: The primary designation for this NearEarthObject.
        :param name: The IAU name for this NearEarthObject.
        :param diameter: The diameter, in kilometers, of this NearEarthObject.
        :param hazardous: Whether or not this NearEarthObject is potentially hazardous.
        :param approaches: A collection of this NearEarthObjects close approaches to Earth.
        """
        # ̶ T̶O̶D̶O̶:̶ A̶s̶s̶i̶g̶n̶ i̶n̶f̶o̶r̶m̶a̶t̶i̶o̶n̶ f̶r̶o̶m̶ t̶h̶e̶ a̶r̶g̶u̶m̶e̶n̶t̶s̶ p̶a̶s̶s̶e̶d̶ t̶o̶ t̶h̶e̶ c̶o̶n̶s̶t̶r̶u̶c̶t̶o̶r̶
        # ̶ o̶n̶t̶o̶ a̶t̶t̶r̶i̶b̶u̶t̶e̶s̶ n̶a̶m̶e̶d̶ `̶d̶e̶s̶i̶g̶n̶a̶t̶i̶o̶n̶`̶,̶ `̶n̶a̶m̶e̶`̶,̶ `̶d̶i̶a̶m̶e̶t̶e̶r̶`̶,̶ a̶n̶d̶ `̶h̶a̶z̶a̶r̶d̶o̶u̶s̶`̶.̶
        # ̶ Y̶o̶u̶ s̶h̶o̶u̶l̶d̶ c̶o̶e̶r̶c̶e̶ t̶h̶e̶s̶e̶ v̶a̶l̶u̶e̶s̶ t̶o̶ t̶h̶e̶i̶r̶ a̶p̶p̶r̶o̶p̶r̶i̶a̶t̶e̶ d̶a̶t̶a̶ t̶y̶p̶e̶ a̶n̶d̶
        # ̶ h̶a̶n̶d̶l̶e̶ a̶n̶y̶ e̶d̶g̶e̶ c̶a̶s̶e̶s̶,̶ s̶u̶c̶h̶ a̶s̶ a̶ e̶m̶p̶t̶y̶ n̶a̶m̶e̶ b̶e̶i̶n̶g̶ r̶e̶p̶r̶e̶s̶e̶n̶t̶e̶d̶ b̶y̶ `̶N̶o̶n̶e̶`̶
        # ̶ a̶n̶d̶ a̶ m̶i̶s̶s̶i̶n̶g̶ d̶i̶a̶m̶e̶t̶e̶r̶ b̶e̶i̶n̶g̶ r̶e̶p̶r̶e̶s̶e̶n̶t̶e̶d̶ b̶y̶ `̶f̶l̶o̶a̶t̶(̶'̶n̶a̶n̶'̶)̶`̶.̶
        self.designation = str(designation)
        self.name = str(name) if name else None
        self.diameter = float(diameter) if diameter else float('nan')
        self.hazardous = bool(hazardous)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # T̶O̶D̶O̶:̶ U̶s̶e̶ s̶e̶l̶f̶.̶d̶e̶s̶i̶g̶n̶a̶t̶i̶o̶n̶ a̶n̶d̶ s̶e̶l̶f̶.̶n̶a̶m̶e̶ t̶o̶ b̶u̶i̶l̶d̶ a̶ f̶u̶l̶l̶n̶a̶m̶e̶ f̶o̶r̶ t̶h̶i̶s̶ o̶b̶j̶e̶c̶t̶.̶
        _name = f" ({self.name})" if self.name else ""
        return f'{self.designation}{_name}'

    def __str__(self):
        """Return `str(self)`."""
        # ̶ T̶O̶D̶O̶:̶ U̶s̶e̶ t̶h̶i̶s̶ o̶b̶j̶e̶c̶t̶'̶s̶ a̶t̶t̶r̶i̶b̶u̶t̶e̶s̶ t̶o̶ r̶e̶t̶u̶r̶n̶ a̶ h̶u̶m̶a̶n̶-̶r̶e̶a̶d̶a̶b̶l̶e̶ s̶t̶r̶i̶n̶g̶ r̶e̶p̶r̶e̶s̶e̶n̶t̶a̶t̶i̶o̶n̶.̶
        # ̶ T̶h̶e̶ p̶r̶o̶j̶e̶c̶t̶ i̶n̶s̶t̶r̶u̶c̶t̶i̶o̶n̶s̶ i̶n̶c̶l̶u̶d̶e̶ o̶n̶e̶ p̶o̶s̶s̶i̶b̶i̶l̶i̶t̶y̶.̶ P̶e̶e̶k̶ a̶t̶ t̶h̶e̶ _̶_̶r̶e̶p̶r̶_̶_̶
        # ̶ m̶e̶t̶h̶o̶d̶ f̶o̶r̶ e̶x̶a̶m̶p̶l̶e̶s̶ o̶f̶ a̶d̶v̶a̶n̶c̶e̶d̶ s̶t̶r̶i̶n̶g̶ f̶o̶r̶m̶a̶t̶t̶i̶n̶g̶.̶
        return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and {'is' if  self.hazardous else 'is not'} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")

    def add_approach(self, approach):
        self.approaches.append(approach)


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # ̶ T̶O̶D̶O̶:̶ H̶o̶w̶ c̶a̶n̶ y̶o̶u̶,̶ a̶n̶d̶ s̶h̶o̶u̶l̶d̶ y̶o̶u̶,̶ c̶h̶a̶n̶g̶e̶ t̶h̶e̶ a̶r̶g̶u̶m̶e̶n̶t̶s̶ t̶o̶ t̶h̶i̶s̶ c̶o̶n̶s̶t̶r̶u̶c̶t̶o̶r̶?̶
    # ̶ I̶f̶ y̶o̶u̶ m̶a̶k̶e̶ c̶h̶a̶n̶g̶e̶s̶,̶ b̶e̶ s̶u̶r̶e̶ t̶o̶ u̶p̶d̶a̶t̶e̶ t̶h̶e̶ c̶o̶m̶m̶e̶n̶t̶s̶ i̶n̶ t̶h̶i̶s̶ f̶i̶l̶e̶.̶

    def __init__(self, designation, time, distance, velocity, neo=None):
        """Create a new `CloseApproach`.

        :param time: The date and time, in UTC, at which the NEO passes closest to Earth.
        :param distance: The nominal approach distance, in astronomical units, of the NEO to Earth at the closest point.
        :param velocity: The velocity, in kilometers per second, of the NEO relative to Earth at the closest point.
        :param neo: The NearEarthObject that is making a close approach to Earth.
        """
        # ̶ T̶O̶D̶O̶:̶ A̶s̶s̶i̶g̶n̶ i̶n̶f̶o̶r̶m̶a̶t̶i̶o̶n̶ f̶r̶o̶m̶ t̶h̶e̶ a̶r̶g̶u̶m̶e̶n̶t̶s̶ p̶a̶s̶s̶e̶d̶ t̶o̶ t̶h̶e̶ c̶o̶n̶s̶t̶r̶u̶c̶t̶o̶r̶
        # ̶ o̶n̶t̶o̶ a̶t̶t̶r̶i̶b̶u̶t̶e̶s̶ n̶a̶m̶e̶d̶ `̶_̶d̶e̶s̶i̶g̶n̶a̶t̶i̶o̶n̶`̶,̶ `̶t̶i̶m̶e̶`̶,̶ `̶d̶i̶s̶t̶a̶n̶c̶e̶`̶,̶ a̶n̶d̶ `̶v̶e̶l̶o̶c̶i̶t̶y̶`̶.̶
        # ̶ Y̶o̶u̶ s̶h̶o̶u̶l̶d̶ c̶o̶e̶r̶c̶e̶ t̶h̶e̶s̶e̶ v̶a̶l̶u̶e̶s̶ t̶o̶ t̶h̶e̶i̶r̶ a̶p̶p̶r̶o̶p̶r̶i̶a̶t̶e̶ d̶a̶t̶a̶ t̶y̶p̶e̶ a̶n̶d̶ h̶a̶n̶d̶l̶e̶ a̶n̶y̶ e̶d̶g̶e̶ c̶a̶s̶e̶s̶.̶
        # ̶ T̶h̶e̶ `̶c̶d̶_̶t̶o̶_̶d̶a̶t̶e̶t̶i̶m̶e̶`̶ f̶u̶n̶c̶t̶i̶o̶n̶ w̶i̶l̶l̶ b̶e̶ u̶s̶e̶f̶u̶l̶.̶
        self._designation = designation
        # TODO: Use the cd_to_datetime function for this attribute.
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # ̶ T̶O̶D̶O̶:̶ U̶s̶e̶ t̶h̶i̶s̶ o̶b̶j̶e̶c̶t̶'̶s̶ `̶.̶t̶i̶m̶e̶`̶ a̶t̶t̶r̶i̶b̶u̶t̶e̶ a̶n̶d̶ t̶h̶e̶ `̶d̶a̶t̶e̶t̶i̶m̶e̶_̶t̶o̶_̶s̶t̶r̶`̶ f̶u̶n̶c̶t̶i̶o̶n̶ t̶o̶
        # ̶ b̶u̶i̶l̶d̶ a̶ f̶o̶r̶m̶a̶t̶t̶e̶d̶ r̶e̶p̶r̶e̶s̶e̶n̶t̶a̶t̶i̶o̶n̶ o̶f̶ t̶h̶e̶ a̶p̶p̶r̶o̶a̶c̶h̶ t̶i̶m̶e̶.̶
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        # ̶ T̶O̶D̶O̶:̶ U̶s̶e̶ t̶h̶i̶s̶ o̶b̶j̶e̶c̶t̶'̶s̶ a̶t̶t̶r̶i̶b̶u̶t̶e̶s̶ t̶o̶ r̶e̶t̶u̶r̶n̶ a̶ h̶u̶m̶a̶n̶-̶r̶e̶a̶d̶a̶b̶l̶e̶ s̶t̶r̶i̶n̶g̶ r̶e̶p̶r̶e̶s̶e̶n̶t̶a̶t̶i̶o̶n̶.̶
        # ̶ T̶h̶e̶ p̶r̶o̶j̶e̶c̶t̶ i̶n̶s̶t̶r̶u̶c̶t̶i̶o̶n̶s̶ i̶n̶c̶l̶u̶d̶e̶ o̶n̶e̶ p̶o̶s̶s̶i̶b̶i̶l̶i̶t̶y̶.̶ P̶e̶e̶k̶ a̶t̶ t̶h̶e̶ _̶_̶r̶e̶p̶r̶_̶_̶
        # ̶ m̶e̶t̶h̶o̶d̶ f̶o̶r̶ e̶x̶a̶m̶p̶l̶e̶s̶ o̶f̶ a̶d̶v̶a̶n̶c̶e̶d̶ s̶t̶r̶i̶n̶g̶ f̶o̶r̶m̶a̶t̶t̶i̶n̶g̶.̶
        time_array = self.time_str.split()
        return f"On {time_array[0]} at {time_array[1]}, '{self.neo.fullname}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
