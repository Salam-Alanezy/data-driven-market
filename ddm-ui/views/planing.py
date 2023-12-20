import json
from flask import Blueprint, render_template, session, redirect, url_for
from datetime import datetime

planing = Blueprint('planing', __name__)

@planing.route('/planing')
def planing_page():
    if 'email' not in session:
        return redirect(url_for('auth.login'))

    # Load marketing data
    with open('updated_marketing-data.json', 'r', encoding='utf-8') as file:
        events = json.load(file)

    # Mapping eventType from the JSON to colors.
    event_type_to_color = {
        "Nasjonal": "#EDB7ED",
        "Religiøs": "#8DDFCB",
        "Festlig": "#82A0D8",
        "Annet": "#ECEE81"
    }

    # Adding the color to each event and converting date strings to datetime objects
    for event in events:
        event['color'] = event_type_to_color.get(event['eventType'], '#ECEE81')
        event['date'] = datetime.strptime(event['date'], '%Y-%m-%d')

    # Sort events by date and select the 9 nearest events
    events.sort(key=lambda x: x['date'])
    events = events[:9]

    expiring_soon_count = 0
    return render_template('planing.html', events=events, expiring_soon_count=expiring_soon_count)
