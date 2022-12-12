

import streamlit as st
import numpy as np
import pickle
import pandas as pd


#pickle_in = open ("model.pkl", "rb")
#loaded_model = pickle.load(pickle_in)

#**************************replace path here with the folder path where the files are**********************************************
pickle_inn = open ("model2.pkl", "rb")
loaded_model2 = pickle.load(pickle_inn)

def welcoming_message():
    return "Linear Regression to predict the selling prices of houses based on a variety of features "

def predict(X):
    #bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat, long, sqft_living15,sqft_lot15 ):
   # return loaded_model.predict(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat, long, sqft_living15,sqft_lot15 )
   return loaded_model.predict(X)
#def theTypes(features):
 #   intFeatures=[]
  #  for feature in features:
   #     intFeatures.append(type(int(feature)))
    #return intFeatures

def predict2(X):
          return loaded_model2.predict(X)


def main():
    st.title("Linear regression analysis")

    #temporary html with styling
    html_tmp= """<div style=" background-color: navyblue; padding:10px">
    <h2 style=" colour:blue;text-allign:center;">Streamlit Linear Regression</h2>
    </div>
    <div> <h3 style="colour: offwhite; text-allign: left;">This project consists of a linear regression model 
    predicting the selling prices of houses based on a variety of features on which the value of 
    the house is evaluated.</h3>
    </div>
    """
    st.markdown(html_tmp,unsafe_allow_html=True)
    
    features=[]
    intFeatures=[]
    
    # Get input values - numeric variables
    bedrooms = st.slider('Please enter the number of bedrooms:',
                                min_value =1,
                                max_value = 10
                                )
    bathrooms = st.slider('Please enter the number of bathrooms:',
                                min_value =  0.75,
                                max_value = 8.0 
                                )
    sqft_living = st.slider('Please enter number of squarefeet size of the living room:',
                                min_value = 890,
                                max_value = 13540
                                )
    features.append(bedrooms)
    features.append(bathrooms)
    features.append(sqft_living)
                                
    sqft_lot = st.slider('Please enter squarefeet size of the lot',
                                min_value =  520,
                                max_value =1651359 
                                )
    floors = st.slider('Please enter the number of floors:',
                                min_value =  1.0,
                                max_value =  3.5
                                )
    waterfront = st.slider('Please enter if the house would have a waterfront',
                                min_value =  0,
                                max_value =  1
                               )
    features.append(sqft_lot)
    features.append(floors)
    features.append(waterfront)

    view = st.slider('Please enter the number of view sides',
                                min_value = 0,
                                max_value = 4 
                               )
    condition = st.slider('Please enter the condition of the house:',
                                min_value =  1,
                                max_value = 5 
                                )
    grade= st.slider('Please enter the house grade',
                                min_value =  5,
                                max_value = 13 
                                )
    features.append(view)
    features.append(condition)
    features.append(grade)

    sqft_above = st.slider('Please enter the squarefeet size of the above attick:',
                                min_value =   580,
                                max_value =  9410
                               )
    sqft_basement = st.slider('Please enter the squarefeet size of the basement:',
                                min_value =  0,
                                max_value = 4820
                                )
    yr_built = st.slider('Please enter the year the house was built in:',
                                min_value =  1900,
                                max_value = 2015
                                )
    yr_renovated = st.slider('renovated or not?',
                               min_value =  0,
                               max_value = 1
                               )
    features.append(sqft_above)
    features.append(sqft_basement)
    features.append(yr_built)
    features.append(yr_renovated)

    zipcode = st.slider('Please enter zipcode of the house:',
                               min_value =  98001,
                               max_value = 98199 
                               )
    lat = st.slider('please enter latitude:',
                               min_value =  47.1593,
                               max_value = 47.7764
                               )
    long = st.slider('please enter longitude:',
                               min_value =  -121.691,
                               max_value = -122.514
                               )
    sqft_living15 = st.slider('Please enter Living room area in 2015 ',
                               min_value =  860,
                               max_value = 6210 
                               )         

    sqft_lot15 = st.slider('Please enter lotSize area in 2015 ',
                               min_value =  967,
                               max_value =  871200
                               )  
    features.append(zipcode)
    features.append(lat)
    features.append(long)
    features.append(sqft_living15)
    features.append(sqft_lot15)




   # features.append(bedrooms = st.text_input("Bedrooms", "How many bedrooms should the hosue have?", "Type in a number","visible"))
   # features.append(bathrooms =  st.text_input("bathrooms","Type in a number"))
   # features.append(sqft_living = st.text_input("living space in squarefeet","Type in a number"))
    #features.append(sqft_lot= st.text_input("lot in squarefeet","Type in a number"))
    #features.append(floors= st.text_input("floors","How many floors?"))
    #features.append(waterfront= st.text_input("waterfroont","Type in a number"))
    #features.append(view = st.text_input("view","Type in a number"))
    #features.append(condition= st.text_input("condition","Type in a number"))


    #features.append(grade = st.text_input("grade","Type in a number"))
    #features.append(sqft_above= st.text_input("attick in squarefeet","Type in a number"))
    #features.append(sqft_basement= st.text_input("basement in squarefeet","Type in a number"))
    #features.append(yr_built= st.text_input("year built","Type in a number"))
    #features.append(yr_renovated= st.text_input("renovated","Type in a number"))
    #features.append(zipcode= st.text_input( "zipcode","Type in a number"))
    #features.append(sqft_living15= st.text_input("sqft_living15","Type in a number"))
    #features.append(sqft_lot15   = st.text_input("sqft_lot15","Type in a number"))
  
    #intFeatures=theTypes(features)
    result=""

    

    X = pd.DataFrame({'bedrooms':[bedrooms],
                      'bathrooms':[bathrooms], 
                      'sqft_living':[sqft_living], 
                      'sqft_lot':[sqft_lot], 
                      'floors':[floors],
                      'waterfront':[waterfront],
                      'view ':[view ], 
                      'condition':[condition],
                      'grade':[grade], 
                      'sqft_above':[sqft_above], 
                      'sqft_basement':[sqft_basement],
                      'yr_built':[yr_built], 
                      'yr_renovated':[yr_renovated],
                      'zipcode':[zipcode],
                       'lat':[lat],
                        'long':[long],
                       'sqft_living15':[sqft_living15] ,
                        'sqft_lot15':[sqft_lot15]
                       
                     })

  #  if st.button("predict with RigeModel"):
       
     # Making predictions            


  #      result = predict(X)
        #predict( [bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat, long,sqft_living15,sqft_lot15 ])
  #      st.success('The output is {}'.format(result))

    if st.button("predict price"):
       
     # Making predictions            


        result = predict2(X)
        #predict( [bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat, long,sqft_living15,sqft_lot15 ])
        st.success('The output is {}'.format(result))




    if st.button("about"):

        st.text("regression_data 2")
       # try: 
        

        # Open the file in read mode
        objectRep = open("datafile.picl", "rb")
        # Unpickle the objects
        data = pickle.load(objectRep)
        
        objectRep.close()

        #fig = px.line(data, x = X, y = data['price'], title='home prices based on features')
        #fig.show()
      
        

        df =pd.DataFrame(data)
        df
        
        #chart =(alt.Chart(df).mark_circle(size=40).encode(x=df['grade'], y=df['price']).properties(height=400, width=500))
        #chart



            

        # exp = hip.Experiment.from_csv(data)
        # hip.Experiment.to_streamlit()
        # ret_val=exp.display_st(key="hip")
        #ret_val = exp.to_streamlit(ret="selected_uids", key="hip").display()

        # st.markdown("hiplot returned " + json.dumps(ret_val))
        #exp.to_streamlit(key="hip1").display()  # Does not return anything
        # except AttributeError:
            #   pass       

        # Instead of calling directly `.display()`
        # just convert it to a streamlit component with `.to_streamlit()` before
        

if __name__ =='__main__':
        main()
  


