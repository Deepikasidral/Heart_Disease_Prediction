# chat_patterns.py

patterns = [
    (r'what is heart disease/?', ['Heart disease, also known as cardiovascular disease, refers to a class of diseases that involve the heart or blood vessels. It is a broad term that encompasses various conditions, and the most common type is coronary artery disease.']),
    (r'what are the symptoms of heart disease/?', ['Common symptoms of heart disease include chest pain, shortness of breath, fatigue, and irregular heartbeat.']),
    (r'how is heart disease diagnosed/?', ['Heart disease is diagnosed through various tests, including electrocardiogram (ECG or EKG), blood tests, echocardiogram, and stress tests.']),
    (r'what are the risk factors for heart disease/?', ['Major risk factors for heart disease include high blood pressure, high cholesterol, smoking, obesity, and a sedentary lifestyle.']),
    (r'can heart disease be prevented/?', ['Yes, heart disease can often be prevented by adopting a healthy lifestyle, including regular exercise, a balanced diet, and avoiding tobacco and excessive alcohol consumption.']),
    (r'what is a heart-healthy diet/?', ['A heart-healthy diet includes plenty of fruits, vegetables, whole grains, lean proteins, and limited saturated fats and sodium.']),
    (r'is stress a risk factor for heart disease/?', ['Chronic stress can contribute to heart disease. Managing stress through relaxation techniques and coping strategies is important for heart health.']),
    (r'what are the types of heart diseases/?', ['There are various types of heart diseases, including coronary artery disease, heart failure, arrhythmias, and valvular heart diseases.']),
    (r'how is heart disease treated/?', ['Treatment for heart disease may include lifestyle changes, medications, angioplasty, stent placement, or coronary artery bypass grafting (CABG) depending on the severity.']),
    (r'are heart attacks and cardiac arrests the same/?', ['No, a heart attack (myocardial infarction) occurs when blood flow to the heart muscle is blocked, while cardiac arrest is the sudden loss of heart function.']),
    
    (r'heart disease/?', ['Heart disease refers to conditions that affect the heart, such as coronary artery disease, heart rhythm problems, and heart defects.']),(r'heart disease/?', ['Heart disease refers to conditions that affect the heart, such as coronary artery disease, heart rhythm problems, and heart defects.']),
    (r'symptoms/?', ['Common symptoms of heart disease include chest pain or discomfort, shortness of breath, fatigue, and irregular heartbeat.']),
    (r'prevent/?', ['You can reduce your risk of heart disease by maintaining a healthy diet, exercising regularly, avoiding tobacco smoke, managing stress, and getting regular check-ups.']),
    (r'risk factors/?', ['Risk factors for heart disease include high blood pressure, high cholesterol, diabetes, smoking, obesity, and a sedentary lifestyle.']),
    (r'diagnosed/?', ['Heart disease can be diagnosed through physical examination, medical history review, blood tests, imaging tests (such as ECG or echocardiogram), and cardiac catheterization.']),
    (r'treatment options/?', ['Treatment options for heart disease depend on the specific condition but may include lifestyle changes, medications, medical procedures (such as angioplasty or bypass surgery), and cardiac rehabilitation.']),
    (r'quit', ['Thank you for using our heart disease chatbot!']),
    # Additional patterns:
    (r'causes of heart disease/?', ['The causes of heart disease can vary depending on the specific condition but may include factors such as genetics, unhealthy lifestyle choices, and underlying medical conditions.']),
    (r'cardiovascular health/?', ['Maintaining cardiovascular health is important for reducing the risk of heart disease. This includes regular exercise, a balanced diet, avoiding smoking, and managing stress.']),
    (r'heart attack/?', ['A heart attack occurs when the blood flow to part of the heart is blocked, often by a blood clot. Symptoms may include chest pain, shortness of breath, nausea, and sweating.']),
    (r'stroke/?', ['A stroke occurs when the blood supply to part of the brain is interrupted or reduced, leading to damage to brain tissue. Symptoms may include sudden weakness, numbness, or paralysis, typically on one side of the body.']),
    (r'cholesterol/?', ['High cholesterol levels in the blood can increase the risk of heart disease. It is important to maintain healthy cholesterol levels through diet, exercise, and, if necessary, medication.']),
    (r'blood pressure/?', ['High blood pressure, or hypertension, is a risk factor for heart disease. It is important to monitor blood pressure regularly and take steps to lower it if it is too high.']),
    (r'diet and heart health/?', ['A healthy diet is essential for heart health. This includes eating plenty of fruits, vegetables, whole grains, lean proteins, and healthy fats, while limiting processed foods, sugary drinks, and excess salt.']),
    (r'exercise and heart health/?', ['Regular exercise is important for maintaining heart health. Aim for at least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous-intensity activity each week, along with muscle-strengthening exercises on two or more days.']),
    (r'smoking and heart disease/?', ['Smoking is a major risk factor for heart disease. Quitting smoking can significantly reduce the risk of heart attack, stroke, and other cardiovascular problems.']),
    (r'stress and heart health/?', ['Chronic stress can contribute to heart disease by raising blood pressure, increasing cholesterol levels, and promoting unhealthy behaviors. It is important to find healthy ways to manage stress, such as exercise, relaxation techniques, and social support.']),
    (r'alcohol and heart health/?', ['Moderate alcohol consumption may have some cardiovascular benefits, but excessive drinking can increase the risk of heart disease and other health problems. It is important to drink alcohol in moderation, if at all.']),
    (r'genetics and heart disease/?', ['Genetic factors can play a role in the development of heart disease. If you have a family history of heart disease, it is important to be aware of your risk factors and take steps to prevent or manage the condition.']),
    (r'women and heart disease/?', ['Heart disease is not just a problem for men. It is the leading cause of death for women in many countries. Women may experience different symptoms of heart disease than men, so it is important to be aware of the signs and seek medical attention if necessary.']),
    (r'children and heart health/?', ['Heart health begins in childhood. Encourage healthy habits early, such as eating a balanced diet, staying active, and avoiding tobacco smoke, to reduce the risk of heart disease later in life.']),
    (r'heart-healthy recipes/?', ['Eating a heart-healthy diet can be delicious! Look for recipes that include plenty of fruits, vegetables, whole grains, and lean proteins, and experiment with herbs and spices for flavor.']),
    (r'heart disease support groups/?', ['Joining a support group can provide valuable emotional support and practical advice for managing heart disease. Look for local or online groups where you can connect with others who are going through similar experiences.']),
    
    (r'overview of heart disease./?', ['Heart disease encompasses various conditions affecting the heart, including coronary artery disease, arrhythmias, congenital heart defects, and heart failure.']),
    (r'pathophysiology of heart disease/?', ['Heart disease often involves abnormalities in the structure or function of the heart, leading to impaired blood flow, inadequate oxygen supply, and compromised cardiac performance.']),
    (r'risk factors for heart disease/?', ['Common risk factors for heart disease include hypertension, dyslipidemia, diabetes mellitus, smoking, obesity, sedentary lifestyle, and family history of heart disease.']),
    (r'common symptoms of heart disease/?', ['Symptoms of heart disease can vary depending on the specific condition but may include chest pain, shortness of breath, palpitations, fatigue, dizziness, and edema.']),
    (r'diagnostic tests for heart disease.', ['Diagnostic tests for heart disease include electrocardiography (ECG/EKG), echocardiography, stress testing, cardiac catheterization, computed tomography (CT) scans, magnetic resonance imaging (MRI), and blood tests.']),
    (r'management of heart disease/?', ['Management of heart disease involves lifestyle modifications (diet, exercise, smoking cessation), medications (antiplatelets, antihypertensives, lipid-lowering agents), interventional procedures (angioplasty, stenting), and surgical interventions (bypass surgery, valve repair/replacement).']),
    (r'prevention of heart disease/?', ['Preventive measures for heart disease include promoting healthy lifestyle habits, screening for risk factors, early detection and treatment of hypertension and dyslipidemia, and public health initiatives to reduce smoking and obesity rates.']),
    (r'latest research in heart disease/?', ['Recent research in heart disease includes advancements in risk prediction models, novel therapeutic targets, minimally invasive interventions, and regenerative medicine approaches to cardiac repair and regeneration.']),
    (r'role of genetics in heart disease/?', ['Genetic factors play a significant role in the pathogenesis of certain types of heart disease, such as familial hypercholesterolemia, hypertrophic cardiomyopathy, and congenital heart defects.']),
    (r'impact of lifestyle on heart health/?', ['Adopting a healthy lifestyle, including a balanced diet, regular exercise, stress management, and avoidance of tobacco and excessive alcohol consumption, can significantly reduce the risk of developing heart disease.']),
    (r'emerging therapies for heart disease/?', ['Emerging therapies for heart disease include gene editing techniques, stem cell therapy, tissue engineering approaches, and the use of innovative drug delivery systems to target specific molecular pathways implicated in cardiac pathology.']),
    (r'role of inflammation in heart disease/?', ['Chronic inflammation plays a critical role in the development and progression of atherosclerosis, myocardial infarction, heart failure, and other cardiovascular disorders, highlighting the potential therapeutic value of anti-inflammatory agents in managing heart disease.']),
    (r'impact of COVID-19 on heart health/?', ['COVID-19 can have significant cardiovascular manifestations, including myocardial injury, arrhythmias, thrombotic events, and myocarditis, emphasizing the importance of cardiovascular monitoring and management in patients with COVID-19.']),
    (r'advances in imaging modalities for heart disease/?', ['Advances in cardiac imaging modalities, such as cardiac magnetic resonance imaging (MRI), computed tomography (CT), and 3D echocardiography, offer improved accuracy and precision in diagnosing heart disease and assessing cardiac structure and function.']),
    (r'role of artificial intelligence in heart disease/?', ['Artificial intelligence (AI) holds promise in revolutionizing the diagnosis, risk stratification, and personalized treatment of heart disease by leveraging big data analytics, machine learning algorithms, and predictive modeling techniques.']),
    (r'ethical considerations in heart disease research/?', ['Ethical considerations in heart disease research encompass issues such as patient autonomy, informed consent, confidentiality, equity in access to care, conflicts of interest, and responsible conduct of clinical trials and experimental studies.']),
    (r'heart disease in special populations/?', ['Certain populations, such as women, elderly individuals, racial and ethnic minorities, and individuals with comorbid conditions (e.g., diabetes, chronic kidney disease), may have unique risk factors, clinical presentations, and treatment considerations for heart disease.']),
    (r'role of public health interventions in reducing heart disease/?', ['Public health interventions, including health education campaigns, policy initiatives (e.g., tobacco control measures, taxation on sugary beverages), and community-based programs (e.g., access to healthy foods, recreational facilities), play a crucial role in preventing and controlling heart disease at the population level.']),
   (r'congenital heart defects/?', ['Congenital heart defects are structural abnormalities present at birth, affecting the chamber of the heart, valves, or major blood vessels. These defects may range from mild to severe and often require early detection, specialized care, and surgical interventions to optimize outcomes.']),
    (r'cardiomyopathies/?', ['Cardiomyopathies are diseases of the heart muscle, characterized by abnormalities in myocardial structure and function, leading to impaired cardiac performance and increased risk of heart failure, arrhythmias, and sudden cardiac death. These conditions may be inherited or acquired and require comprehensive evaluation and management by cardiologists.']),
    (r'role of telemedicine in managing heart disease/?', ['Telemedicine, including remote monitoring, teleconsultation, and tele-rehabilitation services, offers opportunities to improve access to specialized cardiac care, enhance patient-provider communication, and optimize treatment outcomes for individuals with heart disease, particularly in rural and underserved areas.']),
    (r'heart disease complications/?', ['Complications of heart disease may include heart failure, arrhythmias, myocardial infarction, stroke, peripheral artery disease, cardiogenic shock, and sudden cardiac arrest, underscoring the importance of early detection, risk stratification, and comprehensive management to prevent adverse outcomes.']),
    (r'heart disease terminology/?', ['Understanding common terminology used in cardiology, such as myocardial ischemia, atherosclerosis, mitral valve prolapse, ventricular remodeling, and cardiac arrest, is essential for medical students to effectively communicate with colleagues, patients, and interdisciplinary healthcare teams in clinical practice.']),
    (r'role of non-invasive testing in heart disease/?', ['Non-invasive testing modalities, including electrocardiography, echocardiography, stress testing, and cardiac imaging (MRI, CT), play a crucial role in the initial evaluation, risk stratification, and long-term monitoring of patients with suspected or known heart disease, providing valuable diagnostic information without the need for invasive procedures.']),
    (r'heart disease and pregnancy/?', ['Heart disease complicating pregnancy, such as congenital heart defects, valvular heart disease, cardiomyopathies, and hypertensive disorders, presents unique challenges for maternal and fetal health, requiring multidisciplinary management and specialized obstetric and cardiac care to optimize outcomes for both mother and baby.']),
   
    (r'.types of heart disease/?', ['Heart disease includes conditions like coronary artery disease, heart failure, arrhythmias, valvular heart disease, and congenital heart defects.']),
    (r'.pathophysiology of heart disease/?', ['Understanding the pathophysiology of heart disease involves studying factors such as atherosclerosis, myocardial ischemia, myocardial infarction, and cardiac remodeling.']),
    
    # Risk Factors
    (r'.risk factors for heart disease/?', ['Common risk factors for heart disease include hypertension, dyslipidemia, diabetes mellitus, smoking, obesity, sedentary lifestyle, and family history of heart disease.']),
    (r'.modifiable risk factors/?', ['Modifiable risk factors for heart disease are those that can be controlled or modified through lifestyle changes or medical intervention, such as smoking, diet, physical activity, and stress management.']),
    (r'.non-modifiable risk factors/?', ['Non-modifiable risk factors for heart disease are those that cannot be changed, such as age, gender, family history, and genetic predisposition.']),
    
    # Symptoms and Diagnosis
    (r'.symptoms of heart disease/?', ['Symptoms of heart disease can vary depending on the specific condition but may include chest pain, shortness of breath, fatigue, palpitations, dizziness, and swelling in the legs.']),
    (r'.diagnosis of heart disease/?', ['The diagnosis of heart disease involves a combination of patient history, physical examination, diagnostic tests (e.g., electrocardiogram, echocardiogram, stress test, cardiac catheterization), and laboratory investigations (e.g., lipid profile, cardiac enzymes).']),
    
    # Treatment and Management
    (r'.treatment of heart disease/?', ['Treatment options for heart disease may include lifestyle modifications (e.g., diet, exercise), medications (e.g., antiplatelets, beta-blockers, ACE inhibitors), interventional procedures (e.g., angioplasty, stent placement), and surgical interventions (e.g., bypass surgery, valve repair/replacement).']),
    (r'.management of heart disease/?', ['The management of heart disease involves a comprehensive approach aimed at controlling symptoms, reducing complications, improving quality of life, and preventing disease progression. This may include medication adherence, regular follow-up visits, monitoring of cardiac function, and patient education.']),
    
    # Prevention and Lifestyle
    (r'.prevention of heart disease/?', ['Preventive measures for heart disease include adopting a heart-healthy lifestyle, managing risk factors, such as hypertension and hyperlipidemia, avoiding tobacco use, maintaining a healthy weight, engaging in regular physical activity, and following a balanced diet low in saturated fats, cholesterol, and sodium.']),
    (r'.lifestyle modifications for heart disease/?', ['Lifestyle modifications play a crucial role in the management of heart disease and may include dietary changes (e.g., Mediterranean diet), regular exercise, smoking cessation, stress reduction techniques (e.g., mindfulness, relaxation), and adherence to prescribed medications.']),
    
    # Research and Innovation
    (r'.research on heart disease/?', ['Ongoing research on heart disease focuses on areas such as novel therapeutic targets, genetic predisposition, personalized medicine approaches, innovative diagnostic techniques, and strategies for improving outcomes in high-risk populations.']),
    (r'.innovations in heart disease management/?', ['Recent innovations in heart disease management include advancements in minimally invasive procedures, such as transcatheter valve replacement, development of targeted therapies for specific subtypes of heart disease, and integration of digital health technologies for remote monitoring and patient engagement.']),
    
    # Education and Resources
    (r'.resources for heart disease education/?', ['Medical students can access various resources for learning about heart disease, including textbooks, online courses, academic journals, professional societies (e.g., American College of Cardiology, American Heart Association), clinical practice guidelines, and educational conferences and workshops.']),
    (r'.heart disease organizations/?', ['There are several organizations dedicated to heart disease research, advocacy, and patient support, such as the World Heart Federation, British Heart Foundation, and Heart Foundation (Australia). These organizations provide valuable resources, educational materials, and funding opportunities for medical students and healthcare professionals.']),
    
    # Specific Conditions
    (r'.coronary artery disease/?', ['Coronary artery disease is characterized by the narrowing or blockage of coronary arteries, leading to reduced blood flow to the heart muscle.']),
    (r'.heart failure/?', ['Heart failure, also known as congestive heart failure, occurs when the heart is unable to pump enough blood to meet the bodys needs.']),
    (r'.arrhythmias/?', ['Arrhythmias are abnormalities in the hearts rhythm, which can cause the heart to beat too fast, too slow, or irregularly.']),
    (r'.valvular heart disease/?', ['Valvular heart disease involves abnormalities in one or more of the heart valves, impairing the flow of blood through the heart.']),
    (r'.congenital heart defects/?', ['Congenital heart defects are structural abnormalities present at birth, affecting the hearts chambers, valves, or blood vessels.']),
    
    # Additional Topics
    (r'.cardiovascular system/?', ['The cardiovascular system consists of the heart and blood vessels, including arteries, veins, and capillaries, which circulate blood throughout the body.']),
    (r'.atherosclerosis/?', ['Atherosclerosis is a progressive disease characterized by the buildup of plaque (cholesterol, fat, and other substances) in the arteries, leading to narrowing and reduced blood flow.']),
    (r'.myocardial infarction/?', ['Myocardial infarction, commonly known as a heart attack, occurs when blood flow to a part of the heart is blocked, leading to damage or death of the heart muscle.']),
    (r'.hypertension/?', ['Hypertension, or high blood pressure, is a leading risk factor for heart disease and other cardiovascular complications.']),
    (r'.hyperlipidemia/?', ['Hyperlipidemia refers to elevated levels of lipids (e.g., cholesterol, triglycerides) in the blood, which can contribute to atherosclerosis and increase the risk of heart disease.']),
    (r'.types of heart disease.', ['There are various types of heart disease, including coronary artery disease, heart failure, arrhythmias, valvular heart disease, and congenital heart defects. Each type has its own unique pathophysiology and clinical presentation.']),
   (r'.pathophysiology of heart disease.', ['The pathophysiology of heart disease involves processes such as atherosclerosis, myocardial ischemia, myocardial infarction, cardiac remodeling, and impaired cardiac function. Understanding these mechanisms is essential for effective diagnosis and treatment.']),
   
   # Risk Factors and Genetics
   (r'.major risk factors for heart disease/?', ['Major risk factors for heart disease include hypertension, dyslipidemia, diabetes mellitus, smoking, obesity, sedentary lifestyle, and family history.']),
   (r'.role of genetics in heart disease/?', ['Genetic factors can predispose individuals to heart disease, influencing susceptibility, disease progression, and response to treatment. Familial predisposition and genetic testing can help identify individuals at higher risk.']),
   
   # Symptoms and Diagnosis
   (r'.typical symptoms of heart disease/?', ['Typical symptoms of heart disease include chest pain, shortness of breath, fatigue, palpitations, dizziness, and swelling in the legs. However, atypical symptoms, especially in women and older adults, may also occur.']),
   (r'.diagnosis of heart disease/?', ['The diagnosis of heart disease involves a combination of patient history, physical examination, diagnostic tests (e.g., electrocardiogram, echocardiogram, stress test, cardiac catheterization), and laboratory investigations (e.g., lipid profile, cardiac enzymes).']),
   
   # Treatment and Management
   (r'.principles of treatment for heart disease/?', ['Treatment for heart disease aims to control symptoms, prevent complications, improve quality of life, and reduce mortality. It may include lifestyle modifications, medications, interventional procedures, and surgical interventions.']),
   (r'.importance of lifestyle modifications in heart disease/?', ['Lifestyle modifications such as diet, exercise, smoking cessation, and stress management play a crucial role in the prevention and management of heart disease. They can help control risk factors and improve overall cardiovascular health.']),
   
   # Research and Advancements
   (r'.latest advancements in heart disease research/?', ['Recent advancements in heart disease research include novel therapies, precision medicine approaches, advancements in imaging technology, and insights into the role of inflammation, genetics, and environmental factors.']),
   (r'.impact of research on clinical practice in heart disease/?', ['Research findings have led to improvements in diagnostic techniques, treatment strategies, and patient outcomes in heart disease. Translation of research into clinical practice requires evidence-based guidelines and multidisciplinary collaboration.']),
   
   # Special Populations and Ethics
   (r'.manifestation of heart disease in special populations/?', ['Heart disease may manifest differently in special populations such as women, elderly individuals, racial and ethnic minorities, and individuals with comorbidities. Understanding these differences is essential for tailored management and care.']),
   (r'.ethical considerations in heart disease management/?', ['Ethical considerations in heart disease management include patient autonomy, informed consent, confidentiality, resource allocation, end-of-life care, and equitable access to healthcare. Balancing beneficence, non-maleficence, justice, and autonomy is paramount.'])
    
    
]
