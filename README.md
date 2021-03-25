# FCracker

**Current Release: v0.0.1 (2021.25.03)**


Overview
--------
- FCrack is a command-line tool designed to brute force encrypted files like zip, 7z, rar, pdf etc.
- At present it works only in linux with proper depencences. This tool is made for both personal and CTF use.

- FCrack is developed by [@zZBlackArrowZz](https://twitter.com/zZBlackArrowZz)


Installation & Usage
------------

```python
git clone https://github.com/TarunYenni/FCracker.git
cd FCracker
python FCrack.py

############################################################################
############################################################################
########################### File Cracker ###################################
###################### Using John / Hashcat ################################
#################### Author: zZBlackArrowZz ################################
############################################################################
############################################################################
################### Currently in development ###############################


Supported file formats: .zip, .rar, .pdf, .7z, .doc/.docx (2007/2013)
usage: FCrack.py [-h] -f <Input_File> -w <wordlist>
FCrack.py: error: argument -f/--ifile is required
```

Dependences
-----------
```
sudo apt-get install john -y
sudo apt install libcompress-raw-lzma-perl -y

```

Options
-------


```
usage: FCrack.py [-h] -f <Input_File> -w <wordlist>

optional arguments:
  -h, --help            show this help message and exit
  -f <Input_File>, --ifile <Input_File>
                        Take's a file_name as input
  -w <wordlist>, --wordlist <wordlist>
                        Take's a wordlist as input
```

