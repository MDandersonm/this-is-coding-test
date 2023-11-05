def time_to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


def find_wait_time(current_time, bus_times):
    current_minutes = time_to_minutes(current_time)
    bus_minutes = [time_to_minutes(bus_time) for bus_time in bus_times]

    # 현재 시간 이후로 도착하는 버스만 필터링
    future_buses = [bus for bus in bus_minutes if bus >= current_minutes]

    # 만약 현재 시간 이후로 도착하는 버스가 있다면
    if future_buses:
        return min(future_buses) - current_minutes
    # 그렇지 않다면, 다음날 첫 버스를 기다려야 함
    else:
        return (24 * 60 - current_minutes) + min(bus_minutes)


if __name__ == "__main__":
    current_time = input().strip()
    bus_times = input().strip().split()
    print(find_wait_time(current_time, bus_times))
