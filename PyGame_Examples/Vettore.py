import math

class Vector2(object):

	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __str__(self):
		return "( %s %s )" % (self.x, self.y)
		
	# Crea un nuovo oggetto Vector2 utilizzando un metodo di classe invece di modificarne uno esistente
	@classmethod
	def from_points(cls, P1, P2):
		return cls( P2[0] - P1[0], P2[1] - P1[1])
		
	def get_magnitude(self):
		return math.sqrt(self.x**2 + self.y**2)
		
	def normalize(self):
		magnitude = self.get_magnitude()
		self.x /= magnitude
		self.y /= magnitude
	
	# rhs = Right Hand Size
	def __add__(self, rhs):	
		return Vector2 (self.x + rhs.x, self.y + rhs.y)
		
	def __sub__(self, rhs):
		return Vector2 (self.x - rhs.x, self.y - rhs.y)
		
	def __neg__(self):
		return Vector2(-self.x, -self.y)
	
	def __mul__(self, scalar):
		return Vector2(self.x * scalar, self.y * scalar)
		
	def __div__(self, scalar):
		return Vector2(self.x / scalar, self.y / scalar)


'''		
A = (10.0, 20.0)
B = (30.0, 35.0)
C = (15.0, 45.0)
AB = Vector2.from_points(A,B)
BC = Vector2.from_points(B,C)
print "Vettore AB ", AB
print "Vettore BC", BC 
print "Grandezza Vettore AB ", AB.get_magnitude()
AB.normalize()
print "Vettore AB Normalizzato ", AB
AB = Vector2.from_points(A,B)

AC = Vector2.from_points(A,C)
print "Vettore AC = ", AC

AC = AB + BC
print "AB + BC = ", AC

AC = AB - BC
print "AB - BC = ", AC


# spostamento ogni 1 secondo se AB viene percorso in 10 secondi
AB= Vector2.from_points(A,B)

step = AB * .1
position = Vector2(A[0],A[1])
for n in range(10):
	position += step
	print position
'''