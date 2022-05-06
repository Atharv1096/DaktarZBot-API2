from tkinter import *
from tkinter import ttk
from PIL import ImageTk,ImageTk

root =Tk()
root.title('Daktarz - The Healthcare Platform')
root.iconbitmap('D:/Daktarz/pp.ico')
root.geometry("500x500")

#Dropdown menu
def show():
    if (str(clicked.get()) == "Default") or (str(clicked2.get()) == "Default") or (str(clicked3.get()) == "Default"):
        label.config( text='You must choose first three symptoms')
    else:
        if str(clicked4.get()) == "Default" and str(clicked5.get()) == "Default":
            label.config( text='"'+str(clicked.get())+','+str(clicked2.get())+','+str(clicked3.get())+'"')
        elif str(clicked4.get()) == "Default":
            label.config( text='"'+str(clicked.get())+','+str(clicked2.get())+','+str(clicked3.get())+str(clicked5.get())+'"')
        elif str(clicked5.get()) == "Default":
            label.config( text='"'+str(clicked.get())+','+str(clicked2.get())+','+str(clicked3.get())+','+str(clicked4.get())+'"')
        else:
             label.config( text='"'+str(clicked.get())+','+str(clicked2.get())+','+str(clicked3.get())+','+str(clicked4.get())+','+str(clicked5.get())+'"')

clicked = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()

clicked.set("Default")
clicked2.set("Default")
clicked3.set("Default")
clicked4.set("Default")
clicked5.set("Default")

drop = OptionMenu(root, clicked, "Itching","Skin Rash","Nodal Skin Eruptions","Continuous Sneezing","Shivering","Chills","Joint Pain","Upper Abdomen Pain","Acidity","Ulcers On Toungue","Muscle Wasting","Vomiting","Burning Micturition","Fatigue","Weight Gain","Anxiety","Cold Hands And Feets","Mood Swings","Weight Loss","Restlessness","Lethargy","Sore Throat","Irregular Sugar Level","Coungh","High Fever","Sunken Eyes","Breathlessness","Sweating","Dehydration","Indigestion","Headache",
                                 "Yellowish Skin","Dark Urine","Nausea","Loss Of Appetite","Pain Behind The Eyes","Back Pain","Constipation","Abdominal Pain","Diarrhoea","Mild Fever","Yellow Urine","Yellowing Of Eyes","Acute Liver Failure","Fluid Overload","Enlarged Lymph Nodes","Malaise","Blurred And Distorted Vision","Sputum In Cough","Throat Irritation","Redness Of Eyes","Runny Nose","Congestion","chest Pain","Weakness in Limbs","Fast Heart Rate","Pain In Abdomen",
                                 "Pain While Passing Stools","Bloody Stool","Itching In Perineal Region","Neck Pain","Dizziness","Cramps","Bruising","Obesity","Swollen Legs","Swollen Blood Vessels","Puffy Face And Eyes","Enlarged Thyroid","Brittle Nails","Swollen Extremeties","Excessive Hunger","Extra Marital Contacts","Dying And Tingling Lips","Slurred Speech","Knee Pain","Hip Joint Pain","Muscle Weakness","Stiff Neck","Swelling Joints","Movement Stiffness","Spining Movements",
                                 "Loss Of Balance","Unsteadiness","Weakness Of One Body Side","Loss Of Smell","Increase In Frequency Of Urine","Foul Smell Of Urine","Incomplete Emptying Of Urine","Passage Of Gases","Internal Itching","Toxic Look (typhos)","Depression","Irritability","Muscle Pain","Altered Sensorium","Red Spots Over Body","Belly Pain","Abnormal Menstruation","Dischromic Patches","Watering From Eyes","Increased Appetite","Polyuria","Family History","Mucoid Sputum",
                                 "Rusty Sputum","Lack Of Concentration","Visual Disturbance","Receiving Nlood Transfusion","Injecting Drugs Using Unsterile Injection","Coma","Blood In The Vomitus","Distention Of Abdomen","History Of Alcohol Consumption","Fluid Overload","Blood In Sputum","Prominetne Veins On Calf","Palpitations","Painful Walking","Pus Filled Pimples","Blackheads","Scurring","Skin Peeling","Sliver Like Dusting","Small Dents In nails","Inflammotry Nails","Blister",
                                 "Red Sore Around Nose","Yellow Crust Ooze","White Ring Like Patches","Redness Over The Area","Swelling Over The Red Area","Pain Over Swollen Area","Reddish Dots All Over Body")


