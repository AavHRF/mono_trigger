## Mono_Trigger

##### An easier method for handling triggering.

Mono_Trigger uses a GUI to assist in triggering. You supply a list of trigger regions with comma-separated values, and it gives you the go order when it is time to jump.

***
## How To Install
Download and unzip the source file from the [latest release.](https://github.com/AavHRF/mono_trigger/releases/tag/v1.0.1a)

Using Python3, you need to install the following packages
* BeautifulSoup (bs4)
* Requests (requests)
* LXML (lxml)
* PySimpleGUI (PySimpleGUI)

Use the following command to install these packages all at once:

```
python3 -m pip install bs4 requests lxml PySimpleGUI
```

## What Does it Look Like?
![image](https://user-images.githubusercontent.com/65682563/91416179-e0a9ed00-e803-11ea-9477-ba4b94e80924.png)

## How To Set Up
Once you have downloaded the program, and unzipped it, you can run it with the following command in your working directory. `python3 app.py`

You need to supply a list of trigger regions, click the "Load List" button to get the list in the program. This list can be generated using [Snapsheet](https://aavhrf.github.io/webtrigger/snapsheet.html) and [Quickdraw](https://aavhrf.github.io/webtrigger/quickdraw.html).


## Safety Features
* Useragent verification
* Automatic ratelimiting
