from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("airplane_dataset_200_entries.csv")

def get_plane_info(user_query):
    user_query = user_query.lower()
    for _, row in df.iterrows():
        if row["Model"].lower() in user_query:
            return (
                f"<b>✈️ Plane Information:</b><br>"
                f"<b>Model:</b> {row['Model']}<br>"
                f"<b>Manufacturer:</b> {row['Manufacturer']}<br>"
                f"<b>Type:</b> {row['Type']}<br>"
                f"<b>Max Speed:</b> {row['Max Speed (km/h)']} km/h<br>"
                f"<b>Range:</b> {row['Range (km)']} km<br>"
                f"<b>Wingspan:</b> {row['Wingspan (m)']} m<br>"
                f"<b>First Flight:</b> {row['First Flight']}"
            )
    return "❌ Sorry, I couldn't find any plane matching your query."

@app.route("/", methods = ['GET', 'POST'])

def home():
    response = ''
    if request.method == 'POST':
        user_input = request.form['query']
        response = get_plane_info(user_input)
    return render_template('index.html', response = response)

if __name__ == "__main__":
    app.run(debug = True)