drop2=OptionMenu(root, clicked2, "Itching","Skin Rash","Nodal Skin Eruptions","Continuous Sneezing","Shivering","Chills","Joint Pain","Upper Abdomen Pain","Acidity","Ulcers On Toungue","Muscle Wasting","Vomiting","Burning Micturition","Fatigue","Weight Gain","Anxiety","Cold Hands And Feets","Mood Swings","Weight Loss","Restlessness","Lethargy","Sore Throat","Irregular Sugar Level","Coungh","High Fever","Sunken Eyes","Breathlessness","Sweating","Dehydration","Indigestion","Headache",
                                 "Yellowish Skin","Dark Urine","Nausea","Loss Of Appetite","Pain Behind The Eyes","Back Pain","Constipation","Abdominal Pain","Diarrhoea","Mild Fever","Yellow Urine","Yellowing Of Eyes","Acute Liver Failure","Fluid Overload","Enlarged Lymph Nodes","Malaise","Blurred And Distorted Vision","Sputum In Cough","Throat Irritation","Redness Of Eyes","Runny Nose","Congestion","chest Pain","Weakness in Limbs","Fast Heart Rate","Pain In Abdomen",
                                 "Pain While Passing Stools","Bloody Stool","Itching In Perineal Region","Neck Pain","Dizziness","Cramps","Bruising","Obesity","Swollen Legs","Swollen Blood Vessels","Puffy Face And Eyes","Enlarged Thyroid","Brittle Nails","Swollen Extremeties","Excessive Hunger","Extra Marital Contacts","Dying And Tingling Lips","Slurred Speech","Knee Pain","Hip Joint Pain","Muscle Weakness","Stiff Neck","Swelling Joints","Movement Stiffness","Spining Movements",
                                 "Loss Of Balance","Unsteadiness","Weakness Of One Body Side","Loss Of Smell","Increase In Frequency Of Urine","Foul Smell Of Urine","Incomplete Emptying Of Urine","Passage Of Gases","Internal Itching","Toxic Look (typhos)","Depression","Irritability","Muscle Pain","Altered Sensorium","Red Spots Over Body","Belly Pain","Abnormal Menstruation","Dischromic Patches","Watering From Eyes","Increased Appetite","Polyuria","Family History","Mucoid Sputum",
                                 "Rusty Sputum","Lack Of Concentration","Visual Disturbance","Receiving Nlood Transfusion","Injecting Drugs Using Unsterile Injection","Coma","Blood In The Vomitus","Distention Of Abdomen","History Of Alcohol Consumption","Fluid Overload","Blood In Sputum","Prominetne Veins On Calf","Palpitations","Painful Walking","Pus Filled Pimples","Blackheads","Scurring","Skin Peeling","Sliver Like Dusting","Small Dents In nails","Inflammotry Nails","Blister",
                                 "Red Sore Around Nose","Yellow Crust Ooze","White Ring Like Patches","Redness Over The Area","Swelling Over The Red Area","Pain Over Swollen Area","Reddish Dots All Over Body")

