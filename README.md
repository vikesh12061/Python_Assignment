# Python_Assignment
# CSVReader
CSV Reader is simple application to transform the CSV file in to a nested JSON file which will form a tree structure

# Technology Used
Python, as a high level programming language, allows you to focus on core functionality of the application by taking care of common programming tasks.


# How to Run
Run Command on same project location
```
	python csvReader.py
```

# Ouput
1. It create a 'output.json' file in same folder location
2. It create a 'csvReaderLog.log' file same folder location

# Unit Testing
Run Command on same project location
```
	python -m unittest test_csvReader.py
```



# To change different input CSV file
Specify you input CSV file path at entry point of CSVReader application

```
e.g.
	if __name__ == '__main__':
		r = CSVReader('<file_path>/<file_name>') 
```

# The desired output.json form
From CSV we get nested JSON in below format
```
[  
  {
    "label": "Meat & Fish",
    "id": "179549",
    "link": "https://groceries.morrisons.com/browse/179549",
    "children": [
      {
        "label": "3 For £9.00 Meat & Poultry",
        "id": "179545",
        "link": "https://groceries.morrisons.com/browse/179549/179545",
        "children": []
      },
      {
        "label": "Fish",
        "id": "176741",
        "link": "https://groceries.morrisons.com/browse/179549/176741",
        "children": [
          {
            "label": "Fish Counter",
            "id": "176780",
            "link": "https://groceries.morrisons.com/browse/179549/176741/176780",
            "children": [
              {
                "label": "Salmon",
                "id": "176979",
                "link": "https://groceries.morrisons.com/browse/179549/176741/176780/176979",
                "children": []
              }
            ]
          }
        ]
      }
    ]
  }
]

```
