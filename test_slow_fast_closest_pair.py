import random_clusters as rc
import project_3 as p3
import time

clusters_sizes = [rc.gen_random_clusters(size) for size in xrange(2, 201)]

def time_trial_slow(cluster_list):
    cluster_size = len(cluster_list)
    start = time.clock()
    p3.slow_closest_pair(cluster_list)
    stop = time.clock()
    elapsed = (stop - start)
    return elapsed

def time_trial_fast(cluster_list):
    cluster_size = len(cluster_list)
    start = time.clock()
    p3.fast_closest_pair(cluster_list)
    stop = time.clock()
    elapsed = (stop - start)
    return elapsed

