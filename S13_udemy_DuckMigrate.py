from S12_udemy_DuckChallenge import Duck as D
from S12_udemy_DuckChallenge import Flock as F
from S12_udemy_DuckChallenge import Penguin as P
from S12_udemy_DuckChallenge import Mallard as M
#from S12_udemy_DuckChallenge import Migrate as M

flock = F()
donald = D()
duck1 = D()
duck2 = D()
duck3 = D()
duck4 = D()
duck5 = D()
duck6 = D()
duck7 = D()
percy = P() #Penguin
mark = M() #Mallard


flock.add_duck(donald)
flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(mark) #MARK WILL FAIL ALTHOUGH IT EXTENDS DUCK SINCE ONLY CHECKING FOR DUCK CLASS
flock.add_duck(percy) #PENGUIN CANT FLY - ADDED ANNOTATION TO WARN YOU
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
