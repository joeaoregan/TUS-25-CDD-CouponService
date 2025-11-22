# Question 3 [TOTAL MARKS: 20]
# The Westermo network traffic dataset contains labeled network traffic data for analyzing and detecting 
# various types of network intrusions and malicious activities.  The file net_data.csv is a comma
# separated values file containing a subset of the data set over a 10 minute period.  The following is an 
# extract:

# Minute    Protocol    Duration    sPackets    rPackets    Type
# 0         ARP         0.000003    3           0           Normal
# 0         LLDP        0.000001    1           0           Normal
# 0         IPV4-TCP    0.47865     40          30          Normal
# 0         IPV4-TCP    0.499777    16          22          Normal
# 0         IPV4-TCP    0.499604    10          20          Normal
# 0         IPV4-2      0.002299    4           0           Normal

# Each line of the file is associated with a specific network event.  The column headings are explained in 
# Figure 3.2 overleaf.

# Write a Python program to visualise the data, as follows.  You may assume that matplotlib.pyplot 
# has been imported as plt.  You may not import anything else.


# Q 3(a) [3 Marks]

# (i)
# Open the file for reading; use exception handling to deal with the situation where the file 
# cannot be found.

# (ii)
#  Create the following data structures:
#  •A dictionary to store the number of network events per minute.
#  •Lists to store the values of the Duration, sPackets and rPackets columns.
#  •Dictionaries to store the frequencies of the values in the Protocol and Type columns.
#  Figure 3.3 overleaf provides a table showing sample data for the data structures.

filename = "net_data.csv"

# 3(a)(ii)
duration_list = []
event_type_dict = {} # event type frequency
events_dict = {}     # number of network events per minute.
protocol_dict = {}   # protocol frequency
rPackets_list = []
sPackets_list = []


try:
    with open(filename) as data_file: # 3(a)(i)
        # print("Open")
        _ = data_file.readline() # 3(b)
        for line in data_file:
            try:
                minute, protocol, duration, spackets, rpackets, type = line.strip().split(",")

                event_type_dict[type] = event_type_dict.get(type, 0) + 1
                events_dict[int(minute)] = events_dict.get(int(minute), 0) + 1
                protocol_dict[protocol] = protocol_dict.get(protocol, 0) + 1

                duration_list.append(float(duration))
                rPackets_list.append(float(rpackets))
                sPackets_list.append(float(spackets))


            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
except FileNotFoundError:
    print(f"File not found: {filename}")

# print(duration_list)
# print(event_type_dict)
print(events_dict)
# print(protocol_dict)
# print(rPackets_list)
# print(sPackets_list)

# Q3(c)
import matplotlib.pyplot as plt

fig,axs = plt.subplots(2,3, figsize=(15,12))
# fig.set_size_inches(15,12) # width, height

fig.suptitle("Network Data") # Q3(c)(ii)

axs[0,0].set_title("Events")
axs[0,0].plot(events_dict.keys(),events_dict.values())
axs[0,0].set_xlabel("Minute")
axs[0,0].set_ylabel("Number of events")
bins_list = [ i for i in events_dict.keys() ]
axs[0,0].set_xticks(bins_list)

axs[0,1].set_title("Event Duration")
axs[0,1].set_xlabel("Time in Seconds")
axs[0,1].set_ylabel("Frequency")
axs[0,1].hist(duration_list,bins=6,ec="black")

axs[0,2].set_title("Event Type")
axs[0,2].pie(event_type_dict.values(),labels=event_type_dict.keys(), autopct="%.0f%%")


axs[1,0].set(title="Protocols", xlabel="Protocol",ylabel="Frequency")
axs[1,0].bar(protocol_dict.keys(), protocol_dict.values())

axs[1,1].set_title("Packets: Box Plots")
axs[1,1].set_ylabel("Number of Packets")
axs[1,1].boxplot([sPackets_list, rPackets_list], 
                 showmeans=True,
                 meanline=True, 
                 labels=["Sent","Received"]) # pass in the list of labels

axs[1,2].set(title="Packets: Scatter Plot", xlabel="Sent", ylabel="Received")
axs[1,2].scatter(sPackets_list, rPackets_list, marker=".")

plt.show()

fig.savefig("q3.png",bbox_inches='tight')