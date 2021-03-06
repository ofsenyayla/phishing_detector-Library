# PHISHING DETECTOR

Phishing Detector is a library that can be used to detect phishing websites. You can query any website and find out if it is a phishing site within one line of code.

<b>Note:</b> In order to use this library, you must have an API key of Phishing Detector. For more information check our [blog post](http://phishingdetector.live/support/python-library-usage/).

### Setup

```
pip install phishing_detector
```

### Usage

- Single URL Query

```python
from phishing_detector import Detector

# while initializing the detector, you should pass your api_key as a parameter
# if you don't have an api_key, you can get one from your profile page:
# http://phishingdetector.live/profile/
detector = Detector(api_key)

detector.query('https://google.com') # it returns Legitimate or Phishing
```

- Multiple URL Query by File

```python
from phishing_detector import Detector

# while initializing the detector, you should pass your api_key as a parameter
# if you don't have an api_key, you can get one from your profile page:
# http://phishingdetector.live/profile/
detector = Detector(api_key)

# it creates a new column in the input file and saves the results in this column
# it saves into the input file by default
detector.query_by_file("input.csv")

# also you can set an output filename and save the results in a new file
detector.query_by_file("input.csv", output_file="output.csv")

# to query the urls inside a file, multithreading is used to speed up the process
# by default, max_workers is set to 10, but you can change it
detector.query_by_file("input.csv", output_file="output.csv", max_workers=20)
```

- Multiple URL Query by List

```python
from phishing_detector import Detector

# while initializing the detector, you should pass your api_key as a parameter
# if you don't have an api_key, you can get one from your profile page:
# http://phishingdetector.live/profile/
detector = Detector(api_key)

url_list = ["https://www.google.com", "https://www.facebook.com"]

# it creates the output file and saves the results in this file
detector.query_by_list(url_list, output_file="output.csv")

# to query the urls inside a list, multithreading is used to speed up the process
# by default, max_workers is set to 10, but you can change it
detector.query_by_list(url_list, output_file="output.csv", max_workers=20)
```

### Requirements

In order to work this library properly, following libraries must be installed on your computer:

- [requests](https://pypi.org/project/requests/)
- [validators](https://pypi.org/project/validators/)
- [pandas](https://pypi.org/project/pandas/)
