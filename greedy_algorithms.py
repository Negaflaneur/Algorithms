## set covering problem

states_required = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
stations = {}
stations['kone'] = set(["id", "uv", "ut", "ca", "az"])
stations['ktwo'] = set(["wa", "id", "mt"])
stations['kthree'] = set(["or", "nv", "ca"])
stations['kfour'] = set(["nv", "ut"])
stations['kfive'] = set(["ca", "az"])
final_stations = []

while states_required:
    best_station = None
    states_currently_covered = set()
    for station, states_covered_by_station in stations.items():
        covered = states_covered_by_station & states_required
        if len(covered) > len(states_currently_covered):
            best_station = station
            states_currently_covered = states_covered_by_station
    states_required -= states_currently_covered
    final_stations.append(best_station)
print(final_stations)