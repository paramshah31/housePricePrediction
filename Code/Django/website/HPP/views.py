from django.shortcuts import render
import pandas as pd
import pickle


# Create your views here.
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

    print(location, "\n")
    print(sqft, "\n")
    print(bath, "\n")
    print(bhk, "\n")

    prediction = model.predict(pd.DataFrame([[location, bhk, sqft, bath]], columns=["location", "size_BHK", "total_sqft", "bathroom"]))
    print(prediction, "rupees")

    return render(request, "result.html", {'ans': prediction[0]})



