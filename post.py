import os
import argparse

print('0x0.st Uploader\nCoded by ToxidWorm')
print('Usage: python post.py --h')

parser = argparse.ArgumentParser(description='0x0.st Uploader')
parser.add_argument("--F", type=str, help="File to upload")
args = parser.parse_args()

os.system(f'curl -F file=@{args.F} https://0x0.st')