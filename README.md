# UPM-instances
It contains instances for the Unrelated Parallel Machine scheduling problem with machine eligibility and availability. Additionally, this repository has the Python code for creating instances ([create_instances.py](https://github.com/auribev1/UPM-instances/blob/main/create_instances.py)) and for extracting the information ([read_instance.py](https://github.com/auribev1/UPM-instances/blob/main/read_instance.py)).

# Instances information
Each instance is organized as follows:

The name of the file contains the parameters settings and takes the form of j(#1)_m(#2)_a(#3)_(e)_p(#4)p(#5)_(#6).txt

After j, #1 is the number of jobs. 

After m, #2 is the number of machines.

After a, #3 is the shift length.

e is the eligibility method (s for sparse, d for dense).

After p, #4 is the lower bound, and #5 is the upper bound for the activity duration.

#6 is the seed or instance to read.

For example, j10_m3_a10_d_p1p10_0.txt. has 10 jobs, and 3 machines, each shift length of 10 time intervals, the eligibility matrix is dense, the activities length between 1 and 10 time intervals, and the instance 0.

# Instances structure
Each instance has the following structure:

![image](https://github.com/user-attachments/assets/6869866b-a4a5-4be4-91fe-343cf7f737c9)

The first line corresponds to the number of jobs j.

The second line is the number of machines m.

The third line has the time interval where each working shift ends (column). For this particular case, there are 8 shifts.

The next m lines have the length of each shift (column) for each machine (row). Most of the time (as in the example) the length is equal for all machines during all shifts. Nevertheless, some machines have shorter shifts due to randomly generated maintenance periods.

The next j+1 (considering a dummy job) lines correspond to a randomly generated duration for each activity (row) in each machine (column).

Finally, the next j+1 lines (considering a dummy job) contain the eligibility matrix where each column represents if the machine m (column) is capable of processing job j (row) taking a value of 1 and 0 otherwise.


