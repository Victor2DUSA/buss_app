import psycopg2


#Connect to database 
conn = psycopg2.connect(
    host = "localhost",
    dbname = "Newbuss_time_table",
    user = "postgres",
    password = "123451"
)

#define the search criteria 
location = input("enter your location: ")
bus_stop_name = ""
start_time = ""
end_time = ""

query = " SELECT departure_time, stop_name FROM timetable WHERE route_name = 'Murdoch Valley to Cape Town' AND stop_name = 'Retreat' AND departure_time BETWEEN '09:00' AND '12:00'"

cursor = conn.cursor()
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    departure_time = row[0]
    stop_name = row[1]
    print(f"Departure time: {departure_time}, Stop name: {stop_name}")

# Close the cursor and database connection
cursor.close()
conn.close()