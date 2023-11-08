import json
from flask import Blueprint, render_template, session, redirect, url_for

planing = Blueprint('planing', __name__)

@planing.route('/planing')
def planing_page():
    if 'email' not in session:
        return redirect(url_for('auth.login'))

    # Load marketing data
    with open('marketing-data.json', 'r', encoding='utf-8') as file:
        events = json.load(file)

    # Mapping eventType from the JSON to colors.
    event_type_to_color = {
        "Nasjonal": "#EDB7ED",
        "Religiøs": "#8DDFCB",
        "Festlig": "#82A0D8",
        "Annet": "#ECEE81"
    }

    # Adding the color to each event
    for event in events:
        event['color'] = event_type_to_color.get(event['eventType'], '#ECEE81')

    expiring_soon_count = 0
    return render_template('planing.html', events=events, expiring_soon_count=expiring_soon_count)
