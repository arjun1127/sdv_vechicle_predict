import traci
import pandas as pd
import time

# Connect to SUMO
sumoCmd = ["sumo", "-c", "config.sumocfg", "--start"]
traci.start(sumoCmd)

# Create an empty list to store traffic data
traffic_data = []

# Simulation loop
step = 0
while step < 1000:  # Run for 1000 simulation steps
    traci.simulationStep()
    vehicles = traci.vehicle.getIDList()

    for vehicle_id in vehicles:
        speed = traci.vehicle.getSpeed(vehicle_id)
        lane = traci.vehicle.getLaneID(vehicle_id)
        edge = traci.vehicle.getRoadID(vehicle_id)
        position = traci.vehicle.getPosition(vehicle_id)

        traffic_data.append([step, vehicle_id, speed, lane, edge, position[0], position[1]])

    step += 1
    time.sleep(0.01)  # Slow down simulation for real-time effect

# Close TraCI connection
traci.close()

# Save collected data to CSV
df = pd.DataFrame(traffic_data, columns=["TimeStep", "VehicleID", "Speed", "LaneID", "EdgeID", "X", "Y"])
df.to_csv("traffic_data.csv", index=False)
print("Traffic data saved to traffic_data.csv")
