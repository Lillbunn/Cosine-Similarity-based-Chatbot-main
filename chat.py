from db_call import QASystem
#import pandas as pd
import csv

def chatbot(input):
    # First try to get a response from the QASystem
    # Initialize the QASystem
    qa = QASystem('test.csv')
    try:
        qa_response = qa.get_response(input)
        print("Try")

    except Exception as e:
        qa_response = "I can't answer this question."
        print("Exception:", e)

        # Save the question and the AI's response to the CSV file
        openingfile = open('save.csv','w', newline='')
        w = csv.writer(openingfile)
        w.writerow([input, qa_response])


        # Save the question and the AI's response to the CSV file
        #df = pd.DataFrame([[input]], columns=['Questions'])
        #df.to_csv('test1.csv', mode='a', header=False, index=False)
        
    return qa_response
