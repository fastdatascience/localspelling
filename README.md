![Fast Data Science logo](https://raw.githubusercontent.com/fastdatascience/brand/main/primary_logo.svg)

<a href="https://fastdatascience.com"><span align="left">🌐 fastdatascience.com</span></a>
<a href="https://www.linkedin.com/company/fastdatascience/"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/linkedin.svg" alt="Fast Data Science | LinkedIn" width="21px"/></a>
<a href="https://twitter.com/fastdatascienc1"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/x.svg" alt="Fast Data Science | X" width="21px"/></a>
<a href="https://www.instagram.com/fastdatascience/"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/instagram.svg" alt="Fast Data Science | Instagram" width="21px"/></a>
<a href="https://www.facebook.com/fastdatascienceltd"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/fb.svg" alt="Fast Data Science | Facebook" width="21px"/></a>
<a href="https://www.youtube.com/channel/UCLPrDH7SoRT55F6i50xMg5g"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/yt.svg" alt="Fast Data Science | YouTube" width="21px"/></a>

# Local spelling

Developed by Fast Data Science, https://fastdatascience.com

Source code at https://github.com/fastdatascience/localspelling

Python library for localising spelling between British and American conventions, conserving case.

Please note this library converts only spelling variants such as US "honour" vs UK "honor".
It does not localise vocabulary such as "pavement" vs "sidewalk" or "aubergine" vs "eggplant".

It also does not localise spellings where there is more than one correct conversion, such as US "program",
which corresponds to both "programme" and "program" in British spelling.

# Requirements

Python 3.6 and above

# Installation

```
pip install localspelling
```

# Usage examples

Example 1

```
from localspelling import convert_spelling

convert_spelling("it has been an honor", "gb")
```

outputs

```
'it has been an honour'
```

Example 2: you can retrieve the dictionary used for the single words (this won't match wildcards like '-isation')

```
from localspelling import get_dictionary

get_dictionary("us")["honour"]
```

outputs

```
'honor'
```


# Who to contact

Thomas Wood at https://fastdatascience.com
