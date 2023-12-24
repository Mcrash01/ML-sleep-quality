import streamlit as st

def data_analysis():
    st.title('DATA ANALYSIS')
    
    st.write(
    """
Here is the EDA (Exploration Data Analysis for the dataset.)
    """)

    st.write("Missing values:")
    st.image('img/missing_values.png', width=500)

    st.write("Data repartition :")
    st.image('img/features_distribution.png', width=500)

    st.write("Sleep Quality Count :")
    st.image('img/sleep_quality_count.png', width=500)

    st.write("Sleep Quality vs Sleep Duration :")
    st.image('img/sleep_quality_vs_duration.png', width=500)
    st.write(
    """"We can see something that looks like a linear relationship between sleep duration and sleep quality: the more we sleep, the better we sleep! Let's we what factors help us to have a better and longer sleep.""")


    st.write("relationship between solationship_with_sleep_quality.png'me features and sleep quality :")
    st.image('img/features_vs_sleep_quality.png', width=500)
    st.write(
    """
We can observe that daily physical activity improves sleep quality, although the number of daily steps does not influence it proportionally. Stress level, on the other hand, is an essential and determining factor in sleep quality.""")
    
    st.write("distribution of age in the dataset :")
    st.image('img/age_distribution.png', width=500)

    st.write("job occupation repartition :")
    st.image('img/occupation_pie.png', width=500)    

    st.write("ocupation vs sleep quality :")
    st.image('img/occupation_vs_sleep_quality.png', width=500)
    st.write(
    """It seems that our careers choices will influence our sleep quality!""")

    st.write("impact of career choice on sleep")
    st.image('img/occupation_vs_sleep_quality_duration.png', width=500)
    st.write("""
Here it is interesting to see that the interquartile range of sleep quality and sleep duration varies greatly between occupations. This means that sleep quality and quantity are highly variable between different professions. This confirms the idea that our life/career choices greatly influence our sleep. I think it is interesting to correlate this with the stress level to see if thoose features are linked <br>
(ie job->stress level->sleep quality/duration)""")
    
    st.write("stress level vs occupation:")
    st.image('img/occupation_vs_stress_sleep_quality.png', width=500)
    st.write("""we see an inverse relationships between both subplots ie this confirms the idea of:
job -> stress level -> sleep quality/duration
with -> = influences""")
    
    st.write("sleep disorder:")
    st.image('img/sleep_disorder_count.png', width=500)
    st.image('img/sleep_disorder_gender.png', width=500)

    st.write("impact of age on sleep :")
    st.image('img/sleep_vs_age.png', width=500)

    st.write("sleep disorder by BMI category :")
    st.image('img/treemap.png', width=500)

    st.write("BMI, Blood Pressure and Heart Rate correlation:")
    st.image('img/BMI_heatmap.png', width=500)
    
    st.write("correlation matrix:")
    st.image('img/corr_matrix.png', width=500)