import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import fcluster
import seaborn as sns
import matplotlib.pyplot as plt
from flet.plotly_chart import PlotlyChart
import matplotlib
#from  simpledt import CSVDataTable
from flet.matplotlib_chart import MatplotlibChart

def load_data(path):
    
    dataSet=pd.read_csv(f"myUploads/{path}")
    dataSet
    missing_values = dataSet.isnull().any()
    missing_values
    for column in dataSet.columns:
        if missing_values[column]:
            mean_value = dataSet[column].mean()
            dataSet[column].fillna(mean_value, inplace=True)
    missing_values
    male = dataSet['GENDER'] == 'M'
    female = dataSet['GENDER'] == 'F'
    dataSet.loc[male, 'GENDER'] = 1
    dataSet.loc[female, 'GENDER'] = 0
    #methode 2
    #dataSet['GENDER'] = dataSet['GENDER'].map({'M':1,'F':0})
    dataSet
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(dataSet)
    dataSet_normalized = pd.DataFrame(scaled_data, columns=dataSet.columns)
    dataSet_normalized

    plt.subplots_adjust(hspace=0.8, wspace=0.8)
    matrice_correlation = dataSet_normalized .corr()
    matriceFig, ax1 = plt.subplots(figsize=(8, 6))
    sns.heatmap(matrice_correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matrice de corrélation")
    acp_norme=PCA()
    principal_components=acp_norme.fit_transform(dataSet_normalized)
    nbComposantes = acp_norme.n_components_
    print(nbComposantes)
    dfX=pd.DataFrame(principal_components,columns=dataSet_normalized.columns)
    dfX
    lamdas=acp_norme.explained_variance_
    print(lamdas)
    print(lamdas.sum())
    screeFig  = plt.figure(figsize=(8, 6))
    plt.plot(np.arange(1, len(lamdas) + 1), lamdas, marker='o', linestyle='-')
    plt.title("Scree Plot")
    plt.xlabel("Nombre de composantes")
    plt.ylabel("Valeurs propres")
    plt.grid(True)
    
    
    GraphFig = plt.figure(figsize=(8, 6))
    plt.plot(np.arange(1, len(lamdas) + 1), np.cumsum(acp_norme.explained_variance_ratio_), marker='o', linestyle='-')
    plt.bar(np.arange(1, len(lamdas) + 1), np.cumsum(acp_norme.explained_variance_ratio_))
    plt.title("Graphique des Variances Cumulées Expliquées")
    plt.xlabel("Nombre de Composantes Principales")
    plt.ylabel("Variance Cumulative Expliquée")
    plt.grid(True)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(principal_components)
    cluster_labels_kmeans = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # Visualize K-means Clustering
    KmeanFig=plt.figure(figsize=(10, 5))
    plt.scatter(principal_components[:, 0], principal_components[:, 1], c=cluster_labels_kmeans, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=300, c='r', label='Centroids')
    plt.title('K-means Clustering')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    Z = linkage(principal_components, method='ward')
    cluster_labels_hierarchical = fcluster(Z, 2, criterion='maxclust')  # Assigning cluster labels

    # Hierarchical Clustering (CAH)
    CAHFig=plt.figure(figsize=(10, 5))
    dendrogram(Z)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Sample Index')
    plt.ylabel('Distance')

    # Compare the results of K-means and Hierarchical Clustering
    # You can compare based on silhouette scores, cluster centroids, or visual inspection of clusters.

    # Silhouette Score for Hierarchical Clustering
    silhouette_avg_hierarchical = silhouette_score(principal_components, cluster_labels_hierarchical)
    print("Silhouette Score for Hierarchical Clustering:", silhouette_avg_hierarchical)
    print(silhouette_score(principal_components, cluster_labels_kmeans))
    print(cluster_labels_kmeans)
    # 20. Calculer la matrice de corrélation des anciennes et des nouvelles variables du plan factoriel
    loading_matrix = acp_norme.components_.T * np.sqrt(val_propres)
    print("Matrice de corrélation des anciennes et des nouvelles variables :\n", loading_matrix)

    # 21. Analyser la saturation des variables en projetant les variables sur le cercle de corrélation
    circleFig=plt.figure(figsize=(10,10))
    plt.Circle((0,0), 1, color='blue', fill=False)
    for i in range(len(loading_matrix)):
        x, y = loading_matrix[i, 0], loading_matrix[i, 1]
        plt.plot([0, x], [0, y], linestyle='-', marker='o', label=dataSet.columns[i])
        plt.text(x, y, dataSet.columns[i])
    plt.xlabel('Composante principale 1')
    plt.ylabel('Composante principale 2')
    plt.title('Cercle de corrélation')
    plt.grid()
    plt.axis('equal')
    plt.legend(loc='upper center',bbox_to_anchor=(0.2, -0.02), ncol=3)
    csv=CSVDataTable(f"myUploads/{path}")
    table=csv.datatable
    eboliFig=plt.figure(figsize=(10,10))
    plt.bar(np.arange(0,15), lamdas,color='teal')
    plt.plot(np.arange(0, 15), lamdas,color='red')
    plt.scatter(dfX.values[15,0], dfX.values[15,1],s=50)

    #dataSet_normalized.to_csv('file2.csv')
    L=[matriceFig,screeFig,GraphFig,KmeanFig,CAHFig,circleFig,eboliFig,table]
    return L
        
        

