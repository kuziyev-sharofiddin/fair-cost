configs = [12]


def getUserConfig(userId):
    return next(config for config in configs if config["user"] == userId)


x = [1, 2, 3, 4, 5, 6]
x[2] = 5
