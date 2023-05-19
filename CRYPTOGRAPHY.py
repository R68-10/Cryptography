from tkinter import *
from tkinter import messagebox,filedialog,simpledialog
import pyperclip #module for copy to clipboard
import os

#----------------------------------------------------------------------------------------------------
def Caeser_Cipher_encrypt():
    """function to encrypt a message based on ceaser cipher algorithm"""

    message= e1.get()
    message=message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_messege = ""
    key= simpledialog.askinteger("Key","Please Enter a key")

    for ch in message:
        if ch in alphabet:
            index = alphabet.find(ch)
            newindex = (index + key) % 26
            newCharacter = alphabet[newindex]
            encrypted_messege += newCharacter
        else:
            encrypted_messege += ch

    messagebox.showinfo("Result",("Your super secret message is ",encrypted_messege))
    pyperclip.copy(encrypted_messege) #to copy the message to the clipboard
#----------------------------------------------------------------------------------------------------
def Caeser_Cipher_decrypt():
    """function to decrypt a message based on ceaser cipher algorithm"""

    message= e1.get()
    message=message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_messege = ""
    key= simpledialog.askinteger("Key","Please Enter a key")

    for ch in message:
        if ch in alphabet:
            index = alphabet.find(ch)
            newindex = (index - key) % 26
            newCharacter = alphabet[newindex]
            decrypted_messege += newCharacter
        else:
            decrypted_messege += ch

    messagebox.showinfo("Result",("Your super secret message is ",decrypted_messege))
    pyperclip.copy(decrypted_messege) #to copy the message to the clipboard
#----------------------------------------------------------------------------------------------------
def ASCII_encrypt():
    """function to enecrypt the message based on ASCII code algorithm"""

    message= e1.get()
    result=""
    for i in message:
    
        encrypted_letter=0
                        
        o=ord(i)
        encrypted_letter=o+10
        encrypted_letter=chr(encrypted_letter)
        result+=encrypted_letter
                            
    messagebox.showinfo("Result",("Your super secret message is ",result))
    pyperclip.copy(result)
#----------------------------------------------------------------------------------------------------
def ASCII_decrypt():
    """function to decrypt the message based on ASCII code algorithm"""
    message= e1.get()
    result=""

    for i in message:            
        decrypted_letter=0
        do=ord(i)
        decrypted_letter=do-10
        decrypted_letter=chr(decrypted_letter)
        result+=decrypted_letter
                           
    messagebox.showinfo("Result",("Your decrypt message is ",result))
    pyperclip.copy(result)
#----------------------------------------------------------------------------------------------------
def Morse_code_encrypt():
    """function to encrypt a message based on morse code cipher algorithm"""
    # resourse is (https://www.geeksforgeeks.org/morse-code-translator-python/)

    message= e1.get()
    message=message.upper()
    encrypted_messege = ""

    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

    for letter in message:
        if letter != ' ':
            encrypted_messege += MORSE_CODE_DICT[letter] + ' ' #space to serapate diffrent characters
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            encrypted_messege += ' '

    messagebox.showinfo("Result",("Your super secret message is ",encrypted_messege))
    pyperclip.copy(encrypted_messege) #to copy the message to the clipboard
#----------------------------------------------------------------------------------------------------
def Morse_code_decrypt():
    """function to encrypt a message based on morse code cipher algorithm"""
    # resourse is (https://www.geeksforgeeks.org/morse-code-translator-python/)

    message= e1.get()
    message += ' '
    decrypted_messege = ""
    citext = ""

    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decrypted_messege += ' '
            else:
                decrypted_messege += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)] 
                citext = ''

    decrypted_messege=decrypted_messege.lower()
    
    messagebox.showinfo("Result",("Your super secret message is ",decrypted_messege))
    pyperclip.copy(decrypted_messege) #to copy the message to the clipboard
