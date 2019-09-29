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
            "placeholder": "Enter Title",
            "required": "",
            "autofocus": "",
        },
    )
    comp_subtitle = StringField(
        "Subtitle",
        render_kw={
            "class": "form-control",
            "placeholder": "(Optional)",
            "required": "",
            "autofocus": "",
        },
    )
    comp_range = StringField("Duration", validators=[DataRequired()], render_kw={
            "class": "form-control",
            "placeholder": "Ex: 24 July - 1 Aug. 2019",
            "required": "",
            "autofocus": "",
        },)
    comp_url = StringField("Competition Url", validators=[DataRequired(),],render_kw={
            "class": "form-control",
            "placeholder": "URL",
            "required": "",
            "autofocus": "",
        },)
    # Text Area类型，段落输入框
    comp_description = TextAreaField("Competition Description", render_kw={
            "class": "form-control",
            "placeholder": "(Optional)",
            "required": "",
            "autofocus": "",
        },)
    comp_host_name = StringField("Competition Hostname", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "Ex: Kaggle, 天池, ...",
            "required": "",
            "autofocus": "",
        },)
    comp_host_url = StringField("Competition Host Url", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "URL",
            "required": "",
            "autofocus": "",
        },)
    prize_currency = StringField("Currency Type")
    prize_amount = StringField("Prize")
    # Text Field类型，文本输入框，必须输入是"年-月-日 时:分:秒"格式的日期
    deadline = DateTimeField(
        "Entry Deadline", format="%Y-%m-%d %H:%M:%S", render_kw={
            "class": "form-control",
            "placeholder": "Ex: %s" % datetime.datetime.today().strftime(format="%Y-%m-%d %H:%M:%S"),
            "required": "",
            "autofocus": "",
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
        "Competition Scenario",
        choices=[
            ("DM", "Data Mining"),
            ("CV", "Computer Vision"),
            ("NLP", "Natural Language Processing"),
            ("SP", "Speech/Signal Proccessing"),
        ],
        validators=[DataRequired()],
    )
    # comp_scenario  = BooleanField('Competition Scenario', default='checked',
    #                             validators=[DataRequired()])
    data_feature = StringField("Data Feature", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Competition Updating Form
class CompetitionUpdateForm(FlaskForm):
    # Text Field类型，文本输入框，必填
    comp_title = StringField(
        "Competition Title",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter Title",
            "required": "",
            "autofocus": "",
        },
    )
    comp_subtitle = StringField(
        "Subtitle",
        render_kw={
            "class": "form-control",
            "placeholder": "(Optional)",
            "required": "",
            "autofocus": "",
        },
    )
    comp_range = StringField("Duration", validators=[DataRequired()], render_kw={
            "class": "form-control",
            "placeholder": "Ex: 24 July - 1 Aug. 2019",
            "required": "",
            "autofocus": "",
        },)
    comp_url = StringField("Competition Url", validators=[DataRequired(),],render_kw={
            "class": "form-control",
            "placeholder": "URL",
            "required": "",
            "autofocus": "",
        },)
    # Text Area类型，段落输入框
    comp_description = TextAreaField("Competition Description", render_kw={
            "class": "form-control",
            "placeholder": "(Optional)",
            "required": "",
            "autofocus": "",
        },)
    comp_host_name = StringField("Competition Hostname", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "Ex: Kaggle, 天池, ...",
            "required": "",
            "autofocus": "",
        },)
    comp_host_url = StringField("Competition Host Url", validators=[DataRequired()],render_kw={
            "class": "form-control",
            "placeholder": "URL",
            "required": "",
            "autofocus": "",
        },)
    prize_currency = StringField("Currency Type")
    prize_amount = StringField("Prize")
    # Text Field类型，文本输入框，必须输入是"年-月-日 时:分:秒"格式的日期
    deadline = DateTimeField(
        "Entry Deadline", format="%Y-%m-%d %H:%M:%S", render_kw={
            "class": "form-control",
            "placeholder": "Ex: %s" % datetime.datetime.today().strftime(format="%Y-%m-%d %H:%M:%S"),
            "required": "",
            "autofocus": "",
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
        "Competition Scenario",
        choices=[
            ("DM", "Data Mining"),
            ("CV", "Computer Vision"),
            ("NLP", "Natural Language Processing"),
            ("SP", "Speech/Signal Proccessing"),
        ],
        validators=[DataRequired()],
    )
    # comp_scenario  = BooleanField('Competition Scenario', default='checked',
    #                             validators=[DataRequired()])
    data_feature = StringField("Data Feature", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Competition Deleting Form
class CompetitionDeleteForm(FlaskForm):
    verification = SubmitField("DELETE Anyway")
