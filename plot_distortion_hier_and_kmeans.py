import singleton_lists as sl
import data_tables as dt
import project_3
import cluster_distortion as cd
import matplotlib.pyplot as plt

#data = sl.singleton_list_111
#data = sl.singleton_list_290
#data = sl.singleton_list_896
data = sl.singleton_list_3108

#data_table = dt.data_111
#data_table = dt.data_290
#data_table = dt.data_896
data_table = dt.data_3108

cluster_sizes = []
hier_errors = []
kmeans_errors = []
for num_clusters in xrange(6, 21):

    hier_clusters = project_3.hierarchical_clustering(data, num_clusters)
    kmeans_clusters = project_3.kmeans_clustering(data, num_clusters, 5)

    hier_error = cd.compute_distortion(hier_clusters, data_table)
    kmeans_error = cd.compute_distortion(kmeans_clusters, data_table)

    cluster_sizes.append(num_clusters)
    hier_errors.append(hier_error)
    kmeans_errors.append(kmeans_error)


plot_title = 'distortion of the clusters produced by hierarchical and k-means clustering on ' + str(len(data)) + ' county data set'

plt.plot(cluster_sizes, hier_errors, 'g', label='hierarchical clustering', linewidth=3.0)
plt.plot(cluster_sizes, kmeans_errors, 'b', label='kmeans clustering', linewidth=3.0)

plt.xlabel('number of output clusters')
plt.ylabel('distortion x 10^11')
plt.title(plot_title)
plt.legend(loc='upper right')
plt.grid(True)

plt.show()



