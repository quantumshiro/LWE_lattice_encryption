import numpy as np

# parameters
n = 230
q = 2053
A = np.random.randint(q, size=(n, n))
alpha = 8.0

def randint_from_gaussian(size):
    sigma = alpha/np.sqrt(2*np.pi)
    x = np.random.normal(0, sigma, size)
    return np.rint(x)

print ('[+] parameters')
print ("lattice dimension: n = %d" % n)
print ("prime modulus: q = %d" % q)
print ('lattice basis: A = \n', A)
print ("error distribution parameter: alpha = %f" % alpha)
print (" ")

# keys
s = np.random.randint(q, size=n)
G = A.dot(s) % q
e = randint_from_gaussian(size=n)
T = (G + e) % q

print ('[+] secret key')
print ('s =\n', s)
print ('e =\n', e)
print ('[+] public key')
print ('T =\n', T)
print (" ")

# encryption
plain_bit = 1
print ("[+] plain_bit = %d" % plain_bit)
print (" ")

r = randint_from_gaussian(size=n)
C1 = r.dot(A) % q
M = (q+1)/2 * plain_bit
C2 = (r.dot(T) - M) % q

print ('[+] ciphertext')
print ('C1 =\n', C1)
print ('C2 =\n', C2)
print (" ")

# decryption
p = (C1.dot(s) - C2) % q
decrypted_bit = int((q+1)/4 < p < 3*(q+1)/4)
print ("[+] decrypted_bit = %d" % decrypted_bit)