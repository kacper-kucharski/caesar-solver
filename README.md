# Information

This program allows you to encrypt and decrypt plaintext using the caesar cipher.

### Prerequisite

You need to have [Python3](https://www.python.org/download/releases/3.0/) installed.

### Installation

Clone the project into the folder that you want it to be in (Desktop is perfectly fine).

```bash
git clone https://github.com/kacper-kucharski/caesar-solver
```

### Usage

Start python in your terminal, make sure that when u start it you check that the python version is 3.0+ (for me the command is python but for you, it could be python3).

```bash
python
```

This is an example of the commands that u can use after starting python.

The encrypt and decrypt caesar functions both need the number for the rotational shift. If you want to encrypt a plaintext and then be able to decrypt it, u would need to use the same number.

The solve_caear() function tries to decrypt the encrypted text automatically without the need for the rotational shift number.

```python
>>> import caesar
>>> caesar.encrypt_caesar("The die has been cast!", 3) # returns 'Wkh glh kdv ehhq fdvw!'
>>> caesar.decrypt_caesar("S mkwo, S ckg, S myxaeobon.", 10) # returns 'I came, I saw, I conquered.'
>>> caesar.quadgram_fitness("Wkh glh kdv ehhq fdvw!") # returns 280.95670257053285
>>> caesar.solve_caesar("Lqdqlm ivl Kwvycmz!") # returns 'Divide and Conquer!'
>>> exit() # exits the program
```