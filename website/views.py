from datetime import time

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
import os

from .ut import get_veggie, get_details

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        img = request.files.get('photo')  # 从post请求中获取图片数据
        img = img.stream.read()

        veggie = get_veggie(img)
        if veggie is not None:
            nourishment, effect, attention = get_details(veggie)
            return render_template('info.html', veggie=veggie, user=current_user, nourishment=nourishment,
                                   effect=effect, attention=attention)

    return render_template("home.html", user=current_user)

