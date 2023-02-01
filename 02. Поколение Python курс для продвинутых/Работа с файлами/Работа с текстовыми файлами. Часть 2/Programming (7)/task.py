with open('population.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        name, population = line.strip().split('\t')
        if name.startswith('G') and int(population) > 500000:
            print(name)

'''
China	1368050000
India	1266480000
United States	320341000
Indonesia	255461700
Brazil	203841000
Pakistan	188894000
Nigeria	183523000
Bangladesh	157784000
Russia	146270033
Japan	127020000
Mexico	121005815
Philippines	100959800
Vietnam	90730000
Ethiopia	90076012
Egypt	87965900
Germany	80767000
Iran	78096500
Turkey	77695904
Democratic Republic of the Congo	71246000
France	66092000
Thailand	64871000
United Kingdom	64105654
Italy	60782897
South Africa	54002000
Burma	51419420
South Korea	50423955
Colombia	47984800
Tanzania	47421786
Kenya	46749000
Spain	46464053
Argentina	43131966
Ukraine	42953889
Algeria	39500000
Poland	38496000
Sudan	38435252
Iraq	36004552
Canada	35675834
Uganda	34856813
Morocco	33516100
Saudi Arabia	31521418
Peru	31151643
Venezuela	30620404
Uzbekistan	30492800
Malaysia	30483800
Nepal	28037904
Ghana	27043093
Afghanistan	26556800
Yemen	25956000
Mozambique	25727911
North Korea	25155000
Angola	24383301
Australia	23735500
Taiwan	23433753
Ivory Coast	22671331
Syria	22265000
Madagascar	21842167
Cameroon	21143237
Sri Lanka	20359439
Romania	19942642
Niger	19268000
Chile	18006407
Kazakhstan	17397200
Burkina Faso	17322796
Netherlands	16888500
Malawi	16310431
Mali	16259000
Ecuador	15925700
Guatemala	15806675
Zambia	15473905
Cambodia	15405157
Chad	13606000
Senegal	13508715
Zimbabwe	13061239
South Sudan	11892934
Bolivia	11410651
Belgium	11233192
Cuba	11210064
Somalia	11123000
Rwanda	10996891
Greece	10992589
Tunisia	10982754
Haiti	10911819
Guinea	10628972
Czech Republic	10521600
Portugal	10477800
Dominican Republic	10378267
Benin	10315244
Hungary	9879000
Burundi	9823827
Sweden	9743087
Azerbaijan	9583200
United Arab Emirates	9577000
Belarus	9481000
Honduras	8725111
Austria	8572895
Israel	8296000
Switzerland	8211700
Tajikistan	8161000
Papua New Guinea	7398500
Bulgaria	7245677
Hong Kong (China)	7234800
Togo	7171000
Serbia	7146759
Paraguay	6893727
Laos	6802000
Eritrea	6738000
Jordan	6687470
El Salvador	6401240
Sierra Leone	6319000
Libya	6317000
Nicaragua	6134270
Turkmenistan	5888000
Kyrgyzstan	5874100
Denmark	5655750
Finland	5475526
Singapore	5469700
Slovakia	5421034
Norway	5156450
Central African Republic	4803000
Costa Rica	4773130
Republic of the Congo	4671000
Ireland	4609600
New Zealand	4559890
Palestine	4550368
Liberia	4503000
Georgia	4490500
Croatia	4267558
Lebanon	4104000
Oman	4099904
Bosnia and Herzegovina	3791622
Panama	3713312
Moldova	3557600
Puerto Rico (U.S.)	3548397
Mauritania	3545620
Uruguay	3404189
Kuwait	3268431
Armenia	3013900
Mongolia	3000000
Lithuania	2921920
Albania	2895947
Jamaica	2717991
Qatar	2235431
Lesotho	2120000
Namibia	2113077
Macedonia	2065769
Slovenia	2065549
Botswana	2024904
Latvia	1988400
The Gambia	1882450
Kosovo	1816891
Guinea-Bissau	1788000
Gabon	1751000
Equatorial Guinea	1430000
Trinidad and Tobago	1328019
Bahrain	1316500
Estonia	1312252
Mauritius	1261208
East Timor	1212107
Swaziland	1106189
Djibouti	900000
Fiji	859178
Cyprus	858000
Reunion (France)	840974
Comoros	763952
Bhutan	756940
Guyana	746900
Macau (China)	631000
Montenegro	620029
Western Sahara	604000
Solomon Islands	581344
Luxembourg	549700
Suriname	534189
Cape Verde	518467
Transnistria	505153
Malta	416055
Guadeloupe (France)	405739
Brunei	393372
Martinique (France)	386486
The Bahamas	368390
Belize	349728
Maldives	341256
Iceland	328170
Northern Cyprus	294906
Barbados	285000
New Caledonia (France)	268767
French Polynesia (France)	268270
Vanuatu	264652
Abkhazia	240705
French Guiana (France)	239648
Mayotte (France)	212645
Samoa	187820
Sao Tome and Principe	187356
Saint Lucia	185000
Guam (U.S.)	159358
Curacao (Netherlands)	154843
Saint Vincent and the Grenadines	109000
Aruba (Netherlands)	107394
Kiribati	106461
United States Virgin Islands (U.S.)	106405
Grenada	103328
Tonga	103252
Federated States of Micronesia	101351
Jersey (UK)	99000
Seychelles	89949
Antigua and Barbuda	86295
Isle of Man (UK)	84497
Andorra	76949
Dominica	71293
Bermuda (UK)	64237
Guernsey (UK)	63085
Greenland (Denmark)	56295
Marshall Islands	56086
Cayman Islands (UK)	55691
American Samoa (U.S.)	55519
Saint Kitts and Nevis	55000
Northern Mariana Islands (U.S.)	53883
South Ossetia[24]	51547
Faroe Islands (Denmark)	48605
Sint Maarten (Netherlands)	37429
Liechtenstein	37132
Monaco	36950
Collectivity of Saint Martin (France)	35742
San Marino	32777
Turks and Caicos Islands (UK)	31458
Gibraltar (UK)	30001
Aland Islands (Finland)	28875
British Virgin Islands (UK)	28054
Caribbean Netherlands (Netherlands)	23296
Palau	20901
Cook Islands (New Zealand)	14974
Anguilla (UK)	13452
Wallis and Futuna (France)	13135
Tuvalu	11323
Nauru	10084
Saint Barthelemy (France)	9131
Saint Pierre and Miquelon (France)	6069
Montserrat (UK)	4922
Saint Helena, Ascension and Tristan da Cunha (UK)	4000
Falkland Islands (UK)	3000
Svalbard and Jan Mayen (Norway)	2562
Norfolk Island (Australia)	2302
Christmas Island (Australia)	2072
Niue (New Zealand)	1613
Tokelau (NZ)	1411
Vatican City	839
Cocos (Keeling) Islands (Australia)	550
Pitcairn Islands (UK)	56
'''