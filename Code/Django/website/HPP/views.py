from django.shortcuts import render
import pandas as pd
import pickle


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def predict_house_price(request):
    house = pd.read_csv('Bengaluru_House_Data_Cleaned.csv')
    locations = sorted(house['location'].unique())
    return render(request, 'main_input.html', {"locations": locations})


def predict_price_actual(request):
    model = pickle.load(open('BangloreHousePricePredictioModel.pkl', 'rb'))
    location = request.GET['location']
    sqft = request.GET['sqft']
    bath = request.GET['bath']
    bhk = request.GET['bhk']

    prediction = model.predict(pd.DataFrame([[location, bhk, sqft, bhk]], columns=["location", "size_BHK", "total_sqft", "bathroom"]))
    print(prediction, "rupees")

    return render(request, "result.html", {'ans': prediction[0], 'location': location, 'sqft':sqft, 'bath':bath, 'bhk':bhk})



