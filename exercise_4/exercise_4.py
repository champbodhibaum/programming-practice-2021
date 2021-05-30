def exercise_4(inputs): # DO NOT CHANGE THIS LINE
    """
    from __future__ import division
    import numpy as np
    import matplotlib.pyplot as plt
    import random

    #optimization method

    def evaluation_salomon(variables):
        variables=np.array(variables)
        return (1.0 - np.cos(2.0*np.pi*np.sqrt(sum(variables**2.0))) + 0.1*np.sqrt(sum(variables**2.0)))

    def evaluation_sphere(variables): 
        return np.sum(np.square(variables))

    def evaluation_rosenbrock(variables):
        f=0
        variable_num=len(variables)
        for i in range(variable_num-1):
            f+=100*np.power(variables[i+1]-np.power(variables[i],2),2)+np.power(variables[i]-1,2)
        return f

    #--------------------------DE------------------------------------

    def mutation(pop,number_of_individuals,F):
        index1=np.random.randint(number_of_individuals)
        index2=np.random.randint(number_of_individuals)
        index3=np.random.randint(number_of_individuals)
        mut_vector=(pop[index1]-pop[index2]*F + pop[index3])
        return mut_vector

    def crossover(father,mut_vector,number_of_variables):
        child=[father[i] if np.random.rand() < 0.8 else mut_vector[i] for i in range(number_of_variables)]
        return child

    class DE:

        def __init__(self,number_of_variables,number_of_individuals,F,bounds,evaluation):
            self.number_of_variables = number_of_variables
            self.number_of_individuals = number_of_individuals
            self.bounds = bounds
            self.pop=np.random.uniform(low=self.bounds[0],high=self.bounds[1], size=(number_of_individuals,number_of_variables))
            self.F=F
            self.evaluation = evaluation
            self.generations = 1000
            # print(self.pop)

            #mut_vector=mutation(self.pop,number_of_individuals,F)
            #print(mut_vector)

        def optimize1(self):
            graph1=[]
            fig = plt.figure(figsize=(8,8))

            if self.number_of_variables == 2:
                ax = fig.add_subplot(111)
                ax.set_xlim(-4,4)
                ax.set_ylim(-4,4)
                ax.set_xlabel("variable 1")
                ax.set_ylabel("variable 2")
            elif self.number_of_variables == 3:
                ax = fig.add_subplot(111, projection='3d')
                ax.set_xlim(-4,4)
                ax.set_ylim(-4,4)
                ax.set_zlim(-4,4)
                ax.set_xlabel("variable 1")
                ax.set_ylabel("variable 2")
                ax.set_zlabel("variable 3")


            for gen in range(self.generations):
                pop_eval=[]
                x=[]
                y=[]
                z=[]
                for index,individual in enumerate(self.pop):

                    mut_vector=mutation(self.pop,self.number_of_individuals,self.F)

                    child=crossover(individual,mut_vector,self.number_of_variables)

                    if self.evaluation(child)<self.evaluation(individual):
                        self.pop[index]=child

                    pop_eval.append(self.evaluation(self.pop[index]))
                    if self.number_of_variables == 2:
                        x.append(self.pop[index][0])
                        y.append(self.pop[index][1])
                    elif self.number_of_variables == 3:
                        x.append(self.pop[index][0])
                        y.append(self.pop[index][1])
                        z.append(self.pop[index][2])


                avg_evaluation=np.mean(pop_eval)
                graph1.append(avg_evaluation)
                print(avg_evaluation)
                if self.number_of_variables == 2:
                    p = ax.scatter(x,y)
                    plt.draw()
                    plt.pause(0.0000001)
                    p.remove()
                elif self.number_of_variables == 3:
                    p = ax.scatter(x,y,z)
                    plt.draw()
                    plt.pause(0.0000001)
                    p.remove()

                # plt.plot(graph1)
                # plt.draw()
                # plt.pause(0.0001)
                # plt.clf()
            y=graph1[-1]
            return y

    #-------------------------------PSO-----------------------------------

    generations = 1000
    constant1 = 0.75
    constant2 = 1
    constant3 = 2
    initial_fitness = float("inf")

    class Particle:
        def __init__(self, number_of_variables, number_of_particles, bounds, evaluation):
            self.particle_position = []
            self.particle_velocity = []
            self.local_best_particle_position = []
            self.fitness_local_best_particle_position = initial_fitness
            self.fitness_particle_position = initial_fitness
            self.number_of_variables = number_of_variables
            self.number_of_particles = number_of_particles
            self.bounds = bounds
            self.evaluation = evaluation

            for i in range(number_of_variables):
                self.particle_position.append(
                    random.uniform(bounds[i][0], bounds[i][1])
                    )
                self.particle_velocity.append(random.uniform(-1, 1))

        def evaluate(self, objective_function):
            self.fitness_particle_position = objective_function(self.particle_position)
            if self.fitness_particle_position < self.fitness_local_best_particle_position:
                self.local_best_particle_position = self.particle_position
                self.fitness_local_best_particle_position = self.fitness_particle_position
            return self.fitness_local_best_particle_position

        def update_velocity(self, global_best_particle_position):
            for i in range(self.number_of_variables):
                r1 = random.random()
                r2 = random.random()

                cognitive_velocity = constant2 * r1 * (self.local_best_particle_position[i] - self.particle_position[i])
                social_velocity = constant3 * r2 * (global_best_particle_position[i] - self.particle_position[i])
                self.particle_velocity[i] = constant1 * self.particle_velocity[i] + cognitive_velocity + social_velocity

        def update_position(self):
            for i in range (self.number_of_variables):
                self.particle_position[i] = self.particle_position[i] + self.particle_velocity[i]

        def optimize2(self):
            fig = plt.figure(figsize=(8,8))
            if self.number_of_variables == 2:
                ax = fig.add_subplot(111)
                ax.set_xlim(-4,4)
                ax.set_ylim(-4,4)
                ax.set_xlabel("variable 1")
                ax.set_ylabel("variable 2")
            if self.number_of_variables == 3:
                ax = fig.add_subplot(111, projection="3d")
                ax.set_xlim(-4,4)
                ax.set_ylim(-4,4)
                ax.set_zlim(-4,4)
                ax.set_xlabel("variable 1")
                ax.set_ylabel("variable 2")
                ax.set_zlabel("variable 3")

            fitness_global_best_particle_position = initial_fitness
            global_best_particle_position = []
            swarm_particle = []
            for i in range(self.number_of_particles):
                swarm_particle.append(Particle(self.number_of_variables,self.number_of_particles,self.bounds,self.evaluation))

            graph2=[]

            for i in range(generations):
                x=[]
                y=[]
                z=[]
                pop_eval = []
                for j in range(self.number_of_particles):
                    pop_eval.append(swarm_particle[j].evaluate(self.evaluation))

                    if swarm_particle[j].fitness_particle_position < fitness_global_best_particle_position:
                        global_best_particle_position = list(swarm_particle[j].particle_position)
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)

                for j in range(self.number_of_particles):
                    swarm_particle[j].update_velocity(global_best_particle_position)
                    swarm_particle[j].update_position()
                    if self.number_of_variables == 2:
                        x.append(swarm_particle[j].particle_position[0])
                        y.append(swarm_particle[j].particle_position[1])
                    if self.number_of_variables == 3:
                        x.append(swarm_particle[j].particle_position[0])
                        y.append(swarm_particle[j].particle_position[1])
                        z.append(swarm_particle[j].particle_position[2])

                avg_eval=np.mean(pop_eval)
                graph2.append(avg_eval)
                print(avg_eval)
                if self.number_of_variables == 2:
                    p = ax.scatter(x,y)
                    plt.draw()
                    plt.pause(0.0001)
                    p.remove()
                if self.number_of_variables == 3:
                    p = ax.scatter(x,y,z)
                    plt.draw()
                    plt.pause(0.0001)
                    p.remove()

                # plt.plot(graph2)
                # plt.draw()
                # plt.pause(0.0001)
                # plt.clf()

            x=graph2[-1]
            return x
    """
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
