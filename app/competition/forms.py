from flask_wtf import FlaskForm
import datetime

from wtforms import (
    StringField,
    SubmitField,
    SelectField,
    SelectMultipleField,
    TextAreaField,
    BooleanField,
    DateTimeField,
    DateField,
)
from wtforms.validators import DataRequired, EqualTo, Email, URL


# Competition Inserting Form
class CompetitionInsertForm(FlaskForm):
    # Text Field类型，文本输入框，必填
    comp_title = StringField(
        "Competition Title",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": 'Titanic: Machine Learning from Disaster',
            "required": "",
            "autofocus": "",
        },
    )
    comp_subtitle = StringField(
        "Subtitle (optional)",
        render_kw={
            "class": "form-control",
            "placeholder": "Start here! Predict survival on the Titanic and get familiar with ML basics",
            "required": "",
            "autofocus": "",
        },
    )
    comp_range = StringField("Duration", validators=[DataRequired()], render_kw={
            "class": "form-control",
            "placeholder": "24 July - 1 Aug. 2019",
            "required": "",
            "autofocus": "",
        },)
    comp_url = StringField("Competition Url", validators=[DataRequired(),],render_kw={
            "class": "form-control",
            "placeholder": "https://www.kaggle.com/c/titanic",
            "required": "",
            "autofocus": "",
        },)
    # Text Area类型，段落输入框
    comp_description = TextAreaField("Competition Description (optional)", render_kw={
            "class": "form-control",
            "placeholder": "In this competition, you’ll gain access to two similar datasets that include passenger information like name, age, gender, socio-economic class, etc. One dataset is titled `train.csv` and the other is titled `test.csv`. \nUsing the patterns you find in the train.csv data, predict whether the other 418 passengers on board (found in test.csv) survived. ",
            "required": "",
            "autofocus": "",
            "rows": 3, 
            "cols": 5,
        },)
    comp_host_name = StringField("Competition Hostname", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "Kaggle",
            "required": "",
            "autofocus": "",
        },)
    comp_host_url = StringField("Competition Host Url", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "https://www.kaggle.com",
            "required": "",
            "autofocus": "",
        },)
    prize_currency = StringField("Prize Type (optional)", render_kw={
            "class": "form-control",
            "placeholder": "USD / RMB / Swag / ...",
            "required": "",
            "autofocus": "",
        },)
    prize_amount = StringField("Prize (optional)", render_kw={
            "class": "form-control",
            "placeholder": "10,000,000 / Nvidia GTX 1080ti x 4 / 2 resea. fellowships up to 12 months / ...",
            "required": "",
            "autofocus": "",
        },)
    # Text Field类型，文本输入框，必须输入是"年-月-日 时:分:秒"格式的日期
    deadline = DateTimeField(
        "Entry Deadline", format="%Y-%m-%d %H:%M:%S", render_kw={
            "class": "form-control js-inline-picker",
            "placeholder": "%s" % (datetime.datetime.today().strftime(format="%Y-%m-%d")+" 23:59:59"),
            "required": "",
            "autofocus": "",
            "value": "%s" % (datetime.datetime.today().strftime(format="%Y-%m-%d")+" 23:59:59"),
        },
    )
    timezone = SelectField(
        "Timezone",
        choices=[
            ("UTC", "UTC"),
            ("Asia/Shanghai", "Asia/Shanghai"),
        ],
        validators=[DataRequired()],
    )
    comp_scenario = SelectMultipleField(
        "Competition Scenario (multiple choices)",
        choices=[
            ("DM", "Data Mining"),
            ("CV", "Computer Vision"),
            ("NLP", "Natural Language Processing"),
            ("SP", "Speech/Signal Proccessing"),
            ("RL", "Reinforcement Learning/Robotics"),
        ], 	
        description = "多选",
        render_kw={
            "multiple": "multiple",
            "style": "height: 100px;"
            },
        validators=[DataRequired()],
    )
    data_feature = SelectMultipleField(
        "Data Feature (multiple choices)", 
        choices=[
            ("Structured data", "Structured data"),
            ("1-dim non-structured data", "1-dim non-structured data"),
            ("2-dim non-structured data", "2-dim non-structured data"),
            ("3-dim non-structured data", "3-dim non-structured data"),
        ], 	        
        validators=[DataRequired()])
    submit = SubmitField("Submit")


