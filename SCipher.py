'''
Author: Omer Mirza

I created this Cipher based on a meme I found on reddit

I used two dictionaries for conversion back and forth

'''
convdict =	{
  'A': 'H',
  'B': 'R',
  'C': 'A',
  'D': 'I',
  'E': 'B',
  'F': 'D',
  'G': 'G',
  'H': 'W',
  'I': 'E',
  'J': 'F',
  'K': 'L',
  'L': 'M',
  'M': 'N',
  'N': 'S',
  'O': 'X',
  'P': 'J',
  'Q': 'K',
  'R': 'Q',
  'S': 'O',
  'T': 'P',
  'U': 'C',
  'V': 'T',
  'W': 'V',
  'X': 'Y',
  'Y': 'U',
  'Z': 'Z',
  'a': 'h',
  'b': 'r',
  'c': 'a',
  'd': 'i',
  'e': 'b',
  'f': 'd',
  'g': 'g',
  'h': 'w',
  'i': 'e',
  'j': 'f',
  'k': 'l',
  'l': 'm',
  'm': 'n',
  'n': 's',
  'o': 'x',
  'p': 'j',
  'q': 'k',
  'r': 'q',
  's': 'o',
  't': 'p',
  'u': 'c',
  'v': 't',
  'w': 'v',
  'x': 'y',
  'y': 'u',
  'z': 'z'

}

solvdict = {
  'H':'A',
  'R':'B',
  'A':'C',
  'I':'D',
  'B':'E',
  'D':'F',
  'G':'G',
  'W':'H',
  'E':'I',
  'F':'J',
  'L':'K',
  'M':'L',
  'N':'M',
  'S':'N',
  'X':'O',
  'J':'P',
  'K':'Q',
  'Q':'R',
  'O':'S',
  'P':'T',
  'C':'U',
  'T':'V',
  'V':'W',
  'Y':'X',
  'U':'Y',
  'Z':'Z',
  'h':'a',
  'r':'b',
  'a':'c',
  'i':'d',
  'b':'e',
  'd':'f',
  'g':'g',
  'w':'h',
  'e':'i',
  'f':'j',
  'l':'k',
  'm':'l',
  'n':'m',
  's':'n',
  'x':'o',
  'j':'p',
  'k':'q',
  'q':'r',
  'o':'s',
  'p':'t',
  'c':'u',
  't':'v',
  'v':'w',
  'y':'x',
  'u':'y',
  'z':'z'
}

choice = input("Type 1 for encryption, Type 2 for decryption")

if choice == "1":
    txt = input("Say something you want written in code!\n")

    code = ''

    for c in txt:
        if c in convdict:
            code = code + convdict.get(c)
        else:
            code = code + c
    
    print(code)
    

elif choice == "2":
    
    txt = input("Say something in code that you want to decipher!\n")

    code = ''

    for c in txt:
        if c in solvdict:
            code = code + solvdict.get(c)
        else:
            code = code + c
    
    print(code)


