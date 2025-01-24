from random import randint

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a  # Coefficient a
        self.b = b  # Coefficient b
        self.p = p  # Prime modulus

    def point_addition(self, P, Q):
        """Add two points P and Q on the elliptic curve."""
        if P == (None, None):  # P is the point at infinity
            return Q
        if Q == (None, None):  # Q is the point at infinity
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 == -y2 % self.p:  # P + (-P) = O
            return (None, None)

        if P == Q:  # Point doubling
            m = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p) % self.p
        else:  # Regular addition
            m = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p

        x3 = (m**2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_multiplication(self, k, P):
        """Multiply a point P by a scalar k."""
        R = (None, None)  # Point at infinity
        Q = P

        while k:
            if k & 1:  # Add Q to R if the least significant bit of k is 1
                R = self.point_addition(R, Q)
            Q = self.point_addition(Q, Q)  # Double the point Q
            k >>= 1  # Shift k to the right by 1 bit
        return R

a = 2
b = 3
p = 97
curve = EllipticCurve(a, b, p)

# Define generator point
G = (3, 6)

# Define private key
private_key = 76495842643314008545346424279562195354941958683362425580595127034263011573530

# Calculate public key
public_key = curve.scalar_multiplication(private_key, G)
print("Public Key:", public_key)