
# House Price Prediction in King County, Washington

This web application, developed using Python, employs linear regression and data visualization techniques to predict and display house prices in King County, Washington. Built with Streamlit, this app offers an interactive interface for users to visualize housing data and engage with predictive models.

## Features

- **Data Visualization**: Displays house prices on maps and through various graphs.
- **Interactive Selections**: Users can select parameters like area, price range, bedrooms, bathrooms, etc., to filter the data.
- **Price Prediction**: Uses linear regression to predict house prices based on selected criteria.
- **Responsive Maps**: Showcases houses meeting user criteria on an interactive map.

## Installation

Before running the application, ensure that the required packages are installed. You can install these packages using the following commands in your Command Prompt or Terminal:

```bash
pip install streamlit sklearn seaborn plotly
```

## Running the App

To launch the application:

1. Open Command Prompt or Terminal.
2. Navigate to the directory containing the `code.py` file.
3. Run the command:

   ```bash
   streamlit run code.py
   ```

## Usage Guide

1. **Data Overview**: Initially, the complete dataset is displayed, giving users an overview of the housing market in King County.

   ![Complete Dataset](https://user-images.githubusercontent.com/59567512/90033476-24b5d180-dcdd-11ea-9c59-f03b25939508.png)

2. **Sidebar Filters**: Use the sidebars to filter data based on specific criteria such as price range, number of bedrooms/bathrooms, and more.

   ![Sidebar Filters](https://user-images.githubusercontent.com/59567512/90033535-35664780-dcdd-11ea-87ca-aebd383fcc01.png)

3. **Data Visualization**: The app presents average prices and the number of houses corresponding to the selected filters.

   ![Data Visualization](https://user-images.githubusercontent.com/59567512/90033721-69416d00-dcdd-11ea-8e46-48f9d569ed5a.png)

4. **Predictive Analysis**: The application predicts house prices based on user-selected criteria and displays this data graphically.

   ![Predictive Analysis](https://user-images.githubusercontent.com/59567512/90033809-80805a80-dcdd-11ea-8213-318920d3dec0.png)

5. **Mapping Choices**: Houses matching the user's selections are plotted on an interactive map for a geographical view.

   ![Mapping Choices](https://user-images.githubusercontent.com/59567512/90033912-9ee65600-dcdd-11ea-9f5d-f4388c33141e.png)

## Contributions and Feedback

Contributions to this project are welcome! If you have suggestions or feedback, feel free to open an issue or submit a pull request.
