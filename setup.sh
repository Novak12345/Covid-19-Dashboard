mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor="#0013ff"\n\
backgroundColor="#040404"\n\
secondaryBackgroundColor="#696973"\n\
textColor="#ffffff"\n\
\n\" > ~/.streamlit/config.toml

echo"\
.mapbox_token="pk.eyJ1Ijoibm92YWsxMjMiLCJhIjoiY2tyaXkyZ21uMzhlNjJ1cDh2Y3BlMzdtbiJ9.dI6MTui4cz64pmmrliGdyA"
">~/.streamli/secrets.toml
