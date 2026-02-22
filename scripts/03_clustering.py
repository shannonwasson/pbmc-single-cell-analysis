import scanpy as sc



data_a = sc.datasets.pbmc3k()

# Setting up for Leiden Clustering
sc.pp.filter_cells(data_a, min_genes=200)
sc.pp.filter_genes(data_a, min_cells=3)
sc.pp.normalize_total(data_a)
sc.pp.log1p(data_a)
sc.tl.pca(data_a)
sc.pp.neighbors(data_a)
sc.tl.umap(data_a)

# Starting Clustering
sc.tl.leiden(data_a)
sc.pl.umap(data_a, color='leiden', show = False, save="_clusters.png")

sc.tl.rank_genes_groups(data_a, 'leiden', method='t-test')
sc.pl.rank_genes_groups(data_a, show = False, save="_marker_genes.png")

print(data_a.obs["leiden"].value_counts())