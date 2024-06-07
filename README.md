# Spatial exam: Anayzying Data Centers

## Setup:

### 1. Changing the Kernel in Jupyter Notebook

1. Open your Spatial_Exam in VS Code.

2. Go into the notebook (ends with .ipynb)

3. If you do not have IPyKernel installed it will prompt you to do so please click `Accept`

4. In the top right choose your `kernel`

    - It will prompt you to choose between python and jupyter
    - Choose `Python`
    - Then `Python 3.12`

<br>
<br>

### 2. Installing the packages

Open local_setup.ipynb

Run the first cell:

```python
!pip install pandas geopandas polars numpy matplotlib ipympl openpyxl pyxlsb xlsx2csv opencage shapely tqdm ipywidgets contextily pointpats
```

There are also optional code-blocks at the top of every notebook, which you can run to install just the required libraries for that specific notebook.

The packages will be installed locally
<br><br><br><br>

### 3. Getting the data:

In the paper, there should be link to download the `datacenters_usa_clean.csv` file from sciencedata.dk. When downladed, put the `.csv` file into the `/in/` folder of this directory.

**EXPLAIN REST OF DATA FILES HERE**

### 4. Running the notebooks
When running the notebooks, there is a certain order you need to run them. The order in which we recommend is:
1. local_setup.ipynb
2. maps.ipynb
3. kde plot.ipynb
4. ripley g.ipynb
5. mean_power.ipynb

We have also included the notebook we used for geocoding, although you do not have to run this one, as the datacenter file you you downloaded already has the geocoded locations added. It is simply included to show *how* we used the geocoder.

We have also included the script we used to generate the dummy data set. This script is also not required for you to run, since you won't have to use the dummy data.
