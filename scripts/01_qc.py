import scanpy as sc
import matplotlib.pyplot as plt

# Loading the Data from Scanpy
data_a = sc.datasets.pbmc3k()

print(data_a.shape)

# Annotating Mitochondrial Genes
data_a.var['mt'] = data_a.var_names.str.startswith('MT-')

# Calculating QC Metrics
sc.pp.calculate_qc_metrics(
    data_a,
    qc_vars=['mt'],
    percent_top=None,
    log1p=False,
    inplace=True
)
# Visualize the QC Metrics
sc.pl.violin(data_a, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
                jitter=0.4, multi_panel=True,
                show=False)
plt.savefig('../figures/qc_violin_plots.png')
