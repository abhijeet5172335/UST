UST Pre-Interview Coding
==========================

Problem - 1
-------------
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
○ Eg - line = “which is better python 2 or python 3”
○ Output –
('2', 1)
('3', 1)
('better', 1)
('is', 1)
('or', 1)
('python', 2)
('which', 1)

Pseudo code:
--------------
1. 1st file named "read_file.py" will read the file and return its entire content.

2. 2nd file named "count_frequency.py" contains a function, that takes:
    * takes a string as a parameter
    * returns a sorted list of tuples containing word and frequency

3. 3rd file, "main.py" will:
    * imoprts "read_file.py" and "count_frequency.py"
    * calls the function in "read_file.py" and stores the returned string value in a variable
    * calls the function in "count_frequency.py" and stores the returned list of tuples in a variable
    * prints the tuples containing words and frequency

4. 3rd file "test_frequency.py" will do unit testing using pytest

