import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from main import predictDisease # import the function from main.py

# initialize Tkinter
root = tk.Tk()
root.title("Disease Predictor")

# function to handle prediction
def predict_symptoms():
    symptoms = entry_symptoms.get()
    if symptoms.strip() == "":
        messagebox.showerror("Error", "Please enter symptoms.")
        return
    
    try:
        predictions = predictDisease(symptoms)
        rf_prediction = predictions["rf_model_prediction"]
        nb_prediction = predictions["naive_bayes_prediction"]
        svm_prediction = predictions["svm_model_prediction"]
        final_prediction = predictions["final_prediction"]
        
        result_text = f"Random Forest Prediction: {rf_prediction}\n"
        result_text += f"Naive Bayes Prediction: {nb_prediction}\n"
        result_text += f"SVM Prediction: {svm_prediction}\n"
        result_text += f"Final Prediction: {final_prediction}"
        
        label_result.config(text=result_text)
        
    except KeyError:
        messagebox.showerror("Error", "Invalid symptom entered.")
