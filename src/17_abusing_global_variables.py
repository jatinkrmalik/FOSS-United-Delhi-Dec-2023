global chaos, pandemonium, mayhem
chaos = 42
pandemonium = 0
mayhem = 7

def wreakHavoc():
    global chaos, pandemonium
    chaos += 1
    pandemonium -= chaos

def causeChaos():
    global chaos, mayhem
    mayhem *= chaos
    chaos = mayhem - pandemonium

def unleashPandemonium():
    global pandemonium, mayhem
    if pandemonium > 10:
        pandemonium = 10
    mayhem += pandemonium * 2

def totalMayhem():
    global chaos, pandemonium, mayhem
    return chaos + pandemonium + mayhem

# Example usage
wreakHavoc()
causeChaos()
unleashPandemonium()
print("Total Mayhem:", totalMayhem())
