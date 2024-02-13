# NBA Statistics Web Scraping and Predictive Modeling Project

## Overview

This project focuses on collecting NBA player statistics from the Proballers website and from the ESPN Hollinger Columnist section, through web scraping techniques and leveraging the gathered data to build a predictive model. The aim is to analyze player performance and develop insights that can contribute to a predictive model for future performance predictions.

#### NOTE:
All data collection has been done over the course of multiple days. Scraping of the sources had been spread out as to **not** accidentally flood these websites with HTTPS requests and **cause a DDoS attack**. If you chose to clone this repository make sure that you do not take data that has already been collected.

## Project Structure

- data_scraping: Contains scripts for web scraping NBA statistics from Proballers.

- data_analysis: Jupyter notebooks or Python scripts for exploratory data analysis (EDA) and feature engineering.

- modeling: Code for building and evaluating predictive models.

- results: Store the results of the predictive models, visualizations, and any other relevant outputs.

## Prerequisites

Ensure you have the required Python packages by running:

```bash
pip install re
pip install pandas
```

## Data Collection

1. Run the web scraping script in the data_scraping folder to gather NBA player statistics from Proballers.

2. Store the collected data in the data directory.

## Exploratory Data Analysis (EDA)

Explore the collected data using Jupyter notebooks or Python scripts in the data_analysis folder. Perform data cleaning, visualization, and feature engineering to gain insights into the dataset.
## Modeling

Implement predictive models using machine learning algorithms. The modeling folder contains code for model training, evaluation, and hyperparameter tuning.
## Results

Store the results of your predictive models, visualizations, and any other relevant outputs in the results directory.
## Usage

1. Clone the repository:

```bash
git clone https://github.com/flannelmonke/HoopsForecast_Pro.git
```
1. Follow the steps in the "Data Collection," "Exploratory Data Analysis," and "Modeling" sections.

2. Use the models for predictions or further analysis.

## Contributing

Feel free to contribute to the project by opening issues, suggesting improvements, or submitting pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgments

Proballers website for providing the NBA player statistics.
ESPN Hollinger Columnist

# Project outline

## Data Science Project: Predictive Model for Basketball Games

### 1. [Introduction](./README.md)
   - Brief overview of the project
   - Importance of predicting basketball game outcomes
   - Objectives and goals

### 2. Problem Definition
   - Clearly define the problem statement
   - Specify what you want to predict (e.g., game winner, point difference, player performance)

### 3. [Data Collection](./1_Data_Collection/webscraping_notebook.ipynb)
   - Identify and gather relevant data sources
     - Historical game data
     - Player statistics
     - Team statistics
     - Venue details
     - Injury reports
   - Consider APIs, databases, or scraping techniques

### 4. [Data Cleaning and Preprocessing](./2_Data_Preprocessing/Data_Pre_Processing.ipynb)
   - Handle missing values
   - Remove duplicates
   - Standardize/normalize numerical features
   - Convert categorical variables (team names, player positions) into numerical representations
   - Feature engineering (create new features based on existing ones)

### 5. Exploratory Data Analysis (EDA)
   - Understand the distribution of key variables
   - Identify correlations between variables
   - Visualize patterns and trends
   - Gain insights into the data

### 6. Feature Selection
   - Use statistical methods or machine learning techniques to select the most relevant features
   - Remove redundant or irrelevant features

### 7. Model Selection
   - Choose appropriate models for prediction (e.g., logistic regression, decision trees, random forests, neural networks)
   - Split the dataset into training and testing sets

### 8. Model Training
   - Train the selected models on the training dataset
   - Fine-tune hyperparameter to improve model performance
   - Validate models using cross-validation techniques

### 9. Model Evaluation
   - Evaluate the models on the testing dataset
   - Use appropriate metrics (accuracy, precision, recall, F1-score, etc.)
   - Compare multiple models to select the best-performing one

### 10. Hyperparameter Tuning
   - Fine-tune model hyperparameter using techniques like grid search or random search
   - Optimize the model for better performance

### 11. Deployment
   - Implement the model in a production environment
   - Develop a user-friendly interface if applicable
   - Ensure scalability and efficiency

### 12. Monitoring and Maintenance
   - Implement a system for monitoring model performance over time
   - Periodic updates and retraining to account for new data and trends
   - Handle model drift and maintain data quality

### 13. Documentation
   - Document the entire process, from data collection to model deployment
   - Include details about data sources, preprocessing steps, model selection, and performance metrics

### 14. Conclusion
   - Summarize findings
   - Discuss limitations and potential areas for improvement
