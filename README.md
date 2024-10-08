conda create --name "Os_base" python=3.9 --yes






# mlops

#MLOPS 3PFreamwork

SCOPING   ->   DATA                    ->    MODELING           ->    Deployment          
Project        Define and    Labeling        Traing    Error          Deploy     Monitor and 
Definition     Stablish      Data            Model     Analysis                  Maintain 
               Baseline

SUPERVISED MACHINE LEARNING 

Reegression:
Relationship and patterns  between independent variables(DATASET) or features, labelled input and output,
            
                                  x      ->       y 
                                Input         Prediction
                               Feature   ->     Target
     

Models that are trained to forecast or predict trends and outcomes on time series visualisations
Forecasting                             Predicting                                              Analysing




REGRESION TYPE:
1.Simple linear regresion
      Model                 Cost Function                              Gradient Decent 
	                               m          (i)   (i) 2                   
f w,b(x) = w x + b     j(w,b) =  1/2m SUM (f w,b(x)  -  y )         w = w - a A @/@w J(w,b)
                                      i= 1                          b = b - a A @/@w J(w,b)


2.Multiple linear regression 

def predict_single_loop(x, w, b)
return f_wb = prediction

def predict(x, w, b)
return p = np.dot(x, w) + b  

def compute_cost(X, y, w, b): 
return cost / (2 * m)  + (f_wb_i - y[i])**2

def compute_gradient(X, y, w, b): 
dj_db = dj_db + err = (np.dot(X[i], w) + b) - y[i] 
return dj_db/m, dj_dw/m

Learning rate     Feature Scaling    Feature Normalization

Binary Clasification 

3.Logistic regression 

def sigmoid(z):
return  g = 1/(1+np.exp(-z))pwd


def compute_cost_logistic(X, y, w, b):
cost +=  -y[i]*np.log(f_wb_i) - (1-y[i])*np.log(1-f_wb_i) | cost / m

Loss,Cost, Objective f(x)
"Loss function is a unitary sample from the average  error cost function where trying to optimize an Objective function "

Underfiting High Bias                        Generalization              OverFit High Variance 

Cost Function with Regularization 
1.Regularized Linear Regresion
def compute_cost_lineaar_regresion (X,y,w,b,,lamba_=1)

m = X_train.shape[0]
n = len(w)
cost = 0.

for i in range(m):
	f_wb = np.dot(X[i], w) + b
	cost = cost + (f_wb - y[i])**2 
	cost = cost / (2 * m)

	reg_cost = 0
	for j in range(n)
 		reg_cost = +- (w[j]**2)
		reg_cost = (lambda_/(2*m)) * reg_cost
return  total_cost =  cost + reg_cost 


2.Regularized Logisctic Regresion  









UNSUPERVISED LEARNING 
Algo learns patterns and structures from unlabeled data:

Clustering 
Dimentionality Reduction
Anomaly Detection 


//1.DATA Prep 

/*E:UnavailableInvalidChannel: The channel is not accessible or is invalid.
  channel name: new_channel_url
  channel url: https://conda.anaconda.org/new_channel_url
  error code: 404
*/
Fix: 
conda config --show channels
conda config --remove channels new_channel_url













