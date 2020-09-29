# Text Summarizer - Python
 
This is a backend project written in Python which accepts text input, parses and eliminates phrases, and generates a summarized version of the text. It utilizes modules and tools from the Natural Language Toolkit (NLTK) to tokenize and parse text using stemmers, tokenizers, and stopwords. 

## How does it work

1. Tokenize block of text by words and sentences with tokenization module from NLTK library

```
token_sent = sent_tokenize(statement)
token_words = word_tokenize(sent)
```

2. Further break down the text by breaking down words to their root words + removing NLTK stopwords and punctuation using list comprehension

```
token_words = [word for word in token_words if word.isalnum()]
filtered = [w for w in token_words if not w in stopWords]
```

3. Score sentences using a word frequency dict 

```
for word in filtered:
        numWords[word] = numWords.get(word,0) + 1
    sent_score[sent] = sum(filtered.values())
```

4. Filter sentences using sentence scores and word frequencies

## Results 

### Input

>The ocean is the most important subsystem of the Earth’s climate system and functions as its heart, regulating the energy distribution of the planet. It has absorbed more than 90% of the energy accumulated since 1971 and about 30% of the emitted anthropogenic carbon dioxide. As a result, water temperature rises and oceans acidify and deoxygenate, which lead to changes in oceanic circulation and biogeochemistry, to rising sea levels, to more extreme weather events, to shifts in the distribution of species and migratory routes, and to loss of species and habitat diversity. Awareness of the importance of oceans for the sustainability of the global human population is increasing, including the conservation of biodiversity and its legacy to future generations. For instance, oceanic organisms are more vulnerable to warming than terrestrial ones, as the former are generally at temperatures near their upper thermal limits and lack of thermal refuges. Half of the atmospheric carbon fixed annually in natural systems is cycled into the ocean mainly by the biological carbon pump in the open ocean, but some of the main areas capturing and storing this carbon (as mangroves, seagrasses, salt marshes, and coastal upwelling ecosystems) cover less than 3% of the world’s ocean surface. Particularly, eastern boundary upwelling systems are highly productive ecosystems, with up to 40% of the reported global fish catch.
In addition, there are growing human pressures on the ocean and on its resources. Today, the coastal zone has the largest economic importance in human history and the number of initiatives to use the ocean and its resources grow each year. However, fishery productions stabilized at 90–95 million tons since the mid-1990s, but global aquaculture production and the world trade of fish and fishery products rapidly increased in response to rising demand. These activities depend on healthy ecosystems, but the impacts of climate change and other anthropogenic pressures challenge their resilience and adaptive capacity at the local and regional scales. Human activities also alter the amount and spatiotemporal distribution of nutrients and toxins delivered to the ocean.

### Output

>  As a result, water temperature rises and oceans acidify and deoxygenate, which lead to changes in oceanic circulation and biogeochemistry, to rising sea levels, to more extreme weather events, to shifts in the distribution of species and migratory routes, and to loss of species and habitat diversity. Half of the atmospheric carbon fixed annually in natural systems is cycled into the ocean mainly by the biological carbon pump in the open ocean, but some of the main areas capturing and storing this carbon (as mangroves, seagrasses, salt marshes, and coastal upwelling ecosystems) cover less than 3% of the world’s ocean surface. However, fishery productions stabilized at 90–95 million tons since the mid-1990s, but global aquaculture production and the world trade of fish and fishery products rapidly increased in response to rising demand.
