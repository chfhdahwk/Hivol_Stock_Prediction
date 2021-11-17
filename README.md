# Hivol_Stock_Prediction
Development of stock trading system based on neural network using highly volatile stock price patterns


We developed a stock price prediction model using high fluctuation patterns and used the DNN structure. 

The high fluctuation pattern is a stock price fluctuation pattern using the concept of upper and lower limits in some countries. We filtered daily stock data into this pattern and used it as learning data and verification data of the deep learning model. 

# Details of the files are as follows. 
- hivol-file folder: is the learning, testing, and fund simulation data of the prediction model. 
- Fund-simulation.ipynb: It is a code for calculating the cumulative rate of return on data from the prediction result. 
- hybrid_model.ipynb: A file containing data loading and learning, and performance evaluation codes.
- rank_measure.py : The code used for normalization of input data of the model.
