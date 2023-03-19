# Suicides-Analysis

This is a Dash app that displays data about suicides in different countries and years. The analysis is based on the dataset for [Suicide Rates Overview (1985 to 2021)](https://www.kaggle.com/datasets/omkargowda/suicide-rates-overview-1985-to-2021). The app focuses on analyzing suicide numbers and rates as they vary by different countries in the world, and how these numbers have changed over time. More details on the reserach question and user persona can be found in the [`proposal.md`](https://github.com/UBC-MDS/suicide_indicator_r/blob/main/proposal.md) file. You can find the deployed app [here](https://suicides-analysis.onrender.com/)

The app is built using the Dash library, which provides a framework for building interactive web applications in Python. The app uses [Altair](https://altair-viz.github.io/) for data visualization and the [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) library for styling the layout. Overall, this Dash app provides a simple and interactive way to explore data about suicides in different countries and years, and demonstrates the power and flexibility of the Dash framework for building data-driven web applications.

## Usage

This code is a Python script that creates a dashboard application using the Dash library. The application allows the user to select a country and a year using dropdown menus and a slider, and displays two interactive charts based on the data for the selected country and year. The charts are created using the Altair library and are embedded in HTML iframes in the dashboard.

The first chart is a bar chart that shows the number of suicides by gender for the selected country and year. The chart has a horizontal axis for the number of suicides and a vertical axis for the gender. The bars are colored based on gender, and the chart displays the exact number of suicides as a tooltip when the user hovers over a bar.

The second chart is a pie chart that shows the number of suicides by age range for the selected country and year. The chart has a circle shape and is divided into slices based on the age range. The size of each slice represents the number of suicides, and the color of each slice represents the age range. The chart also displays the exact number of suicides as a tooltip when the user hovers over a slice.

The data used contains information about suicides around the world from 1985 to 2021, including the `country`, `year`, `gender`, `age`, and `number of suicides`.

## Contributing to the project

Interested in contributing? Check out the contributing guidelines [here](https://github.com/qurat-azim/Suicides-Analysis-Dash/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/qurat-azim/Suicides-Analysis-Dash/blob/main/CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## References

The dataset used in this project is the Suicide Rates Overview (1985 to 2021) available on Kaggle. The data was originally sourced from the United Nations Development Program, World Bank and World Health Organization.

Please refer to the original data sources for more information on how the data was collected and processed.

## License

`Suicides-Analysis-Dash` was created by Qurat-ul-Ain Azim. The materials of this project are licensed under the [MIT license](https://github.com/qurat-azim/Suicides-Analysis-Dash/blob/main/LICENSE). If re-using/re-mixing please provide attribution and link to this webpage.
