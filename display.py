import matplotlib.pyplot as plt
import objects

def draw(system):
    plt.rcParams['figure.figsize']=[7.5,3.5]
    plt.rcParams['figure.autolayout']=True

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    
    for body in system.bodies:
        ax.scatter(*body.position, c='red', s=body.size[0])

    plt.show()

