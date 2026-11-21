# Monthly Electricity Calculator (Python)

A simple Streamlit web app for sharing one monthly electricity bill:
- General household electricity is split 50/50.
- Estimated washer + dryer electricity is split by laundry hours.
- Five monthly inputs; no accounts, database, or stored bills.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publish on Streamlit Community Cloud for free

1. Create a public repository on GitHub.
2. Upload `app.py` and `requirements.txt` to the root of the repository.
3. Sign in to https://share.streamlit.io using GitHub.
4. Create a new app from your GitHub repository, using `app.py` as the main file.
5. Share your generated `*.streamlit.app` address.

Streamlit Community Cloud is free under its current terms, with resource and inactivity limitations. It may put unused apps to sleep; visitors can wake them by opening the link.

### Sample

- Total 406 kWh, $155.99
- Combined power 7.44 kW
- Me 11 hours, You 20 hours
- Laundry 230.64 kWh; household 175.36 kWh
- Me $65.13; You $90.86

The usage model assumes the dryer and washer draw their rated combined power for every counted hour; actual measured usage can differ.
