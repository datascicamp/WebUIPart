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
            "data-adg-tooltip-simple": "A qualifying subtitle (optional) is used as an</br>additional and supplementary examination.<br><img src='/static/img/Subtitle.png' >",
            "placeholder": "Predict survival on the Titanic and get familiar with ML basics",
            "required": "",
            "autofocus": "",
        },
    )
    comp_range = StringField("Duration", validators=[DataRequired()], render_kw={
            "class": "form-control",
            "data-adg-tooltip-simple": "Specify the time periods as you want it to be! Eg: <br><span class='text-muted'>Now - 30 September, 2018<br>Oct. 1, 2019 - Never<br>Oct 13th, 2019 - maybe Feb, 2020</span><br><img src='/static/img/Duration.png'>",
            "placeholder": "24 July - 1 Aug. 2019",
            "required": "",
            "autofocus": "",
        },)
    comp_url = StringField("Competition Url", validators=[DataRequired(),],render_kw={
            "class": "form-control",
            "data-adg-tooltip-simple": 'The complete URL of the competition. <span class="text-muted">The URL<br>must include the protocol (<code>http://</code> or <code>https://</code>)<br>to be processed correctly.<br><img src="/static/img/URL.png"></span>',
            "placeholder": "https://www.kaggle.com/c/titanic",
            "required": "",
            "autofocus": "",
        },)
    # Text Area类型，段落输入框
    comp_description = TextAreaField("Competition Description (optional)", render_kw={
            "class": "form-control",
            "data-adg-tooltip-simple":'In one or two paragraphs, describe what the task will achieve<br>and describe the data as simply as possible while still<br>capturing their important features.',
            "placeholder": "In this competition, you’ll gain access to two similar datasets that include passenger information like name, age, gender, socio-economic class, etc. Using the patterns you find in the dataset, predict whether the other 418 passengers on board survived.",
            "required": "",
            "autofocus": "",
            "rows": 3, 
            "cols": 5,
        },)
    comp_host_name = StringField("Competition Hostname", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "Kaggle",
            "style": 'width: 80%;display: inline',
            "required": "",
            "autofocus": "",
        },)
    comp_host_url = StringField("Competition Host Url", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "https://www.kaggle.com",
            "style": 'width: 80%;display: inline',
            "required": "",
            "autofocus": "",
        },)
    prize_currency = StringField("Prize Type (optional)", render_kw={
            "class": "form-control",
            "placeholder": "Prize_block2",#,"USD / RMB / Swag / ...",
            "style": 'width: 30%;display: inline',       
            "data-adg-tooltip-simple": 'If no prize at all, just leave them empty.<br>Eg: <span class="text-muted"><u>10,000</u> <u>USD</u></span> or <span class="text-muted"><u>Kaggle</u> <u>Swag</u></span><br>Eg: <span class="text-muted"><u>20万</u> <u>RMB</u></span> or <span class="text-muted"><u>Nvidia GTX 1080ti</u> <u>x 4</u></span><br><img src="/static/img/Prize.png">',     
            "required": "",
            "autofocus": "",
        },)
    prize_amount = StringField("Prize (optional)", render_kw={
            "class": "form-control",
            "placeholder": "Prize_block1",#,"10,000,000 / Nvidia GTX 1080ti x 4 / 2 resea. fellowships up to 12 months / ...",
            "style": 'width: 30%;display: inline',
            "data-adg-tooltip-simple": 'If no prize at all, just leave them empty.<br>Eg: <span class="text-muted"><u>10,000</u> <u>USD</u></span> or <span class="text-muted"><u>Kaggle</u> <u>Swag</u></span><br>Eg: <span class="text-muted"><u>20万</u> <u>RMB</u></span> or <span class="text-muted"><u>Nvidia GTX 1080ti</u> <u>x 4</u></span><br><img src="/static/img/Prize.png">',     
            "required": "",
            "autofocus": "",
        },)
    # Text Field类型，文本输入框，必须输入是"年-月-日 时:分:秒"格式的日期
    deadline = DateTimeField(
        "Entry Deadline", format="%Y-%m-%d %H:%M:%S", validators=[DataRequired()],
        render_kw={
            "class": "form-control js-inline-picker",
            "placeholder": "%s" % (datetime.datetime.today().strftime(format="%Y-%m-%d")+" 23:59:59"),
            "required": "",
            "style": 'width: 18%;display: inline',
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
        render_kw={
            "style": 'height: 37px;display: inline',
        },
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
            "style": "height: 100px;width: 50%;",
            "data-adg-tooltip-simple": """<b>Data Mining</b>(DM): Usually Structured data or tabular/spreadsheet, with columns and rows that clearly define its attributes.<br>
                                          <b>Computer Vision</b>(CV): Including image/video processing with matrix/arrays as data structures.<br>
                                          <b>Natural Language Processing</b>(NLP): Usually natural language-based data like text/speech or word lattices.<br>
                                          <b>Speech/Signal Proccessing</b>(SP): Specifically, 1-dim non-structured data like signal/music/sound, and even symbolic logic-based data.<br>
                                          <b>Reinforcement Learning/Robotics</b>(RL): Using the concepts of agents or environments.""",
            },
        validators=[DataRequired()],
    )
    data_feature = SelectMultipleField(
        "Data Feature (multiple choices)", 
        choices=[
            ("Structured", "Structured"),
            ("Non-structured", "Non-structured"),
            ("Semi-supervised", "Semi-supervised"),
            ("Supervised", "Supervised"),
            ("Geographic", "Geographic"),
            ("Time-series", "Time-series"),
            ("Natural language-based", "Natural language-based"),
        ],
        render_kw={
            "multiple": "multiple",
            "style": "height: 140px;width: 50%;",     
            },               
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
            "data-adg-tooltip-simple": "A qualifying subtitle (optional) is used as an</br>additional and supplementary examination.<br><img src='/static/img/Subtitle.png' >",
            "placeholder": "Predict survival on the Titanic and get familiar with ML basics",
            "required": "",
            "autofocus": "",
        },
    )
    comp_range = StringField("Duration", validators=[DataRequired()], render_kw={
            "class": "form-control",
            "data-adg-tooltip-simple": "Specify the time periods as you want it to be! Eg: <br><span class='text-muted'>Now - 30 September, 2018<br>Oct. 1, 2019 - Never<br>Oct 13th, 2019 - maybe Feb, 2020</span><br><img src='/static/img/Duration.png'>",
            "placeholder": "24 July - 1 Aug. 2019",
            "required": "",
            "autofocus": "",
        },)
    comp_url = StringField("Competition Url", validators=[DataRequired(),],render_kw={
            "class": "form-control",
            "data-adg-tooltip-simple": 'The complete URL of the competition. <span class="text-muted">The URL<br>must include the protocol (<code>http://</code> or <code>https://</code>)<br>to be processed correctly.<br><img src="/static/img/URL.png"></span>',
            "placeholder": "https://www.kaggle.com/c/titanic",
            "required": "",
            "autofocus": "",
        },)
    # Text Area类型，段落输入框
    comp_description = TextAreaField("Competition Description (optional)", render_kw={
            "class": "form-control",
            "data-adg-tooltip-simple":'In one or two paragraphs, describe what the task will achieve<br>and describe the data as simply as possible while still<br>capturing their important features.',
            "placeholder": "In this competition, you’ll gain access to two similar datasets that include passenger information like name, age, gender, socio-economic class, etc. Using the patterns you find in the dataset, predict whether the other 418 passengers on board survived.",
            "required": "",
            "autofocus": "",
            "rows": 3, 
            "cols": 5,
        },)
    comp_host_name = StringField("Competition Hostname", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "Kaggle",
            "style": 'width: 80%;display: inline',
            "required": "",
            "autofocus": "",
        },)
    comp_host_url = StringField("Competition Host Url", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "https://www.kaggle.com",
            "style": 'width: 80%;display: inline',
            "required": "",
            "autofocus": "",
        },)
    prize_currency = StringField("Prize Type (optional)", render_kw={
            "class": "form-control",
            "placeholder": "Prize_block2",#,"USD / RMB / Swag / ...",
            "style": 'width: 30%;display: inline',       
            "data-adg-tooltip-simple": 'If no prize at all, just leave them empty.<br>Eg: <span class="text-muted"><u>10,000</u> <u>USD</u></span> or <span class="text-muted"><u>Kaggle</u> <u>Swag</u></span><br>Eg: <span class="text-muted"><u>20万</u> <u>RMB</u></span> or <span class="text-muted"><u>Nvidia GTX 1080ti</u> <u>x 4</u></span><br><img src="/static/img/Prize.png">',     
            "required": "",
            "autofocus": "",
        },)
    prize_amount = StringField("Prize (optional)", render_kw={
            "class": "form-control",
            "placeholder": "Prize_block1",#,"10,000,000 / Nvidia GTX 1080ti x 4 / 2 resea. fellowships up to 12 months / ...",
            "style": 'width: 30%;display: inline',
            "data-adg-tooltip-simple": 'If no prize at all, just leave them empty.<br>Eg: <span class="text-muted"><u>10,000</u> <u>USD</u></span> or <span class="text-muted"><u>Kaggle</u> <u>Swag</u></span><br>Eg: <span class="text-muted"><u>20万</u> <u>RMB</u></span> or <span class="text-muted"><u>Nvidia GTX 1080ti</u> <u>x 4</u></span><br><img src="/static/img/Prize.png">',     
            "required": "",
            "autofocus": "",
        },)
    # Text Field类型，文本输入框，必须输入是"年-月-日 时:分:秒"格式的日期
    deadline = DateTimeField(
        "Entry Deadline", format="%Y-%m-%d %H:%M:%S", validators=[DataRequired()],
        render_kw={
            "class": "form-control js-inline-picker",
            "placeholder": "%s" % (datetime.datetime.today().strftime(format="%Y-%m-%d")+" 23:59:59"),
            "required": "",
            "style": 'width: 18%;display: inline',
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
        render_kw={
            "style": 'height: 37px;display: inline',
        },
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
            "style": "height: 100px;width: 50%;",
            "data-adg-tooltip-simple": """<b>Data Mining</b>(DM): Usually Structured data or tabular/spreadsheet, with columns and rows that clearly define its attributes.<br>
                                          <b>Computer Vision</b>(CV): Including image/video processing with matrix/arrays as data structures.<br>
                                          <b>Natural Language Processing</b>(NLP): Usually natural language-based data like text/speech or word lattices.<br>
                                          <b>Speech/Signal Proccessing</b>(SP): Specifically, 1-dim non-structured data like signal/music/sound, and even symbolic logic-based data.<br>
                                          <b>Reinforcement Learning/Robotics</b>(RL): Using the concepts of agents or environments.""",
            },
        validators=[DataRequired()],
    )
    data_feature = SelectMultipleField(
        "Data Feature (multiple choices)", 
        choices=[
            ("Structured", "Structured"),
            ("Non-structured", "Non-structured"),
            ("Semi-supervised", "Semi-supervised"),
            ("Supervised", "Supervised"),
            ("Geographic", "Geographic"),
            ("Time-series", "Time-series"),
            ("Natural language-based", "Natural language-based"),
        ],
        render_kw={
            "multiple": "multiple",
            "style": "height: 140px;width: 50%;",     
            },               
        validators=[DataRequired()])
    submit = SubmitField("Submit")


# Competition Deleting Form
class CompetitionDeleteForm(FlaskForm):
    verification = SubmitField("DELETE Anyway")
