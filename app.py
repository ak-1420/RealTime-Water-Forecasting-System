#improt flask

from logging import debug
from flask import Flask , render_template , request
from datetime import date
import numpy as np
import joblib
import pandas as pd
import dill as pickle

#create an instance of Flask

app = Flask(__name__)


#store list of reservoirs

dams = [
 'Damanganga',
 'Doyang Hep',
 'Gumti Reservoir',
 'MayurakshiMasanjor Reservoir',
 'Kangsabati Reservoir',
 'Balimela Reservoir',
 'Sapua',
 'Upper Kolab Reservoir',
 'MachkundJalaput Reservoir',
 'Rengali Reservoir',
 'Upper Indrawati Reservoir',
 'Salandi Reservoir',
 'Hirakud Reservoir',
 'Konar Reservoir',
 'Tilaiya Reservoir',
 'Tenughat Reservoir',
 'Maithon Reservoir',
 'Panchat Reservoir',
 'Ramganga Reservoir',
 'Tehri Reservoir',
 'Sharda Sagar',
 'Rihand Reservoir',
 'Jirgo Dam',
 'Matatila Reservoir',
 'Tawa Reservoir',
 'Kolar',
 'Ban Sagar',
 'Gandhi Sagar',
 'Indira Sagar',
 'BargiRani Avanti Bai Sagar',
 'Barna',
 'Sanjay Sarovar (Upper Wainganga)',
 'Omkareshwar',
 'MahanadiRavishankar Sagar',
 'Minimata BangoiHasdeo Reservoir',
 'Dudhawa',
 'Srisailam Reservoir',
 'KANDALERU RESERVOIR',
 'LOWER SAGILERU ANI CUT',
 'YOGI VEMANA (MADDILERU) RESERVOIR',
 'BHAIRAVANITHIPPA PROJECT',
 'VARAHA RESERVOIR',
 'MUNIYERU PROJECT',
 'SRISAILAM R',
 'OWK RESERVOIR',
 'Cherlopalli Reservoir',
 'BUGGAVANKA RESERVOIR',
 'NELLORE ANICUT',
 'PENNA AHOBILAM BALANCING RESERVOIR',
 'GORAKKALU BALANCING RESERVIOR',
 'VELIGALLU RESERVOIR',
 'ANNAMAYYA (CHEYYERU) RESERVOIR',
 'BUGGAVAGU',
 'SARVARAJA SAGAR',
 'NARAYANAPURAM ANICUT',
 'PEDDAGEDDA RESERVOIR',
 'VARADARAJASWAMY GUDI PROJECT',
 'ANDRA RESERVOIR',
 'Yeleru',
 'KONAM RESERVOIR',
 'KALANGI RESERVOIR',
 'MEHADRIGADD RESERVOIR',
 'BAHUDA RESERVOIR',
 'YELERU RESERVOIR',
 'CHAGALLU BALANCING RESERVOIR',
 'PINCHA PROJECT',
 'ALAGANURU BALANCING RESERVOIR',
 'KOVVADAKALVA RESERVOIR',
 'VATTIGEDDA RESERVOIR',
 'GODDAMVARIPALLI SR3',
 'MYLAVARAM(PENNAR) RESERVOIR',
 'MADDUVALASA PROJECT',
 'MID PENNAR RESERVOIR',
 'PAMPA RESERVOIR',
 'VELOGODU BALANCING RESERVOIR',
 'KANIGIRI RESERVOIR',
 'GAJJILIGEDDA RESERVOIR',
 'GANDIKOTA RESERVOIR',
 'VIJAYARAI ANICUT',
 'GANDIPALEM RESERVOIR PROJECT',
 'NTR Jalasayam',
 'CUM BUM TANK',
 'GONELAVAGU RESERVOIR',
 'KRISHNAPURAM PROJECT',
 'BHUPATIPALEM RESERVOIR',
 'SUBSIDIARY RESERVOIR -II',
 'YERRAKALVA RESERVOIR',
 'BRAHMAMSAGAR RESERVOIR',
 'PEDDERU RESERVOIR',
 'GUNDLAKAMMA RESERVOIR',
 'KALINGADAL PROJECT',
 'Srisailam Reservoir_1',
 'RAIWADA RESERVOIR',
 'NTR RESERVOIR',
 'UPPER PENNAR',
 'SUREMPALEM RESERVOIR',
 'Somasila Reservoir',
 'SIR AURTHUR COTTON BARRAGE',
 'RALLAPADU RESERVOIR',
 'MUSURIMALLI',
 'JALLERU RESERVOIR',
 'GAJULADINNE PROJECT',
 'GOTTA BARRAGE',
 'GOLLAPALLI RESERVOIR',
 'SWARNAMUKHI BARRAGE CUM BRIDGE',
 'SUBBAREDDY SAGAR',
 'DAMODARAM SAGARAM',
 'BADVEL TANK',
 'THATIPUDI RESERVOIR',
 'RAMA THIRTHAM',
 'MADDIGEDDA PROJECT',
 'Somasila Reservoir_2',
 'MOPADU RESERVOIR PROJECT',
 'SARVEPALLI RESERVOIR',
 'ARANIAR RESERVOIR',
 'ZURRERU RESERVOIR',
 'PAIDIPALEM BALANCING RESERVOIR',
 'TANDAVA RESERVOIR',
 'MALLIMADUGU',
 'NELLORE TANK',
 'KALYANI DAM',
 'PEDDERU RESERVOIR PROJECT',
 'TAMMILERU RESERVOIR',
 'VAMIKONDA SAGAR RESERVOIR',
 'NAGARJUNA SAGAR',
 'SANGAM ANICUT / BARRGE',
 'JEEDIPALLI RESERVOIR',
 'PRAKASAM BARRAGE',
 'CHITRAVATI BALANCING RESERVOIR',
 'VENGALRAYA SAGARAM',
 'CHENNARAYA SWAMI GUDI PROJECT',
 'SUBSIDIARY RESERVOIR -I',
 'Marala Reservoir',
 'THOTAPALLI REGULATOR / BARRAGE',
 'Parambikulam Reservoir',
 'Vagai Reservoir',
 'Mettur Reservoir',
 'Lower Bhawani  Bhavanisagar Reservoir',
 'Aliyar Reservoir',
 'Sholayar Reservoir',
 'Lower ManairG.V.Sudhakar Rao Reservoir',
 'Nagarjuna Sagar.1',
 'Nizam sagar',
 'Singur',
 'PULICHINTHALA PROJECT',
 'Sriram Sagar',
 'SUNKESULA BARRAGE',
 'Nagarjuna Sagar_3',
 'Almatti Reservoir',
 'Bhadra Reservoir',
 'Linganamakki Reservoir',
 'Narayanapura Reservoir',
 'Tattihalla',
 'Harangi Reservoir',
 'Mani Dam',
 'GhatPrabhaHidkal Reservoir',
 'Vanivilasa Sagar',
 'Gerusoppa Reservoir',
 'Kabini Reservoir',
 'Malaprabha Reservoir',
 'Hemavathy Reservoir',
 'Tungabhadra Reservoir',
 'Supa Reservoir',
 'Krishnaraja Sagar',
 'Kallada Reservoir',
 'Kakki Reservoir',
 'Idukki Reservoir',
 'Idamalayar Reservoir',
 'Malampuzha',
 'Periyar Reservoir',
 'Upper TapiHatnur Reservoir',
 'Isapur Reservoir',
 'Bhatsa',
 'Koyana/Shivaji Sagar',
 'Dudhganga',
 'Khadakwasla Reservoir',
 'Bhandardara',
 'Upper Vaitarana Reservoir',
 'Manikdoh',
 'Yeldari Reservoir',
 'Urmodi',
 'Niradevghar',
 'Upper Wardha Reservoir',
 'Mula Reservoir',
 'PenchTotladoh Reservoir',
 'Bhatghar',
 'Dhom',
 'Thokarwadi',
 'JayakwadiNath Sagar',
 'Girna Reservoir',
 'Mulshi Dam',
 'BhimaUjjani Reservoir',
 'Alwandi',
 'Kanher Dam',
 'Uben',
 'Phadangbeti',
 'Ukai Reservoir',
 'Sodvadar',
 'Lank',
 'Ghelo-I',
 'Prempara',
 'Pingli',
 'Guhai',
 'Goma',
 'Malgadh',
 'Damanganga Reservoir',
 'Gajod',
 'Hiran-I',
 'Demi - III',
 'Edalwada',
 'Hasanapur',
 'Khedva',
 'Phodarness',
 'Shell-Dedumal',
 'Kharo',
 'Dholi',
 'Wodisang',
 'Demi - II',
 'Sankroli',
 'WNKL.-BHEY',
 'Ranghola',
 'Khodapipar',
 'Kalubhar',
 'Machchhu-II',
 'Triveni Thanga',
 'Bhadar Reservoir',
 'Dhatarvadi',
 'Und-I',
 'Phophal - I',
 'Dharoi',
 'Bangawadi',
 'Fatehgadh',
 'Amipur',
 'Shingoda',
 'Nyari-II',
 'Sani',
 'Sindhani',
 'Ozat-II',
 'Phophal-II',
 'Nimbmani',
 'Aji-I',
 'Advana',
 'Vansal',
 'Kakdi-Amba',
 'Rojki',
 'Varansi',
 'Sabali',
 'Sukhbhadar',
 'Karjan',
 'Pigut',
 'Ukai',
 'Chopadvav',
 'Minsar (V)',
 'Nara',
 'Hanol',
 'Gorathiya',
 'Lim-Bhogavo-II',
 'Fulzar-II',
 'Thebi',
 'Khambhada',
 'Nyka',
 'Tappar',
 'Raval',
 'Ishwaria',
 'Saran',
 'Karnuki',
 'Patadungari',
 'Watrak',
 'Kalaghogha',
 'Lakhigam',
 'Machchhu - I',
 'Lalpari',
 'Harnav-II',
 'Panam',
 'Aji - II',
 'Fulzar-I',
 'Wanakbori',
 'Mitti',
 'Jhuj',
 'Brahmani',
 'Ruparel',
 'Bhadar - II',
 'Lakhanka',
 'Javanpura',
 'Vijarkhi',
 'Khambhala',
 'Machhu II',
 'Jaspara-Mandva',
 'Kabarka',
 'Brahmani-I',
 'Karad',
 'Mukteshwar',
 'Saburi',
 'Ambajal',
 'Watrak_4',
 'Munjiasar',
 'Brahmani-II',
 'Berachia',
 'Dhatarwadi-II',
 'Kabir-Sarovar',
 'Utavali',
 'Raidy',
 'Baldeva',
 'Gadhaki',
 'Mathal',
 'Machhu I',
 'Vachhapari',
 'Ozat-Weir',
 'Waidy',
 'Kabutari',
 'Machchhanala',
 'Ghelo - S',
 'Rami',
 'Demi - I',
 'Kelia',
 'Sardar Sarovar',
 'Rupavati',
 'Falku',
 'Veradi',
 'Jhanjeshri',
 'Rajawal',
 'Bhukhi',
 'Sorthi',
 'Shedhabhadthari',
 'Venu-II',
 'Kadana',
 'Ozat-Weir(Vanthali)',
 'Vrajmi',
 'Meshwo',
 'Lim-Bhogavo-I',
 'Machchhu-III',
 'Kaniyad',
 'Morshal',
 'Hamirpara',
 'Und I',
 'Dholidhaja',
 'Sukhi',
 'Dia-Minsar',
 'Und-II',
 'Bhadar',
 'Rana Khirasara',
 'Machhundri',
 'Kaswati',
 'Gajansar',
 'Deo',
 'Panam Reservoir',
 'Bagad',
 'Kali - II',
 'Hathmati',
 'Gondali',
 'Sapada',
 'Sukhi Tank',
 'Veri',
 'Malpara',
 'Sipu',
 'Aji-IV',
 'Dondi',
 'Sonmati',
 'Khodiyar',
 'Madhuvanti',
 'Draphad',
 'Survo',
 'Kankavati',
 'Vartu-II',
 'Aji-III',
 'Motisar',
 'Kankawati',
 'Bhimdad',
 'Niruna',
 'Dantiwada',
 'Hathmati_5',
 'Karjan Reservoir',
 'Dantiwada Reservoir',
 'Dhari',
 'Und-III',
 'Mazam',
 'Godhatad',
 'Rudramata',
 'Puna',
 'Sanandro',
 'Umaria',
 'Surajwadi',
 'Umiyasagar',
 'Veradi-II',
 'Mota-Gujariya',
 'Kaila',
 'Ghee',
 'Rangmati',
 'Karmal',
 'Ver-II',
 'Shetrunji',
 'Malan',
 'Doswada',
 'Suvi',
 'Vadiya',
 'Nyari - I',
 'Moj',
 'Kadana Reservoir',
 'Kalindri',
 'Vadi',
 'Ghodadhroi',
 'Shetrunji Reservoir',
 'Hadaf',
 'Bantva-Kharo',
 'Hiran-II',
 'Sasoi',
 'Bhadar (P)',
 'Vartu-I',
 'Don',
 'Fulzar (KB)',
 'Chhaparwadi-II',
 'Jangdia',
 'Sabarmati Reservoir',
 'TheinRanjit Sagar',
 'Bisalpur',
 'Jhakam Reservoir',
 'Ranapratap Sagar',
 'Mahi Bajaj Sagar',
 'Gobind SagarBhakra Reservoir',
 'Kol Dam',
 'Pong Reservoir']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/rainfall')
