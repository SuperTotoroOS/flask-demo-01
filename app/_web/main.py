from app._models.gift import Gift
from app._view_models.book import BookViewModel
from app.web.fisher import web
from flask import render_template
from flask_login import login_required, current_user


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
@login_required
def personal_center():
    return render_template('personal.html', user=current_user.summary)
