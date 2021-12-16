# Methodological Foundation of a Numerical Taxonomy of Urban Form
Code repository for the **Methodological Foundation of a Numerical Taxonomy of Urban
Form** paper.

> Fleischmann M, Feliciotti A, Romice O and Porta S (2021) Methodological Foundation of
> a Numerical Taxonomy of Urban Form. Environment and Planning B: Urban Analytics and
> City Science, doi: [10.1177/23998083211059835](https://doi.org/10.1177/23998083211059835)

Martin Fleischmann<sup>1, 2</sup>, Alessandra Feliciotti<sup>2</sup>, Ombretta
Romice<sup>2</sup>, Sergio Porta<sup>2</sup>

1 Department of Geography and Planning, University of Liverpool

2 Urban Design Studies Unit, Department of Architecture, University of Strathclyde

Contact: martin@martinfleischmann.net

Date: 28/10/2021

[![maps](leaflet_maps.png)](https://martinfleis.github.io/numerical-taxonomy-maps/)

The online interactive maps of the final classification are available at [https://martinfleis.github.io/numerical-taxonomy-maps/](https://martinfleis.github.io/numerical-taxonomy-maps/).

## Code

The code is split into two folders - `code_method` containing cleaned reproducible
Python code for everyone willing to use the method, and `code_production` containing an
archive of the used (and somewhat messy) code.

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

Alternatively, you can use the Docker container `darribas/gds_py:7.0`.

### The code
The folder `code_production` is an archive of the actual production code used to
generate the analysis presented in the paper. However, it is recommended to use the code
in the `code_method` folder if you want to reproduce the work. The code in the folder is
stored for archival purposes and different parts may depend on different versions of
dependecies.

## Data

Non-proprietary data are archived on figshare as
[10.6084/m9.figshare.16897102](https://doi.org/10.6084/m9.figshare.16897102). The
archive contains input geometry, generated geometry, all measured morphometric
characters and a final classification labels for Prague and Amsterdam. It does not
contain validation data, which are available upon request (due to the licensing).

The online interactive maps of the final classification are available at [https://martinfleis.github.io/numerical-taxonomy-maps/](https://martinfleis.github.io/numerical-taxonomy-maps/).

## Preprint

Preprint of the final manuscript is available from [arXiv](https://arxiv.org/abs/2104.14956).

## Abstract

Cities are complex products of human culture, characterised by a startling diversity of
visible traits. Their form is constantly evolving, reflecting changing human needs and
local contingencies, manifested in space by many urban patterns. Urban Morphology laid
the foundation for understanding many such patterns, largely relying on qualitative
research methods to extract distinct spatial identities of urban areas. However, the
manual, labour-intensive and subjective nature of such approaches represents an
impediment to the development of a scalable, replicable and data-driven urban form
characterisation.  Recently, advances in Geographic Data Science and the availability of
digital mapping products, open the opportunity to overcome such limitations. And yet,
our current capacity to systematically capture the heterogeneity of spatial patterns
remains limited in terms of spatial parameters included in the analysis and hardly
scalable due to the highly labour-intensive nature of the task. In this paper, we
present a method for numerical taxonomy of urban form derived from biological
systematics, which allows the rigorous detection and classification of urban types.
Initially, we produce a rich numerical characterisation of urban space from minimal data
input, minimizing limitations due to inconsistent data quality and availability. These
are street network, building footprint, and morphological tessellation, a spatial unit
derivative of Voronoi tessellation, obtained from building footprints. Hence, we derive
homogeneous urban tissue types and, by determining overall morphological similarity
between them, generate a hierarchical classification of urban form. After framing and
presenting the method, we test it on two cities - Prague and Amsterdam - and discuss
potential applications and further developments. The proposed classification method
represents a step towards the development of an extensive, scalable numerical taxonomy
of urban form and opens the way to more rigorous comparative morphological studies and
explorations into the relationship between urban space and phenomena as diverse as
environmental performance, health and place attractiveness.
