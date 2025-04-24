We have defined a new class named "CSV_DataSample" in 1D_PINN_with_real_data.ipynb file to extract the required feature data.  <br>
\
In the `S&P500(2015-2019)_with_hedging_profits.csv` file:  <br>
A condition of used data: cp_flag == 'P' (Pricing of Put Options);  <br>
strike_price / 1000 = K;  <br>
ttm is time _t_, option_price is _ground truth P_.  <br>
\
In the `美国标准普尔500指数历史数据.xlsx` file:  <br>
Feature "收盘" is considered as the "underlying asset price".  <br>
(Correspond the extracted data according to the date)  <br>
\
Due to the fact that it is difficult to find dataset that meet the requirements in the market, this project only conducted tests on 1-dimensional real data.

### figures
We did the tests under different _T_ and _K_ conditions, and the generated figuers of loss values were saved in the `figures` folder.

### visualization
In order to present the relationship between the loss values of free boundary and _T_ and _K_ with the real data more intuitively, we made visualized figures in the `visualization` folder.
