# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

from sample_madlibs import zombie, hungergames
import random

if __name__ == "__main__":
    play_madlib = random.choice([zombie, hungergames])
    play_madlib.madlib()