drop3=OptionMenu(root, clicked3, "Itching","Skin Rash","Nodal Skin Eruptions","Continuous Sneezing","Shivering","Chills","Joint Pain","Upper Abdomen Pain","Acidity","Ulcers On Toungue","Muscle Wasting","Vomiting","Burning Micturition","Fatigue","Weight Gain","Anxiety","Cold Hands And Feets","Mood Swings","Weight Loss","Restlessness","Lethargy","Sore Throat","Irregular Sugar Level","Coungh","High Fever","Sunken Eyes","Breathlessness","Sweating","Dehydration","Indigestion","Headache",
                                 "Yellowish Skin","Dark Urine","Nausea","Loss Of Appetite","Pain Behind The Eyes","Back Pain","Constipation","Abdominal Pain","Diarrhoea","Mild Fever","Yellow Urine","Yellowing Of Eyes","Acute Liver Failure","Fluid Overload","Enlarged Lymph Nodes","Malaise","Blurred And Distorted Vision","Sputum In Cough","Throat Irritation","Redness Of Eyes","Runny Nose","Congestion","chest Pain","Weakness in Limbs","Fast Heart Rate","Pain In Abdomen",
                                 "Pain While Passing Stools","Bloody Stool","Itching In Perineal Region","Neck Pain","Dizziness","Cramps","Bruising","Obesity","Swollen Legs","Swollen Blood Vessels","Puffy Face And Eyes","Enlarged Thyroid","Brittle Nails","Swollen Extremeties","Excessive Hunger","Extra Marital Contacts","Dying And Tingling Lips","Slurred Speech","Knee Pain","Hip Joint Pain","Muscle Weakness","Stiff Neck","Swelling Joints","Movement Stiffness","Spining Movements",
                                 "Loss Of Balance","Unsteadiness","Weakness Of One Body Side","Loss Of Smell","Increase In Frequency Of Urine","Foul Smell Of Urine","Incomplete Emptying Of Urine","Passage Of Gases","Internal Itching","Toxic Look (typhos)","Depression","Irritability","Muscle Pain","Altered Sensorium","Red Spots Over Body","Belly Pain","Abnormal Menstruation","Dischromic Patches","Watering From Eyes","Increased Appetite","Polyuria","Family History","Mucoid Sputum",
                                 "Rusty Sputum","Lack Of Concentration","Visual Disturbance","Receiving Nlood Transfusion","Injecting Drugs Using Unsterile Injection","Coma","Blood In The Vomitus","Distention Of Abdomen","History Of Alcohol Consumption","Fluid Overload","Blood In Sputum","Prominetne Veins On Calf","Palpitations","Painful Walking","Pus Filled Pimples","Blackheads","Scurring","Skin Peeling","Sliver Like Dusting","Small Dents In nails","Inflammotry Nails","Blister",
                                 "Red Sore Around Nose","Yellow Crust Ooze","White Ring Like Patches","Redness Over The Area","Swelling Over The Red Area","Pain Over Swollen Area","Reddish Dots All Over Body")

drop4=OptionMenu(root, clicked4, "Itching","Skin Rash","Nodal Skin Eruptions","Continuous Sneezing","Shivering","Chills","Joint Pain","Upper Abdomen Pain","Acidity","Ulcers On Toungue","Muscle Wasting","Vomiting","Burning Micturition","Fatigue","Weight Gain","Anxiety","Cold Hands And Feets","Mood Swings","Weight Loss","Restlessness","Lethargy","Sore Throat","Irregular Sugar Level","Coungh","High Fever","Sunken Eyes","Breathlessness","Sweating","Dehydration","Indigestion","Headache",
                                 "Yellowish Skin","Dark Urine","Nausea","Loss Of Appetite","Pain Behind The Eyes","Back Pain","Constipation","Abdominal Pain","Diarrhoea","Mild Fever","Yellow Urine","Yellowing Of Eyes","Acute Liver Failure","Fluid Overload","Enlarged Lymph Nodes","Malaise","Blurred And Distorted Vision","Sputum In Cough","Throat Irritation","Redness Of Eyes","Runny Nose","Congestion","chest Pain","Weakness in Limbs","Fast Heart Rate","Pain In Abdomen",
                                 "Pain While Passing Stools","Bloody Stool","Itching In Perineal Region","Neck Pain","Dizziness","Cramps","Bruising","Obesity","Swollen Legs","Swollen Blood Vessels","Puffy Face And Eyes","Enlarged Thyroid","Brittle Nails","Swollen Extremeties","Excessive Hunger","Extra Marital Contacts","Dying And Tingling Lips","Slurred Speech","Knee Pain","Hip Joint Pain","Muscle Weakness","Stiff Neck","Swelling Joints","Movement Stiffness","Spining Movements",
                                 "Loss Of Balance","Unsteadiness","Weakness Of One Body Side","Loss Of Smell","Increase In Frequency Of Urine","Foul Smell Of Urine","Incomplete Emptying Of Urine","Passage Of Gases","Internal Itching","Toxic Look (typhos)","Depression","Irritability","Muscle Pain","Altered Sensorium","Red Spots Over Body","Belly Pain","Abnormal Menstruation","Dischromic Patches","Watering From Eyes","Increased Appetite","Polyuria","Family History","Mucoid Sputum",
                                 "Rusty Sputum","Lack Of Concentration","Visual Disturbance","Receiving Nlood Transfusion","Injecting Drugs Using Unsterile Injection","Coma","Blood In The Vomitus","Distention Of Abdomen","History Of Alcohol Consumption","Fluid Overload","Blood In Sputum","Prominetne Veins On Calf","Palpitations","Painful Walking","Pus Filled Pimples","Blackheads","Scurring","Skin Peeling","Sliver Like Dusting","Small Dents In nails","Inflammotry Nails","Blister",
                                 "Red Sore Around Nose","Yellow Crust Ooze","White Ring Like Patches","Redness Over The Area","Swelling Over The Red Area","Pain Over Swollen Area","Reddish Dots All Over Body")

