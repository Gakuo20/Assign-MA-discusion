import random
import datetime
def sensor_per_cluster():
    readings = []
    for i in range (16):
        readings.append(random.random())
    for i in range (1):
        del readings[3]
        readings.append('err')
    x = datetime.datetime.now()
    dated_readings = {}
    dated_readings[datetime.datetime.now().strftime('%y/%m/%d.%H:%M:%S')] = readings
    print(dated_readings)
    sensor_per_cluster()
def clusters_of_sensors():
    clusters = {}
    for i in range (32):
        clusters[i] = sensor_per_cluster()
        print(clusters)
clusters_of_sensors()





        

        
                
                
                
            

        










#sensor_per_cluster()
#def cluster_values():
    #cluster = {}
    #for j in range (32):
#import time
        #datetime.datetime.now()
        #cluster[datetime.datetime.now().strftime('%y/%m/%d.%H:%M:%S')] = readings
        #print(cluster)
#cluster_values()











