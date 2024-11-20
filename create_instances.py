import numpy as np

def instance_generator(n_jobs, n_machines, n_alpha, n_seeds, eligibility_methods, processing_times, path):
    for jobs in n_jobs:
        for machines in n_machines:
            for eligibility in eligibility_methods:
                for processing_time in processing_times:
                    for alpha in n_alpha:
                        for seed in range(n_seeds):
                            np.random.seed(seed)
                            p = np.random.randint(processing_time[0], processing_time[1]+1, size=(jobs + 1, machines))
                            p[0] = 0

                            BigM = np.ceil(sum([t.max() for t in p]))
                            alpha_sm = []
                            for m in range(machines):
                                S_m = []
                                a_sm = []
                                init_time = 0
                                while sum(a_sm) < BigM:
                                    S_m.append(init_time + alpha)
                                    a_sm.append(alpha)
                                    init_time += alpha
                                prob = np.random.random()
                                if prob <= 0.5:
                                    maintenance_time = np.random.randint(alpha)
                                    maintenance_shift = np.random.randint(len(a_sm))
                                    a_sm[maintenance_shift] = maintenance_time
                                alpha_sm.append(a_sm)

                            # Machine eligibility
                            if eligibility == "sparse": prob = 0.3
                            else: prob = 0.7

                            me = np.random.binomial(1, prob, size=(jobs + 1, machines))

                            me[0] = 1
                            filename = f"j{jobs}_m{machines}_a{alpha}_{eligibility[0]}_p{processing_time[0]}p{processing_time[1]}_{seed}.txt"
                            text = open(f"{path}{filename}", "w")
                            text.write(f"{jobs}\n")
                            text.write(f"{machines}\n")

                            for element in S_m:
                                text.write(f"{element} \t")
                            text.write("\n")

                            for row in alpha_sm:
                                for element in row:
                                    text.write(f"{element} \t")
                                text.write("\n")

                            for row in p:
                                for element in row:
                                    text.write(f"{element} \t")
                                text.write("\n")

                            for i in range(len(p)):
                                if sum(me[i,:]) == 0:
                                    me[i, np.random.randint(len(me[i,:]))] = 1
                                for m in range(machines):
                                    text.write(f"{me[i, m]} \t")
                                text.write("\n")

                            text.close()


# Example generation instances for different jobs, machines, shift lengths, eligibility setups and processing times
n_jobs = [10, 25, 50]
n_machines = [3, 6]
shift_length = [10, 20] # shift length
eligibility_methods = ["sparse", "dense"]
activities_length = [(1,10), (5, 10)]  # tuples with lower and upper bound for activities duration
n_seeds = 3 # Number of seeds or instances per configuration
path = "" # Path were you want to store ir

instance_generator(n_jobs, n_machines, shift_length, n_seeds, eligibility_methods, activities_length, path)