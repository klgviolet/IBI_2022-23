class Triathlon:
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = str(
            int(swim_time.strip("min")) + int(cycle_time.strip("min")) + int(run_time.strip("min"))) + "min"

    def details(self):
        print(f"Name: {self.first_name} {self.last_name}, Location: {self.location}, "
              f"Swim time: {self.swim_time}, Cycle time: {self.cycle_time}, "
              f"Run time: {self.run_time}, Total time: {self.total_time}")


# Example for test
record1 = Triathlon("Peter", "Lee", "China", "60min", "30min", "90min")
record2 = Triathlon("John", "Sam", "US", "55min", "25min", "89min")
record1.details()
record2.details()
