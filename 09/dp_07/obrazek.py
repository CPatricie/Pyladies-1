def nakresli_obesence(spatny_tip):
    obesenec = ["""






~~~~~~~
------------------""", """+
|
|
|
|
|
~~~~~~~
------------------""", """+---.
|
|
|
|
|
~~~~~~~
------------------""", """+---.
|   |
|
|
|
|
~~~~~~~
------------------""", """+---.
|   |
|   O
|
|
|
~~~~~~~
------------------""", """+---.
|   |
|   O
|   |
|
|
~~~~~~~
------------------""", """+---.
|   |
|   O
| --|
|
|
~~~~~~~
------------------""", """+---.
|   |
|   O
| --|--
|
|
~~~~~~~
------------------""", """+---.
|   |
|   O
| --|--
|  /
|
~~~~~~~
------------------""", """+---.
|   |
|   O
| --|--
|  / \
|
~~~~~~~
------------------"""]

    return obesenec[spatny_tip - 1]