#----------------------------------------------------------------------------------------------------
def Baconian_cipher_encrypt():
    """function to encrypt a message based on Baconian cipher algorithm"""

    baconian={'A':'aaaaa ', 'B':'aaaab ', 'C':'aaaba ', 'D':'aaabb ','E':'aabaa ',
    'F':'aabab ', 'G':'aabba ', 'H':'aabbb ', 'I':'abaaa ', 'J':'abaab ',
    'K':'abaab ', 'L':'ababa ', 'M':'ababb ', 'N':'abbaa ', 'O':'abbab ',
    'P':'abbba ', 'Q':'abbbb ', 'R':'baaaa ', 'S':'baaab ', 'T':'baaba ',
    'U':'babaa ', 'V':'babab ', 'W':'babaa ', 'X':'babab ', 'Y':'babba ', 
    'Z':'babbb '}

    message= e1.get()
    message=message.upper()
    encrypted_messege = ""

    for ch in message:
        if(ch != ' '):
            encrypted_messege += baconian[ch]
        else:
            # adds space
            encrypted_messege += ' '
    
    messagebox.showinfo("Result",("Your super secret message is ",encrypted_messege))
    pyperclip.copy(encrypted_messege)
#----------------------------------------------------------------------------------------------------
def Baconian_cipher_decrypt():
    """function to decrypt a message based on Baconian cipher algorithm"""

    baconian={'aaaaa ':'A', 'aaaab ':'B', 'aaaba ':'C', 'aaabb ':'D','aabaa ':'E',
    'aabab ':'F', 'aabba ':'G', 'aabbb ':'H', 'abaaa ':'I', 'abaab ':'J',
    'abaab ':'K', 'ababa ':'L', 'ababb ':'M', 'abbaa ':'N', 'abbab ':'O',
    'abbba ':'P', 'abbbb ':'Q', 'baaaa ':'R', 'baaab ':'S', 'baaba ':'T',
    'babaa ':'U', 'babab ':'V', 'babaa ':'W', 'babab ':'X', 'babba ':'Y', 
    'babbb ':'Z'}

    message= e1.get()
    decrypted_messege = "" 
    
    try:
        for i in range (0,len(message),6):
            decrypted_messege=decrypted_messege+baconian[message[i:i+6]]
       
        decrypted_messege=decrypted_messege.lower()
    
        messagebox.showinfo("Result",("Your super secret message is ",decrypted_messege))
        pyperclip.copy(decrypted_messege)

    except Exception:
        messagebox.showerror("Error",("Please Try again, this algorithm take only letter from a-z without a space "))
#----------------------------------------------------------------------------------------------------
#the main encryption funtion
def clicked_encrypt():
    try:
        message= e1.get()
        algorithm=list1.get(list1.curselection()[0])

        if message != "" :  #to make sure that the user enterd a massage
            
            if algorithm == "Caeser Cipher":
                Caeser_Cipher_encrypt()
            
            elif algorithm == "Morse Code Cipher":
                Morse_code_encrypt()

            elif algorithm == "Baconian Cipher":
                Baconian_cipher_encrypt()

            elif algorithm == "ASCII Code Cipher":
                ASCII_encrypt()
        else:
           messagebox.showwarning("Warning",("Please enter a massage"))

    except IndexError:
        #this error occur when the user does not select an algorithm from the listbox
        messagebox.showwarning("Warning",("Please choose an algorithem for encryption  "))
#-----------------------------------------------------------------------------------------
#the main decryption funtion
def clicked_decrypt():
    try:
        message= e1.get()
        algorithm=list1.get(list1.curselection()[0])

        if message != "" : #to make sure that the user enterd a massage

            if algorithm == "Caeser Cipher":
                Caeser_Cipher_decrypt()
                
            elif algorithm == "Morse Code Cipher":
                Morse_code_decrypt()

            elif algorithm == "Baconian Cipher":
                Baconian_cipher_decrypt()

            elif algorithm == "ASCII Code Cipher":
                ASCII_decrypt()
        else:
           messagebox.showwarning("Warning",("Please enter a massage"))
    except IndexError:
        messagebox.showwarning("Warning",("Please choose an algorithem for decryption "))
#----------------------------------------------------------------------------------------------------
def clicked_reset():
    """to clear message entry and listbox"""
    #refrence is (https://www.codegrepper.com/code-examples/python/how+to+reset+entry+in+tkinter)

    e1.delete(0, END)
    list1.selection_clear(list1.curselection())
