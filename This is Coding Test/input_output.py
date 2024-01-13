import time
start_time = time.time()

for i in range(0,1000):
  print(i)

end_time = time.time()
print("time : ", end_time - start_time)