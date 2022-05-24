from .utils import Bot, Target
import os

def main():
	target_folder = './targets/'
	targets = [Target(target_folder+ref) for ref in os.listdir(target_folder)]
	miner = Bot()

	while True:
		for target in targets:
			hit = miner.find(target.image)
			if not hit:
				print("None found, still looking!")
				continue
			miner.mine(hit)