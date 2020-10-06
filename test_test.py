from datetime import datetime

start_with = datetime.now()

sum(range(10000000))

end_with = datetime.now() - start_with
print(end_with)