import streamlit as st

def ml_models():
    st.title('ML MODELS')

    st.write('Here you can find the different ML models that we have trained and tested and the results of each one of them.')

    st.write('This XGB Classifier will try to predict the sleep quality of a person based on the following features:')
    st.write("""
            -Gender	\n
             -Age \n    
             -Occupation \n	
             -Sleep Duration \n	
             -Physical Activity Level \n
             -Stress Level \n
             -BMI Category \n
             -Blood Pressure \n	
             -Heart Rate \n
             -Daily Steps \n	
             -Sleep Disorder""")
    
    st.write('We have used a LabelEncoder to transform the categorical features into numerical ones.')
    st.write('For target value, we made a mapping as XGBClassifier needs classes that start from 0.')
    
    st.write('Accuracy of the model: 0.97')

    st.write('Confusion Matrix:')
    st.image('img/conf_matrix.png', width=500)

    st.write('Feature Importance:')
    st.image('img/feature_importance.png', width=500)

    st.write("""
Conclusion: We see that we can achieve good prediction results with the XGB Classifier.
The most important features are the Sleep Duration, Stress Level and Age. \n
Countrary to what we could have thought, the Daily steps is not a very important feature for the prediction.
Sleep Disorder is also interesting as it seems not to be the first indicator of sleep quality, this is confirmed by the graph : sleep quality vs age / sleep disorder vs age where we see that the pics of disorders does not correspond to the sleep quality inverse peaks:
             """)
    st.image('img/sleep_vs_age.png', width=500)