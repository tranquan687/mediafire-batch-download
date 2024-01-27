<h1 align="center">
  mediafire-batch-download

</h1>

## Description

**mediafire-dl** is a script written in Python to automate the download of files from [mediafire.com](https://mediafire.com) with a simple command-line interface.

> Much of the code comes from [gdown](https://github.com/wkentaro/gdown)

## Prerequisites

It is necessary to have **python3** and **pip3**


## Installation

```bash
pip3 install git+https://github.com/Juvenal-Yescas/mediafire-dl
```

## Usage
**Step 1**: Select files to download. \
**Step 2**: Copy share link.  
![Alt text](./readme_img/tutorial.PNG?raw=true "Title")
**Step 3**: From Command Line. 
```bash
cd mediafire-batch-download
python main.py "copied/link"  --out_folder "path/to/save/folder"

```


## Build with

* [Python3](https://www.python.org/download/releases/3.0/) - Python is an interpreted, high-level, general-purpose programming language. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Inspired by :
* [gdown](https://github.com/wkentaro/gdown)
* [openload-dl](https://github.com/gius-italy/openload-dl)
* [mediafire-dl](https://github.com/Juvenal-Yescas/mediafire-dl)