def rainfall():
    return render_template('rainfall.html')

@app.route('/reservoirs')
def reservoirs():
    return render_template('reservoirs.html',reservoirs = list(dams))


@app.route('/forecast_rainfall',methods=['GET','POST'])
def forecast_rainfall():
    
    days_to_forecast = request.form['rainfall_days']  

    start_date = date(2021,1,1)
    end_date =  date.today()
    
    total_days = days_between_dates(start_date , end_date)

    total_days = int(total_days) + int(days_to_forecast)


    date_labels = pd.date_range(start_date, periods=total_days + 1).strftime("%d-%m-%Y ").tolist()

    
    # convert entered days into feedable data
    # i.e to convert as numpy array
    prediction_input = preprocess(7672,total_days)

    # now predict with the reservoir_model
    rainfall_forecaster = joblib.load(open("rainfall_model.pkl","rb"))
    
    #predict

    prediction_result = rainfall_forecaster.predict(prediction_input)

    labels = date_labels
    values = prediction_result.tolist()

    #actual values we need
    labels = labels[-(int(days_to_forecast)):]
    values = values[-(int(days_to_forecast)):]


    return render_template('rainfall.html',labels = labels , values = values)



@app.route('/forecast_reservoir',methods=['GET','POST'])
def forecast_reservoir():

    days_to_forecast = request.form['reservoir_days']  
    reservoir_name = request.form['target-reservoir']

    print('reservoir_name:',reservoir_name)
    print('days_to_forecast:',days_to_forecast)

    start_date = date(2021,1,1)
    end_date =  date.today()
    
    total_days = days_between_dates(start_date , end_date)

    total_days = int(total_days) + int(days_to_forecast)

    date_labels = pd.date_range(start_date, periods=total_days + 1).strftime("%d-%m-%Y ").tolist()
    
    prediction_input = preprocess(7688,total_days)

    # now predict with the reservoir_model
    # reservoir_forecaster = joblib.load(open("reservoir_model.pkl","rb"))

    #multioutput 

    #multi_model = pickle.load(open("multioutput_reservoir_model.pkl","rb"))

    multi_model = pickle.load(open('predictor.pkl','rb'))

    #
    
    #predict

    #prediction_result = reservoir_forecaster.predict(prediction_input)

    #predict with multi-output

    prediction_result = multi_model(reservoir_name , prediction_input)



    labels = date_labels
    values = prediction_result.tolist()

    #actual values we need
    labels = labels[-(int(days_to_forecast)):]
    values = values[-(int(days_to_forecast)):]

    return render_template('reservoirs.html',labels = labels , values = values,reservoir_name = reservoir_name)



@app.route('/about')
def about():
    return render_template('about.html')



def days_between_dates(d0 , d1):
    delta = d1 - d0
    return delta.days

def preprocess(last_number,total_days):

    data = np.arange(last_number , last_number + total_days + 1)

    return data

if __name__ == '__main__':
    app.run()