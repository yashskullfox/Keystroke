# Keystroke
README NOTES:

The project is in python 3.7. So, to run a program you will be need a python environment and also need to import packages pandas and Scipy. I have implemented this program in Python IDE development environment.
Please change the path of the input data in the program.
For N=200 there is a file name 200 where you can change the threshold value in Ôthr=' attribute and can get output for different threshold values. Same goes for N=100(100) and N=300(300).
All the output files are in the output folder and code file in the code folder.
You are required to implement Manhattan verifier and report false accept (impostor pass) and false reject rates on a publicly available keystroke biometric dataset. You may use any programming language, as long as it can be compiled.

Dataset: The data consist of keystroke-timing information from 51 subjects (typists), each typing a password (.tie5Roanl) 400 times. (http://www.cs.cmu.edu/~keystroke/)
Verification Task: For each user, (a) compute the template using mean key hold and key interval features calculated on the first N typing samples; (b) compute the genuine and impostor scores using Manhattan distance; and (c) calculate and report false accept (im- postor pass) and false reject rates at a given threshold T.
Program Input: (1) N is the number of samples to be used for building the template (e.g., if N = 200, use the first 200 samples of each user to compute the average vector and the remaining 200 for testing; if N = 100, use the first 100 samples for the template and the remaining 300 for testing); and (2) T is the verification threshold.
Program Output: Clearly display false accept (impostor pass) and false reject rates at a given threshold T.
