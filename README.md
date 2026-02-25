# Workshops

Workshop material and other support material for the workshops

* Tutorial notebooks that demo the approaches and reuse the code in other repositories
* Notes and scripts for configuring [WebODM](github.com/OpenDroneMap/WebODM) / OpenDroneMap for use in a tutorial


# MAMBO WP4 - workshops

This repository holds workshop material that covers machine learning methods for analysing drone images in complement with other data sources.

> [!WARNING]
> These are early drafts based on previously existing material. The "live" versions currently in Google Colab have a lot of improvements. Please contact the maintainers or check back in November 2025.

## Contents 

Current contents:

* Preparing data for training - [try on Colab](https://colab.research.google.com/drive/1Jw6aOe1ulKMfaSIUqwGEbnCwyzUSM9lv?usp=sharing)
* Training a model and assessing its quality [try on Colab](https://colab.research.google.com/drive/1FZEvjp5--BEk2Gmr29rnyDK5VmPgQslM?usp=sharing)
* Using the model to make predictions about where shrubs are [try on Colab](https://colab.research.google.com/drive/1PEJNda63960oLgcxx07EPQIpweB3bYmI?usp=sharing)

We supply data for use during the workshops, but aim for participants to be able to reproduce the results on their own data. All the functions defined in notebooks are also available in installable python packages, for use in pipelines.


## Additions

Planned additions:

* Walkthrough of a simpler, Random Forest based approach to estimating shrub heights given geometries extracted with a deep learning model
