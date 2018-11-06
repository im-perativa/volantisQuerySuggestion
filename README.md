# volantisQuerySuggestion

Contoh REST API (tanpa GUI) untuk fitur tambahan yang dapat digunakan untuk mempermudah pencarian dengan text similarity pada platform volantis.io

## Memulai

Untuk mendapatkan copy dari project ini untuk digunakan pada mesin lokal anda, silakan clone repository ini

### Menyiapkan Environment Lokal

1. Download dan install [Git][1]
2. Download dan install [Python3][2]
3. Buat folder baru untuk menyimpan project ini
4. Buka folder baru dan clone project ini ke dalam folder tersebut

```
git init
git clone https://github.com/imperativa/volantisQuerySuggestion
```

[1]: https://git-scm.com/downloads
[2]: https://www.python.org/getit/


### Instalasi 

Untuk dapat menggunakan volantisQuerySuggestion, install semua library yang diperlukan pada virtual environment

```
source venv/bin/activate
pip install -r requirement.txt
deactivate
```

## Menjalankan REST API

Untuk dapat menjalankan volantisQuerySuggestion, masuk ke dalam virtual environment dan run `app.py`

```
source venv/bin/activate
python app.py
```

### URI
```
/query
```

### Form Body
* `query` - Search query

### Contoh Hasil

`query`: "Drink"  
```
[
    {
        "title": "Canada Production and Stocks of Tea Coffee Cocoa and Process Cheese (1946 - 1994)",
        "similarity": 0.5122280652306186
    },
    {
        "title": "Wine Dataset",
        "similarity": 0.5018565420603127
    },
    {
        "title": "Craft Beers Dataset",
        "similarity": 0.4951684779658376
    },
    {
        "title": "Flowers and Fruits Coffee Production 2015 - 2016",
        "similarity": 0.4949710941238208
    },
    {
        "title": "Fast Food Restaurants Across America",
        "similarity": 0.4852875768392291
    }
]
```

`query`: "Computer Price"  
```
[
    {
        "title": "1300 Laptop Prices",
        "similarity": 0.7270224030210517
    },
    {
        "title": "simple laptop price",
        "similarity": 0.7193491154077535
    },
    {
        "title": "laptop prices based on specifications",
        "similarity": 0.7133145974431971
    },
    {
        "title": "Laptop Prices with 5 features",
        "similarity": 0.6713759660215457
    },
    {
        "title": "laptop price prediction",
        "similarity": 0.6615189558255555
    }
]
```

`query`: "College"  
```
[
    {
        "title": "World University Rankings",
        "similarity": 0.6412657955909788
    },
    {
        "title": "Prediction University Score with Random Forest",
        "similarity": 0.5632472832017524
    },
    {
        "title": "Prediction University Score with Decision Tree",
        "similarity": 0.5583400256572105
    },
    {
        "title": "Prediction University Score with Isotonic Regresion",
        "similarity": 0.5539713672492729
    },
    {
        "title": "Accredited Universities in The USA",
        "similarity": 0.5459227862063514
    }
]
```

`query`: "Disease"  
```
[
    {
        "title": "Zika Virus Epidemic",
        "similarity": 0.678525681077377
    },
    {
        "title": "Lower Back Pain Symptoms",
        "similarity": 0.6039499350255548
    },
    {
        "title": "Dengue Cases at Philippines",
        "similarity": 0.5104936023748938
    },
    {
        "title": "Diabetes Dataset - Pima Indian heritage",
        "similarity": 0.5092409450367811
    },
    {
        "title": "Body Mass Index Prediction with Decision Tree",
        "similarity": 0.4749832359760606
    }
]
```

`query`: "Food"  
```
[
    {
        "title": "Fast Food Restaurants Across America",
        "similarity": 0.7400498235972779
    },
    {
        "title": "Nutrition Data of Cereal Products",
        "similarity": 0.664449975449146
    },
    {
        "title": "Canada Production and Stocks of Tea Coffee Cocoa and Process Cheese (1946 - 1994)",
        "similarity": 0.6127799640574634
    },
    {
        "title": "List of Coffee Growing in Countries",
        "similarity": 0.5862108605524592
    },
    {
        "title": "Flowers and Fruits Coffee Production 2015 - 2016",
        "similarity": 0.572210077503153
    }
]
```

`query`: "Terror"  
```
[
    {
        "title": "Terrorist Attacks",
        "similarity": 0.6963410033530324
    },
    {
        "title": "Religious Terrorist Attack",
        "similarity": 0.6866494128774574
    },
    {
        "title": "Political Corruption Perception Index",
        "similarity": 0.46151955198719774
    },
    {
        "title": "Mass Shooting in US",
        "similarity": 0.41791128257519705
    },
    {
        "title": "Country Statistic in the World",
        "similarity": 0.40332504202594366
    }
]
```
