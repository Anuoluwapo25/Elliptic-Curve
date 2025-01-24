from random import randint

# Define the elliptic curve
class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a  # Coefficient of x
        self.b = b  # Constant term
        self.p = p  # Prime modulus
    
    def is_point_on_curve(self, x, y):
        """Check if a point (x, y) lies on the curve."""
        return (y**2 - (x**3 + self.a * x + self.b)) % self.p == 0

    def mod_inverse(self, value, p):
        """Compute modular inverse of value mod p."""
        return pow(value, -1, p)

    def point_addition(self, P, Q):
        """Add two points P and Q on the elliptic curve."""
        if P == (None, None):  
            return Q
        if Q == (None, None):  
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 == -y2 % self.p: 
            return (None, None)

        if P == Q:  
            m = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p) % self.p
        else:  
            m = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p

        x3 = (m**2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)


# Curve parameters (secp256k1 example)
a = 0
b = 7
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)


curve = EllipticCurve(a, b, p)


private_key = randint(1, p - 1)
print("Private Key:", private_key)


public_key = curve.scalar_multiplication(private_key, G)
print("Public Key:", public_key)
