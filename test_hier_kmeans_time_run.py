import singleton_lists as sl
import project_3 as p3
import time

cluster_1 = sl.singleton_list_111
cluster_2 = sl.singleton_list_290
cluster_3 = sl.singleton_list_896
cluster_4 = sl.singleton_list_3108

def time_trial_hierarchical(cluster_list):
    start = time.clock()
    p3.hierarchical_clustering(cluster_list, 6)
    stop = time.clock()
    elapsed = (stop - start)
    return elapsed

def time_trial_kmeans(cluster_list):
    start = time.clock()
    p3.kmeans_clustering(cluster_list, 6, 3)
    stop = time.clock()
    elapsed = (stop - start)
    return elapsed

def run_trial(cluster):
    hier_time = time_trial_hierarchical(cluster)
    kmeans_time = time_trial_kmeans(cluster)
    print('hierarchical time: ' + str(hier_time))
    print('kmeans time: ' + str(kmeans_time))

print("111 county data:")
run_trial(cluster_1)
print
print("290 county data:")
run_trial(cluster_2)
print

print("896 county data:")
run_trial(cluster_3)
print
print("3108 county data:")
run_trial(cluster_4)
print
