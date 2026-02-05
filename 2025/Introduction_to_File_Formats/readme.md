# Introduction to File Formats

In January 2026 we hosted an expert session on identifying file formats and recorded the talk which can be found online [here](https://youtu.be/E27E3jPysZ0).

The topic covered specific tools and the differences between them, such as [DROID (Digital Record Object Identification)](https://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/) and [Siegfried](https://www.itforarchivists.com/).

### Why is this useful?

1. Preservation: You cannot preserve a file if you don't know what it is. Identification is the first step in digital archiving.
2. Security: Malware often hides by masquerading as a harmless file type (e.g., an .exe renamed to .jpg). Identification tools look at the binary signature, not just the file extension.
3. Troubleshooting: When a file won't open, it is often because the extension doesn't match the actual format.

### Pre-requisites

For this session it might be useful if you have access to a few tools.

1.	A Hex Editor

You need a tool to view the raw binary data of a file, here are some tools that you can use, and others are available.
Windows: [HxD](https://mh-nexus.de/en/hxd/)
macOS: [Hex Fiend](https://hexfiend.com/)
Linux: GHex or Bless

2.	An Identification Tool
   
These exercises will focus on [DROID (Digital Record Object Identification)](https://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/) and [Siegfried](https://www.itforarchivists.com/). Siegfried has a more accessible command line interface whilst DROID can be more approachable with a GUI. 


3.	Access to sample files

We have placed some sample files in the [Bits and Bots repository](https://github.com/Lotte-W/Bits-and-Bots-study-group/tree/main/2025/Introduction_to_File_Formats/File_Samples), GitHub is also an excellent resource for downloading sample files or you may already have some files sets that you wish to analyze on your computer.

## Exercises

### Analyse Your Files

### Research a File Format

Are there any file formats in your collection that you can’t identify, or do you have an area of interest you want to explore further. PRONOM also has [lists of file formats that do not yet contain full descriptions or have signatures](https://ffdev-info.github.io/pronom-page/). If you want to take on a challenge and create a description for a file format in PRONOM, or (hard mode) attempt to create a signature for a file that doesn’t have one then the PRONOM Research GitHub repository has all the tools and lists you would need in the readme. If you have your own files you would like to explore further then have a go following the steps in the [Starter Guide](https://github.com/digital-preservation/PRONOM_Research/blob/main/Resources/Starter_Pack.md).

### Finding Common Hex Patterns

For this exercise we will be looking at [these files](https://github.com/Lotte-W/Bits-and-Bots-study-group/tree/main/2025/Introduction_to_File_Formats/File_Samples). Open the files and drag and drop these into your hex editor. Can you find any consistent patterns within the file format? Is this the “File Signature” or “Magic Number”? Can you work out how these files could be identified? For tips on using a hex editor and analysing files you can use the [Starter Guide](https://github.com/digital-preservation/PRONOM_Research/blob/main/Resources/Starter_Pack.md).

## Optional Python Challenge

For those comfortable with Python, try to write a script that mimics what Siegfried does.
Create a python script that iterates through the Sample Dataset.
For example:

```
downloadcontent_copy
expand_less
  with open('filename','rb') as f:
  print(f.read(4).hex())
```

Create a simple dictionary (Key: Value) where the Hex Signature is the key, and the Format Name is the value.
Print out the format of the files based on your dictionary lookup.

## Further Reading

For further reading we would recommend the [PRONOM Starter Guide](https://github.com/digital-preservation/PRONOM_Research/blob/main/Resources/Starter_Pack.md) (also [available in Spanish](https://github.com/digital-preservation/PRONOM_Research/blob/main/Resources/Starter_Pack.md)) as well as the other resources and links that can be found on the [PRONOM GitHub Repository](https://github.com/digital-preservation/PRONOM_Research/tree/main).


