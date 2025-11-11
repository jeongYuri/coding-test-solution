def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0]*bridge_length
    onbridge = sum(bridge)
    while bridge:
        time+=1
        onbridge-=bridge.pop(0)
        if truck_weights:
            if onbridge+truck_weights[0]<=weight:
                new_truck = truck_weights.pop(0)
                bridge.append(new_truck)
                onbridge += new_truck
            else:
                bridge.append(0)
    return time