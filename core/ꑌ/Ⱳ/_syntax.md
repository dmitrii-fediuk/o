# Ⱳ T
## Syntax
~~~code
Ⱳ T
~~~
## Meaning
The `ꑌ𝔼` representing the `ꑌꕤ` of the `ꑌ𐏕` which is the `ꑌⱳ_Topic` of the `ꑌⱳ_Article` at `https://en.wikipedia.org/wiki/<T>`.
### Parameters   
- `T` — the Last Path Segment of the `ꑌⱳ_Article`'s `ꑌURI`.
## Example
⟨ Ⱳ Ontology_(information_science) ⟩ ≡ ⟨ An ontology: a representation, formal naming, and definitions of the categories, properties, and relations between the concepts, data, or entities ⟩

# Ⱳ T₀#T
## Syntax
~~~code
Ⱳ T₀#T
~~~
## Meaning
The `ꑌ𝔼` representing the `ꑌꕤ` of the `ꑌ𐏕` which is the heading of a particular section of the `ꑌⱳ_Article` at `https://en.wikipedia.org/wiki/<T₀>#<T>`.
### Parameters    
- `T` — the `ꑌURI_Fragment_Identifier` of the section.
- `T₀` — the Last Path Segment of the `ꑌⱳ_Article`'s `ꑌURI`.

## Example
⟨ Ⱳ Partially_ordered_set#Intervals ⟩ ≡ ⟨ `ꑌ𝔼` «**interval**» в контексте «an **interval** in a poset `P` is a subset that can be defined with interval notation <…>» ⟩
## Rationale
Я использую этот синтаксис, когда для описываемого мной `ꑌ𝔼` отсутствует a standalone `ꑌⱳ_Article`. 

# Ⱳ T₀∷T
## Syntax
~~~code
Ⱳ T₀∷T
~~~
## Meaning
`ꑌ𝔼` `T` в контексте the `ꑌⱳ_Article` по адресу `https://en.wikipedia.org/wiki/<T₀>`.  
## Example
⟨ Ⱳ Theory_of_categories∷category ⟩ ≡ ⟨ `ꑌ𝔼` «**category**» в контексте «In ontology, the theory of categories concerns itself with the **categories** of being: the highest genera or kinds of entities. To investigate the categories of being, or simply **categories** <…>» ⟩
## Rationale
Я использую этот синтаксис в тех случаях, когда для описываемого мной `ꑌ𝔼` отсутствует и standalone `ꑌⱳ_Article`, и даже standalone section (with a Fragment Identifier) of a `ꑌⱳ_Article`.