# Competition Updating Form
class CompetitionUpdateForm(FlaskForm):
    # Text Field类型，文本输入框，必填
    comp_title = StringField(
        "Competition Title",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": 'Titanic: Machine Learning from Disaster',
            "required": "",
            "autofocus": "",
        },
    )
    comp_subtitle = StringField(
        "Subtitle (optional)",
        render_kw={
            "class": "form-control",
            "placeholder": "Start here! Predict survival on the Titanic and get familiar with ML basics",
            "required": "",
            "autofocus": "",
        },
    )
    comp_range = StringField("Duration", validators=[DataRequired()], render_kw={
            "class": "form-control",
            "placeholder": "24 July - 1 Aug. 2019",
            "required": "",
            "autofocus": "",
        },)
    comp_url = StringField("Competition Url", validators=[DataRequired(),],render_kw={
            "class": "form-control",
            "placeholder": "https://www.kaggle.com/c/titanic",
            "required": "",
            "autofocus": "",
        },)
    # Text Area类型，段落输入框
    comp_description = TextAreaField("Competition Description (optional)", render_kw={
            "class": "form-control",
            "placeholder": "In this competition, you’ll gain access to two similar datasets that include passenger information like name, age, gender, socio-economic class, etc. One dataset is titled `train.csv` and the other is titled `test.csv`. \nUsing the patterns you find in the train.csv data, predict whether the other 418 passengers on board (found in test.csv) survived. ",
            "required": "",
            "autofocus": "",
            "rows": 3, 
            "cols": 5,
        },)
    comp_host_name = StringField("Competition Hostname", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "Kaggle",
            "required": "",
            "autofocus": "",
        },)
    comp_host_url = StringField("Competition Host Url", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "https://www.kaggle.com",
            "required": "",
            "autofocus": "",
        },)
    prize_currency = StringField("Prize Type (optional)", render_kw={
            "class": "form-control",
            "placeholder": "USD / RMB / Swag / ...",
            "required": "",
            "autofocus": "",
        },)
    prize_amount = StringField("Prize (optional)", render_kw={
            "class": "form-control",
            "placeholder": "10,000,000 / Nvidia GTX 1080ti x 4 / 2 resea. fellowships up to 12 months / ...",
            "required": "",
            "autofocus": "",
        },)
    # Text Field类型，文本输入框，必须输入是"年-月-日 时:分:秒"格式的日期
    deadline = DateTimeField(
        "Entry Deadline", format="%Y-%m-%d %H:%M:%S", render_kw={
            "class": "form-control js-inline-picker",
            "placeholder": "%s" % (datetime.datetime.today().strftime(format="%Y-%m-%d")+" 23:59:59"),
            "required": "",
            "autofocus": "",
            "value": "%s" % (datetime.datetime.today().strftime(format="%Y-%m-%d")+" 23:59:59"),
        },
    )
    timezone = SelectField(
        "Timezone",
        choices=[
            ("UTC", "UTC"),
            ("Asia/Shanghai", "Asia/Shanghai"),
        ],
        validators=[DataRequired()],
    )
    comp_scenario = SelectMultipleField(
        "Competition Scenario (multiple choices)",
        choices=[
            ("DM", "Data Mining"),
            ("CV", "Computer Vision"),
            ("NLP", "Natural Language Processing"),
            ("SP", "Speech/Signal Proccessing"),
            ("RL", "Reinforcement Learning/Robotics"),
        ], 	
        description = "多选",
        render_kw={
            "multiple": "multiple",
            "style": "height: 100px;"
            },
        validators=[DataRequired()],
    )
    data_feature = SelectMultipleField(
        "Data Feature (multiple choices)", 
        choices=[
            ("Structured data", "Structured data"),
            ("1-dim non-structured data", "1-dim non-structured data"),
            ("2-dim non-structured data", "2-dim non-structured data"),
            ("3-dim non-structured data", "3-dim non-structured data"),
        ], 	        
        validators=[DataRequired()])
    submit = SubmitField("Submit")


# Competition Deleting Form
class CompetitionDeleteForm(FlaskForm):
    verification = SubmitField("DELETE Anyway")
