import streamlit as st

def homepage():
    st.title('HOMEPAGE')

    st.image('img/sleeping-cat.jpg', width=500)
    st.title('Introduction')
    st.write("""
Did you know that, on average, a human spends nearly one-third of their life sleeping? Sleep, though a common aspect of our lives, remains a complex and often misunderstood phenomenon. In a world where everything is accelerating, is it true that our sleep quality is deteriorating?

After this semester's exams, I wanted to approach this very interesting subject in a more relaxed way for this ML project, in order to understand how, as students or people in working life, we can improve the quality of our sleep in order to be more efficient or productive on a daily basis. For this we will explore the following dataset on sleep quality and then try to predict sleep quality score based on different features.
In this exploration, we'll delve into factors influencing sleep quality beyond the familiar advice of a balanced diet and regular exercise. What are the other factors involved? How do our lifestyle and career choices affect our nightly rest? Let's examine these questions to unravel the intricacies of sleep and uncover insights that may enhance our daily lives. Get ready to embark on a quest where the path to a well-rested life may lie in the art of resting wisely.
""")
    
    st.title('Dataset')
    st.write('The dataset is available at https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset')
