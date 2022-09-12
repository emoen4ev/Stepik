import random as rng
vocab = {1: 'Jack', 2: 'Bill', 3: 'Piter', 4: 'Vasya'}
keys = list(vocab.keys())
rng.shuffle(keys)
print([(key, vocab[key]) for key in keys])