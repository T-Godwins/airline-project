1. How do customer reviews align with operational flight data? (Combining both datasets)
Investigate if there's a connection between customer reviews (from the Delta dataset) and flight punctuality or route data (from the Airline dataset).

2. Predicting customer satisfaction (Delta dataset)

### Model Results
- Mean Squared Error: 14.93
- R² Score: -0.26

#### Feature Importance
![Feature Importance](images/feature_importance.png)
1. Date: Accounts for most of the variance in ratings
2. Traveler Types: Has less impact on ratings

#### Decision Tree Visualization
![Decision Tree](images/decision_tree.png)

#### Model Interpretation
- The current model shows poor performance (negative R² score) suggesting that:
  - We need more features (like Seat Type, Routes, Country)
  - Date might need better preprocessing (e.g., extract month, day of week)
  - Text analysis of reviews could provide valuable insights
  - Consider using more advanced models or ensemble methods


### Model Results
- Mean Squared Error: 14.93
- R² Score: -0.26

#### Feature Importance
![Feature Importance](images/feature_importance.png)
1. Date: Accounts for most of the variance in ratings
2. Traveler Types: Has less impact on ratings

#### Decision Tree Visualization
![Decision Tree](images/decision_tree.png)

#### Model Interpretation
- The current model shows poor performance (negative R² score) suggesting that:
  - We need more features (like Seat Type, Routes, Country)
  - Date might need better preprocessing (e.g., extract month, day of week)
  - Text analysis of reviews could provide valuable insights
  - Consider using more advanced models or ensemble methods

Use the Delta dataset to predict customer satisfaction based on various features.

3. Analyzing flight punctuality (Airline dataset)
Analyze the Airline dataset to understand flight punctuality and identify key factors influencing it.
