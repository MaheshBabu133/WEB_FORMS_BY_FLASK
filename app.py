from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
FAI=Flask(__name__)


@FAI.route('/WebForm',methods=['GET','POST'])
def WebForm():
    NFO=NameForm()
    if request.method=="POST":
        NFO=NameForm(request.form)
        if NFO.validate():
            return NFO.sname.data

    return render_template('WebForm.html',NFO=NFO)


class NameForm(Form):
    sname=StringField(validators=[DataRequired()])
    submit=SubmitField()




if __name__=="__main__":
    FAI.run(debug=True)