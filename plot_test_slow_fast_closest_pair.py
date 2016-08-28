import test_slow_fast_closest_pair as cp
import matplotlib.pyplot as plt

initial_clusters = [len(cp.clusters_sizes[cluster]) for cluster in xrange(len(cp.clusters_sizes))]  
slow_plot_time = [cp.time_trial_slow(cluster_list) for cluster_list in cp.clusters_sizes]
fast_plot_time = [cp.time_trial_fast(cluster_list) for cluster_list in cp.clusters_sizes]

plt.plot(initial_clusters, slow_plot_time, 'g', label='slow closest pair', linewidth=3.0)
plt.plot(initial_clusters, fast_plot_time, 'b', label='fast closest pair', linewidth=3.0)

plt.xlabel('number of initial clusters')
plt.ylabel('running time of function in seconds')
plt.title('slow and fast closest pair function comparision')
plt.legend(loc='upper left')
plt.grid(True)

plt.show()
