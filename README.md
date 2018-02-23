# Nuages
 
## Topic Modeling on Healthcare Forum Posts. 

#### Overview 
Nuages is the topic modeling project using Health Forum posts. People suffering from a health condition use online forums to give and recieve support or find resources to manage their condition. A wide body of social research has shown that online support can make a meaningful difference in the quality of life of patients. The goal of the project is get a better understanding the issues discussed by people suffering from migraines. The first step of the project is to generate Word Cloud of main of topic on the forum. 

#### Output 
Topic visualization using pyLDAvis: 

![topic_modelling](https://user-images.githubusercontent.com/25650135/36598654-2d71a9bc-18ad-11e8-91c4-70ef709f1cdd.PNG)


#### Technical Outline  
The script 'gensim_study.py' prepares unstructured text data to generate lists of tokens ('documents') that feed a Latent Dirichtlet Model (LDA) to generate the main topics in the body of text. The pyLDAvis Library is then used to visualize the topics. 
