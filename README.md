# Methodological Foundation of a Numerical Taxonomy of Urban Form
Code repository for the preprint of **Methodological Foundation of a Numerical Taxonomy
of Urban Form**.

Contact: martin@martinfleischmann.net

Date: 30/04/2021

The final description of the contents of this repository will be released alongside the
publication of the final paper (currently under review).

### The method
The folder `code_method` contains generalised code for the method, that should be
reproducible on a custom data. The main notebook `morphometric_assessment.ipynb` has
been updated to work with the recent releases of software. You can create the
reproducible environment to run it using `conda` or `mamba` and the `environment.yaml`
file in the `code_method` folder.

```
conda env create -f environment.yaml
```

You can also create a new environment `taxonomy` manually:

```
conda create -n taxonomy
conda activate taxonomy
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install momepy mapclassify seaborn
```

### The code
The folder `code_production` is an archive of the actual production code used to
generate the analysis presented in the paper.

The reproducible computational environment can be created using Docker container
`darribas/gds_py:5.0`.