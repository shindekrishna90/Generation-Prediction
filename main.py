from flask import Flask,render_template,request,redirect,url_for
import pickle
import numpy as np

model=pickle.load(open('model_master.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST','GET'])
def predict():


    data=np.zeros(8)
    data[0]=int(request.form.get('year'))
    data[1]=int(request.form.get('sex'))
    data[2]=int(request.form.get('age'))
    data[3]=int(request.form.get('suicides_no'))
    data[4]=int(request.form.get('population'))
    data[7]=int(request.form.get('gdp_per_capita'))
    data[5]=int(request.form.get('gdp_for_year'))
    data[6]=float(request.form.get('suicide_rate'))


    pred=model.predict(data.reshape(1,8))
    out=['Boomers', 'G.I. Generation', 'Generation X', 'Generation Z','Millenials', 'Silent']

    if pred==0:
        return f'<html><center><h2> The Predicted Generation Is "{out[0]}"</h2></center></html>'
    elif pred==1:
        return f'<html><center><h2> The Predicted Generation Is "{out[1]}"</h2></center></html>'    
    elif pred==2:
        return f'<html><center><h2> The Predicted Generation Is "{out[2]}"</h2></center></html>'    
    elif pred==3:
        return f'<html><center><h2> The Predicted Generation Is "{out[3]}"</h2></center></html>'    
    elif pred==4:
        return f'<html><center><h2> The Predicted Generation Is "{out[4]}"</h2></center></html>'    
    elif pred==5:
        return f'<html><center><h2> The Predicted Generation Is "{out[5]}"</h2></center></html>'
    
if __name__ =='__main__':
    app.run(debug=True) 