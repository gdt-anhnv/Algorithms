import sys
import os
from glob import glob
import hashlib

def CountDuplicates(path) :
    print path
    hashes = {""}
    duplicated = 0
    for x in os.walk(path) :
        for y in x[2] :
            filename = os.path.join(x[0], y)
            with open(filename, "rb") as f :
                bytes = f.read()
                hash_value = hashlib.sha256(bytes).hexdigest()
                if hash_value in hashes :
                    duplicated += 1
                    print duplicated
                else :
                    hashes.add(hash_value)
                
CountDuplicates(sys.argv[1])