import statistics
data = [10,20,20,40,50,70,80,90]
mean = statistics.mean(data)
median = statistics.median(data) 
mode = statistics.mode(data)
variance = statistics.variance(data)
std_dev = statistics.stdev(data)
print(f"mean:{mean}")
print(f"median:{median}")
print(f"mode:{mode}")
print(f"variance:{variance}")
print(f"standard deviation:{std_dev}")
