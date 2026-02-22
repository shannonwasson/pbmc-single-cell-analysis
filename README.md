# Single-Cell RNA-seq Analysis of Human PBMC Dataset

## Overview
This project performs a standard single-cell RNA-seq analysis pipeline on a publicly available human peripheral blood mononuclear cell (PBMC) dataset using Scanpy. The goal is to identify immune cell subpopulations based on gene expression profiles.

## Dataset
* Source: 10x Genomics 3k PBMC dataset accessed via Scanpy built-in dataset `sc.datasets.pbmc3k()`
* Data type: Single-cell RNA sequencing
* Number of cells: Approximately 2,700
* Number of genes: After filtering and quality control, approximately 1,800

Each row in this dataset represents an individual immune cell and each column represents the gene. 
Values represent RNA counts. 

## Methods
1. Quality Control Filtering
    * Removed low quality cells or low expression genes. 
    * Marked mitochondrial genes (indication of stressed or dying cells) and calculated a mitochondrial percentage. A higher mitochondrial percentage is an indicator of a bad quality cell. 
2. Normalization and Log Transformation
3. Feature Selection
    * Indication of highly variable genes.
4. Dimensionality Reduction
    * Principal Component Analysis (PCA)
    * UMAP visualization
5. Graph-based Clustering Using Leiden Clustering
6. Marker Gene Identification
    * Differential expression Bctween clusters

## Results
* UMAP visualization revealed distinct cellular clusters.
* Marker gene analysis identifies cluster-specific genes.
* Clusters likely to correspond to immune cell subtypes, meaning groupings of T cells, B cells, and monocytes.

