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
f1-vis can produce multiple visualizations at once. Input each as a separate row in the .csv or dataframe:

| segment | true positive | false positive | true negative | false negative | 
| ------------- | ------------- | ------------- | ------------- |
| all | 0.56 | 0.12 | 0.22 | 0.1 | 
| recent | 0.52 | 0.13 | 0.24 | 0.11 | 
| active | 0.59 | 0.1 | 0.23 | 0.08 | 

### Theme
Set the theme to either ```light``` (good for printing) or ```dark``` (nice for slides -- background is #3c3c3c).
