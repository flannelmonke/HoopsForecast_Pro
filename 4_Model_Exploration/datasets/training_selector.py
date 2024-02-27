import shutil
import os, random

# Set the seed for reproducibility
for i in range(4):
    shutil.copy("./finalized_scripts/datasets/game_data/" + random.choice(os.listdir("./finalized_scripts/datasets/game_data/")), "./4_Model_Exploration/datasets/training_data/")
