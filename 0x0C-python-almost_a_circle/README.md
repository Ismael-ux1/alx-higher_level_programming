This is a readme file for the project python-almost_a_circle

Python Project: Review Everything About Python
This project covers various topics in Python, including import, exceptions, classes, private attributes, getter/setter methods, class methods, static methods, inheritance, file handling (read/write), args and kwargs, serialization/deserialization, and JSON. Additionally, it introduces unit testing for Python scripts.

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the project folder is mandatory
Your code should adhere to PEP 8 style guidelines (pycodestyle version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
Documentation should be a complete sentence, explaining the purpose of the module, class, or method (length will be verified)
Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder named tests
You have to use the unittest module for writing unit tests
All your test files should have a .py extension
All your test files and folders should start with test_
Your file organization in the tests folder should mirror your project structure (e.g., for models/base.py, unit tests must be in tests/test_models/test_base.py)
All your tests should be executed using the command: python3 -m unittest discover tests
Individual test files can be executed using the command: python3 -m unittest tests/test_models/test_base.py
Collaboration on test cases is encouraged to cover all edge cases
Classes
Base
Represents the "base" class for all other classes in the project. It includes the following features:

Private class attribute __nb_objects = 0
Public instance attribute id
Class constructor def __init__(self, id=None): If id is None, increments __nb_objects and assigns its value to the public instance attribute id. Otherwise, sets the public instance attribute id to the provided id.
Static method def to_json_string(list_dictionaries): Returns the JSON string serialization of a list of dictionaries. If list_dictionaries is None or empty, returns the string "[]".
Class method def save_to_file(cls, list_objs): Writes the JSON serialization of a list of objects to a file. The parameter list_objs is expected to be a list of Base-inherited instances. If list_objs is None, the function saves an empty list. The file is saved with the name <cls name>.json (e.g., Rectangle.json). It overwrites the file if it already exists.
Static method def from_json_string(json_string): Returns a list of objects deserialized from a JSON string. The parameter json_string is expected to be a string representing a list of dictionaries. If json_string is None or empty, the function returns an empty list.
Class method def create(cls, **dictionary): Instantiates an object with provided attributes. It instantiates an object with the attributes given in **dictionary.
Class method def load_from_file(cls): Returns a list of objects instantiated from a JSON file. It reads from the JSON file <cls name>.json (e.g., Rectangle.json). If the file does not exist, the function returns an empty list.
Class method def save_to_file_csv(cls, list_objs): Writes the CSV serialization of a list of objects to a file. The parameter list_objs is expected to be a list of Base-inherited instances. If list_objs is None, the function saves an empty list. The file is saved with the name <cls name>.csv (e.g., Rectangle.csv). It serializes objects in the format <id>,<width>,<height>,<x>,<y> for Rectangle objects and <id>,<size>,<x>,<y> for Square objects.
Class method def load_from_file_csv(cls): Returns a list of objects instantiated from a CSV file. It reads from the CSV file <cls name>.csv (e.g., Rectangle.csv). If the file does not exist, the function returns an empty list.
Static method def draw(list_rectangles, list_squares): Draws Rectangle and Square instances in a GUI window using the turtle module. The parameter list_rectangles is expected to be a list of Rectangle objects to print. The parameter list_squares is expected to be a list of Square objects to print.
Rectangle
Represents a rectangle that inherits from Base. It includes the following features:

Private instance attributes __width, __height, __x, and __y
Each private instance attribute features its own getter/setter methods
Class constructor def __init__(self, width, height, x=0, y=0, id=None): Raises TypeError if either of width, height, x, or y is not an integer. Raises ValueError if either width or height is >= 0, or if either x or y is less than 0. The width and height of the Rectangle superclass are assigned using the value of size.
Public method def area(self): Returns the area of the Rectangle instance.
Public method def display(self): Prints the Rectangle instance to stdout using the # character. Prints new lines for the y coordinate and spaces for the x coordinate.
Overwrite of __str__ method to print a Rectangle instance in the format [Rectangle] (<id>) <x>/<y>.
Public method def update(self, *args, **kwargs): Updates an instance of a Rectangle with the given attributes. *args must be supplied in the following order: 1st: id, 2nd: width, 3rd: height, 4th: x, 5th: y. **kwargs is expected to be a double pointer to a dictionary of new key/value attributes to update the Rectangle with. **kwargs is skipped if *args exists.
Public method def to_dictionary(self): Returns the dictionary representation of a Rectangle instance.
Square
Represents a square that inherits from Rectangle. It includes the following features:

Class constructor def __init__(self, size, x=0, y=0, id=None): The width and height of the Rectangle superclass are assigned using the value of size.
Overwrite of __str__ method to print a Square instance in the format [Square] (<id>) <x>/<y>.
Public method def update(self, *args, **kwargs): Updates an instance of a Square with the given attributes. *args must be supplied in the following order: 1st: id, 2nd: size, 3rd: x, 4th: y. **kwargs is expected to be a double pointer to a dictionary of new key/value attributes to update the Square with. **kwargs is skipped if *args exists.
Public method def to_dictionary(self): Returns the dictionary representation of a Square.
