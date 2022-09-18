import pandas as pd
from plotnine import *
from plotnine.data import *

def f1vis(df,theme_name):
    # Create legend dataframe
    labels, pred_labels, x, y = ['positive','negative','positive','negative'],['true','false','false','true'],[24,24,25,25],[7,6,7,6]
    label_dict = {'label':labels,'pred_label':pred_labels,'x':x,'y':y,'circle_size':10,'dot_size':0}
    legend_df = pd.DataFrame(label_dict)
    legend_df.loc[legend_df['pred_label'] == 'false','dot_size'] = 1
    
    for s in range(0,len(df)):
        ## PROCESS INPUTS ##
        # Get the number for each element in the confusion matrix
        confusion_matrix_df = input_data.loc[s:s,:]

        # Get the number for each element in the confusion matrix
        segment = confusion_matrix_df.loc[s,'segment']
        tp = confusion_matrix_df.loc[s,'true positive']
        fp = confusion_matrix_df.loc[s,'false positive']
        tn = confusion_matrix_df.loc[s,'true negative']
        fn = confusion_matrix_df.loc[s,'false negative']
        confusion_matrix_list = [tn,fn,fp,tp] 

        # Calculate precision, recall and F1
        precision = round(tp/(tp+fn),2)
        recall = round(tp/(tp+fp),2)
        f1 = round((2*precision*recall)/(precision+recall),2)
        metrics_dict = {'precision':precision,'recall':recall,'f1':f1}

        ## CREATE VISUAL DATA ##
        #Create a dataframe indicating how many dots should be plotted for each group
        labels, pred_labels, dot_cnt = ['negative','negative','positive','positive'],['true','false','false','true'],[n * 100 for n in confusion_matrix_list]
        vis_dict = {'label':labels,'pred_label':pred_labels,'dot_cnt':dot_cnt}
        vis_df = pd.DataFrame(vis_dict)

        # Repeat rows based on value from confusion matrix
        vis_df = vis_df.loc[vis_df.index.repeat(vis_df.dot_cnt)].reset_index(drop=True)
        vis_df = vis_df.reset_index()

        # Get x/y coordinates for plotting true/false based on index number
        vis_df['x'] = vis_df['index'] // 10 + 1
        vis_df['y'] = vis_df['index'] % 10
        vis_df[['circle_size','dot_size']] = 10, 0

        # Get x/y coordinates for plotting negatives based on index number
        df_neg = vis_df.loc[(vis_df['pred_label'] == 'false')].copy()
        df_neg[['dot_size']] = 1

        # Combine all dataframes
        vis_df = vis_df.append(df_neg).append(legend_df)

        # Plot function
        print(plot_data(theme_name,vis_df,segment,metrics_dict))
        
def plot_data(theme_name,data,segment_name,metrics_dict):
    ## DEFINITIONS ##
    precision_definition = 'PRECISION\nWhat percentage of\nall the “yes” predictions are correct?'
    recall_definition = 'RECALL\nWhat percentage of all\nthe real “yes”es were correctly predicted?'
    f1_definition = 'F1\nHow good is the model\nat finding all of the real “yes”es?'
    
    # Set the theme
    theme_name = theme_name #Options: light, dark
    padding = 1.5

    if theme_name == 'light':
        theme_set(theme_void())
        background = 'white'
        colors = {'negative':'#e06666', 'positive':'#93c47d', 'true':'#FFFFFF00', 'false':'white', 'plot':'white'}
        font_color = '#3C3C3C'
    elif theme_name == 'dark':
        theme_set(theme_void()) 
        background = '#3C3C3C'
        colors = {'negative':'#EA9999', 'positive':'#b6d7a8ff', 'true':'#FFFFFF00', 'false':'#3C3C3C', 'plot':'#3C3C3C'}
        font_color = '#FFFFFF'

    # Define the plot
    p = (ggplot(aes(x='x', y='y'), data)
        # Visualization
        + geom_point(aes(color='label',size='circle_size'))
        + geom_point(aes(color='pred_label',size='dot_size'))
        + scale_color_manual(values=colors,guide=False)
        + scale_size_continuous(guide=False)

        # Titles
        + annotate("text", x=.75, y=10.5, size=12, va='bottom', ha='left', lineheight=1, color=font_color, fontweight=600, label='F1: '+segment_name.upper())
        + annotate("text", x=.75, y=9.5, size=10, va='bottom', ha='left', lineheight=1, color=font_color, label='VISUAL')
        + annotate("text", x=11.5, y=9.5, size=10, va='bottom', ha='left', lineheight=1, color=font_color, label='METRICS')
        + annotate("text", x=21.5, y=9.5, size=10, va='bottom', ha='left', lineheight=1, color=font_color, label='LEGEND')

        # Metrics
        + annotate("text", x=10+padding, y=9, size=8, va='top', ha='left', lineheight=1.5, color=font_color, label=metrics_dict.get('precision'))
        + annotate("text", x=10+padding, y=7, size=8, va='top', ha='left', lineheight=1.5, color=font_color, label=metrics_dict.get('recall'))
        + annotate("text", x=10+padding, y=5, size=8, va='top', ha='left', lineheight=1.5, color=font_color, label=metrics_dict.get('f1'))
        + annotate("text", x=10+padding*1.75, y=9, size=8, va='top', ha='left', lineheight=1.5, color=font_color, label=precision_definition)
        + annotate("text", x=10+padding*1.75, y=7, size=8, va='top', ha='left', lineheight=1.5, color=font_color, label=recall_definition)
        + annotate("text", x=10+padding*1.75, y=5, size=8, va='top', ha='left', lineheight=1.5, color=font_color, label=f1_definition)

        # Legend
        + annotate("text", x=24, y=8, size=8, va='top', ha='center', lineheight=1.5, color=font_color, label='YES')
        + annotate("text", x=25, y=8, size=8, va='top', ha='center', lineheight=1.5, color=font_color, label='NO')
        + annotate("text", x=23, y=7, size=8, va='top', ha='center', lineheight=1.5, color=font_color, label='YES')
        + annotate("text", x=23, y=6, size=8, va='top', ha='center', lineheight=1.5, color=font_color, label='NO')
        + annotate("text", x=22, y=6.5, size=8, va='center', ha='center', lineheight=1.5, color=font_color, angle = 90, label='REALITY')
        + annotate("text", x=24.5, y=8.5, size=8, va='center', ha='center', lineheight=1.5, color=font_color, label='PREDICTION')
        )

    # Plot the plot
    return(p + theme(figure_size=(11,5)
        , panel_background=element_rect(fill=background)
        , legend_position=(None)
        ))

## INPUT DATA ##
# Read in a csv of the data...
# input_data = pd.read_csv('sample-confusion-matrix.csv')

# Or create a dataframe from a dictionary of dictionaries
input_data_dict = {
    1:{'segment':'all','true positive':0.56,'false positive':0.12,'true negative':0.22,'false negative':0.1},
    2:{'segment':'recent','true positive':0.52,'false positive':0.13,'true negative':0.24,'false negative':0.11},
    3:{'segment':'active','true positive':0.59,'false positive':0.1,'true negative':0.23,'false negative':0.08}
    }
input_data = pd.DataFrame(input_data_dict).transpose().reset_index(drop=True)

# Create visuals. Theme options are 'light' and 'dark'
f1vis(input_data,'light') 
