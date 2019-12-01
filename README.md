# Folder Content Divider ![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
Divides all the files inside a directory and create sub-directory for each file division. 

## Intro
This program converts this
```
├── dummy
│   ├── 0.txt
│   ├── 100.txt
│   ├── 101.txt
│   ├── 102.txt
│   ├── 103.txt
│   ├── 104.txt
│   ├── 105.txt
│   ├── 106.txt
│   ├── 107.txt
│   ├── ...txt
│   ├── ...txt
│   ├── 212.txt
```
into this
```
├── dummy
│   ├── dummy_1
│   │   ├── 0.txt
│   │   ├── 101.txt
│   │   ├── ...txt
│   │   ├── ...txt
│   │   ├── 120.txt
│   ├── dummy_2
│   │   ├── 100.txt
│   │   ├── ...txt
│   │   ├── ...txt
│   │   ├── 110.txt
│   └── dummy_3
│       ├── 123.txt
│       ├── ...txt
│       ├── ...txt
│       └── 79.txt
```

## Testing
- Run `folder_creator.py` to create some files inside `dummy` folder
- Run `main.py` 