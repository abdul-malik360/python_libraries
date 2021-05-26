from datetime import date, timedelta
dt = date.today()

for x in range(0, 10):
    dt = dt + timedelta(weeks=2)
    print("Date two weeks from last: ", dt)
