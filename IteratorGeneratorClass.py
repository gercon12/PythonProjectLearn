def remote_control_next():
    yield "cnn"
    yield "espn"
    yield "hbo"

itr = remote_control_next()

print(next(itr))
print(next(itr))

print("-------------------------------------------------")

for c in remote_control_next():
    print(c)
