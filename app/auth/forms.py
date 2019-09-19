from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, widgets
from wtforms.validators import DataRequired, EqualTo, Email


# Reset password form
class ResetPasswordForm(FlaskForm):
    new_password = PasswordField("Your new Password", validators=[DataRequired()])
    re_new_password = PasswordField(
        "Entry again", validators=[DataRequired(), EqualTo("new_password")]
    )
    submit = SubmitField("Reset")


# Reset password request form
class ResetPasswordRequestForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")


# Register request form
class RegisterRequestForm(FlaskForm):
    submit = SubmitField("Click to Verify Your Email")


# Login form
class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        widget=widgets.TextInput(),
        render_kw={
            "class": "form-control",
            "placeholder": "Enter email",
            "required": "",
            "autofocus": "",
        },
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        widget=widgets.PasswordInput(),
        render_kw={
            "class": "form-control",
            "placeholder": "Password",
            "required": "",
            "autofocus": "",
        },
    )
    captcha = StringField(
        "CAPTCHA",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "CAPTCHA",
            "required": "",
            "autofocus": "",
        },
    )
    submit = SubmitField("Login")


# Register form
class RegisterForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter your Email",
            "required": "",
            "autofocus": "",
        },
    )
    nickname = StringField(
        "Username",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter your Username",
            "required": "",
            "autofocus": "",
        },
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter your Password!",
            "required": "",
            "autofocus": "",
        },
    )
    re_password = PasswordField(
        "Confirm",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter your Password again!",
            "required": "",
            "autofocus": "",
        },
    )
    captcha = StringField(
        "CAPTCHA",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "CAPTCHA",
            "required": "",
            "autofocus": "",
        },
    )
    submit = SubmitField("Register")