#----------------------------------------------------------------------------------------------------
def save_file():
    #refrense is :(https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python)

    message= e1.get()
    file_path = filedialog.asksaveasfilename() #make the user choose the location and file name
    f= open(file_path+".txt","w+")
    
    new_messege=pyperclip.paste() # to paste the clipboard to the file
    f.write(("Your Message is: "+message+"\nYour New Message is: "+new_messege))
    f.close()

    #refresne is (https://stackoverflow.com/questions/15054434/how-can-i-open-files-in-external-programs-in-python)
    fileName = file_path+".txt"
    os.system("notepad.exe " + fileName) #to automaticly open the file 
#----------------------------------------------------------------------------------------------------
#GUI 
root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("841x598")
root.configure(bg = "#131D34")
root.resizable(width=False,height=False) #to make the root window as the same size and can not be bigger

#adding the left background
frame1 = Frame(
    root,
    bg = "#192542",
    height = 598,
    width = 370,
    highlightthickness = 0,
    relief = "ridge")
frame1.place(x = 0, y = 0)

#adding center background
frame2 = Frame(
    root,
    bg = "#192542",
    height =500,
    width =385,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
frame2.place(x = 415, y = 63)

#adding img 
img = PhotoImage(file = f"C:\\Users\\Raghed Alrefi\\Desktop\\HI\\logo.png")
panel = Label(
    root, 
    bg = "#192542", 
    image = img)
panel.place(x =50, y = 90)

#adding labels
l1=Label(
    root,
    fg = "#7E53D6",
	bg = "#192542",
    text="CRYPTOGRAPHY",
    font = ("Montserrat", 25, 'bold'))
l1.place(x = 45, y = 346)

l2=Label(root,
    fg = "#70D8FA",
	bg = "#192542",
    text="Welcome to cryptograpgy, the best  \nprogram to hide your masseges.",
    font = ("Montserrat",11),padx=10, pady=5,justify = 'left')
l2.place(x = 38, y = 392)

l3=Label( root,
    fg = "#70D8FA",
	bg = "#192542",
    text="Enter the Massage",
    font = ("Montserrat",13,'bold'))
l3.place(x=442,y=103)

l4=Label(root,
    fg = "#70D8FA",
	bg = "#192542",
    text="Choose Encryption Algorithms",
    font = ("Montserrat",13,'bold'))
l4.place(x=442,y=236)
 

#adding entries
e1 = Entry(
    root,
    bd = 0,
    bg = "#202F52",
    font = ("Montserrat",9,),
    fg = "white")
e1.place(x = 445, y = 133, width = 324, height = 84)

e2 = Entry(
    bd = 0,
    bg = "#202F52",
    font = ("Montserrat",9,),
    fg = "white")
e2.place(x = 445, y =266, width = 324, height = 35)

#adding listbox
list1=Listbox(
    root,
    height=4,
    bd = 0,
    bg = "#202F52",
    font = ("Montserrat",11),
    fg = "white",
    highlightthickness = 0,
    selectbackground="#7E53D6")

list1.insert(2,"ASCII Code Cipher")
list1.insert(3,"Baconian Cipher")
list1.insert(0,"Caeser Cipher")
list1.insert(1,"Morse Code Cipher")
list1.place(x = 445, y =266, width = 324, height =85)


#adding buttons
b1 = Button(
    root,
    bg = "#70D8FA",
    bd = 0,
    command = clicked_encrypt,text="Encrypt",
    font = ("Montserrat",12,'bold'),
    fg = "#1A243E",
    relief = "flat")
b1.place(x =446.13, y = 370, width = 147.26, height = 44.96)

b2 = Button(
    root,
    bg = "#7E53D6",
    bd = 0,
    command = clicked_decrypt,
    text="Decrypt",
    font = ("Montserrat",12,'bold'),
    fg = "white",
    relief = "flat")
b2.place(x =621.61, y = 370, width = 147.26, height = 44.96)

b3 = Button(
    root,
    bg = "#202F52",
    bd = 0,
    command = clicked_reset,
    text="Reset",
    font = ("Montserrat",12, 'bold'),
    fg = "white",
    relief = "flat")
b3.place(x =532.81, y = 430, width = 147.26, height = 44.96)

b3 = Button(
    root,
    bg = "#202F52",
    bd = 0,
    command = save_file,
    text="Save in a file",
    font = ("Montserrat",12, 'bold'),
    fg = "white",
    relief = "flat")
b3.place(x =532.81, y = 490, width = 147.26, height = 44.96)

root.mainloop()
