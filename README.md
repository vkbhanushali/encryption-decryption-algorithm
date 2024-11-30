# encryption-decryption-algorithm
Concept of substitution cipher-
Any character from the predetermined fixed set of characters is replaced by another character from the same set according to a key in a substitution cypher. As an illustration, if there was a shift of 1, A would be replaced by B, B by C, and so on.


Concept of transposition cipher-
Transposition Cipher is a cryptographic procedure in which the plaintext's alphabetical order is changed to create a cypher text. The real plain text alphabets are not utilized in this procedure.


Own encryption algo with example-
Four 5 by 5 matrices are used in the encryption, squarely aligned. The letter "j" is often combined with the letter i in each of the 25-letter 5 by 5 matrices; according to Wikipedia, the letter "q" is removed but is not very significant because both q and j are relatively uncommon characters. The "plaintext squares," which are typically the upper-left and lower-right matrices, each have an alphabet in them. The "ciphertext squares" in the upper- right and lower-left corners contain a mixed alphabetic sequence. A keyword may be used to produce the ciphertext squares (dropping duplicate letters), and the remaining spaces can then be filled with the remaining letters of the alphabet in the correct sequence. As an alternative, the ciphertext squares can be produced at random. Two distinct keys, one for each of the two ciphertext matrices, are supported by the four-square method.
 
Example:
Plaintext: attackatdawn

The text 'attack at dawn', with the keys 'zgptfoihmuwdrcnykeqaxvsbl' and 'mfnbdcrhsaxyogvituewlqzkp', becomes: TIYBFHTIZBSY
We write it out in a special way on a number of rails (the key here is 3)

 

The ciphertext is read off along the rows: TFZIBHIBYYTS

Own decryption algo with example- Ciphertext: TFZIBHIBYYTS
We write it out in a special way on a number of rails (the key here is 3)

 

Text = TIYBFHTIZBSY
With the keys 'zgptfoihmuwdrcnykeqaxvsbl' and 'mfnbdcrhsaxyogvituewlqzkp',
 
 

We get the plaintext as = ATTACKATDAWN
