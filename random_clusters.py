import classClaster as alg_cluster
import random

def gen_random_clusters(num_clusters):
    
    random_cluster_list = []
    
    for dummy_i in xrange(num_clusters):
        
        x_cor = random.uniform(-1, 1)
        y_cor = random.uniform(-1, 1)
        
        new_cluster = alg_cluster.Cluster(set([]), x_cor, y_cor, 0, 0)
        
        random_cluster_list.append(new_cluster)
        
    return random_cluster_list
