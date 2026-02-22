import scanpy as sc
data_a = sc.datasets.pbmc3k()

# Filter between cells and genes
sc.pp.filter_cells(data_a, min_genes=200) # Removing cells with fewer than 200 genes
sc.pp.filter_genes(data_a, min_cells=3) # Removing genes that are are expressed in less than 3 cells


# Normalize the data
sc.pp.normalize_total(data_a)
sc.pp.log1p(data_a) # Log transform to stabilize variance across genes

# Identify highly variable genes
sc.pp.highly_variable_genes(data_a)

# PCA
sc.tl.pca(data_a)

# Compute the neighborhood graph
sc.pp.neighbors(data_a)

# UMAP
sc.tl.umap(data_a)

sc.pl.umap(data_a, show=False, save="_pbmc3k.png")