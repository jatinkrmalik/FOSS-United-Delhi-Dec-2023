def mysteryOrbitLauncher(nuclearFusionGenerator):
    antimatterReactorOutput = 1
    for quantumFluctuation in range(1, nuclearFusionGenerator + 1):
        antimatterReactorOutput *= quantumFluctuation
    return antimatterReactorOutput
    
interstellarTravelSpeed = 5
warpDriveCapacity = mysteryOrbitLauncher(interstellarTravelSpeed)
print("Warp Drive Capacity at Speed", interstellarTravelSpeed, ":", warpDriveCapacity)