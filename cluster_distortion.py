import classClaster as alg_cluster
import project_3
import singleton_lists as sl
import data_tables as dt

def compute_distortion(cluster_list, data_table):


    cluster_error = 0
    for cluster in cluster_list:
        error = cluster.cluster_error(data_table)
        cluster_error += error
    return cluster_error

"""
#data_table = dt.data_111
data_table = dt.data_290
#data_table = dt.data_896
#data_table = dt.data_3108


#data = sl.singleton_list_111
data = sl.singleton_list_290
#data = sl.singleton_list_896
#data = sl.singleton_list_3108


hier_clusters = project_3.hierarchical_clustering(data, 16)
#hier_clusters = project_3.hierarchical_clustering(data, 9)

kmeans_clusters = project_3.kmeans_clustering(data, 16, 5)
#kmeans_clusters = project_3.kmeans_clustering(data, 9, 5)


hier_err = compute_distortion(hier_clusters, data_table)
kmeans_err = compute_distortion(kmeans_clusters, data_table)


print
print('Cluster error for hierarchal clustering with ' + str(len(hier_clusters)) + ' clusters on ' + str(len(data)) + ' county: '
      + str(hier_err))
print

print('Cluster error for kmeans clustering with ' + str(len(kmeans_clusters)) + ' clusters and 5 iterations on ' + str(len(data)) + ' county: '
      + str(kmeans_err))
print
"""
