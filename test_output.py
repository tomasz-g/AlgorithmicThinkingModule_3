import classClaster as alg_cluster
import clasters_input_for_tests as cl
import project_3 as pr
"""
print('List 1')
for cluster in cl.input_1:
    print(str(cl.input_1.index(cluster)) + ': ' + str(cluster))
print
print('List 1 - slow - output')
print(pr.slow_closest_pair(cl.input_1))
print
print('List 1 - fast - output')
print(pr.fast_closest_pair(cl.input_1))
print
print('List 1 - hierarchical - output with two clusters')
print(pr.hierarchical_clustering(cl.input_1, 2))
print
print('List 1 - kmeans - output with two clusters and zero iterations')
print(pr.kmeans_clustering(cl.input_1, 2, 0))
print

print('List 2')
for cluster in cl.input_2:
    print(str(cl.input_2.index(cluster)) + ': ' + str(cluster))
print
print('List 2 - slow - output')
print(pr.slow_closest_pair(cl.input_2))
print
print('List 2 - fast - output')
print(pr.fast_closest_pair(cl.input_2))
print
print('List 2 - hierarchical - output with two clusters')
print(pr.hierarchical_clustering(cl.input_2, 2))
print
print('List 2 - kmeans - output with two clusters and zero iterations')
print(pr.kmeans_clustering(cl.input_2, 2, 0))
print

print('List 3')
for cluster in cl.input_3:
    print(str(cl.input_3.index(cluster)) + ': ' + str(cluster))
print
print('List 3 - slow - output')
print(pr.slow_closest_pair(cl.input_3))
print
print('List 3 - fast - output')
print(pr.fast_closest_pair(cl.input_3))
print
print('List 3 - hierarchical - output with four clusters')
print(pr.hierarchical_clustering(cl.input_3, 4))"""
print
print('List 3 - kmeans - output with four clusters and zero iterations')
print(pr.kmeans_clustering(cl.input_3, 4, 5))
print
"""
#sorted_list = list(cl.input_3)
#sorted_list.sort(key = lambda cluster: cluster.total_population())
#print('List 3 sorted by population')
#print(sorted_list[:4])
#print

print
print('Example of mege method')
print('claster with index 0 and 1 before merge:')
print('Cluser 0: ' + str(cl.input_3[0]))
print('Cluser 1: ' + str(cl.input_3[1]))
print

cl.input_3[0].merge_clusters(cl.input_3[1])
print('claster with index 0 and 1 after merge:')
print('Cluser 0: ' + str(cl.input_3[0]))
print('Cluser 1: ' + str(cl.input_3[1]))
print
"""
