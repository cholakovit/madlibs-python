from sample_madlibs import code, hp, hungergames, zombie
import random

if __name__ == "__main__":
    m = random.choice([zombie, code, hp, hungergames])
    m.madlib()
