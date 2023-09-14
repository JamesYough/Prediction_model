plt.rcParams["figure.figsize"] = (11,5)
churned_df = df.query("Churned > 0" )
sb.scatterplot( x = churned_df.Tenure_in_Months , y = churned_df.Total_Revenue ,alpha= 0.7,hue= churned_df.Offer );