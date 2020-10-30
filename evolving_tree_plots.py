import matplotlib.pyplot as plt

arr_time = [.167, .367, .5, 0.7, 1.05, 1.383, 2.217, 2.617]
arr_nodes = [100, 200, 300, 400, 500, 600, 700, 800]

'''
fig = plt.figure()
ax = plt.axes()

plt.plot(arr_time)
plt.show()
'''

fig, ax = plt.subplots()
#ax.plot(arr_nodes, arr_time)
ax.plot(arr_nodes, arr_time, "ro")
ax.set(xlabel='Number of nodes', ylabel='Time (minutes)',
       #title='Epoch = 400')
       title='Topics graphs')
fig.savefig("Topics_time.png")
plt.show()

