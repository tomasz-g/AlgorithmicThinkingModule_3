"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""


import math
import random
import urllib2
import classClaster as alg_cluster
import data_tables as dt
import singleton_lists as sl
import project_3 as alg_project3_solution
import alg_clusters_matplotlib
import cluster_hier_cl as cl_hc
import cluster_kmeans_cl as cl_kmc

###################################################
# data tables

DATA_3108_URL = 'C:/Users/tom/Desktop/Coursea/Project_3_data/unifiedCancerData_3108.csv'
DATA_896_URL = 'C:/Users/tom/Desktop/Coursea/Project_3_data/unifiedCancerData_896.csv'
DATA_290_URL = 'C:/Users/tom/Desktop/Coursea/Project_3_data/unifiedCancerData_290.csv'
DATA_111_URL = 'C:/Users/tom/Desktop/Coursea/Project_3_data/unifiedCancerData_111.csv'
                

#####################################################################

def run_example():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters
    """
    
    data_table = dt.data_111
    #data_table = dt.data_290
    #data_table = dt.data_896
    #data_table = dt.data_3108

    singleton_list = sl.singleton_list_111
    #singleton_list = sl.singleton_list_290
    #singleton_list = sl.singleton_list_896
    #singleton_list = sl.singleton_list_3108
    
    #cluster_list = cl_hc.cl_hc_111_9
    #cluster_list = cl_hc.cl_hc_290_9
    #cluster_list = cl_hc.cl_hc_896_9
    #cluster_list = cl_hc.cl_hc_3108_9

    #cluster_list = cl_hc.cl_hc_3108_15
    
    #cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, 15)
    #print "Displaying", len(cluster_list), "hierarchical clusters"
    #print cluster_list

    #cluster_list = cl_kmc.cl_kmc_111_9_5
    #cluster_list = cl_kmc.cl_kmc_290_9_5
    #cluster_list = cl_kmc.cl_kmc_896_9_5
    #cluster_list = cl_kmc.cl_kmc_3108_9_5
    
    #cluster_list = cl_kmc.cl_kmc_3108_15_5
    
    cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, 9, 1)
    #print "Displaying", len(cluster_list), "k-means clusters"
    #print cluster_list

            
    # draw the clusters using matplotlib
    #alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  #add cluster centers
    
run_example()