drop5=OptionMenu(root, clicked5, "Itching","Skin Rash","Nodal Skin Eruptions","Continuous Sneezing","Shivering","Chills","Joint Pain","Upper Abdomen Pain","Acidity","Ulcers On Toungue","Muscle Wasting","Vomiting","Burning Micturition","Fatigue","Weight Gain","Anxiety","Cold Hands And Feets","Mood Swings","Weight Loss","Restlessness","Lethargy","Sore Throat","Irregular Sugar Level","Coungh","High Fever","Sunken Eyes","Breathlessness","Sweating","Dehydration","Indigestion","Headache",
                                 "Yellowish Skin","Dark Urine","Nausea","Loss Of Appetite","Pain Behind The Eyes","Back Pain","Constipation","Abdominal Pain","Diarrhoea","Mild Fever","Yellow Urine","Yellowing Of Eyes","Acute Liver Failure","Fluid Overload","Enlarged Lymph Nodes","Malaise","Blurred And Distorted Vision","Sputum In Cough","Throat Irritation","Redness Of Eyes","Runny Nose","Congestion","chest Pain","Weakness in Limbs","Fast Heart Rate","Pain In Abdomen",
                                 "Pain While Passing Stools","Bloody Stool","Itching In Perineal Region","Neck Pain","Dizziness","Cramps","Bruising","Obesity","Swollen Legs","Swollen Blood Vessels","Puffy Face And Eyes","Enlarged Thyroid","Brittle Nails","Swollen Extremeties","Excessive Hunger","Extra Marital Contacts","Dying And Tingling Lips","Slurred Speech","Knee Pain","Hip Joint Pain","Muscle Weakness","Stiff Neck","Swelling Joints","Movement Stiffness","Spining Movements",
                                 "Loss Of Balance","Unsteadiness","Weakness Of One Body Side","Loss Of Smell","Increase In Frequency Of Urine","Foul Smell Of Urine","Incomplete Emptying Of Urine","Passage Of Gases","Internal Itching","Toxic Look (typhos)","Depression","Irritability","Muscle Pain","Altered Sensorium","Red Spots Over Body","Belly Pain","Abnormal Menstruation","Dischromic Patches","Watering From Eyes","Increased Appetite","Polyuria","Family History","Mucoid Sputum",
                                 "Rusty Sputum","Lack Of Concentration","Visual Disturbance","Receiving Nlood Transfusion","Injecting Drugs Using Unsterile Injection","Coma","Blood In The Vomitus","Distention Of Abdomen","History Of Alcohol Consumption","Fluid Overload","Blood In Sputum","Prominetne Veins On Calf","Palpitations","Painful Walking","Pus Filled Pimples","Blackheads","Scurring","Skin Peeling","Sliver Like Dusting","Small Dents In nails","Inflammotry Nails","Blister",
                                 "Red Sore Around Nose","Yellow Crust Ooze","White Ring Like Patches","Redness Over The Area","Swelling Over The Red Area","Pain Over Swollen Area","Reddish Dots All Over Body")

#drop2=drop2.remove(str(drop))
#drop3=drop3.remove(str(clicked2))
#drop4=drop4.remove(str(clicked3))
Label(root, text="\n\nChoose first symptom").pack()
drop.pack()
Label(root, text="\nChoose second symptom").pack()
drop2.pack()
Label(root, text="\nChoose third symptom").pack()
drop3.pack()
Label(root, text="\nChoose fourth symptom").pack()
drop4.pack()
Label(root, text="\nChoose fifth symptom").pack()
drop5.pack()
Label(root, text="\n").pack()
MyButton = Button(root, text="Show Diagnosis", command=show).pack()

label = Label( root , text = " " )
label.pack()

root.mainloop()
