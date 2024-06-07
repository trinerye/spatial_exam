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

Some of the data files used, we are not allowed to directly distribute, however they are freely available for you to download and import manually. When downloaded, place inside the `/in/` folder.

1. **States_shapefile-shp**
Can be downloaded from: https://hub.arcgis.com/datasets/1b02c87f62d24508970dc1a6df80c98e/explore?location=37.249090%2C-97.282458%2C5.18
After downloading, place entire States_shapefile-shp folder inside `/in/` folder.

2. **most-humid-states-2024.csv**
This `.csv` file can be downloaded freely from World Population Review at: https://worldpopulationreview.com/state-rankings/most-humid-states
After downloading, place the `most-humid-states-2024.csv` file inside `/in/` folder.

3. **united-states-by-density-2024.csv**
This `.csv` file can also be downloaded freely from World Population Review at: https://worldpopulationreview.com/state-rankings/state-densities
After downloading, place the `united-states-by-density-2024.csv` file inside `/in/` folder.

4. **datacenters_usa_clean.csv**
<u>For examiners</u>, there is an invite only download link in the metadata table of the paper, whihic will direct you to datascience.dk.

5. **<u>For non examiners only</u>**
If you are not an examiner, you an use the provided `dummy_coordinates.csv` in the `/in/` folder. You can either rename this file to `datacenters_usa_clean.csv`, or change the notbooks to use `dummy_coordinates.csv` instead. This is a fake dataset made to emulate the official data set.

When done, your `/in/` folder should look like this:

```
spatial_exam/
    └── in/
        ├── States_shapefile-shp/
        │   ├── States_shapefile.cpg
        │   ├── States_shapefile.dbf
        │   ├── States_shapefile.prj
        │   ├── States_shapefile.shp
        │   └── States_shapefile.shx
        ├── avgprice_annual.xlsx
        ├── datacenters_usa_clean.csv
        ├── dummy_coordinates.csv
        ├── green_states.csv
        ├── most-humid-states-2024.csv
        ├── state_temp.csv
        ├── united-states-by-density-2024.csv
        └── .gitkeep
```

### 4. Running the notebooks
When running the notebooks, there is a certain order you need to run them. The order in which we recommend is:
1. local_setup.ipynb
2. maps.ipynb
3. kde plot.ipynb
4. ripley g.ipynb
5. mean_power.ipynb

We have also included the notebook we used for geocoding, although you do not have to run this one, as the datacenter file you you downloaded already has the geocoded locations added. It is simply included to show *how* we used the geocoder.

We have also included the script we used to generate the dummy data set. This script is also not required for you to run, since you won't have to use the dummy data.
