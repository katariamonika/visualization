## Visualization 2: Top 10 TTC LRT Stations by Total Delay Minutes (Bar Chart)

![Top 10 TTC LRT Stations by Total Delay Minutes](visualization_2_bar_top10_stations.png)


**What software did you use to create your data visualization?**  
This visualization was created using Microsoft Excel. The underlying summary data was generated using Python and exported as a CSV file.

**Who is your intended audience?**  
The intended audience includes transit operations staff and infrastructure planners seeking to identify locations associated with higher cumulative delay burden.

**What information or message are you trying to convey with your visualization?**  
The visualization highlights the ten TTC LRT stations with the highest total delay minutes, drawing attention to locations that may warrant targeted operational or infrastructure interventions.

**What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?**  
A bar chart was chosen to support direct comparison across categorical values. Stations were ordered by total delay minutes to facilitate rapid interpretation. Axis labels include units and a single color was used to avoid misinterpretation.

**How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?**  
While the Excel visualization itself is not programmatically reproducible, reproducibility was supported by generating the aggregated dataset using Python and saving it as a CSV file. This ensures transparency in data processing and allows the chart to be recreated if needed.

**How did you ensure that your data visualization is accessible?**  
Station names are clearly labeled, numeric values are scaled appropriately and units are explicitly stated. The visualization avoids excessive decoration and does not rely on color alone to convey information.

**Who are the individuals and communities who might be impacted by your visualization?**  
Communities served by the identified stations, particularly riders who experience repeated delays as well as decision-makers responsible for service planning and equity.

**How did you choose which features of your chosen dataset to include or exclude from your visualization?**  
The Station and Min Delay variables were selected to quantify delay burden by location. Other variables, such as delay codes or vehicle numbers, were excluded to keep the focus on spatial patterns.

**What ‘underwater labour’ contributed to your final data visualization product?**  
Aggregating delay minutes by station, ranking and filtering results, exporting summary data, and iterating on chart orientation and labeling contributed to the final visualization.
