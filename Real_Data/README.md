We have defined a new class named "CSV_DataSample" in 1D_PINN_with_real_data.ipynb file to extract the required feature data.  <br>
In the `S&P500(2015-2019)_with_hedging_profits.csv` file:  <br>
A condition of used data: cp_flag == 'P' (Pricing of Put Options);  <br>
strike_price / 1000 = K;  <br>
ttm is time _t_;  <br>
option_price is _ground truth_.  <br>
