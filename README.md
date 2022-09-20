# f1-vis
Visualize F1 in a non-stats and non-tech friendly way. Useful for model cards reviewed by business partners and executive leadership.

## Requirements
Requires the plotnine library.
```
pip install plotnine
```

## Instructions
Update the f1vis function with a dataframe and theme name.

```
f1vis(df=input_data,theme_name='dark')
```

### Dataframe Structure
f1-vis can produce multiple visualizations at once by inputting each as a separate row in the .csv or dataframe. Example below and included as ```sample-confusion-matrix.csv```:

| segment | true positive | false positive | true negative | false negative | 
| ------- | ------------- | -------------- | ------------- | -------------- |
| all | 0.56 | 0.12 | 0.22 | 0.1 | 
| recent | 0.52 | 0.13 | 0.24 | 0.11 | 
| active | 0.59 | 0.1 | 0.23 | 0.08 | 

### Theme
Set the theme to either ```light``` (good for printing) or ```dark``` (nice for slides -- background is #3c3c3c).

## Example Outputs
### Light Theme
![f1vis-light](https://user-images.githubusercontent.com/83668288/191360647-7883d328-5e51-434b-8a80-ccdf941ca568.png)

### Dark Theme
![f1vis-dark](https://user-images.githubusercontent.com/83668288/191360678-ca40b319-d7ee-4e7c-aee7-3f33ef965e8f.png)
