import numpy as np

def read_instance(path, instance):
    with open(path+instance, "r") as file:
        instance_info = file.read().splitlines()
        n_jobs = int(instance_info[0])
        n_machines = int(instance_info[1])
        sm = list(map(int, instance_info[2].strip().split("\t")))
        S_m = [sm for _ in range(n_machines)]
        count = 3 + n_machines
        alpha_sm = []
        for linea in instance_info[3:count]:
            elementos = linea.strip().split("\t")
            fila = list(map(int, elementos))
            alpha_sm.append(fila)

        p = []
        for linea in instance_info[count:count+n_jobs+1]:
            elementos = linea.strip().split("\t")
            fila = list(map(int, elementos))
            p.append(fila)
        p = np.array(p)

        count = count + n_jobs + 1
        me = np.zeros((n_jobs + 1, n_machines), dtype=int)
        for i, linea in enumerate(instance_info[count:]):
            elementos = linea.strip().split("\t")
            fila = list(map(int, elementos))
            for m, elemento in enumerate(fila):
                me[i, m] = elemento

    return n_jobs, n_machines, S_m, alpha_sm, p, me


# Example read instance
n_jobs = 10
n_machines = 3
shift_length = 10
eligibility_method = "sparse"
job_duration = (1,10)
seed = 0
path = "" # Path where you want to store solution

jobs, machines, shifts_m, alpha_sm, durations, machine_eligibility = read_instance(path, f"j{n_jobs}_m{n_machines}_a{shift_length}_{eligibility_method[0]}_p{job_duration[0]}p{job_duration[1]}_{seed}.txt")