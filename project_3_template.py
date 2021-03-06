"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane

Note!!
Uncomment line 20 and comment out line 19 and 18 to test by OwlTest 
"""

import math
import classClaster as alg_cluster
import clasters_input_for_tests as cl
#import alg_cluster



######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """

    cluster_list_length = len(cluster_list)
    closest_pair = (float('inf'), -1, -1)
    for point_1 in xrange(cluster_list_length):
        for point_2 in xrange(cluster_list_length):
            if point_1 != point_2:
                
                temp_closest_pair = pair_distance(cluster_list, point_1, point_2)
                
                if temp_closest_pair[0] < closest_pair[0]:
                    closest_pair = temp_closest_pair
    return closest_pair


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """

    closest_pair = (float('inf'), -1, -1)
    cluster_list_length = len(cluster_list)
    
    if cluster_list_length <= 3:
        closest_pair = slow_closest_pair(cluster_list)

    else:
        half_cluster_list_length = (cluster_list_length / 2)
        left_closest_pair = fast_closest_pair(cluster_list[:half_cluster_list_length])
        right_closest_pair = fast_closest_pair(cluster_list[half_cluster_list_length:])

        if left_closest_pair[0] < right_closest_pair[0]:
            closest_pair = left_closest_pair
        else:
            closest_pair = (right_closest_pair[0],
                            right_closest_pair[1] + half_cluster_list_length,
                            right_closest_pair[2] + half_cluster_list_length)
            
        middle_horizontal_line = (cluster_list[half_cluster_list_length -1].horiz_center() + cluster_list[half_cluster_list_length].horiz_center()) / 2
        line_closest_pair = closest_pair_strip(cluster_list, middle_horizontal_line, closest_pair[0])

        if line_closest_pair[0] < closest_pair[0]:
            closest_pair = line_closest_pair
        
    return closest_pair


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """

    strip_cluster_list = []

    # add clusters which lie in max: half_width distance to the left from the horiz_center to the 'strip_cluster_list'
    for cluster in xrange((len(cluster_list) / 2 -1), -1, -1):                  
        if cluster_list[cluster].horiz_center() >= (horiz_center - half_width):
            strip_cluster_list.append(cluster_list[cluster])
        else:
            break
    # add clusters which lie in max: half_width distance to the right from the horiz_center to the 'strip_cluster_list'
    for cluster in xrange((len(cluster_list) / 2), len(cluster_list)):
        if cluster_list[cluster].horiz_center() <= (horiz_center + half_width):
            strip_cluster_list.append(cluster_list[cluster])
        else:
            break
        
    strip_cluster_list.sort(key = lambda cluster: cluster.vert_center())
    length_cluster_list = len(strip_cluster_list)
    closest_pair = (float('inf'), -1, -1)

    for point_1 in xrange(length_cluster_list -1):
        for point_2 in xrange((point_1 +1), min((point_1 +4), (length_cluster_list))):

            temp_closest_pair = pair_distance(strip_cluster_list, point_1, point_2)
            if temp_closest_pair[0] < closest_pair[0]:
                closest_pair = temp_closest_pair

    if closest_pair[0] != float('inf'):
        point_1_indx = cluster_list.index(strip_cluster_list[closest_pair[1]])
        point_2_indx = cluster_list.index(strip_cluster_list[closest_pair[2]])
        closest_pair = (closest_pair[0], min(point_1_indx, point_2_indx), max(point_1_indx, point_2_indx))
    
    return closest_pair
            
 
    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    while len(cluster_list) > num_clusters:
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
        closest_clusters = fast_closest_pair(cluster_list)
        cluster_1 = cluster_list[closest_clusters[1]]
        cluster_2 = cluster_list[closest_clusters[2]]
        cluster_1.merge_clusters(cluster_2)
        cluster_list.remove(cluster_2)        
    
    return cluster_list

######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
    """
    if len(cluster_list) <= num_clusters:
        return cluster_list
    
    clusters_centers = []
    for cluster in cluster_list:
        if len(clusters_centres) < num_clusters:
            clusters_centres.append(cluster.copy())
        else:
            clusters_centres.sort(key = lambda cluster: cluster.total_population())
            if cluster.total_population() > clusters_centres[0].total_population():
                clusters_centres.remove(clusters_centres[0])
                clusters_centres.append(cluster.copy())
                
    for dummy_i in xrange(num_iterations):
        clusters = [alg_cluster.Cluster(set([]), cluster.horiz_center(), cluster.vert_center(), 0, 0) for cluster in clusters_centres]

        for cluster_2 in cluster_list:
            smallest_dist_cluster = alg_cluster.Cluster(set([]), float('inf'), float('inf'), 0, 0)
            for cluster_1 in clusters:
                distance = cluster_1.distance(cluster_2)
                
        

    
    return clusters_centers
    """

    if len(cluster_list) <= num_clusters:
        return cluster_list

    kmeans_cluster_list = list(cluster_list)
    kmeans_cluster_list.sort(key = lambda cluster: cluster.total_population())

    clusters_centers = []
    for cluster in range(num_clusters):
        clusters_centers.append(kmeans_cluster_list[cluster].horiz_center(), kmeans_cluster_list[cluster].vert_center())
    print('kmeans')
    print kmeans_cluster_list
    print clusters_centers

    






    
        
    
    
    







    


