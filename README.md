# Baltimore_City_Employees_Salaries
Visualize Baltimore City Employees Salaries Dataset

## Enviromment 
Conda is used to set up my environment. Packages are installed from `conda-forge`. Starting in my base environment,  I  did the following to setup my environment, which I called `data_viz`:   

`conda config --add channels conda-forge`  
`conda config --set channel_priority strict`  
`conda create --name data_viz python=3.8 numpy pandas matplotlib jupyterlab`  
`conda activate data_viz`  
`conda env export -f environment.yml`  

The last command created a yaml file with the specific package versions and package dependencies. 

## Getting the Data
Go to the [Baltimore City Employees Salaries](https://data.baltimorecity.gov/City-Government/Baltimore-City-Employees-Salaries/w28m-utix) webpage. In the upper right of the page, there is an export button. Download as a `csv` file (not `csv for excel`). Place the file downloaded file, `Baltimore_City_Employees_Salaries.csv`, in the data directory.